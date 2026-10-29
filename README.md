# Poteto candidate 1.0.0

Public source package; not yet installed or accepted for real work. Role `workflow-advisor`, display Poteto, entry `poteto-advisor`. The actual role is currently unavailable. This package does not modify Pstack, global Codex configuration or upstream `pstack-poteto-agent`.

The canonical model-agnostic contract is `poteto-advisor/references/contract.md`; the thin entry discovers and dispatches it. Coordinator and evaluation references define host integration and promotion evidence. Generic continuity is orientation, not live authority. Private project reports, tool returns, review receipts and session exports belong in approved task storage outside this source.

Requires Python 3.11+ (stdlib only). From this directory:

```sh
python3.12 -m unittest discover -s tests -v
python3.12 scripts/manage.py render
python3.12 scripts/manage.py check
```

`render` writes only `codex/workflow-advisor.toml` beneath the selected source, creating it exclusively; an identical existing file is untouched and any differing file is refused. Reconcile an owned stale candidate manually before regeneration. Linked destinations are refused. `check` is read-only and catches exact contract/path/profile drift. `--source PATH` selects a local package; there is no install command. The generated candidate embeds the canonical contract and exact current source path; moving the package requires deliberate regeneration. These checks prove file consistency, not runtime behavior or semantic reliability.

Before installation: freeze controlled expectations, retain baseline/treatment outputs separately, obtain fresh independent review, and test the actual registered desktop role. Public source publication is authorized. No role launch, real-work pilot, installation or team rollout is claimed. Installation requires a separate decision. Generated machine-specific profiles are ignored by Git; render a local candidate from your own checkout.

Made with 🍵
