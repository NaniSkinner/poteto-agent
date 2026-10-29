# Original evidence and acceptance

The worker preserves its reads/results; the coordinator checks completeness before startup release and before accepting independent review. Keep records in the approved task output root, outside the reusable package. Apply target privacy/retention rules first; capture authority is not permission to retain excluded content. Choose safe inputs and content-free extraction where required, rather than exporting protected raw data to make a receipt complete.

## Capture at the call boundary

For each load-bearing call, save a record with these fields:

- `id`: local stable record ID and host call/chunk ID when exposed.
- `tool` and `arguments`: exact invoked tool and structured arguments, including command/cwd for shell calls. Do not reconstruct a command from stdout.
- `result`: actual returned object or an immutable file containing its complete serialized value. Preserve errors, exit/status, truncation flags and original fields. JSON serialization preserves values; it is not a byte-for-byte claim about transport encoding. Never use a prose recap as this field.
- `capture_kind`: `original-tool-return`, `supported-history-export`, `fresh-source-copy`, or `authored-summary`. Keep separate records for different classes.
- `coverage`: the exact files/ranges/artifact revision checked, completeness and any unavailable fields. Link the load-bearing requirement/claim to the appropriate record.

When tools run through an orchestration wrapper, assign the returned object, save it immediately with its invocation arguments to a new task-owned file, and display only the necessary bounded excerpt. Await the save before another dependent operation. Use structured file-writing tools or safe serialization; do not embed large transcripts in shell strings or parse file paths back out of shell commands. Do not repeat the original mistake of turning shell punctuation into filename text.

If direct tools cannot expose complete objects, preserve the supported transcript/export with exact limits and label it correctly. Never scrape private host stores. The inability to obtain original envelopes is a limitation, not proof the call failed. Original final responses and immutable artifacts can still establish their own scoped content.

## Bounded reads and repairs

Before a large read, determine file size/line count and use numbered sections or separate file reads sized to fit the tool and capture budget. Preserve each actual return. If an original result is truncated, read only the missing required sections and preserve those new returns before proceeding. If only a later history export is truncated, do not infer that the original model read was truncated; recover additional supported coverage when possible and retain the export limit.

Fresh source copies prove current bytes, not earlier activity. Label a late new read with its actual sequence, retain the failed/incomplete record and do not backdate it. Do not rerun product operations or paid/mutating calls just to recreate a missing receipt; return the narrow limitation and any separately required authority instead.

## Coordinator acceptance

For startup and again for independent review, record `accepted`, `needs-bounded-repair`, or `provisional` with evidence locators for:

1. Current required instruction/source coverage, exact scope/revision and returned result records.
2. Original checkpoint or reviewer completion, material findings and the primary evidence supporting them.
3. Output ownership/handling and permissions actually checked, retaining unknown sync/access controls.
4. Dispatch/release ordering and available role/fork evidence. Requested settings remain separate from host-enforced attestation.

Missing essential instruction/source coverage or missing exact candidate/review output means `needs-bounded-repair`; withhold the affected release or completed-review claim. Request only missing reads/records or a bounded clarification. If the host exposes no stronger metadata, preserve `provisional` for that metadata and continue permitted work without claiming stronger independence. Unavailable nonessential metadata need not block all useful work. Inspect saved files and confirm their identity/coverage; a worker saying “saved” is insufficient. Do not silently replace originals or treat a later summary as a repaired original. Keep final reporting at the weakest material evidence level.

Made with 🍵
