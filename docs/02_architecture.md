# System Architecture & Design Guidelines
**Project:** Biz360 Financial Engine

## 1. High-Level Data Flow
`[ERP MSSQL]` --> `[Python ETL]` --> `[SQL Staging (Silver)]` --> `[SQL Production (Gold)]` --> `[Power BI / Excel]`

## 2. The Medallion Architecture

### Layer 1: Bronze (Raw Ingestion)
* **Goal:** Create an exact copy of the source data.
* **Storage:** Temporary SQL Tables or CSV dumps.
* **Rule:** No transformations allowed. If the source says "Revnue" (typo), we store "Revnue".

### Layer 2: Silver (Validation & Cleaning)
* **Goal:** Ensure accounting integrity.
* **Transformations:**
    * Standardize column names (e.g., `trx_date` -> `TransactionDate`).
    * Handle NULL values.
* **The Gatekeeper (Forensic Audit):**
    * Check: `SUM(Debits) - SUM(Credits) = 0`
    * Check: `TransactionDate <= Today`
    * Action: If checks fail, alert the engineer. Do not load to Gold.

### Layer 3: Gold (Reporting Ready)
* **Goal:** Business logic and aggregation.
* **Structure:**
    * **Dim_ChartOfAccounts:** The list of all GL accounts (Assets, Liabilities, etc.).
    * **Fact_GeneralLedger:** The transactions.
    * **Fact_TrialBalance:** Monthly aggregated balances.

## 3. Naming Conventions (Strict)
* **SQL Tables:** `tbl_[Layer]_[Description]`
    * Example: `tbl_Bronze_GL_Dump`, `tbl_Gold_TrialBalance`
* **SQL Columns:** `PascalCase`
    * Example: `AccountCode`, `FiscalYear`, `AmountGHS`
* **Python Variables:** `snake_case`
    * Example: `connection_string`, `df_gl_data`

## 4. Technology Stack details
* **Database:** SQL (SQLite for local dev, MSSQL for prod).
* **Language:** Python 3.10+ (Pandas, SQLAlchemy).
* **Orchestration:** Python scripts running in sequence.