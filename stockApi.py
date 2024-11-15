from scrape import Scrape
import yfinance as yf
# from sectors import Sectors
from requests import Session
from requests_cache import CacheMixin, SQLiteCache
from requests_ratelimiter import LimiterMixin, MemoryQueueBucket
from pyrate_limiter import Duration, RequestRate, Limiter

class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass

session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*5)), # max 2 requests per 5 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
)




# session = requests_cache.CachedSession('yfinance.cache')
# session.headers['User-agent'] = 'my-program/1.0'
# ticker = yf.Ticker('msft', session = session)


#data from specific sectors
# tech = yf.Sector('technology')

#data from specific industries
# software = yf.Industry('software-infrastructure')

# msft = yf.Ticker("MSFT")
# spy = yf.Ticker('SPY')
# data = spy.funds_data


# my_dict = {
#     'calendar': msft.calendar
# }
# print(my_dict)

# print(data.top_holdings)



# apiCall ='https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'

# response = requests.get(apiCall)

# print(response.json())