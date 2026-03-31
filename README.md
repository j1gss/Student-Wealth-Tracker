# STUDENT FINANCE MANAGER
![Python](https://img.shields.io/badge/Python-3.8%2B-white?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-pink?style=flat&logo=pandas)
![Streamlit](https://img.shields.io/badge/Streamlit-black?style=flat&logo=streamlit)
## Project Review
This project deals with the problem of **Financial Literacy among University Students**. In an era of instant UPI transactions, tracking micro-expenses often becomes secondary,
leading to budget deficits.

**Student Finance Manager** is a Utility-Based Rational Agent designed to help students track and optimize their spending. Unlike static spreadsheets, it uses data 
visualization to provide immediate feedback on financial health, allowing users to make "rational decisions" based on real-time budget constraints.

## Features
- Categorized Expense Logging: Users can input data across diverse categories (Food, Academics, Leisure, etc.).
- Data Persistence: Uses CSV-based storage to maintain record history across sessions.
- Interactive Dashboard: Built with Streamlit to provide real-time metrics and graphical distributions of spending habits.

## Technologies & Tools Used
- Python: Core application logic.
- Pandas: Used for high-performance data manipulation and CSV handling.
- Streamlit: Framework used to create the interactive web interface and dashboards.

## Steps to Install & Run
#### 1.Clone the Repository
```
git clone https://github.com/j1gss/Student-Wealth-Tracker.git
```
```
cd Student-Wealth-Tracker
```
#### 2.Install the dependencies
```
pip install -r requirements.txt
```
#### 3.Basic Usage
```
streamlit run main.py
```

## Instructions for Testing & Advanced Usage
In order to test the functionality of the tool,do the following test cases:

**Test Case 1:Fixed Cost Calculation**
  *Set Rent/Bills to ₹100 and Mess to ₹250. Verify that the "Fixed Costs" output displays ₹350.0 correctly.*
  
**Test Case 2:Negative Liquidity (Debt State)**
  *With an allowance of ₹5000 and total costs exceeding this (e.g., a Flight for ₹5100), verify that "Remaining Liquidity" reflects the negative deficit (e.g., -₹450.0).*
  
**Test Case 3:Emergency Preservation** 
*Adjust the "Emergency Stash %" slider and confirm that the "Emergency Reserve" amount recalculates without affecting fixed cost commitments.*
