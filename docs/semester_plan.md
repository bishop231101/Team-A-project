# CS481 Capstone Semester Project Plan

## Project Information

- **Project:** Project 5 — Zero-Width Unicode Steganography with Social-Media Robustness Engineering
- **Course:** CS481 Capstone Project
- **Semester:** Fall 2026
- **Team:** Team A
- **Team members:**
  - Ifeanyi Emeka — Team Leader
  - Henry Smith — Team Member A
  - Tristan Koch — Team Member B

## Project Objective

Build and evaluate a Python-based steganography system that hides secret messages in ordinary cover text using invisible zero-width Unicode characters. The team will test whether encoded messages survive copying, pasting, posting, editing, and retrieving text on multiple platforms. The project will measure character-survival and message-recovery rates and will add Reed–Solomon, Hamming, or another justified error-correction method to improve recovery when zero-width characters are removed, inserted, reordered, or corrupted.

## Success Criteria

The project will be considered successful when the team has:

1. A documented Python encoder and decoder that pass automated unit tests.
2. A repeatable platform-testing procedure covering at least eight platforms.
3. A versioned dataset containing baseline and error-corrected test results.
4. Quantitative measurements of zero-width character survival and complete-message recovery.
5. An implemented error-correction mode with measured benefits and limitations.
6. A compatibility matrix, charts, final report, presentation, and reliable live demo.
7. A clean GitHub repository with reviewed code, documentation, tests, issues, and tagged releases.

## Team Responsibilities and Weekly Task Ownership

| Team member | Primary ownership | Supporting responsibilities |
|---|---|---|
| **Ifeanyi Emeka** | Project coordination, weekly plan, testing strategy, compatibility matrix, integration, meeting minutes, and pull-request review | Requirements, risk management, report editing, presentation coordination, release management, and demo narration |
| **Henry Smith** | Encoder, decoder, error-correction implementation, and codec unit tests | Technical documentation, test-vector design, debugging platform failures, demo operation, and results interpretation |
| **Tristan Koch** | Platform-testing tools, cross-platform experiments, survival statistics, charts, and compatibility results | Dataset maintenance, automation, reproducibility documentation, presentation visuals, and demo validation |

Every task has one accountable owner. Supporting work does not transfer accountability from the listed owner. Ifeanyi tracks assignments in GitHub issues and confirms acceptance criteria during the weekly planning meeting.

## Standard Engineering and Testing Practices

- Use Python 3 and a documented virtual environment or dependency file.
- Work through GitHub issues and short-lived feature branches; do not commit feature work directly to the main branch.
- Require at least one teammate review before merging a pull request. Ifeanyi performs final integration review; another member reviews Ifeanyi's substantive changes.
- Run the complete automated test suite before every merge and release tag.
- Store reusable test vectors separately from application logic.
- Record platform name, platform version or access date, operating system, browser/app, test operation, original payload, observed payload, trial number, and result.
- Do not place real secrets, credentials, or private conversations in test data. Use synthetic messages only.
- Preserve raw results; perform cleaning and aggregation in separate reproducible scripts.
- Document manual steps and limitations whenever platform automation is prohibited, unreliable, or unavailable.

## Week-by-Week Plan

### Week 2 — Project Selection, Scope, and Planning

- **Tasks:** Ifeanyi creates the charter, semester schedule, issue labels, meeting process, risks, and definition of done. Henry researches candidate zero-width characters, Unicode normalization behavior, framing methods, and encoding schemes. Tristan researches candidate platforms, test constraints, measurable robustness metrics, and manual versus automated test methods. The team agrees on an initial scope and ethical-use statement.
- **Person responsible:** Ifeanyi (plan and charter); Henry (Unicode/codec research); Tristan (platform/testing research); all members (scope approval).
- **Expected output:** Approved charter, role matrix, preliminary architecture, candidate character set, initial platform list, risk register, ethics statement, and semester backlog.
- **Milestone:** **M1 — Project scope and team operating plan approved.**
- **Testing requirements:** Run small exploratory trials for each candidate zero-width character in local Python strings; verify length, UTF-8 round trip, file round trip, and Unicode normalization behavior. Record findings rather than treating exploration as production validation.
- **GitHub deliverables:** `README.md` skeleton, project plan, `docs/project-charter.md`, `docs/ethics-and-scope.md`, research notes, issue templates, initial labeled issues, and a Week 2 meeting-minutes file.

