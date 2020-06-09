# !/Users/adityaoberai/Programming/Python/StockPriceRetriever/venv/bin/python

import portfolio_manager
import trading_strategies
import web
import yf_web_scraper
from utils import multithreading, json_simplifier as json_simp

portfolio_manager.refresh_account()
multithreading.run_thread(web.init_web)
multithreading.run_thread(trading_strategies.evaluate_purchased_stocks)

while True:
    json_simp.read_json()
    most_active_stocks = yf_web_scraper.get_active_tickers()
    print(most_active_stocks)
    portfolio_manager.print_account_status()
    multithreading.run_chunked_threads(most_active_stocks, trading_strategies.run_stock_pipelines, 37)
