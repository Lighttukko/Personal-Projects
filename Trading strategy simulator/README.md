# Trading Strategy Simulator

## Description
Trading Strategy Simulator is an early-stage backend project designed to help myself and beginner investors test simple trading ideas before risking real money in the market. Instead of immediately buying and selling stocks based on intuition, users can use historical market data to evaluate whether a strategy would have been profitable in the past.

The project loads historical stock price data from CSV files, processes the data, and provides backend API endpoints for previewing and analyzing the dataset. This creates the foundation for future backtesting features, where users will be able to simulate trades, measure profit and loss, and compare strategy performance over time. 

While similar tools already exist, I chose to build this project myself to explore the backend architecture in greater depth and to create a version tailored to my own goals and design preferences.

## Current Features
- Loads historical stock data from CSV files
- Validates and preprocesses stock market data
- Sorts and formats historical price records by date
- Exposes FastAPI endpoints for stock data preview
- Returns structured JSON responses for future integration with strategy-testing workflows

## Tech Stack
- **Python**
- **FastAPI**
- **Pandas**
- **Uvicorn**

## Project Goal
The main goal of this project is to build a backend system that can test rule-based trading strategies on historical stock data. This allows users to analyze how a strategy might have performed before using real money.

## Current Progress
At this stage, the project has completed the initial backend foundation:
- Set up the FastAPI application
- Implemented CSV-based stock data ingestion
- Added preprocessing for historical market data
- Built a preview API endpoint to inspect structured stock records

## Future Improvements
- Add strategy execution logic for simulated buy and sell decisions
- Calculate portfolio value and profit/loss
- Support multiple trading strategies
- Add performance metrics such as win rate and drawdown
- Store backtest results in a database
- Build a frontend dashboard for easier visualization

## How to Run
1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies:
   pip install -r requirements.txt