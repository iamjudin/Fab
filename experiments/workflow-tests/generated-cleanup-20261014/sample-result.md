# CSV summary

Source: input.csv

Rows: 4 · Columns: 3

Parsing: encoding utf-8-sig, delimiter ','; values trimmed.

| Column | Present | Missing | Summary |
| --- | ---: | ---: | --- |
| group | 4 | 0 | 2 distinct; top 2: A (2); B (2) |
| value | 3 | 1 | Numeric: min 10, max 30, mean 20 |
| note | 3 | 1 | 3 distinct; top 3: first, row (1); kept &lt;tag&gt; (1); two<br>lines (1) |

## Preview (first 5 rows)

| group | value | note |
| --- | --- | --- |
| A | 10 | first, row |
| A | 20 |  |
| B |  | kept &lt;tag&gt; |
| B | 30 | two<br>lines |

Statistics cover all accepted rows and exclude missing cells. Means may be rounded; top values and preview are partial. No units, dates, causes or trends are inferred.

## Interpretation and limits

The supplied table contains two records each for groups A and B. The three present values are 10, 20 and 30, with an unweighted mean of 20; one value and one note are missing. Group B has only one observed numeric value, so its missing value limits comparisons. These four records do not establish population patterns, trends, causes or business meaning. No units, dates, sampling method or population context are supplied.

## Continuation provenance

The interrupted job's working input copy was verified byte-for-byte against the retained `input.csv`. Its parse notes confirmed four records, three columns, one missing numeric value and no basis for population trends or causes. The report was generated with the bundled standard-library helper and verified against a fresh helper output and the original source.

Source SHA-256: `36664d731da3afa37cce2f1d06e222478eb8459c948680b7cf5d22e0ffc482f6`.

Cleanup: removed only the job-state-listed disposable files `work/job-01/input-copy.csv` and `work/job-01/observations.md` after retaining their useful findings here. Removed the empty task directory. The package, original input, job state and neighboring files were preserved. This task verifies this data summary; it makes no package or installed-host readiness claim.
