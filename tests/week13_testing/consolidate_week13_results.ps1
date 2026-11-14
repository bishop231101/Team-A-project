$ErrorActionPreference = 'Stop'

$repo = (Resolve-Path (Join-Path $PSScriptRoot '..\..')).Path
$prodRoot = Join-Path $repo 'tests\week11_testing\production_testing'
$compRoot = Join-Path $repo 'tests\week12_testing\comparative_experiment_output'
$chartRoot = Join-Path $repo 'tests\week13_testing\chart_data'
New-Item -ItemType Directory -Force -Path $chartRoot | Out-Null

function CsvValue($value) {
    if ($null -eq $value) { return $null }
    return $value
}

function Get-JsonRecords($root) {
    Get-ChildItem -Recurse -Path $root -Filter *.json | ForEach-Object {
        Get-Content -Raw $_.FullName | ConvertFrom-Json
    }
}

$prod = @(Get-JsonRecords $prodRoot | Sort-Object platform, corpus_id, repetition, trial_id)
$comp = @(Get-JsonRecords $compRoot | Where-Object { $_.trial_id -like 'W12_*' } | Sort-Object corpus_id, encoding_mode, corruption_condition, repetition, trial_id)

$platformOrder = @('Gmail','Notepad++','Microsoft Word','Discord','Telegram Web','Browser Console','Microsoft Outlook')
$symbolOrder = @('U+200B','U+200C','U+200D')
$summary = @()
$retention = @()
$trialRows = @()

foreach ($platform in $platformOrder) {
    $rows = @($prod | Where-Object platform -eq $platform)
    $completed = @($rows | Where-Object status -eq 'completed')
    $blocked = @($rows | Where-Object status -eq 'blocked')
    $pending = @($rows | Where-Object { $_.status -ne 'completed' -and $_.status -ne 'blocked' })
    $exact = @($completed | Where-Object { $_.measured_results.exact_match -eq $true })
    $sentTotal = 0
    $retrievedTotal = 0
    $symbolAgg = @{}
    foreach ($symbol in $symbolOrder) {
        $sent = [int](($completed | ForEach-Object { $_.measured_results.sent_counts.$symbol } | Measure-Object -Sum).Sum)
        $retrieved = [int](($completed | ForEach-Object { $_.measured_results.retrieved_counts.$symbol } | Measure-Object -Sum).Sum)
        $sentTotal += $sent
        $retrievedTotal += $retrieved
        $symbolAgg[$symbol] = [pscustomobject]@{ Sent = $sent; Retrieved = $retrieved; Rate = if ($sent) { 100.0 * $retrieved / $sent } else { $null } }
        $retention += [pscustomobject]@{
            Platform = $platform
            Character = $symbol
            CharactersSent = $sent
            CharactersRetrieved = $retrieved
            AggregateRetentionPercentage = if ($sent) { 100.0 * $retrieved / $sent } else { $null }
        }
    }
    $summary += [pscustomobject]@{
        Platform = $platform
        PlannedTrials = $rows.Count
        CompletedTrials = $completed.Count
        BlockedTrials = $blocked.Count
        ExactRecoveries = $exact.Count
        FailedRecoveries = $completed.Count - $exact.Count
        ExactRecoveryRate = if ($completed.Count) { 100.0 * $exact.Count / $completed.Count } else { $null }
        AggregateOverallCharacterRetention = if ($sentTotal) { 100.0 * $retrievedTotal / $sentTotal } else { $null }
        U200BRetention = $symbolAgg['U+200B'].Rate
        U200CRetention = $symbolAgg['U+200C'].Rate
        U200DRetention = $symbolAgg['U+200D'].Rate
        DataStatus = if ($pending.Count) { "Pending records: $($pending.Count)" } elseif ($blocked.Count) { "Complete with blocked trials: $($blocked.Count)" } else { 'Complete' }
    }
}

