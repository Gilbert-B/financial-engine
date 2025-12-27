# Financial Engine

## 1. Executive Summary
The Financial Engine is an enterprise-grade automated data pipeline designed to bridge the gap between transactional ERP data (MSSQL) and strategic financial reporting. It automates the flow of the General Ledger into a CFI-Standard 3-Statement Model and a Power BI Executive Dashboard.

**Status:** Phase 0 (Setup)
**License:** MIT

## 2. Technical Architecture
* **Source:** MSSQL Server (ERP / General Ledger Data)
* **Orchestration:** Python (Pandas/SQLAlchemy)
* **Logic Layer:** SQL Stored Procedures (Trial Balance Aggregation)
* **Presentation (Static):** Excel (CFI Formatting: Blue/Black/Green logic)
* **Presentation (Dynamic):** Power BI (DAX Measures for FP&A)

## 3. Accounting Standards & Integrity
This system is built with strict adherence to:
* **GAAP/IFRS:** Ensuring accurate revenue recognition and expense categorization.
* **The Accounting Equation:** Automated checks ensuring Assets = Liabilities + Equity at every transformation stage.
* **CFI Standards:** Excel modeling utilizing standard color coding (Blue for inputs, Black for formulas, Green for links).

## 4. Directory Structure
* `src/`: Python ETL scripts.
* `sql/`: Database schemas and transformation logic.
* `models/`: Financial models (Excel) and Dashboards (PBIX).
* `docs/`: Product Requirements and Schema documentation.

## 5. Getting Started
(Instructions to be added in Phase 6)