### Week 3 — Basic Encoder Design and Implementation

- **Tasks:** Henry defines the bit-to-character mapping, payload framing, UTF-8 conversion, and encoder API, then implements the first encoder. Ifeanyi reviews requirements and creates an integration checklist. Tristan creates initial test vectors and a local text round-trip harness.
- **Person responsible:** Henry (encoder); Ifeanyi (requirements/review); Tristan (test vectors/harness).
- **Expected output:** Encoder module that converts a secret message into a deterministic zero-width sequence and embeds it in cover text; documented format specification; representative test vectors.
- **Milestone:** Encoder produces deterministic stego text for ASCII and Unicode payloads.
- **Testing requirements:** Unit-test empty, short, long, ASCII, emoji, accented, and multilingual messages; confirm cover text remains visibly unchanged; test deterministic output and invalid input handling.
- **GitHub deliverables:** Encoder feature branch and reviewed pull request, format specification, test-vector fixture, Week 3 issues/project-board update, and meeting minutes.

### Week 4 — Decoder and End-to-End Local Prototype

- **Tasks:** Henry implements extraction, framing validation, decoding, and clear error reporting. Tristan expands the harness to compare sent and recovered payloads and records baseline local results. Ifeanyi integrates modules, defines command-line behavior, and verifies documentation.
- **Person responsible:** Henry (decoder and codec tests); Tristan (round-trip harness/results); Ifeanyi (integration and CLI acceptance).
- **Expected output:** Working local encode/decode pipeline, usable command-line prototype, codec documentation, and automated unit tests.
- **Milestone:** **M2 — Basic encoder/decoder prototype complete.**
- **Testing requirements:** End-to-end tests must cover empty cover text, punctuation, line breaks, repeated encoding, malformed sequences, truncated payloads, unknown zero-width characters, UTF-8 file I/O, and at least 100 generated round trips. Establish an agreed minimum automated-test baseline before release.
- **GitHub deliverables:** Decoder and CLI pull requests, automated test suite, usage examples, updated README, continuous-integration workflow if available, and `v0.1.0` prototype tag.

### Week 5 — Four-Platform Pilot Study

- **Tasks:** Tristan executes a controlled pilot on four selected platforms using the agreed test corpus and operations. Ifeanyi finalizes the test protocol and platform-result schema. Henry investigates decoding failures and adds diagnostic output without tailoring the codec to a single platform.
- **Person responsible:** Tristan (experiment execution); Ifeanyi (protocol and matrix); Henry (failure diagnosis).
- **Expected output:** Pilot dataset, four preliminary platform profiles, failure taxonomy, and revisions to the testing procedure.
- **Milestone:** **M3 — Four-platform pilot completed.**
- **Testing requirements:** On each platform, perform multiple trials for short ASCII, Unicode, and longer payloads; test at least direct copy/paste and post/retrieve workflows where permitted. Calculate zero-width character survival and exact-message recovery rates. Record app/browser and test date.
- **GitHub deliverables:** Versioned protocol, CSV result schema, sanitized raw pilot data, pilot-analysis script/notebook, four platform notes, issues for discovered defects, and meeting minutes.

### Week 6 — Expand Testing and Build Automation

- **Tasks:** Tristan adds at least two platforms and begins a reusable test runner for payload generation, comparison, and result logging. Henry makes codec interfaces stable for the runner and improves diagnostic classifications. Ifeanyi reviews platform coverage, permissions, reproducibility, and risk status.
- **Person responsible:** Tristan (new platforms and runner); Henry (stable interfaces/diagnostics); Ifeanyi (coverage and compliance review).
- **Expected output:** Results from at least six platforms, reusable corpus generator, structured result logger, and revised failure categories.
- **Milestone:** Platform test system supports repeatable data collection.
- **Testing requirements:** Validate the runner against known unchanged, deleted-character, inserted-character, and substituted-character fixtures. Manually audit a sample of generated records. Ensure no automation violates platform terms or exposes credentials.
- **GitHub deliverables:** Test-runner pull request, corpus/config files, data dictionary, results from new platforms, automation setup guide, and updated compatibility matrix.