foreach ($r in $prod) {
    $m = $r.measured_results
    $trialRows += [pscustomobject]@{
        TrialID = $r.trial_id
        Platform = $r.platform
        CorpusID = $r.corpus_id
        Repetition = $r.repetition
        TrialStatus = $r.status
        ExactRecoveryResult = if ($null -ne $m) { $m.exact_match } else { $null }
        SentTotal = if ($null -ne $m) { $m.sent_counts.total } else { $null }
        RetrievedTotal = if ($null -ne $m) { $m.retrieved_counts.total } else { $null }
        OverallRetentionPercentage = if ($null -ne $m) { $m.retention_percentage } else { $null }
        U200BSent = if ($null -ne $m) { $m.sent_counts.'U+200B' } else { $null }
        U200BRetrieved = if ($null -ne $m) { $m.retrieved_counts.'U+200B' } else { $null }
        U200BRetentionPercentage = if ($null -ne $m -and $m.sent_counts.'U+200B') { 100.0 * $m.retrieved_counts.'U+200B' / $m.sent_counts.'U+200B' } else { $null }
        U200CSent = if ($null -ne $m) { $m.sent_counts.'U+200C' } else { $null }
        U200CRetrieved = if ($null -ne $m) { $m.retrieved_counts.'U+200C' } else { $null }
        U200CRetentionPercentage = if ($null -ne $m -and $m.sent_counts.'U+200C') { 100.0 * $m.retrieved_counts.'U+200C' / $m.sent_counts.'U+200C' } else { $null }
        U200DSent = if ($null -ne $m) { $m.sent_counts.'U+200D' } else { $null }
        U200DRetrieved = if ($null -ne $m) { $m.retrieved_counts.'U+200D' } else { $null }
        U200DRetentionPercentage = if ($null -ne $m -and $m.sent_counts.'U+200D') { 100.0 * $m.retrieved_counts.'U+200D' / $m.sent_counts.'U+200D' } else { $null }
        FailureCategory = if ($null -ne $m) { $m.failure_category } else { $null }
        DecoderError = if ($null -ne $m) { $m.decoder_error } else { $null }
    }
}

$recovery = $summary | ForEach-Object {
    [pscustomobject]@{
        Platform = $_.Platform
        ExactRecoveries = $_.ExactRecoveries
        CompletedTrials = $_.CompletedTrials
        ExactRecoveryPercentage = $_.ExactRecoveryRate
        BlockedTrials = $_.BlockedTrials
    }
}

$conditionOrder = @('no_corruption','single_bit_corruption','double_bit_corruption','deletion_1_percent','deletion_5_percent')
$methodOrder = @('baseline','hamming')
$compSummary = @()
foreach ($method in $methodOrder) {
    foreach ($condition in $conditionOrder) {
        $rows = @($comp | Where-Object { $_.encoding_mode -eq $method -and $_.corruption_condition -eq $condition })
        $successful = @($rows | Where-Object outcome -eq 'successful_recovery').Count
        $detected = @($rows | Where-Object outcome -eq 'detected_failure').Count
        $undetected = @($rows | Where-Object outcome -eq 'undetected_error').Count
        $compSummary += [pscustomobject]@{
            EncodingMethod = $method
            CorruptionCondition = $condition
            SuccessfulRecoveries = $successful
            DetectedFailures = $detected
            UndetectedErrors = $undetected
            TotalTrials = $rows.Count
            RecoveryPercentage = if ($rows.Count) { 100.0 * $successful / $rows.Count } else { $null }
        }
    }
}

$compRows = @()
foreach ($r in $comp) {
    $corruption = $r.corruption
    $compRows += [pscustomobject]@{
        TrialID = $r.trial_id
        CorpusID = $r.corpus_id
        Repetition = $r.repetition
        EncodingMethod = $r.encoding_mode
        CorruptionCondition = $r.corruption_condition
        ExactRecoveryClassification = $r.outcome
        OriginalEncodedLength = $r.encoded_length
        EncodedLengthAfterCorruption = if ($null -ne $r.damaged_encoded_sha256) { $r.retrieved_zero_width_character_counts.total } else { $null }
        AffectedSymbolCount = $corruption.affected_symbol_count
        BitSeed = $corruption.bit_seed
        DeletionSeed = $corruption.deletion_seed
        ActualDeletionPercentage = $corruption.actual_deletion_percentage
        FailureDetected = $r.failure_detected
        UndetectedError = $r.incorrect_recovery_without_detection
    }
}

