-- =========================================
-- Database: walmart_data
-- Description: Schema for Walmart weekly sales analysis
-- =========================================

CREATE DATABASE IF NOT EXISTS walmart_data;
USE walmart_data;

CREATE TABLE IF NOT EXISTS sales (
    Store INT,
    Date DATE,
    Weekly_Sales DECIMAL(10,2),
    Holiday_Flag BOOLEAN,
    Temperature FLOAT,
    Fuel_Price FLOAT,
    CPI FLOAT,
    Unemployment FLOAT,
    UNIQUE (Store, Date) 
);