"""Build/runtime seam tests: real file detachment and authority/lifecycle boundaries."""
import copy,hashlib,importlib.util,json,shutil,subprocess,sys,tempfile,unittest
from pathlib import Path
from unittest.mock import patch
ROOT=Path(__file__).resolve().parents[1]
def module(path,name):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
BUILD=module(ROOT/'scripts/build_knowledge.py','knowledge_build_test')
class KnowledgeViewTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory(prefix='fab-knowledge-regression-');self.addCleanup(self.temp.cleanup);self.root=Path(self.temp.name)
  authoring=json.loads((ROOT/'knowledge/current.json').read_text());paths={'knowledge/current.json','plugins/fab/skills/research/scripts/knowledge_view.py','plugins/fab/shared/knowledge/current.json'}|{s['archive'] for u in authoring['records'] for s in u['sources']}
  for name in paths:
   target=self.root/name;target.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(ROOT/name,target)
  self.target=self.root/'plugins/fab/shared/knowledge/current.json';self.authoring=self.root/'knowledge/current.json';self.view=module(self.root/'plugins/fab/skills/research/scripts/knowledge_view.py','view_case');self.data=json.loads(self.target.read_text());self.units={u['id']:u for u in self.data['records']}
 def author(self,mutator):
  data=json.loads(self.authoring.read_text());mutator(data);self.authoring.write_text(json.dumps(data));return data
 def state(self,key='naming',observations=None):
  state={'schemaVersion':2,'family':self.data['family'],'retired':{key:self.units[key]['revision']},'reason':{key:'Accepted retirement pending reviewed restoration.'},'observations':observations or []};path=self.root/'state.json';path.write_text(json.dumps(state));return path
 def observation(self):return {'id':'local-label','aboutUnit':'naming','unitRevision':self.units['naming']['revision'],'text':'One designer preferred default for the local main text style.','origin':'accepted project review fixture'}
 def test_reproducible_build(self):
  first=BUILD.build(self.root);second=BUILD.build(self.root);self.assertEqual(first,second);self.assertEqual(BUILD.build(self.root,check=True),second)
 def test_meanings_preserved_without_global_fixture(self):
  authored=json.loads(self.authoring.read_text());active=[u for u in authored['records'] if u['status']=='active'];self.assertEqual(len(active),75)
  self.assertEqual({u['id']:u['body'] for u in active},{u['id']:u['body'] for u in self.data['records'] if u['status']=='active'});self.assertNotIn('local-naming',self.units);self.assertNotIn('body',self.units['legacy-dimension'])
 def test_stale_compiled_output_rejected(self):
  self.author(lambda d:d['records'][0].update(title='Edited meaning title'))
  with self.assertRaisesRegex(ValueError,'stale-compiled'):BUILD.build(self.root,check=True)
 def test_changed_source_does_not_publish(self):
  ref=json.loads(self.authoring.read_text())['records'][0]['sources'][0];path=self.root/ref['archive'];d=json.loads(path.read_text());next(s for s in d['sections'] if s['id']==ref['section'])['text']+=' changed';path.write_text(json.dumps(d));before=self.target.read_bytes()
  with self.assertRaisesRegex(ValueError,'source-section-mismatch'):BUILD.build(self.root)
  self.assertEqual(before,self.target.read_bytes())
 def test_missing_source_fails_build_only(self):
  ref=json.loads(self.authoring.read_text())['records'][0]['sources'][0];(self.root/ref['archive']).unlink()
  with self.assertRaises(OSError):BUILD.build(self.root)
  self.assertTrue(self.view.read_view(unit_id='dimensions')['units'])
 def test_escaped_source_rejected_before_read(self):
  self.author(lambda d:d['records'][0]['sources'][0].update(archive='../outside.json'))
  with self.assertRaisesRegex(ValueError,'source-outside'):BUILD.build(self.root)
 def test_dangling_relation_rejected(self):
  self.author(lambda d:d['records'][0]['relations'].update(contradicts=['missing']))
  with self.assertRaisesRegex(ValueError,'invalid-relation'):BUILD.build(self.root)
 def test_condition_cycle_rejected(self):
  def change(d):
   for u in d['records']:
    if u['id']=='identity':u['relations']['applies-under']=['recovery']
  self.author(change)
  with self.assertRaisesRegex(ValueError,'condition-cycle'):BUILD.build(self.root)
 def test_local_fixture_cannot_enter_shared_build(self):
  self.author(lambda d:d['records'][0].update(authority='local-evidence'))
  with self.assertRaisesRegex(ValueError,'non-shared-evidence'):BUILD.build(self.root)
 def test_runtime_never_opens_original_reports(self):
  original=Path.read_text
  def guarded(path,*a,**kw):
   if path.name.endswith('.full.json'):raise AssertionError('Runtime opened an original report')
   return original(path,*a,**kw)
  with patch.object(Path,'read_text',guarded):
   result=self.view.read_view(unit_id='pending');self.assertIn('pending',[u['id'] for u in result['units']]);self.assertTrue(result['sourceReceipts'])
 def test_standalone_reader_without_sources_docs_or_builder(self):
  only={self.target,self.root/'plugins/fab/skills/research/scripts/knowledge_view.py'}
  for f in list(self.root.rglob('*')):
   if f.is_file() and f not in only:f.unlink()
  run=subprocess.run([sys.executable,'-B',str(self.root/'plugins/fab/skills/research/scripts/knowledge_view.py'),'--unit','dimensions'],capture_output=True,text=True)
  self.assertEqual(run.returncode,0,run.stderr);self.assertIn('2025.10',json.loads(run.stdout)['units'][0]['body'])
 def test_retired_body_not_returned(self):
  result=self.view.read_view(state_path=self.state(),unit_id='naming');self.assertEqual(result['units'],[]);self.assertNotIn('body',result['unavailable'][0]);self.assertTrue(result['unavailable'][0]['reviewSources'])
 def test_local_evidence_remains_visible_but_not_global(self):
  result=self.view.read_view(state_path=self.state(observations=[self.observation()]),unit_id='naming');self.assertEqual(result['units'],[]);self.assertEqual(result['projectEvidence'][0]['scope'],'project-only');self.assertEqual(result['projectEvidence'][0]['authority'],'local-evidence-not-shared-policy');self.assertEqual(self.target.read_text(),json.dumps(self.data,ensure_ascii=False,indent=2)+'\n')
 def test_local_authority_injection_rejected(self):
  obs=self.observation();obs['authority']='global'
  with self.assertRaisesRegex(ValueError,'invalid-local-evidence'):self.view.read_view(state_path=self.state(observations=[obs]),unit_id='naming')
 def test_local_observation_cannot_replace_global_id(self):
  obs=self.observation();obs['id']='naming'
  with self.assertRaisesRegex(ValueError,'invalid-local-evidence'):self.view.read_view(state_path=self.state(observations=[obs]),unit_id='naming')
 def test_stale_project_pin_rejected(self):
  path=self.state();d=json.loads(path.read_text());d['retired']['naming']='0'*64;path.write_text(json.dumps(d))
  with self.assertRaisesRegex(ValueError,'stale-retirement'):self.view.read_view(state_path=path,unit_id='naming')
 def test_unrelated_meaning_update_preserves_local_binding(self):
  path=self.state(observations=[self.observation()]);old=self.data['revision']
  def change(d):next(u for u in d['records'] if u['id']=='layers')['body']+=' Additional reviewed qualification.'
  self.author(change);BUILD.build(self.root);self.assertNotEqual(old,json.loads(self.target.read_text())['revision']);result=self.view.read_view(state_path=path,unit_id='naming');self.assertEqual(result['projectEvidence'][0]['text'],self.observation()['text']);self.assertEqual(result['units'],[])
 def test_unrelated_source_envelope_update_preserves_unit_revisions(self):
  path=self.state(observations=[self.observation()]);ref=json.loads(self.authoring.read_text())['records'][0]['sources'][0];archive=self.root/ref['archive'];data=json.loads(archive.read_text());data['fixtureMetadata']='unrelated receipt envelope change';archive.write_text(json.dumps(data));BUILD.build(self.root);updated=json.loads(self.target.read_text());self.assertNotEqual(self.data['revision'],updated['revision']);self.assertEqual([u['revision'] for u in self.data['records']],[u['revision'] for u in updated['records']]);self.assertTrue(self.view.read_view(state_path=path,unit_id='naming')['projectEvidence'])
 def test_changed_meaning_requires_project_review(self):
  path=self.state()
  def change(d):next(u for u in d['records'] if u['id']=='naming')['body']+=' Reviewed meaning changed.'
  self.author(change);BUILD.build(self.root)
  with self.assertRaisesRegex(ValueError,'stale-retirement'):self.view.read_view(state_path=path,unit_id='naming')
 def test_corrupt_runtime_view_fails_closed(self):
  data=copy.deepcopy(self.data);data['records'][0]['body']='unreviewed change';self.target.write_text(json.dumps(data))
  with self.assertRaisesRegex(ValueError,'invalid-compiled-view'):self.view.read_view(unit_id='dimensions')
 def test_missing_required_condition_blocks_selected_meaning(self):
  result=self.view.read_view(state_path=self.state('identity'),unit_id='recovery');self.assertEqual(result['units'],[]);self.assertIn('unavailable-condition',result['unavailable'][0]['reason'])
 def test_body_free_tombstone_not_ordinary_advice(self):
  result=self.view.read_view(unit_id='legacy-dimension');self.assertEqual(result['units'],[]);self.assertNotIn('body',result['unavailable'][0])
 def test_legacy_family_pin_preserves_old_meaning(self):
  path=self.state();state=json.loads(path.read_text());state['family']='fab-design-system';path.write_text(json.dumps(state))
  result=self.view.read_view(state_path=path,unit_id='naming');self.assertEqual(result['units'],[]);self.assertIn('project-retired',result['unavailable'][0]['reason'])
 def test_legacy_family_cannot_retire_new_topic(self):
  path=self.state('layout-text-roles');state=json.loads(path.read_text());state['family']='fab-design-system';path.write_text(json.dumps(state))
  with self.assertRaisesRegex(ValueError,'stale-retirement'):self.view.read_view(state_path=path)
 def test_unknown_family_rejected(self):
  path=self.state();state=json.loads(path.read_text());state['family']='other';path.write_text(json.dumps(state))
  with self.assertRaisesRegex(ValueError,'invalid-project-state'):self.view.read_view(state_path=path)
 def test_query_uses_natural_russian_aliases(self):
  cases={'заголовок оторван':'layout-grouping','по тексту карточки':'layout-alignment','слишком много похожих текстовых стилей':'layout-text-roles','обрезается текст':'layout-adaptation'}
  for query,expected in cases.items():
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],expected)
 def test_no_match_does_not_fabricate_advice(self):
  self.assertEqual(self.view.read_view(query='астробиология')['units'],[])
 def test_query_does_not_leak_retired_body(self):
  result=self.view.read_view(state_path=self.state('layout-adaptation'),query='обрезается текст')
  self.assertNotIn('layout-adaptation',[u['id'] for u in result['units']]);self.assertTrue(result['unavailable']);self.assertNotIn('body',json.dumps(result))
 def test_cross_topic_link_returns_existing_meaning(self):
  result=self.view.read_view(unit_id='layout-text-roles',expand_related=True);self.assertIn('layers',[u['id'] for u in result['units']]);self.assertIn('layout-adaptation',[u['id'] for u in result['units']])
 def test_new_topics_cannot_access_original_reports(self):
  original=Path.read_text
  def guarded(path,*a,**kw):
   if path.name.endswith('.full.json'):raise AssertionError('Runtime opened archive')
   return original(path,*a,**kw)
  with patch.object(Path,'read_text',guarded):
   result=self.view.read_view(unit_id='layout-grouping');self.assertTrue(result['sourceReceipts']);self.assertIn('R040',result['units'][0]['body'])
 def test_invalid_discovery_metadata_fails_build(self):
  self.author(lambda d:next(u for u in d['records'] if u['id']=='layout-grouping').update(triggers={'not':'a list'}))
  with self.assertRaisesRegex(ValueError,'invalid-discovery-metadata'):BUILD.build(self.root)
 def test_legacy_family_cannot_attach_new_topic_observation(self):
  path=self.state();state=json.loads(path.read_text());state['family']='fab-design-system';obs=self.observation();obs['aboutUnit']='layout-adaptation';obs['unitRevision']=self.units['layout-adaptation']['revision'];state['observations']=[obs];path.write_text(json.dumps(state))
  with self.assertRaisesRegex(ValueError,'stale-local-evidence'):self.view.read_view(state_path=path)
 def test_product_queries_cross_source_boundaries(self):
  for query,key in [('один экран на сценарий','product-projections'),('контекст вызова','product-continuation'),('потерянное требование','slice-boundary'),('неизвестный результат','operation-outcome'),('полнота сценариев','coverage-sufficiency')]:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_operation_links_do_not_change_scoped_existing_knowledge(self):
  result=self.view.read_view(unit_id='operation-outcome',expand_related=True);ids={u['id'] for u in result['units']};self.assertTrue({'pending','recovery'}<=ids)
  self.assertEqual(next(u for u in result['units'] if u['id']=='pending'),self.units['pending'])
 def test_retiring_related_topic_does_not_create_false_prerequisite(self):
  result=self.view.read_view(state_path=self.state('operation-outcome'),unit_id='product-continuation')
  self.assertIn('product-continuation',[u['id'] for u in result['units']]);self.assertIn('operation-outcome',[u['id'] for u in result['unavailable']])
 def test_technical_dependency_queries_find_distinct_meanings(self):
  for query,key in [('техническая зависимость','technical-promise'),('сохранность данных','persistence-contract'),('глобальная ошибка','operation-connectivity'),('доставка уведомления','external-capability-evidence')]:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_enriched_outcome_revision_requires_review_without_global_invalidation(self):
  old=self.units['operation-outcome']['revision'];path=self.state('operation-outcome')
  self.author(lambda d:next(u for u in d['records'] if u['id']=='operation-outcome').update(body='Revised scoped result knowledge.'))
  BUILD.build(self.root)
  with self.assertRaisesRegex(ValueError,'stale-retirement'):self.view.read_view(state_path=path)
  self.assertEqual(self.view.read_view(unit_id='naming')['units'][0]['revision'],self.units['naming']['revision'])
 def test_related_dependency_not_a_hidden_prerequisite(self):
  result=self.view.read_view(state_path=self.state('persistence-contract'),unit_id='technical-promise')
  self.assertIn('technical-promise',[u['id'] for u in result['units']]);self.assertIn('persistence-contract',[u['id'] for u in result['unavailable']])
 def test_mobile_context_queries_resolve_specific_roles(self):
  for query,key in [('нужны ли вкладки','mobile-access-structure'),('настройки объекта','control-context-ownership'),('мобильная клавиатура','mobile-input-context'),('перенос на платформу','platform-transfer-boundary')]:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_mobile_references_keep_shared_meanings_available(self):
  result=self.view.read_view(unit_id='mobile-input-context',expand_related=True);self.assertIn('layout-adaptation',[u['id'] for u in result['units']])
  self.assertEqual(next(u for u in result['units'] if u['id']=='layout-adaptation'),self.units['layout-adaptation'])
 def test_local_mobile_retirement_does_not_retire_related_platform_topic(self):
  result=self.view.read_view(state_path=self.state('mobile-access-structure'),unit_id='platform-transfer-boundary')
  self.assertIn('platform-transfer-boundary',[u['id'] for u in result['units']]);self.assertIn('mobile-access-structure',[u['id'] for u in result['unavailable']])
 def test_mobile_expansion_does_not_hide_delivery_behind_object_settings(self):
  result=self.view.read_view(query='доставку уведомления');self.assertEqual(result['units'][0]['id'],'external-capability-evidence')
  broad={u['id'] for u in self.view.read_view(query='уведомления')['units']}
  self.assertTrue({'external-capability-evidence','control-context-ownership'}<=broad)
 def test_job_queries_distinguish_concepts_evidence_and_granularity(self):
  for query,key in [('работа или сценарий','job-concept-boundaries'),('гипотеза потребности','job-evidence-status'),('шаг или job','job-granularity')]:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_job_links_preserve_existing_slice_and_do_not_require_retired_concept(self):
  result=self.view.read_view(state_path=self.state('job-concept-boundaries'),unit_id='job-granularity',expand_related=True)
  self.assertIn('job-granularity',[u['id'] for u in result['units']]);self.assertIn('job-concept-boundaries',[u['id'] for u in result['unavailable']])
  self.assertEqual(next(u for u in result['units'] if u['id']=='slice-boundary'),self.units['slice-boundary'])
 def test_job_runtime_does_not_open_preserved_report(self):
  original=Path.read_text
  def guarded(path,*a,**kw):
   if path.name.endswith('.full.json'):raise AssertionError('Runtime opened archive')
   return original(path,*a,**kw)
  with patch.object(Path,'read_text',guarded):
   result=self.view.read_view(unit_id='job-evidence-status');self.assertTrue(result['sourceReceipts']);self.assertIn('job-evidence-status',[u['id'] for u in result['units']])
 def test_completed_topic_discovery_finds_practical_questions(self):
  cases=[('уровень абстракции','job-abstraction'),('метод исследования JTBD','job-research-method'),('четыре силы','job-alternatives-forces'),('анатомия Job Story','job-design-view'),('изменение потребности','rationale-impact'),('отказ в разрешении','permission-context'),('вход из уведомления','external-entry-context')]
  for query,key in cases:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_jtbd_extension_preserves_unrelated_meanings_and_local_binding(self):
  result=self.view.read_view(state_path=self.state('job-alternatives-forces'),unit_id='job-research-method',expand_related=True)
  self.assertIn('job-research-method',[u['id'] for u in result['units']]);self.assertIn('job-alternatives-forces',[u['id'] for u in result['unavailable']])
  self.assertEqual(next(u for u in result['units'] if u['id']=='coverage-sufficiency'),self.units['coverage-sufficiency'])
 def test_new_permission_meaning_retains_external_evidence_without_archive_io(self):
  original=Path.read_text
  def guarded(path,*a,**kw):
   if path.name.endswith('.full.json'):raise AssertionError('Runtime opened archive')
   return original(path,*a,**kw)
  with patch.object(Path,'read_text',guarded):
   result=self.view.read_view(unit_id='permission-context',expand_related=True);self.assertIn('external-capability-evidence',[u['id'] for u in result['units']])
 def test_default_unit_does_not_preload_association_bodies(self):
  result=self.view.read_view(unit_id='job-concept-boundaries')
  self.assertEqual([u['id'] for u in result['units']],['job-concept-boundaries'])
  self.assertIn('job-design-view',[u['id'] for u in result['related']])
  self.assertTrue(all('body' not in u and 'sources' not in u for u in result['related']))
  self.assertTrue(result['sourceReceipts'])
 def test_default_keeps_condition_and_contradiction_bodies(self):
  self.author(lambda d:next(u for u in d['records'] if u['id']=='layout-alignment')['relations'].update(contradicts=['job-granularity']))
  BUILD.build(self.root)
  result=self.view.read_view(unit_id='layout-alignment')
  ids={u['id'] for u in result['units']};self.assertTrue({'layout-alignment','layout-grouping','job-granularity'}<=ids)
  self.assertTrue(all('body' in u for u in result['units']))
 def test_compact_associations_do_not_leak_retired_meaning(self):
  result=self.view.read_view(state_path=self.state('job-design-view'),unit_id='job-concept-boundaries')
  self.assertNotIn('job-design-view',[u['id'] for u in result['related']])
  self.assertIn('job-design-view',[u['id'] for u in result['unavailable']])
  self.assertNotIn('body',json.dumps(result['related'])+json.dumps(result['unavailable']))
 def test_condition_chain_is_complete_without_related_expansion(self):
  self.author(lambda d:next(u for u in d['records'] if u['id']=='layout-grouping')['relations'].update({'applies-under':['naming']}))
  BUILD.build(self.root)
  result=self.view.read_view(unit_id='layout-alignment')
  self.assertIn('naming',[u['id'] for u in result['units']])
 def test_agentic_source_queries_distinguish_context_proof_authority_and_artifact(self):
  cases=[('контекст для агента','context-maintenance'),('что доказывает тест','verification-fit'),('нужно ли делегировать','automation-boundary'),('прототип вместо документа','artifact-role')]
  for query,key in cases:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_agentic_association_does_not_force_unrelated_policy_preload(self):
  result=self.view.read_view(unit_id='artifact-role')
  self.assertEqual([u['id'] for u in result['units']],['artifact-role'])
  self.assertIn('verification-fit',[u['id'] for u in result['related']])
 def test_first_value_queries_separate_result_path_help_and_measurement(self):
  cases=[('первая ценность','first-value-meaning'),('стартовый путь','entry-dependencies'),('нужны ли слайды','learning-aid-choice'),('цель сигнал метрика','goal-signal-metric')]
  for query,key in cases:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_first_value_associations_reuse_existing_permission_and_do_not_require_it(self):
  result=self.view.read_view(state_path=self.state('permission-context'),unit_id='entry-dependencies')
  self.assertIn('entry-dependencies',[u['id'] for u in result['units']]);self.assertIn('permission-context',[u['id'] for u in result['unavailable']])
 def test_paid_knowledge_discovery_separates_value_trial_access_and_external_rules(self):
  cases=[('модель монетизации','commercial-model'),('платная граница','paid-boundary'),('пробный доступ','trial-purpose'),('момент предложения','offer-context'),('платёж и доступ','entitlement-lifecycle'),('актуальность внешних правил','external-rule-freshness')]
  for query,key in cases:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_paid_access_reuses_uncertain_operation_without_claiming_it_a_prerequisite(self):
  result=self.view.read_view(state_path=self.state('operation-outcome'),unit_id='entitlement-lifecycle')
  self.assertIn('entitlement-lifecycle',[u['id'] for u in result['units']]);self.assertIn('operation-outcome',[u['id'] for u in result['unavailable']])
 def test_motivation_queries_find_fit_meaning_elements_progression_and_conflicts(self):
  cases=[('нужна ли геймификация','motivation-fit'),('внутренняя мотивация','motivation-meaning'),('баллы бейджи рейтинги','game-element-purpose'),('обратная связь и прогресс','feedback-progression'),('побочные эффекты наград','incentive-effects')]
  for query,key in cases:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_motivation_does_not_preload_general_effectiveness_as_a_prerequisite(self):
  result=self.view.read_view(state_path=self.state('verification-fit'),unit_id='motivation-fit')
  self.assertIn('motivation-fit',[u['id'] for u in result['units']]);self.assertIn('verification-fit',[u['id'] for u in result['unavailable']])
 def test_distribution_queries_distinguish_visitor_machinery_identity_proof_and_rights(self):
  cases=[('README первый запуск','repository-first-use'),('достаточный состав репозитория','repository-proportion'),('тег и релиз','release-identity'),('проверка установки из канала','delivery-verification'),('права на распространение','distribution-rights-scope')]
  for query,key in cases:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_delivery_related_proof_is_not_a_hidden_prerequisite(self):
  result=self.view.read_view(state_path=self.state('verification-fit'),unit_id='delivery-verification')
  self.assertIn('delivery-verification',[u['id'] for u in result['units']]);self.assertIn('verification-fit',[u['id'] for u in result['unavailable']])
 def test_completed_structure_and_coverage_queries_find_practical_decisions(self):
  cases=[('приоритет доступа','navigation-access'),('проверка структуры продукта','structure-evaluation'),('валидация формы','form-validity'),('техники сокращения тестов','test-case-selection')]
  for query,key in cases:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_coverage_does_not_require_locally_retired_related_technique(self):
  result=self.view.read_view(state_path=self.state('test-case-selection'),unit_id='coverage-sufficiency')
  self.assertIn('coverage-sufficiency',[x['id'] for x in result['units']]);self.assertIn('test-case-selection',[x['id'] for x in result['unavailable']])
 def test_timing_question_does_not_imply_a_scheduler_or_full_backend(self):
  self.assertEqual(self.view.read_view(query='точное время напоминания')['units'][0]['id'],'timing-contract')
  result=self.view.read_view(unit_id='timing-contract')
  self.assertEqual([x['id'] for x in result['units']],['timing-contract'])
  self.assertIn('external-capability-evidence',[x['id'] for x in result['related']])
 def test_interface_language_queries_do_not_collapse_into_layout_only(self):
  for query,key in [('понятные подписи','interface-wording'),('русский набор','russian-typesetting')]:
   with self.subTest(query=query):self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)

 def test_observed_cross_topic_discovery_gaps_remain_findable(self):
  cases=[('обрезка длинного заголовка','layout-adaptation'),
   ('равное количество пунктов в колонках','layout-grouping'),
   ('неизвестен результат оплаты','operation-outcome'),
   ('отличие шага от работы человека','job-granularity'),
   ('неясно создался ли объект после сбоя','recovery')]
  for query,key in cases:
   with self.subTest(query=query):
    self.assertIn(key,[u['id'] for u in self.view.read_view(query=query)['units'][:5]])

 def test_design_family_queries_find_decision_owners(self):
  cases=[('общее ядро и домен','system-reuse'),('контракт компонента','component-contract'),
   ('взрыв variants','context-axes'),('из концепта в систему','concept-extraction'),
   ('тонкая обёртка','behavior-foundation'),('миграция дизайн системы','system-evolution'),
   ('роль имя фокус','accessible-interaction'),('SSR гидратация','browser-integration'),
   ('токен переменная стиль','token-projection')]
  for query,key in cases:
   with self.subTest(query=query):
    self.assertEqual(self.view.read_view(query=query)['units'][0]['id'],key)
 def test_related_native_state_retirement_does_not_hide_component_contract(self):
  result=self.view.read_view(state_path=self.state('native-state'),unit_id='component-contract')
  self.assertIn('component-contract',[u['id'] for u in result['units']])
  self.assertNotIn('native-state',[u['id'] for u in result['units']])
  self.assertIn('native-state',[u['id'] for u in result['unavailable']])
if __name__=='__main__':unittest.main()