$overhead = @()
foreach ($corpus in @('SA01','SU01','LA01','LU01')) {
    $base = @($comp | Where-Object { $_.corpus_id -eq $corpus -and $_.encoding_mode -eq 'baseline' -and $_.corruption_condition -eq 'no_corruption' })[0]
    $ham = @($comp | Where-Object { $_.corpus_id -eq $corpus -and $_.encoding_mode -eq 'hamming' -and $_.corruption_condition -eq 'no_corruption' })[0]
    $overhead += [pscustomobject]@{
        CorpusID = $corpus
        BaselineEncodedLength = $base.encoded_length
        HammingEncodedLength = $ham.encoded_length
        HammingOverheadPercentage = 100.0 * ($ham.encoded_length - $base.encoded_length) / $base.encoded_length
    }
}

$summary | Export-Csv (Join-Path $chartRoot 'platform_summary.csv') -NoTypeInformation -Encoding utf8
$trialRows | Export-Csv (Join-Path $chartRoot 'platform_trial_results.csv') -NoTypeInformation -Encoding utf8
$retention | Export-Csv (Join-Path $chartRoot 'platform_retention_by_symbol.csv') -NoTypeInformation -Encoding utf8
$recovery | Export-Csv (Join-Path $chartRoot 'platform_recovery_summary.csv') -NoTypeInformation -Encoding utf8
$compSummary | Export-Csv (Join-Path $chartRoot 'comparative_recovery_summary.csv') -NoTypeInformation -Encoding utf8
$compRows | Export-Csv (Join-Path $chartRoot 'comparative_trial_results.csv') -NoTypeInformation -Encoding utf8
$overhead | Export-Csv (Join-Path $chartRoot 'hamming_overhead.csv') -NoTypeInformation -Encoding utf8

$fmt = @{ '0.00' = '0.00' }
$table = ($summary | ForEach-Object { "| $($_.Platform) | $($_.PlannedTrials) | $($_.CompletedTrials) | $($_.BlockedTrials) | $($_.ExactRecoveries) | $($_.FailedRecoveries) | $([math]::Round($_.ExactRecoveryRate,2))% | $([math]::Round($_.AggregateOverallCharacterRetention,2))% | $($_.DataStatus) |" }) -join "`n"
$compTable = ($compSummary | ForEach-Object { "| $($_.EncodingMethod) | $($_.CorruptionCondition) | $($_.SuccessfulRecoveries) | $($_.DetectedFailures) | $($_.UndetectedErrors) | $($_.TotalTrials) | $([math]::Round($_.RecoveryPercentage,2))% |" }) -join "`n"
$overTable = ($overhead | ForEach-Object { "| $($_.CorpusID) | $($_.BaselineEncodedLength) | $($_.HammingEncodedLength) | $([math]::Round($_.HammingOverheadPercentage,2))% |" }) -join "`n"
$doc = @"
# Week 13 Results Consolidation

**Project:** CS481 Capstone Project 5 — Zero-Width Unicode Steganography with Social-Media Robustness Engineering  
**Data freeze:** November 14, 2026  
**Source records:** `tests/week11_testing/production_testing/` and `tests/week12_testing/comparative_experiment_output/`

## 1. Overview

This document consolidates the official production-platform trial records currently present on the Week 13 branch and the separate Week 12 Baseline-versus-Hamming comparative experiment. The production dataset contains 168 planned records across seven platforms. The comparative dataset contains 120 records across four corpus messages, two encoding methods, five corruption conditions, and three repetitions per condition.

## 2. Production-testing methodology and scope

