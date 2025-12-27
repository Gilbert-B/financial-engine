# Product Requirements Document (PRD)
**Project:** Financial Engine
**Version:** 1.0
**Status:** Approved
**Author:** Data Architect / Financial Lead

## 1. Executive Summary
**Objective:** Replace manual, estimation-based reporting with an automated, audit-ready financial data pipeline.
**Success Definition:** The Finance team has access to T+1 (Next Day) reporting of the 3 Financial Statements (Income Statement, Balance Sheet, Cash Flow) with 100% accuracy tied to the General Ledger.

## 2. Business Context
* **Industry:** Retail
    * *Key Implications:* High volume of transactions, critical importance of Inventory management and Cost of Goods Sold (COGS).
* **Reporting Currency:** GHS (Ghanaian Cedi)
* **Fiscal Year:** Jan 1 – Dec 31
* **Current State (The Problem):**
    * Financial position and Cash Flows are currently estimated, leading to low confidence in decision-making.
    * Lack of visibility into actual inventory costs vs. sales revenue.
    * Manual data handling creates high risk of human error.

## 3. Functional Requirements

### 3.1 Data Ingestion (ETL)
* **Source:** MSSQL ERP Database.
* **Frequency:** Daily (Overnight Batch).
* **Logic:** Extract raw General Ledger (GL) transactions; aggregate into a Trial Balance.

### 3.2 Financial Logic (The "Brain")
* **Accounting Equation:** Must validate that `Assets = Liabilities + Equity` after every transformation.
* **Currency:** All reporting in GHS.
* **Mapping:** Automated mapping of GL Codes to Financial Statement Line Items (e.g., "GL Account 4001" -> "Revenue").

### 3.3 Outputs
1.  **Excel 3-Statement Model (CFI Standard):**
    * Fully linked Income Statement, Balance Sheet, and Cash Flow.
    * Color-coded: Blue (Hardcodes), Black (Formulas), Green (Links).
    * Format: Monthly Actuals + Forecast capability.
2.  **Power BI Dashboard (Strategic CFO View):**
    * **KPIs:** Gross Margin %, Inventory Turnover, EBITDA, Net Working Capital.
    * **Visuals:** Revenue vs. Budget, Expense Trend Analysis.

## 4. Technical Constraints
* **Auditability:** Every number in the final report must be traceable back to a SQL query.
* **Security:** Read-only access to the ERP; no write-back allowed.
* **Version Control:** All code stored in Git (GitHub).

## 5. Risk Assessment
* **Data Quality:** If the ERP data is bad, the report is bad ("Garbage In, Garbage Out").
    * *Mitigation:* We will build a "Forensic Audit" step in SQL to flag unbalanced journals.