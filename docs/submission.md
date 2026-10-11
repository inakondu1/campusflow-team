# CampusFlow submission links and verified evidence

Prepared from the complete Fellows' Engineering Guide. This packet is not
yet a completed submission: the reviewed integration and individual evidence
remain outstanding.

Repository main: https://github.com/mordecai12-cool/campusflow2/tree/main
Engineer A's existing PR: https://github.com/mordecai12-cool/campusflow2/pull/1
Engineer B's integration PR: https://github.com/mordecai12-cool/campusflow2/pull/2

## Current verification

| Snapshot | Unittest result | Extra contract checks | Scope |
| --- | --- | --- | --- |
| main: 3f068e38d4bf478033415c79b22e18ea11275093 | 15 passed | 2 passed, 5 failed | Current published main; not the completed integration |
| Integration source: daf51ad581bb8fe3e76d3107a38c0f1bdc8288e3 | 66 passed | 7 passed | PR #2 application and tests; not merged |

The assistant actually ran these commands. Evidence: [main test output](main-test-output.txt),
[branch test output](test-output.txt), [main contract checks](main-contract-checks.txt),
[branch contract checks](integration-contract-checks.txt), [demo output](demo-output.txt).
Syntax checks also passed. Subsequent submission-documentation commits do not
change the application or tests; their CI must still pass before merge.

## Guide requirements and remaining actions

| Area | Marks | Verified preparation | Required completion |
| --- | --- | --- | --- |
| Functional implementation | 40 | Integration implements F1-F7 and fixes reproduced main defects | Review and merge, then demonstrate from main |
| Testing and reliability | 15 | 66 branch tests; current main and independent probes recorded | Run full suite on final approved main and record exact SHA/output |
| Professional Git workflow | 20 | Both PR links and original authors are verified | Genuine code/test PR per fellow; two substantive cross-review observations each; final approval before merge |
| AI-native engineering | 20 | Existing logs retained; assistant executions and authorship disclosed | Three actual interactions per fellow, independent results, and a verified correction/improvement/rejection each |
| Technical defence | 5 | README, contracts, demo and defence prompts available | Both fellows explain their work and demonstrate it together |

PR #1 is already merged without recorded review and changes only cache files.
Do not describe retrospective comments as approval before merge. Mordecai
needs a genuine application-and-test PR for his reviewed contribution.
PR #2 needs Mordecai's actual review and approval. Michael's AI-assisted work
must be distinguished from his personally written code and tests.

The five contracts are documented in design-decisions.md; neither fellow's
actual agreement is asserted. Personal prompts, independent experiments and
actual agreement details have been requested in chat and remain pending.

## Finish in this order

1. Both fellows supply actual contribution and learning evidence and discuss
   the five documented contracts. Record the real date and decisions.
2. Mordecai inspects PR #2's final code and checks, leaves at least two
   substantive observations, requests fixes if needed, then approves the
   final tested head. Michael must not approve his own PR.
3. Merge PR #2 only after that approval and passing checks. Mordecai then
   completes a genuine code-and-test change from updated main on an issue
   branch and authors his own PR. Michael reviews that real diff and leaves
   two substantive observations before approving satisfactory final changes.
4. Merge the approved contribution. Fetch final main into a clean checkout,
   record `git rev-parse HEAD`, run `python3 -m unittest discover -s tests -v`,
   syntax checks and `python3 run.py --demo`. Retain actual results.
5. Update this packet with the final main SHA, results and both qualifying
   reviewed PR links. Submit those links and demonstrate both contributions.

No historical commits, individual experiments, reviews or signatures are
fabricated by this packet. miikese/campusflow remains the reference repository.