### Week 7 — Eight-Platform Coverage and Automation Stabilization

- **Tasks:** Tristan expands coverage to at least eight platforms and repeats inconsistent trials. Henry creates a corruption simulator for deletion, insertion, and substitution patterns. Ifeanyi performs a mid-semester scope and integration review and freezes the baseline experimental protocol.
- **Person responsible:** Tristan (eight-platform dataset); Henry (corruption simulator); Ifeanyi (protocol freeze and review).
- **Expected output:** Baseline dataset covering at least eight platforms, stable test runner, corruption simulator, and protocol version 1.0.
- **Milestone:** **M4 — Minimum eight-platform baseline achieved.**
- **Testing requirements:** Use consistent payloads and trial counts across platforms; verify data completeness; repeat outliers; regression-test the codec and runner; compare simulated corruption classifications with selected observed failures.
- **GitHub deliverables:** Eight-platform result set, test protocol v1.0, corruption-simulator pull request, data-validation report, updated risk register, and `v0.2.0` testing-system tag.

### Week 8 — Midterm Report and Demonstration

- **Tasks:** Ifeanyi leads the midterm report, consolidates progress against plan, and documents risks and changes. Henry writes the architecture and codec sections. Tristan creates baseline charts and writes the testing-method and preliminary-results sections. The team rehearses a short prototype demonstration.
- **Person responsible:** Ifeanyi (report owner/editor); Henry (technical sections/demo encoder); Tristan (methods, results, and charts).
- **Expected output:** Complete midterm report, reproducible figures, current compatibility matrix, and working prototype demo.
- **Milestone:** **M5 — Midterm report submitted.**
- **Testing requirements:** Run full regression tests; rerun representative trials from at least two platforms; independently verify all numbers and chart labels; complete one timed demo rehearsal with a saved fallback example.
- **GitHub deliverables:** Versioned midterm-report source, generated figures, report references, reproducibility instructions, demo script, resolved midterm issues, and a midterm release tag.

### Week 9 — Controlled Survival-Rate Data Collection

- **Tasks:** Tristan begins the full controlled experiment using the frozen protocol and balanced test corpus. Ifeanyi audits data quality and maintains the compatibility matrix. Henry supports failure analysis and verifies decoder behavior on recovered sequences.
- **Person responsible:** Tristan (data collection); Ifeanyi (quality audit/matrix); Henry (decoder validation).
- **Expected output:** First half of the production dataset, trial log, anomaly list, and preliminary aggregate statistics.
- **Milestone:** Production data collection is at least 50% complete.
- **Testing requirements:** Meet the agreed trial count for at least half of the platform-operation combinations; use exact-match recovery and character-survival metrics; check missing fields, duplicates, impossible values, and manual transcription errors.
- **GitHub deliverables:** Sanitized raw-data batch 1, validation output, analysis-script updates, compatibility-matrix update, anomaly issues, and meeting minutes.

### Week 10 — Complete Baseline Data and Statistical Analysis

- **Tasks:** Tristan completes baseline trials, reruns anomalies, calculates aggregate statistics, and drafts charts. Ifeanyi signs off dataset completeness and documents threats to validity. Henry confirms whether codec defects affected any trials and supplies fixes with regression tests if needed.
- **Person responsible:** Tristan (dataset/statistics); Ifeanyi (audit and validity); Henry (codec integrity).
- **Expected output:** Complete baseline dataset, survival-rate tables, exact-recovery results, confidence summaries where appropriate, charts, and limitations log.
- **Milestone:** **M6 — Baseline survival-rate study complete.**
- **Testing requirements:** Independently spot-check raw-to-summary calculations; rerun every unexplained outlier; compare analysis output with hand-calculated samples; run the full software suite after any defect fix; preserve pre-fix results if they remain analytically relevant.
- **GitHub deliverables:** Baseline dataset release, analysis code, generated charts, statistical summary, threats-to-validity document, updated matrix, and `v0.3.0` baseline-results tag.

