# Week 7 Testing Results - Ifeanyi Emeka

## Baseline Automated Testing

The complete automated test suite was executed at the beginning of Week 7 to verify that the project remained stable before additional corruption testing.

### Results
- 25 tests passed.
- 118 subtests passed.
- Execution time: 0.18 seconds.
- No automated tests failed.

## Purpose

The baseline test confirms that the existing zero-width Unicode codec and five-copy recovery functionality remain operational before conducting additional Week 7 corruption tests.

## Comparison

Week 7 begins with a successful baseline following the Week 6 recovery improvements. The next phase will test higher corruption levels and compare the results with the Week 5 baseline and Week 6 recovery testing.

## Evidence

Screenshot:

`tests/week7_testing/screenshots/ifeanyi/week7_baseline_tests.png`

## Corruption Testing Results

The five-copy recovery method was tested at three corruption levels.

- **1/5 symbols corrupted per group:** PASS — original secret successfully recovered.
- **2/5 symbols corrupted per group:** PASS — original secret successfully recovered.
- **3/5 symbols corrupted per group:** FAIL — decoder could not recover the original secret.

## Analysis

The Week 7 testing identified the recovery limit of the current five-copy method. The system successfully recovered the hidden message when one or two symbols in each five-copy group were corrupted. When three symbols were corrupted, recovery failed because the corrupted symbols became the majority.

This confirms that the five-copy recovery method can tolerate up to two corrupted symbols per group.

## Evidence

### Baseline Automated Testing

The screenshot below shows the Week 7 baseline automated test results. All 25 tests and 118 subtests passed, confirming that the existing codec and recovery functionality were working before additional corruption testing.

![Week 7 Baseline Test Results](screenshots/ifeanyi/week7_baseline_tests.png)

### Corruption Testing

The screenshot below shows the Week 7 five-copy corruption testing. The hidden message was successfully recovered when 1/5 and 2/5 symbols were corrupted. Recovery failed at 3/5 corrupted symbols, identifying the current recovery limit.

![Week 7 Corruption Test Results](screenshots/ifeanyi/week7_corruption_tests.png)
## Next Step

Compare the Week 7 results with the Week 5 baseline and Week 6 recovery results and continue evaluating the robustness of the recovery method.