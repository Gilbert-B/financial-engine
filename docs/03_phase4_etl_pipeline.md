# Phase 4: ETL Pipeline & Data Ingestion

## Status: COMPLETE

## Overview
Implemented a Python-based ETL pipeline to generate and load synthetic financial transactions into the MSSQL `Fact_GeneralLedger`.

## Technical Implementation
* **Source:** Python Synthetic Data Generator (Mock Data)
* **Target:** MSSQL `Fact_GeneralLedger`
* **Logic:** * Generates matched pairs of Debits and Credits.
    * Enforces Foreign Key constraints against `Dim_ChartOfAccounts`.
    * Transaction Count: 1000 rows.

## Validation
* **Constraint Check:** Validated against Foreign Keys (AccountCode).
* **Accounting Check:** Net sum of `AmountGHS` verified as 0.00 (Balanced Ledger).