### Week 11 — Error-Correction Design and Implementation

- **Tasks:** Henry compares Reed–Solomon and Hamming approaches against observed corruption patterns, records the design decision, and implements the selected method behind an optional codec mode. Tristan converts observed platform failures into reproducible corruption fixtures. Ifeanyi reviews tradeoffs involving overhead, payload capacity, compatibility, and scope.
- **Person responsible:** Henry (design and implementation); Tristan (observed-error fixtures); Ifeanyi (design review).
- **Expected output:** Error-correction design record, working implementation, overhead analysis, and unit-test fixtures based on observed failures.
- **Milestone:** Error-correction mode encodes and recovers payloads under defined corruption limits.
- **Testing requirements:** Test no-error decoding, correctable and uncorrectable corruption, boundary conditions, Unicode payloads, deterministic behavior, false-success prevention, and backward compatibility with baseline mode. Measure encoded-length overhead.
- **GitHub deliverables:** Architecture decision record, error-correction pull request, fixture set, unit tests, benchmark script, documentation, and updated issues.

### Week 12 — Error-Correction Recovery Experiments

- **Tasks:** Henry stabilizes error correction and addresses defects. Tristan runs controlled simulated-corruption tests and selected real-platform retests with baseline and protected modes. Ifeanyi verifies experimental fairness and integrates the protected mode into the CLI and documentation.
- **Person responsible:** Henry (stabilization); Tristan (comparative experiments); Ifeanyi (integration and fairness review).
- **Expected output:** Comparative recovery dataset, recovery curves/tables, overhead-versus-benefit analysis, integrated protected mode, and documented limitations.
- **Milestone:** **M7 — Error-correction implementation and evaluation complete.**
- **Testing requirements:** Use identical payloads and corruption conditions for baseline and protected modes; test multiple corruption rates and patterns; run repeated trials; report exact recovery, partial recovery, detected failure, and undetected-error outcomes separately.
- **GitHub deliverables:** Comparative dataset, recovery-analysis code, charts, integration pull request, CLI documentation, full regression results, and `v0.4.0` error-correction tag.

### Week 13 — Compatibility Matrix and Final Statistics

- **Tasks:** Tristan finalizes statistics, charts, and reproducibility artifacts. Ifeanyi completes the compatibility matrix and reconciles every reported value with the dataset. Henry performs a code-quality pass, improves diagnostics, and documents algorithm constraints.
- **Person responsible:** Tristan (statistics/charts); Ifeanyi (matrix and verification); Henry (code quality/technical limits).
- **Expected output:** Final compatibility matrix, publication-ready figures and tables, reproducible analysis package, and release-candidate software.
- **Milestone:** **M8 — Analysis and compatibility results frozen.**
- **Testing requirements:** Rebuild every table and chart from raw data; peer-review calculations; run linting/static checks if configured; execute all unit, integration, corruption, and CLI tests; verify installation on a clean environment.
- **GitHub deliverables:** Final analysis pull request, compatibility matrix, figure sources, clean-environment verification notes, release-candidate checklist, and `v0.9.0-rc1` tag.

### Week 14 — Final Report Draft and Presentation Storyboard

- **Tasks:** Ifeanyi assembles and edits the full report and manages citations. Henry completes implementation, architecture, error-correction, and technical-limit sections. Tristan completes methodology, results, chart captions, and platform-compatibility sections. The team develops the presentation storyboard and assigns speakers.
- **Person responsible:** Ifeanyi (report/editor and storyboard owner); Henry (technical writing); Tristan (experimental writing and visuals); all members (peer review).
- **Expected output:** Complete first report draft, citation list, presentation outline, slide ownership, and list of evidence needed for final claims.
- **Milestone:** Full report draft and presentation storyboard completed.
- **Testing requirements:** Trace every quantitative claim to a dataset/table; verify references and captions; perform report peer review; run regression tests and a clean installation; execute one full demo dry run.
- **GitHub deliverables:** Report draft, bibliography/source file, slide outline, claim-to-evidence checklist, review issues, demo checklist, and Week 14 minutes.

