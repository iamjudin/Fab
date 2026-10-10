# Design systems — operational brief

Read when repeated components, multiple themes or design/code divergence makes
reuse valuable. Detailed source: [design-systems.full.json](design-systems.full.json).

- Distinguish tokens, components, composed patterns and product-specific
  extensions. Semantic tokens connect a decision to its use, including themes.
- Start from repeated product needs. Define component anatomy, relevant states,
  behaviour and accessibility alongside appearance; variants alone are insufficient.
- Keep design and code meaning aligned, including theme, focus, disabled and
  error states where relevant. Test representative compositions, not only atoms.
- Give shared decisions an owner and an update path. A solo product can use
  lightweight governance; enterprise processes are examples, not prerequisites.
- Prefer existing platform conventions where appropriate; avoid building a
  comprehensive library before a chosen slice supplies actual needs.

Read R003–R010 for scope/build method, R011–R019 for design organisation and
quality, R027–R036 for extension/metrics, R037 onward for sources. Company cases
R020–R026 illustrate practices; they do not prove benefit in a particular project.

Structural method reviewed; current Figma/vendor APIs, numeric rules and
performance claims not exhaustively verified. Refresh against primary platform
documentation when used. Theme/widget/runtime feasibility belongs to Technical
Strategy as well as design; a token model does not prove OS integration.
