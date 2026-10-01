# Week 7 Weekly Journal - Ifeanyi Emeka

## What I Did
This week, I continued testing the five-copy recovery method developed during Week 6. I first ran the full automated test suite to establish a baseline. All 25 tests and 118 subtests passed. I then conducted additional corruption testing at 1/5, 2/5, and 3/5 corrupted symbols per group.

## What I Learned
I learned that the current five-copy recovery method can successfully recover the hidden message when up to two symbols in each five-copy group are corrupted. When three symbols are corrupted, recovery fails because the corrupted symbols become the majority.

## Problems Encountered
I encountered some issues while creating the Week 7 corruption testing script, including import and indentation errors. I corrected the script and successfully completed the testing.

## Results
- 1/5 corrupted symbols: PASS
- 2/5 corrupted symbols: PASS
- 3/5 corrupted symbols: FAIL
- Recovery limit: 2 corrupted symbols per five-copy group

## Testing Evidence

The screenshot below shows the Week 7 baseline automated testing. All 25 tests and 118 subtests passed, confirming that the existing codec and recovery functionality were working correctly before corruption testing.

![Week 7 Baseline Test Results](../../tests/week7_testing/screenshots/ifeanyi/week7_baseline_tests.png)

The screenshot below shows the Week 7 corruption testing used to determine the limit of the five-copy recovery method. The system successfully recovered the secret with 1/5 and 2/5 corrupted symbols but failed when 3/5 symbols were corrupted.

![Week 7 Corruption Test Results](../../tests/week7_testing/screenshots/ifeanyi/week7_corruption_tests.png)

## Next Week's Plan
Next week, I will continue working with the team to improve the robustness of the recovery method and use the Week 7 results to guide additional testing and development.