### Week 15 — Final Report, Presentation, and Demo Readiness

- **Tasks:** Ifeanyi incorporates reviews, freezes the report, coordinates slide integration, and manages final release readiness. Henry prepares the technical/demo segments and a recovery example. Tristan finalizes charts, compatibility visuals, and demo result verification. Every member practices assigned speaking sections and Q&A.
- **Person responsible:** Ifeanyi (final documents/release); Henry (technical demo); Tristan (visuals/result verification); all members (rehearsal).
- **Expected output:** Submission-ready report, polished slide deck, tested demo, backup recording/screenshots, Q&A bank, and release candidate.
- **Milestone:** **M9 — Final submission package ready.**
- **Testing requirements:** Complete at least two timed full-team rehearsals; test the demo on the presentation machine/network; test offline fallback; verify fonts, links, code size, and chart readability; perform final security/privacy review; run the complete test suite.
- **GitHub deliverables:** Final report source/export, final slides source/export, demo instructions, backup demo artifacts, Q&A notes, release notes, passing CI evidence, and `v1.0.0-rc1` tag.

### Week 16 — Final Presentation and Project Closeout

- **Tasks:** The team delivers the presentation and live demo. Ifeanyi leads introductions, project motivation, conclusions, and Q&A coordination. Henry explains the codec and error correction and operates or supports the live encoding/decoding demo. Tristan explains the experiment, compatibility matrix, and statistics. Afterward, Ifeanyi closes issues and archives project materials.
- **Person responsible:** Ifeanyi (presentation lead/closeout); Henry (technical explanation/demo); Tristan (results explanation/demo validation); all members (Q&A).
- **Expected output:** Final presentation, successful live or fallback demo, submitted final report, stable final repository, and closeout/lessons-learned record.
- **Milestone:** **M10 — Final presentation and capstone project completed.**
- **Testing requirements:** Perform same-day smoke tests on the encoder, decoder, protected mode, demo inputs, presentation file, display connection, and fallback artifacts. After release, verify that a fresh clone can follow the documented setup and reproduce the core local demo.
- **GitHub deliverables:** Final tagged `v1.0.0` release, archived final artifacts, reproducibility guide, closed/moved issues, final compatibility matrix, final meeting minutes, and lessons-learned document.

## Major Project Milestones

| ID | Target week | Milestone | Exit criteria |
|---|---:|---|---|
| M1 | 2 | Scope and operating plan approved | Roles, scope, risks, schedule, and test direction documented |
| M2 | 4 | Basic encoder/decoder prototype | Local round trip and automated codec tests pass |
| M3 | 5 | Four-platform pilot | Four platform profiles and pilot dataset completed |
| M4 | 7 | Eight-platform baseline | At least eight platforms tested with protocol v1.0 |
| M5 | 8 | Midterm submission | Report, figures, matrix, and prototype demo ready |
| M6 | 10 | Baseline survival study | Production baseline dataset and statistics completed |
| M7 | 12 | Error-correction evaluation | Protected mode implemented and compared with baseline |
| M8 | 13 | Results freeze | Matrix, statistics, figures, and release candidate verified |
| M9 | 15 | Final package ready | Report, slides, demo, fallback, and release candidate pass review |
| M10 | 16 | Capstone completion | Presentation delivered and final repository released |

## Project Timeline by Phase

| Phase | Weeks | Main outcome |
|---|---|---|
| Initiation and research | 2 | Approved scope, roles, risks, and technical/test direction |
| Core prototype | 3–4 | Functional Python encoder, decoder, CLI, and unit tests |
| Platform pilot and expansion | 5–7 | Repeatable protocol and baseline coverage of at least eight platforms |
| Midterm checkpoint | 8 | Midterm report and prototype demonstration |
| Baseline measurement | 9–10 | Complete survival/recovery dataset and statistical analysis |
| Robustness engineering | 11–12 | Implemented and evaluated error-correction mode |
| Results finalization | 13 | Compatibility matrix and final statistics frozen |
| Final communication | 14–15 | Final report, presentation, demo, and release candidate |
| Presentation and closeout | 16 | Final delivery, `v1.0.0`, and project archive |

