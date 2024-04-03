#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 3 15:19:14 2024

@author: emmanuel
"""

from flask import Flask, render_template, request  # Import 'request' for handling POST data
import yfinance as yf

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/result', methods=['POST'])
def result():
    age = request.form.get('age')
    income = request.form.get('income')
    investment_horizon = request.form.get('investment_horizon')
    risk_tolerance = request.form.get('risk_tolerance')
    portfolio = determine_portfolio(risk_tolerance)
    return render_template('result.html', portfolio=portfolio)

@app.route('/admin')
@app.route('/admin/<asset_type>')
def admin_dashboard(asset_type=None):
    tickers = {'stock': ['AAPL', 'GOOG', 'MSFT'], 'bond': ['TLT', 'BND']}
    data = {}
    
    selected_tickers = tickers.get(asset_type, tickers['stock'] + tickers['bond'])
    
    for ticker in selected_tickers:
        stock = yf.Ticker(ticker)
        data[ticker] = stock.info
        
    return render_template('admin_dashboard.html', data=data, asset_type=asset_type)

def determine_portfolio(risk_tolerance):
    if risk_tolerance == 'low':
        return {'bond': 0.7, 'stock': 0.3}
    elif risk_tolerance == 'medium':
        return {'bond': 0.4, 'stock': 0.6}
    else:  # 'high' risk tolerance
        return {'bond': 0.2, 'stock': 0.8}

if __name__ == '__main__':
    app.run(debug=True)
