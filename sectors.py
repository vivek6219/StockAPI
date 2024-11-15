import yfinance as yf
import pandas as pd

class Sectors:
    
    basic_materials_market_weight = yf.Sector('basic-materials').top_companies.sort_values(by="market weight", ascending=False)
    # basic_materials_market_cap = yf.Sector('basic-materials').top_companies.sort_values(by="market cap", ascending=False)

    communication_services_market_weight = yf.Sector('communication-services').top_companies.sort_values(by="market weight", ascending=False)
    # communication_services_market_cap = yf.Sector('communication-services').top_companies.sort_values(by="market cap", ascending=False)

    consumer_cyclical_market_weight = yf.Sector('consumer-cyclical').top_companies.sort_values(by="market weight", ascending=False)
    # consumer_cyclical_market_cap = yf.Sector('consumer-cyclical').top_companies.sort_values(by="market cap", ascending=False)

    consumer_defensive_market_weight = yf.Sector('consumer-defensive').top_companies.sort_values(by="market weight", ascending=False)
    # consumer_defensive_market_cap = yf.Sector('consumer-defensive').top_companies.sort_values(by="market cap", ascending=False)

    energy_market_weight = yf.Sector('energy').top_companies.sort_values(by="market weight", ascending=False)
    # energy_market_cap = yf.Sector('energy').top_companies.sort_values(by="market cap", ascending=False)

    financial_services_market_weight = yf.Sector('financial-services').top_companies.sort_values(by="market weight", ascending=False)
    # financial_services_market_cap = yf.Sector('financial-services').top_companies.sort_values(by="market cap", ascending=False)
    
    healthcare_market_weight = yf.Sector('healthcare').top_companies.sort_values(by="market weight", ascending=False)
    # healthcare_market_cap = yf.Sector('healthcare').top_companies.sort_values(by="market cap", ascending=False)
    
    industrials_market_weight = yf.Sector('industrials').top_companies.sort_values(by="market weight", ascending=False)
    # industrials_market_cap = yf.Sector('industrials').top_companies.sort_values(by="market cap", ascending=False)
    
    real_estate_market_weight = yf.Sector('real-estate').top_companies.sort_values(by="market weight", ascending=False)
    # real_estate_market_cap = yf.Sector('real-estate').top_companies.sort_values(by="market cap", ascending=False)
    
    technology_market_weight = yf.Sector('technology').top_companies.sort_values(by="market weight", ascending=False)
    # technology_market_cap = yf.Sector('technology').top_companies.sort_values(by="market cap", ascending=False)
    
    utilities_market_weight = yf.Sector('utilities').top_companies.sort_values(by="market weight", ascending=False)
    # utilities_market_cap = yf.Sector('utilities').top_companies.sort_values(by="market cap", ascending=False)


    # print(basic_materials_market_weight)
    # print(communication_services_market_weight)
    # print(consumer_cyclical_market_weight)
    # print(consumer_defensive_market_weight)
    # print(energy_market_weight)
    # print(financial_services_market_weight)
    # print(healthcare_market_weight)
    # print(industrials_market_weight)
    # print(real_estate_market_weight)
    # print(technology_market_weight)
    # print(utilities_market_weight)

    # print(yf.Ticker("LIN").info)

class Industries:
    