## Meeting and Communication Schedule

### Recurring Meetings

| Meeting | Suggested time | Participants | Purpose | Required record |
|---|---|---|---|---|
| Weekly planning meeting | Monday, 30–45 minutes | All members | Review last week, assign issues, confirm acceptance criteria, identify blockers | Agenda, assignments, and updated project board |
| Technical/testing sync | Wednesday, 20–30 minutes | All members | Review codec changes, experiment status, failures, and integration needs | Brief decisions/actions note |
| Weekly review and demo | Friday, 30–45 minutes | All members | Demonstrate completed work, review pull requests, verify tests, and update risks | Meeting minutes, test status, and milestone status |
| Extra rehearsal | Weeks 8, 14, 15, and 16 | All members | Practice reports, presentation, Q&A, and demo recovery | Timed rehearsal log and correction list |

Ifeanyi chairs meetings and maintains minutes. The note-taker may rotate, but Ifeanyi remains accountable for posting minutes within 24 hours. Members report blockers as soon as they arise rather than waiting for the next meeting.

### Weekly Status Format

Each member reports:

1. Work completed and links to issues/pull requests.
2. Test evidence and results produced.
3. Work planned for the next week.
4. Blockers, risks, and decisions needed.
5. Estimate of milestone status: on track, at risk, or blocked.

## GitHub Workflow and Deliverable Standards

1. Ifeanyi creates milestone-linked GitHub issues with an owner, due week, acceptance criteria, and test requirements.
2. Branch names use a consistent form such as `feature/encoder`, `test/platform-runner`, or `docs/final-report`.
3. Pull requests describe the change, linked issue, test commands, results, data/schema effects, and documentation changes.
4. At least one teammate reviews each pull request; all requested changes are resolved before merge.
5. The main branch should remain runnable, documented, and covered by tests.
6. Experiment data is committed only after removing credentials, account identifiers, and private content. Large files use an agreed repository-safe storage method.
7. Releases are tagged at the prototype, testing, baseline-results, error-correction, release-candidate, and final stages.
8. Meeting minutes, protocol revisions, design decisions, and limitations are version controlled alongside the code.

## Measurement Plan

The final analysis will report at minimum:

- **Zero-width character survival rate:** surviving expected zero-width characters divided by transmitted zero-width characters, with the comparison method documented.
- **Exact-message recovery rate:** trials in which the decoded secret exactly matches the original divided by total valid trials.
- **Detected-failure rate:** trials that fail safely with an explicit integrity/decoding error.
- **Undetected-error rate:** trials that return an incorrect message without detecting failure.
- **Error-correction improvement:** protected-mode recovery rate minus baseline recovery rate under matched conditions.
- **Encoding overhead:** protected encoded length compared with unprotected encoded length.

Results will be separated by platform, operation, payload category, and codec mode. The team will report trial counts and limitations and will avoid claiming that results generalize beyond tested versions, workflows, and dates.

## Risk Management

| Risk | Mitigation | Owner |
|---|---|---|
| Platforms remove all zero-width characters | Measure and report incompatibility; compare characters and workflows; do not conceal negative results | Tristan |
| Platform UI/version changes affect reproducibility | Record dates, versions, browser/app, and exact steps; rerun critical trials near final submission | Tristan |
| Error correction adds excessive overhead | Benchmark multiple settings against observed corruption; document payload tradeoffs | Henry |
| Undetected corrupted messages | Add framing/integrity validation and test false-success behavior | Henry |
| Automation violates terms or becomes unreliable | Prefer documented manual tests when necessary; avoid bypassing controls; keep automation optional | Ifeanyi |
| Data or statistics cannot be reproduced | Preserve raw data, schemas, scripts, seeds/configuration, and generated-output instructions | Tristan |
| Integration occurs too late | Integrate weekly, protect the main branch, and create staged release tags | Ifeanyi |
| Live demo fails due to network/platform behavior | Use a locally reproducible core demo and maintain offline backup artifacts | Ifeanyi |
| Team availability disrupts schedule | Keep issues small, document work, identify backups, and escalate slippage during weekly planning | Ifeanyi |

