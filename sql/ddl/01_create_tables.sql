/* Biz360 Financial Engine - Phase 3
    DDL: Initial Table Setup
    Author: Biz360 Architect
*/

-- 1. Dimension: Chart of Accounts
-- This holds the "Master Data" for our accounting structure.
CREATE TABLE Dim_ChartOfAccounts (
    AccountCode VARCHAR(20) PRIMARY KEY,      -- e.g., '4000'
    AccountName VARCHAR(100) NOT NULL,        -- e.g., 'Sales Revenue'
    AccountType VARCHAR(50) NOT NULL,         -- e.g., 'Revenue', 'Expense', 'Asset'
    FinancialStatement VARCHAR(50) NOT NULL,  -- e.g., 'Income Statement', 'Balance Sheet'
    IsActive BIT DEFAULT 1                    -- 1 = Active, 0 = Inactive
);

-- 2. Fact: General Ledger (The Bronze/Silver Layer)
-- This holds the raw transactions.
CREATE TABLE Fact_GeneralLedger (
    TransactionID VARCHAR(50) PRIMARY KEY,    -- Unique ID from ERP
    TransactionDate DATE NOT NULL,
    AccountCode VARCHAR(20) NOT NULL,         -- Links to Dim_ChartOfAccounts
    Description VARCHAR(255),                 -- Context (e.g., 'Inv #1001')
    AmountGHS DECIMAL(18, 2) NOT NULL,        -- Positive = Debit, Negative = Credit
    CreatedDate DATETIME DEFAULT CURRENT_TIMESTAMP,
    
    -- Foreign Key Constraint (Safety Mechanism)
    -- Ensures we don't load transactions for accounts that don't exist.
    FOREIGN KEY (AccountCode) REFERENCES Dim_ChartOfAccounts(AccountCode)
);

-- 3. Validation: Forensic Log
-- If a batch fails validation (Debits != Credits), we log it here.
CREATE TABLE Audit_Log (
    LogID INTEGER PRIMARY KEY,
    CheckName VARCHAR(50),      -- e.g., 'Debit_Credit_Check'
    Status VARCHAR(20),         -- 'PASS' or 'FAIL'
    Message VARCHAR(255),
    LogDate DATETIME DEFAULT CURRENT_TIMESTAMP
);