# Phase 5: Financial Modeling Logic

## 1. Data Source
* **View:** `View_Financial_Model_Source`
* **Method:** Power Query (Import Mode)

## 2. Logic Transformations
* **Revenue:** Inverted sign (Credit -> Positive) for Income Statement.
* **COGS/Expenses:** Maintained debit sign.
* **Retained Earnings:** Manually linked `Net Income` from IS to BS Equity section.

## 3. Validation
* **Trial Balance:** Sums to 0.00.
* **Balance Sheet:** Assets = Liabilities + Equity (Diff: 0.00).