## Final Report Preparation

### Report Structure

1. Abstract
2. Introduction and project motivation
3. Background on Unicode and zero-width steganography
4. Requirements, ethical scope, and threat model
5. System architecture and encoding format
6. Encoder and decoder implementation
7. Platform-testing methodology
8. Baseline results and compatibility matrix
9. Error-correction design and evaluation
10. Discussion, limitations, and threats to validity
11. Project management and team contributions
12. Conclusion and future work
13. References
14. Appendices: protocol, test corpus, additional tables, and reproducibility instructions

### Preparation Schedule

- **Weeks 8–10:** Reuse and refine the midterm material; maintain citations and methods as experiments progress.
- **Weeks 11–13:** Draft error-correction and final-results sections as soon as results are verified.
- **Week 14:** Complete the full draft and perform technical, evidence, citation, and clarity reviews.
- **Week 15:** Incorporate feedback, proofread, verify formatting and figures, and freeze the submission version.
- **Week 16:** Submit/archive the final version and record any presentation-day corrections separately.

Ifeanyi owns editorial consistency and final assembly. Henry owns technical accuracy for the codec and error-correction sections. Tristan owns accuracy and reproducibility for the methods, results, statistics, charts, and compatibility matrix. All members must review the complete report.

## Presentation Preparation

- Use a clear narrative: problem, approach, implementation, experiment, results, robustness improvement, limitations, and conclusion.
- Assign Ifeanyi the opening, project management/context, conclusions, and Q&A coordination.
- Assign Henry the encoding/decoding architecture, error correction, and technical demonstration explanation.
- Assign Tristan the testing protocol, platform compatibility, statistics, and charts.
- Build slides in Week 14, finalize them in Week 15, and freeze the presentation-day copy after a Week 16 smoke test.
- Keep code text readable, label every chart, state sample sizes, and distinguish measured facts from interpretations.
- Prepare a Q&A bank covering Unicode choices, detection/security limitations, platform policies, error-correction tradeoffs, data validity, and future work.
- Perform at least two timed full-team rehearsals and one rehearsal on the intended presentation equipment.

## Live Demo Preparation

### Primary Demo Flow

1. Show a normal cover message and a synthetic secret.
2. Encode the secret and show that the visible cover text appears unchanged.
3. Inspect string length or Unicode code points to demonstrate that hidden characters exist.
4. Decode the untouched message and verify an exact match.
5. Apply a controlled corruption or use a previously validated platform-returned sample.
6. Show baseline decoding failure or degradation.
7. Decode a matched error-corrected sample and demonstrate successful recovery within the supported limit.
8. Display the relevant compatibility statistic and explain the limitation honestly.

### Demo Readiness Requirements

- Use synthetic, non-sensitive messages and prevalidated inputs.
- Keep the core demo local so it does not depend on a platform login or network connection.
- Validate commands, environment, terminal font, Unicode rendering, and display scaling on the presentation machine.
- Prepare a one-command or short documented setup and a clean reset between runs.
- Save known-good input/output files, screenshots, and a short backup recording.
- Assign Henry as primary technical operator, Ifeanyi as narrator/timekeeper, and Tristan as result verifier and backup operator.
- Practice recovery from common failures: wrong directory, missing dependency, terminal rendering issue, corrupted clipboard content, and network loss.

## Definition of Project Completion

The project is complete when the final report and presentation have been delivered; the encoder, decoder, and error-correction mode pass their documented tests; at least eight platforms have reproducible recorded results; all published statistics can be regenerated from preserved data; the compatibility matrix and limitations are complete; and the GitHub repository contains a documented, reproducible `v1.0.0` release.