Production testing reused the encoded input for each corpus ID across three repetitions and recorded the platform interaction, retrieved payload measurements, decoder result, and failure category. A completed trial had an actual platform interaction and an analyzable result. A blocked trial was stopped by a documented platform limitation before transfer. Pending records are included in the trial-level CSV but are excluded from completed-trial denominators. Retention is calculated from aggregate retrieved counts divided by aggregate sent counts; blocked and pending null measurements are not treated as zero.

## 3. Production results by platform

| Platform | Planned | Completed | Blocked | Exact | Failed | Exact recovery | Aggregate retention | Data status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
$table

The finalized production set has 162 completed trials, 110 exact recoveries, and 52 failed recoveries, for an overall completed-trial exact recovery rate of 67.90%. Three Discord LA02 trials are blocked because the unchanged encoded payload exceeded the standard account's message-size limit. Three Outlook SU02 trials remain `ready_for_manual_transfer`; they are visible in the trial dataset but are not included in completed statistics. Outlook is therefore merged and partially validated, not fully complete.

Gmail failed all 24 completed recoveries. Its aggregate overall retention was 5.41%, with U+200B at 0.00%, U+200C at 10.19%, and U+200D at 12.00%; the completed failures were structural corruption or incomplete payload failures. Microsoft Word failed all 24 completed recoveries with 0.00% aggregate retention. Notepad++, Telegram Web, and Browser Console each achieved 24/24 exact recoveries and 100.00% aggregate retention for every zero-width character. Discord achieved 21/21 exact recoveries among completed trials and 100.00% retention, while its three LA02 trials were blocked. Outlook achieved 17/21 exact recoveries among completed trials. Its aggregate overall retention was 90.80%, with U+200B at 90.89%, U+200C at 90.67%, and U+200D at 90.88%.

## 4. Character-retention analysis

Character retention and exact recovery aligned for the fully preserving platforms and for Gmail and Word, but retention alone was not sufficient to guarantee exact recovery. Outlook retained most zero-width characters yet had four failed recoveries, showing that partial loss can be incompatible with exact decoding. Gmail retained a small fraction of U+200C and U+200D but lost all U+200B characters and could not decode any completed trial. The symbol-level CSV preserves the sent and retrieved numerators and denominators for independent charting.

## 5. Exact-recovery analysis and cross-platform comparison

The highest completed-trial results were 100% for Notepad++, Telegram Web, and Browser Console, followed by Discord at 100% of its 21 completed trials and Outlook at 80.95% of its 21 completed trials. Gmail and Microsoft Word achieved 0%. These are results for the documented workflows and corpus set, not universal compatibility guarantees. The Discord block is reported separately from decoder failure, and Outlook's three pending records remain outside all finalized recovery and retention denominators.

## 6. Blocked trials and platform limitations

Discord LA02 R1–R3 were blocked before transfer because the encoded payload exceeded the standard account message-size limit. The records state that the payload was not shortened, split, or otherwise modified. No decoder measurements were collected. Outlook SU02 R1–R3 have authoritative records with `ready_for_manual_transfer` status and no measured results; they require completion before Outlook can be reported as a full 24-trial platform.

## 7. Separate Baseline-versus-Hamming experiment

The comparative experiment remains separate from production-platform testing. It used four corpus messages, Baseline and Hamming encoding, five conditions, and three deterministic repetitions per combination. The seed pairs were R1: 481201/481202, R2: 481211/481212, and R3: 481221/481222 for bit/deletion operations. The 120 individual records validate to 36 successful recoveries, 84 detected failures, and 0 undetected errors.

| Encoding method | Corruption condition | Successful | Detected failures | Undetected errors | Total | Recovery |
|---|---|---:|---:|---:|---:|---:|
$compTable

Baseline recovered all 12 no-corruption trials and none of the four corruption conditions. Hamming recovered all 12 no-corruption trials and all 12 single-bit-corruption trials, but none of the double-bit or deletion trials. With 60 records per method, Baseline's overall recovery rate was 20% and Hamming's was 40%. Because there were only three repetitions per method/condition/corpus combination, these findings describe this controlled experiment rather than a broad statistical guarantee.

## 8. Hamming overhead and error-correction findings

| Corpus | Baseline encoded length | Hamming encoded length | Hamming overhead |
|---|---:|---:|---:|
$overTable

Hamming's measured overhead ranged from 55.70% to 57.24% across the four corpus messages. The trade-off in this experiment was additional encoded length in exchange for successful correction of the tested single-bit corruption. Hamming did not recover from the tested double-bit corruption or the approximately 1% and 5% deletion conditions.

## 9. Chart placeholders

### Chart 1 — Character Retention by Platform

**Placeholder:** Insert chart here. Use `platform_retention_by_symbol.csv`, columns `Platform`, `Character`, and `AggregateRetentionPercentage`. The chart should show that Notepad++, Discord completed trials, Telegram Web, and Browser Console retained all three symbols, while Gmail and Word did not; Outlook retained most but not all characters.

### Chart 2 — Exact Recovery Rate by Platform

**Placeholder:** Insert chart here. Use `platform_recovery_summary.csv`, columns `Platform`, `ExactRecoveries`, `CompletedTrials`, and `ExactRecoveryPercentage`. The chart should exclude blocked and pending records from the denominator and make the zero-recovery Gmail/Word results distinct from the fully successful completed-platform results.

### Chart 3 — Production Platform Comparison

**Placeholder:** Insert chart here. Use `platform_summary.csv`, columns `Platform`, `CompletedTrials`, `BlockedTrials`, `ExactRecoveries`, `FailedRecoveries`, and the retention columns. The chart should make the Discord blocked trials and Outlook pending records visible as data-status limitations.

### Chart 4 — Baseline vs. Hamming Recovery by Corruption Condition

**Placeholder:** Insert chart here. Use `comparative_recovery_summary.csv`, columns `EncodingMethod`, `CorruptionCondition`, and `RecoveryPercentage`. The chart should show Hamming's improvement only for the tested single-bit corruption, with both methods failing the double-bit and deletion conditions.

### Chart 5 — Hamming Encoding Overhead

**Placeholder:** Insert chart here. Use `hamming_overhead.csv`, columns `CorpusID`, `BaselineEncodedLength`, `HammingEncodedLength`, and `HammingOverheadPercentage`. The chart should show the approximately 55.70%–57.24% length increase across corpus messages.

## 10. Conclusions

The production evidence shows strong preservation and exact recovery in Notepad++, Discord completed trials, Telegram Web, and the Chrome Browser Console, complete loss in Microsoft Word, and severe loss in Gmail. Outlook is partially successful but remains incomplete because three records are still pending. Character retention is a necessary observable for exact recovery in these trials, but partial retention does not ensure exact recovery. Separately, the comparative experiment supports a limited result: Hamming doubled the observed overall recovery rate from 20% to 40% by correcting the tested single-bit corruption, at a measured encoded-length overhead of roughly 56%, but it did not withstand the tested double-bit or deletion conditions.

## 11. Limitations and unresolved items

- The production results cover the repository's documented workflows, corpus messages, and three repetitions per corpus message.
- Outlook requires three pending SU02 transfers before its planned 24-trial set is complete.
- Discord's three blocked LA02 trials are platform-limited and are not decoder failures.
- The comparative experiment has three repetitions per condition and should not be generalized beyond the tested corpus and deterministic corruption schedules.
- No suspected technical cause for Outlook failures is asserted beyond the measured records and their documented outcomes.

## 12. Reproducibility references

- Production records: `tests/week11_testing/production_testing/`
- Production manifest: `tests/week11_testing/production_manifest.json`
- Production guides: `tests/week11_testing/production_testing/*/*reproducibility*` and `tests/week11_testing/guides/`
- Comparative methodology: `docs/week12_comparative_experiment_methodology.md`
- Comparative runner: `tests/week12_testing/comparative_experiment.py`
- Comparative records, summary, and report: `tests/week12_testing/comparative_experiment_output/`
- Consolidation script: `tests/week13_testing/consolidate_week13_results.ps1`
- Chart-ready datasets: `tests/week13_testing/chart_data/`
"@
if ($doc.Length -gt 0) {
    Set-Content -Path (Join-Path $repo 'docs\week13_results.md') -Value $doc -Encoding utf8
}

$journal = @"
# Week 13 Individual Journal — Tristan Koch

**Course:** CS481 Capstone Project  
**Week:** 13 (November 9–15, 2026)  
**Role:** Testing, statistical analysis, and reproducibility  
**Project:** Zero-Width Unicode Steganography with Social-Media Robustness Engineering

## Work completed

I audited the current Week 13 branch and consolidated the official production-platform trial records directly from the individual JSON files. The branch includes the merged Outlook contribution and corrected Outlook evidence. I reviewed the production records for Gmail, Notepad++, Microsoft Word, Discord, Telegram Web, Browser Console, and Microsoft Outlook, along with the production manifest, platform guides, compatibility documentation, and recent Week 13 commits.

The production audit found 168 planned records: 162 completed, 3 Discord trials blocked before transfer, and 3 Outlook trials still marked `ready_for_manual_transfer`. The completed records contain 110 exact recoveries and 52 failed recoveries. I kept the three pending Outlook records in the trial-level dataset but excluded them from completed-trial recovery and retention denominators. I also kept the three Discord LA02 records separate from decoder failures because their source records document a message-size limitation before transfer.

I independently recalculated aggregate retention from sent and retrieved symbol counts. Notepad++, Discord completed trials, Telegram Web, and Browser Console retained all three zero-width symbols and achieved exact recovery in every completed trial. Gmail retained 5.41% overall and achieved no exact recoveries. Microsoft Word retained 0.00% and achieved no exact recoveries. Outlook retained 90.80% overall and achieved 17 exact recoveries among 21 completed trials. These results are documented without attributing an unproven technical cause to Outlook failures.

I separately audited the Week 12 Baseline-versus-Hamming experiment. All 120 individual records are present and consistent with the documented 36 successful recoveries, 84 detected failures, and 0 undetected errors. Baseline succeeded in all no-corruption trials and failed under every tested corruption condition. Hamming succeeded in all no-corruption and single-bit-corruption trials and failed under double-bit corruption and both deletion conditions. I recalculated the corpus-level Hamming overhead values from the encoded lengths.

I generated seven chart-ready CSV files under `tests/week13_testing/chart_data/` for platform summaries, production trial results, symbol retention, platform recovery, comparative recovery, comparative trial results, and Hamming overhead. I created `docs/week13_results.md` with the methodology, verified results, limitations, separate comparative analysis, five chart placeholders, and reproducibility references.

## Validation performed

- Confirmed 168 unique production trial IDs and 120 unique comparative trial IDs.
- Confirmed no duplicate records in either dataset.
- Reconciled production counts as 162 completed + 3 blocked + 3 pending = 168 planned.
- Confirmed blocked and pending trials have null measurements and are excluded from completed denominators.
- Recalculated symbol-level and overall aggregate retention from source counts.
- Recalculated exact-recovery totals from individual trial classifications.
- Reconciled comparative totals to 120 records, 36 successful recoveries, 84 detected failures, and 0 undetected errors.
- Recalculated Hamming overhead from Baseline and Hamming encoded lengths.
- Checked that the written results use the generated CSV values and do not carry forward the older pre-Outlook totals.

## Limitations and next steps

Outlook is merged but not fully complete: SU02 repetitions R1–R3 still need authoritative transfer records and evidence. The comparative experiment uses three repetitions per condition, so its conclusions are limited to the tested corpus and deterministic corruption schedules. The actual chart images still need to be created externally and inserted into the five labeled placeholders in `docs/week13_results.md`.
"@
if ($journal.Length -gt 0) {
    Set-Content -Path (Join-Path $repo 'weekly_journals\tristan\week13.md') -Value $journal -Encoding utf8
}

Write-Output ("Generated 7 CSV files from {0} production and {1} comparative records." -f $prod.Count, $comp.Count)
