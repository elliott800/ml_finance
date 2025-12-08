#jansen_lib_mlfat.py
#machine learning for algorithmic trading-stefan ansen
#ip notice
'''The fundamental law of active management
A high Information Ratio (IR) implies attractive out-performance relative to the additional risk taken. The Fundamental Law of Active Management breaks the IR down into the information coefficient (IC) as a measure of forecasting skill, and the ability to apply this skill through independent bets. It summarizes the importance to play both often (high breadth) and to play well (high IC):

its pretty obvious how to mkae these things now.... its data mining but.... i mean its relationship discovery and the way i deal with over fitting i do all my research on one test group of similarly structured assets to another test set, im doing it by eye now but what ill likely do is make a bunch of discriptivbe stats and put them in vectors then GACUC or Kmeans them and then ill cut the groups in half and fit a model to one group and use the other set as the final test group for that model and then catalog it with its stats in a database or something.
and always use 1 fwd shifted returns when doing analysis.

all regression factors require models that feed into the primary model because, the factors have to be predicted 1 step forward then the primary model predicted one step forward and repeat using the predictions as new inputs.
The IC measures the correlation between an alpha factor and the forward returns resulting from its signals and captures the accuracy of a manager's forecasting skills. The breadth of the strategy is measured by the independent number of bets an investor makes in a given time period, and the product of both values is proportional to the IR, also known as appraisal risk (Treynor and Black).

This framework has been extended to include the transfer coefficient (TC) to reflect portfolio constraints (for example, on short-selling) that may limit the information ratio below a level otherwise achievable given IC or strategy breadth. The TC proxies the efficiency with which the manager translates insights into portfolio bets (Clarke et al. 2002).

The fundamental law is important because it highlights the key drivers of outperformance: both accurate predictions and the ability to make independent forecasts and act on these forecasts matter. In practice, managers with a broad set of investment decisions can achieve significant risk-adjusted excess returns with information coefficients between 0.05 and 0.15 (if there is space possibly include simulation chart).

In practice, estimating the breadth of a strategy is difficult given the cross-sectional and time-series correlation among forecasts. '''

'''dude just monte carloing a bunch of price outcomes over x days for a whole bunch of individual options to see which one has the highest expected rutrn when weighting based on the expected probability distributuions [markov chain of distribution states, either a two state model high volatility low volatility or create discriptive stats clustered then probability of moving from one cluster to another gives the weight of that clusters discriptive stats to model]. then combining low correlation options to reduce variance while leaving the return intact so long as the low correlation options have the same return.
'''
'''quantopian shut down in 2020, (underperformance of its investment strategies) a whole lot of ice cream sales predicts polio cases can out weigh the very specific and less easily saught after reliable modeling techniques, instead of overfit the relationship with hyper parameter tuning, more people isnt always smarter, QuantRocket may be the new alternative these quantopian examples are currently untested 11/8/25'''
'''QuantConnect
QuantConnect is another open source, community-driven algorithmic trading platform that competes with Quantopian. It also provides an IDE to backtest and live-trade algorithmic strategies using Python and other languages.

QuantConnect also has a dynamic, global community from all over the world, and provides access to numerous asset classes, including equities, futures, forex, and cryptocurrency. It offers live-trading integration with various brokers such as IB, OANDA, and GDAX.'''


'''AlternativeData.org (supported by provider Yipit) 
lists several categories that can serve as a rough proxy 
for activity in various data-provider segments. 
Social sentiment analysis is by far the largest category, 
while satellite and geolocation data have been growing 
rapidly in recent years:'''

'''Social sentiment data
Social sentiment analysis is most closely associated with Twitter data. Gnip was an early social-media aggregator that provided data from numerous sites using an API and was acquired by Twitter in 2014 for $134 million. Search engines are another source that became prominent when researchers published in nature that investment strategies based on Google Trends for terms such as debt could be used for a profitable trading strategy over an extended period (see the GitHub repo https://github.com/PacktPublishing/Hands-On-Machine-Learning-for-Algorithmic-Trading for references).'''

'''Dataminr
Dataminr was founded in 2009 and provides social-sentiment and news analysis based on an exclusive agreement with Twitter. The company is one of the larger alternative providers and raised an additional $392 million in funding in June 2018 led by Fidelity at a $1,6 billion valuation, bringing total funding to $569 billion. It emphasizes real-time signals extracted from social media feeds using machine learning and serves a wide range of clients, including not only buy and sell-side investment firms but also news organizations and the public sector.'''

'''StockTwits
StockTwits is a social network and micro-blogging platform where several hundred thousand investment professionals share information and trading ideas in the form of StockTwits that are viewed by a large audience across the financial web and social media platforms. This data can be exploited because it may reflect investor sentiment or itself drive trades that, in turn, impact prices. The references on GitHub contain a link to a paper that builds a trading strategy on selected features.'''

'''RavenPack
RavenPack analyzes a large number of diverse, unstructured, text-based data to produce structured indicators, including sentiment scores, that aim to contain information relevant to investors. The underlying data sources range from premium newswires and regulatory information to press releases and over 19,000 web publications. J.P. Morgan tested a long-short sovereign bond and equity strategies based on sentiment scores and achieved positive results with low correlation to conventional risk premiums (see references).'''

'''Satellite data
RS Metrics, founded in 2010, triangulates geospatial data from satellites, drones, and airplanes with a focus on metals and commodities, as well as real-estate and industrial applications. The company offers signals, predictive analytics, alerts, and end-user applications based on its own high-resolution satellites. Use cases include the estimation of retail traffic targeting certain chains or commercial real estate, as well as the production and storage of certain common metals or employment at related production locations.'''

'''Geolocation data
Advan, founded in 2015, serves hedge fund clients with signals derived from mobile phone traffic data, targeting 1,600 tickers across various sectors in the US and EU. The company collects data using apps that install geolocation codes on smartphones with explicit user consent and track location using several channels (such as WiFi, Bluetooth, and cellular signal) for enhanced accuracy. The uses cases include estimates of customer traffic at physical store locations, which in turn can be used as input to models that predict top-line revenues of traded companies.'''

'''Email receipt data
Eagle Alpha provides, among other services, data on a large set of online transactions using email receipts, covering over 5000 retailers, including item—and SKU-level transaction data categorized in 53 product groups. J.P. Morgan analyzed a time series dataset, starting in 2013, that covered a constant group of users active throughout the entire sample period. The dataset contained total aggregate spend, number of orders, and the number of unique buyers per period.'''

'''TA-Lib
The TA-Lib library includes numerous technical factors. A Python implementation is available for local use, for example, with zipline and alphalens, and it is also available on the Quantopian platform. The notebook also illustrates several technical indicators available using TA-Lib.'''

'''Built-in Quantopian factors
The accompanying notebook factor_library.ipynb contains numerous example factors that are either provided by the Quantopian platform or computed from data sources available using the research API from a Jupyter Notebook.

There are built-in factors that can be used, in combination with quantitative Python libraries, in particular numpy and pandas, to derive more complex factors from a broad range of relevant data sources such as US Equity prices, Morningstar fundamentals, and investor sentiment.

For instance, the price-to-sales ratio, the inverse of the sales yield introduce preceding, is available as part of the Morningstar fundamentals dataset. It can be used as part of a pipeline that is further described as we introduce the zipline library.'''

'''Seeking signals – how to use zipline
Historically, alpha factors used a single input and simple heuristics, thresholds or quantile cutoffs to identify buy or sell signals. ML has proven quite effective in extracting signals from a more diverse and much larger set of input data, including other alpha factors based on the analysis of historical patterns. As a result, algorithmic trading strategies today leverage a large number of alpha signals, many of which may be weak individually but can yield reliable predictions when combined with other model-driven or traditional factors by an ML algorithm.

The open source zipline library is an event-driven backtesting system maintained and used in production by the crowd-sourced quantitative investment fund Quantopian (https://www.quantopian.com/) to facilitate algorithm-development and live-trading. It automates the algorithm's reaction to trade events and provides it with current and historical point-in-time data that avoids look-ahead bias.

You can use it offline in conjunction with data bundles to research and evaluate alpha factors. When using it on the Quantopian platform, you will get access to a wider set of fundamental and alternative data. We will also demonstrate the Quantopian research environment in this chapter, and the backtesting IDE in the next chapter. The code for this section is in the 01_factor_research_evaluation sub-directory of the GitHub repo folder for this chapter.

After installation and before executing the first algorithm, you need to ingest a data bundle that by default consists of Quandl's community-maintained data on stock prices, dividends and splits for 3,000 US publicly-traded companies. You need a Quandl API key to run the following code that stores the data in your home folder under ~/.zipline/data/<bundle>:

$ QUANDL_API_KEY=<yourkey> zipline ingest [-b <bundle>]'''

'''The architecture – event-driven trading simulation
A zipline algorithm will run for a specified period after an initial setup and executes its trading logic when specific events occur. These events are driven by the trading frequency and can also be scheduled by the algorithm, and result in zipline calling certain methods. The algorithm maintains state through a context dictionary and receives actionable information through a data variable containing point-in-time (PIT) current and historical data. The algorithm returns a DataFrame containing portfolio performance metrics if there were any trades, as well as user-defined metrics that can be used to record, for example, the factor values. 

You can execute an algorithm from the command line, in a Jupyter Notebook, and by using the run_algorithm() function.

An algorithm requires an initialize() method that is called once when the simulation starts. This method can be used to add properties to the context dictionary that is available to all other algorithm methods or register pipelines that perform more complex data processing, such as filtering securities based, for example, on the logic of alpha factors.

Algorithm execution occurs through optional methods that are either scheduled automatically by zipline or at user-defined intervals. The method before_trading_start() is called daily before the market opens and serves primarily to identify a set of securities the algorithm may trade during the day. The method handle_data() is called every minute.

The Pipeline API facilitates the definition and computation of alpha factors for a cross-section of securities from historical data. A pipeline defines computations that produce columns in a table with PIT values for a set of securities. It needs to be registered with the initialize() method and can then be executed on an automatic or custom schedule. The library provides numerous built-in computations such as moving averages or Bollinger Bands that can be used to quickly compute standard factors but also allows for the creation of custom factors as we will illustrate next. 

Most importantly, the Pipeline API renders alpha factor research modular because it separates the alpha factor computation from the remainder of the algorithm, including the placement and execution of trade orders and the bookkeeping of portfolio holdings, values, and so on.'''

'''Alternative algorithmic trading libraries
Additional open-source Python libraries for algorithmic trading and data collection include (see links on GitHub):

QuantConnect is a competitor to Quantopian
WorldQuant offers online competition and recruits community contributors to a crowd-sourced hedge fund
Alpha Trading Labs offers high-frequency focused testing infrastructure with a business model similar to Quantopian
Python Algorithmic Trading Library (PyAlgoTrade) focuses on backtesting and offers support for paper-trading and live-trading. It allows you to evaluate an idea for a trading strategy with historical data and aims to do so with minimal effort.
pybacktest is a vectorized backtesting framework that uses pandas and aims to be compact, simple and fast (the project is currently on hold)
ultrafinance is an older project that combines real-time financial data collection, analyzing and backtesting of trading strategies
Trading with Python offers courses and a collection of functions and classes for Quantitative trading
Interactive Brokers offers a Python API for live trading on their platform'''

'''A single alpha factor from market data
We are first going to illustrate the zipline alpha factor research workflow in an offline environment. In particular, we will develop and test a simple mean-reversion factor that measures how much recent performance has deviated from the historical average. Short-term reversal is a common strategy that takes advantage of the weakly predictive pattern that stock price increases are likely to mean-revert back down over horizons from less than a minute to one month. See the Notebook single_factor_zipline.ipynby for details.

To this end, the factor computes the z-score for the last monthly return relative to the rolling monthly returns over the last year. At this point, we will not place any orders to simply illustrate the implementation of a CustomFactor and record the results during the simulation.

After some basic settings, MeanReversion subclasses CustomFactor and defines a compute() method. It creates default inputs of monthly returns over an also default year-long window so that the monthly_return variable will have 252 rows and one column for each security in the Quandl dataset on a given day.

The compute_factors() method creates a MeanReversion factor instance and creates long, short, and ranking pipeline columns. The former two contain Boolean values that could be used to place orders, and the latter reflects that overall ranking to evaluate the overall factor performance. Furthermore, it uses the built-in AverageDollarVolume factor to limit the computation to more liquid stocks:'''

from zipline import run_algorithm
from zipline.api import attach_pipeline, pipeline_output, record
from zipline.pipeline import CustomFactor, Pipeline
from zipline.pipeline.factors import AverageDollarVolume, Returns

MONTH, YEAR = 21, 252
N_LONGS = N_SHORTS = 25
VOL_SCREEN = 1000

class MeanReversion(CustomFactor):
    """Compute ratio of latest monthly return to 12m average,
       normalized by std dev of monthly returns"""
    inputs = [Returns(window_length=MONTH)]
    window_length = YEAR
    def compute(self, today, assets, out, monthly_returns):
        df = pd.DataFrame(monthly_returns)
        out[:] = df.iloc[-1].sub(df.mean()).div(df.std())
def compute_factors():
    """Create factor pipeline incl. mean reversion,
        filtered by 30d Dollar Volume; capture factor ranks"""
    mean_reversion = MeanReversion()
    dollar_volume = AverageDollarVolume(window_length=30)
    return Pipeline(columns={'longs'  : mean_reversion.bottom(N_LONGS),
                             'shorts' : mean_reversion.top(N_SHORTS),
                             'ranking': 
                          mean_reversion.rank(ascending=False)},
                          screen=dollar_volume.top(VOL_SCREEN))
'''
The result would allow us to place long and short orders. We will see in the next chapter how to build a portfolio by choosing a rebalancing period and adjusting portfolio holdings as new signals arrive.
The initialize() method registers the compute_factors() pipeline, and the before_trading_start() method ensures the pipeline runs on a daily basis. The record() function adds the pipeline's ranking column as well as the current asset prices to the performance DataFrame returned by the run_algorithm() function:'''
def initialize(context):
    """Setup: register pipeline, schedule rebalancing,
        and set trading params"""
    attach_pipeline(compute_factors(), 'factor_pipeline')
def before_trading_start(context, data):
    """Run factor pipeline"""
    context.factor_data = pipeline_output('factor_pipeline')
    record(factor_data=context.factor_data.ranking)
    assets = context.factor_data.index
    record(prices=data.current(assets, 'price'))
'''Finally, define the start and end Timestamp objects in UTC terms, set a capital base and execute run_algorithm() with references to the key execution methods. The performance DataFrame contains nested data, for example, the prices column consists of a pd.Series for each cell. Hence, subsequent data access is easier when stored in the pickle format:'''
start, end = pd.Timestamp('2015-01-01', tz='UTC'), pd.Timestamp('2018-01-01', tz='UTC')
capital_base = 1e7
performance = run_algorithm(start=start,
                            end=end,
                            initialize=initialize,
                            before_trading_start=before_trading_start,
                            capital_base=capital_base)
performance.to_pickle('single_factor.pickle')
'''We will use the factor and pricing data stored in the performance DataFrame to evaluate the factor performance for various holding periods in the next section, but first, we'll take a look at how to create more complex signals by combining several alpha factors from a diverse set of data sources on the Quantopian platform.'''

'''Combining factors from diverse data sources
The Quantopian research environment is tailored to the rapid testing of predictive alpha factors. The process is very similar because it builds on zipline, but offers much richer access to data sources. The following code sample illustrates how to compute alpha factors not only from market data as previously but also from fundamental and alternative data. See the Notebook multiple_factors_quantopian_research.ipynb for details.

Quantopian provides several hundred MorningStar fundamental variables for free and also includes stocktwits signals as an example of an alternative data source. There are also custom universe definitions such as QTradableStocksUS that applies several filters to limit the backtest universe to stocks that were likely tradeable under realistic market conditions: '''

from quantopian.pipeline import Pipeline
from quantopian.pipeline.data.builtin import USEquityPricing
from quantopian.pipeline.data.morningstar import income_statement
from quantopian.research import run_pipeline

     operation_ratios, balance_sheet
from quantopian.pipeline.data.psychsignal import stocktwits
from quantopian.pipeline.factors import CustomFactor

     SimpleMovingAverage, Returns
from quantopian.pipeline.filters import QTradableStocksUS

We will use a custom AggregateFundamentals class to use the last reported fundamental data point. This aims to address the fact that fundamentals are reported quarterly, and Quantopian does not currently provide an easy way to aggregate historical data, say to obtain the sum of the last four quarters, on a rolling basis:

class AggregateFundamentals(CustomFactor):
    def compute(self, today, assets, out, inputs):
        out[:] = inputs[0]
'''We will again use the custom MeanReversion factor from the preceding code. We will also compute several other factors for the given universe definition using the rank() method's mask parameter:'''

def compute_factors():
    universe = QTradableStocksUS()

    profitability = (AggregateFundamentals(inputs=
                     [income_statement.gross_profit],
                                           window_length=YEAR) /
                     balance_sheet.total_assets.latest).rank(mask=universe)

    roic = operation_ratios.roic.latest.rank(mask=universe)
    ebitda_yield = (AggregateFundamentals(inputs=
                             [income_statement.ebitda],
                                          window_length=YEAR) /
                    USEquityPricing.close.latest).rank(mask=universe)
    mean_reversion = MeanReversion().rank(mask=universe)
    price_momentum = Returns(window_length=QTR).rank(mask=universe)
    sentiment = SimpleMovingAverage(inputs=
                            [stocktwits.bull_minus_bear],
                                    
                            window_length=5).rank(mask=universe)

    factor = profitability + roic + ebitda_yield + mean_reversion + 
             price_momentum + sentiment

    return Pipeline(
            columns={'Profitability'      : profitability,
                     'ROIC'               : roic,
                     'EBITDA Yield'       : ebitda_yield,
                     "Mean Reversion (1M)": mean_reversion,
                     'Sentiment'          : sentiment,
                     "Price Momentum (3M)": price_momentum,
                     'Alpha Factor'       : factor})
'''This algorithm uses a naive method to combine the six individual factors by simply adding the ranks of assets for each of these factors. Instead of equal weights, we would like to take into account the relative importance and incremental information in predicting future returns. The ML algorithms of the next chapters will allow us to do exactly this, using the same backtesting framework.'''

'''Execution also relies on run_algorithm(), but the return DataFrame on the Quantopian platform only contains the factor values created by the Pipeline. This is convenient because this data format can be used as input for alphalens, the library for the evaluation of the predictive performance of alpha factors.'''

Creating forward returns and factor quantiles
To utilize alphalens, we need to provide signals for a universe of assets like those returned by the ranks of the MeanReversion factor, and the forward returns earned by investing in an asset for a given holding period. See Notebook 03_performance_eval_alphalens.ipynb for details.

We will recover the prices from the single_factor.pickle file as follows (factor_data accordingly):

performance = pd.read_pickle('single_factor.pickle')

prices = pd.concat([df.to_frame(d) for d, df in performance.prices.items()],axis=1).T
prices.columns = [re.findall(r"\[(.+)\]", str(col))[0] for col in 
                  prices.columns]
prices.index = prices.index.normalize()
prices.info()

<class 'pandas.core.frame.DataFrame'>
DatetimeIndex: 755 entries, 2015-01-02 to 2017-12-29
Columns: 1661 entries, A to ZTS
dtypes: float64(1661)

'''The GitHub repository's alpha factor evaluation Notebook has more detail on how to conduct the evaluation in a sector-specific way.

We can create the alphalens input data in the required format using the get_clean_factor_and_forward_returns utility function that also returns the signal quartiles and the forward returns for the given holding periods:'''

HOLDING_PERIODS = (5, 10, 21, 42)
QUANTILES = 5
alphalens_data = get_clean_factor_and_forward_returns(factor=factor_data,
                                     prices=prices,
                                     periods=HOLDING_PERIODS,
                                     quantiles=QUANTILES)

'''Dropped 14.5% entries from factor data: 14.5% in forward returns computation and 0.0% in binning phase (set max_loss=0 to see potentially suppressed Exceptions). max_loss is 35.0%, not exceeded: OK!
 The alphalens_data DataFrame contains the returns on an investment in the given asset on a given date for the indicated holding period, as well as the factor value, that is, the asset's MeanReversion ranking on that date, and the corresponding quantile value:'''
#################################################
'''How to build and test a portfolio with zipline
In the last chapter, we introduced zipline to simulate the computation of alpha factors from trailing cross-sectional market, fundamental, and alternative data. Now we will exploit the alpha factors to derive and act on buy and sell signals. We will postpone optimizing the portfolio weights until later in this chapter, and for now, just assign positions of equal value to each holding. The code for this section is in the 01_trading_zipline subdirectory.'''

'''cheduled trading and portfolio rebalancing
We will use the custom MeanReversion factor developed in the last chapter—see the implementation in alpha_factor_zipline_with_trades.py.

The Pipeline created by the compute_factors() method returns a table with a long and a short column for the 25 stocks with the largest negative and positive deviations of their last monthly return from its annual average, normalized by the standard deviation. It also limited the universe to the 500 stocks with the highest average trading volume over the last 30 trading days. before_trading_start() ensures the daily execution of the pipeline and the recording of the results, including the current prices.

The new rebalance() method submits trade orders to the exec_trades() method for the assets flagged for long and short positions by the pipeline with equal positive and negative weights. It also divests any current holdings that are no longer included in the factor signals:'''

def exec_trades(data, assets, target_percent):
    """Place orders for assets using target portfolio percentage"""
    for asset in assets:
        if data.can_trade(asset) and not get_open_orders(asset):
            order_target_percent(asset, target_percent)

def rebalance(context, data):
    """Compute long, short and obsolete holdings; place trade orders"""
    factor_data = context.factor_data
    assets = factor_data.index

    longs = assets[factor_data.longs]
    shorts = assets[factor_data.shorts]
    divest = context.portfolio.positions.keys() - longs.union(shorts)

    exec_trades(data, assets=divest, target_percent=0)
    exec_trades(data, assets=longs, target_percent=1 / N_LONGS)
    exec_trades(data, assets=shorts, target_percent=-1 / N_SHORTS)
'''The rebalance() method runs according to date_rules and time_rules set by the schedule_function() utility at the beginning of the week, right after market_open as stipulated by the built-in US_EQUITIES calendar (see docs for details on rules). You can also specify a trade commission both in relative terms and as a minimum amount. There is also an option to define slippage, which is the cost of an adverse change in price between trade decision and execution:'''

def initialize(context):
    """Setup: register pipeline, schedule rebalancing,
        and set trading params"""
    attach_pipeline(compute_factors(), 'factor_pipeline')
    schedule_function(rebalance,
                      date_rules.week_start(),
                      time_rules.market_open(),
                      calendar=calendars.US_EQUITIES)

    set_commission(us_equities=commission.PerShare(cost=0.00075, min_trade_cost=.01))
    set_slippage(us_equities=slippage.VolumeShareSlippage(volume_limit=0.0025, price_impact=0.01))
'''The algorithm continues to execute after calling the run_algorithm() function and returns the same backtest performance DataFrame. We will now turn to common measures of portfolio return and risk, and how to compute them using the pyfolio library.'''

'''Getting pyfolio input from alphalens
However, pyfolio also integrates with alphalens directly and permits the creation of pyfolio input data using create_pyfolio_input:'''

from alphalens.performance import create_pyfolio_input

qmin, qmax = factor_data.factor_quantile.min(), 
             factor_data.factor_quantile.max()
input_data = create_pyfolio_input(alphalens_data,   
                                  period='1D',
                                  capital=100000,
                                  long_short=False,
                                  equal_weight=False,
                                  quantiles=[1, 5],
                                  benchmark_period='1D')
returns, positions, benchmark = input_data
'''There are two options to specify how portfolio weights will be generated: 

long_short: If False, weights will correspond to factor values divided by their absolute value so that negative factor values generate short positions. If True, factor values are first demeaned so that long and short positions cancel each other out and the portfolio is market neutral.
equal_weight: If True, and long_short is True, assets will be split into two equal-sized groups with the top/bottom half making up long/short positions.
Long-short portfolios can also be created for groups if factor_data includes, for example, sector info for each asset.'''

'''The result of a zipline backtest can be converted into the required pyfolio input using extract_rets_pos_txn_from_zipline:'''

returns, positions, transactions = 
         extract_rets_pos_txn_from_zipline(backtest)

#################################################
'''Walk-forward testing  out-of-sample returns
Testing a trading strategy involves backtesting against historical data to fine-tune alpha factor parameters, as well as forward-testing against new market data to validate that the strategy performs well out of sample or if the parameters are too closely tailored to specific historical circumstances.

Pyfolio allows for the designation of an out-of-sample period to simulate walk-forward testing. There are numerous aspects to take into account when testing a strategy to obtain statistically reliable results, which we will address here. 

The plot_rolling_returns function displays cumulative in and out-of-sample returns against a user-defined benchmark (we are using the S&P 500):'''

from pyfolio.plotting import plot_rolling_returns

plot_rolling_returns(returns=returns,
                     factor_returns=benchmark_rets,
                     live_start_date='2017-01-01',
                     cone_std=(1.0, 1.5, 2.0))
'''The plot includes a cone that shows expanding confidence intervals to indicate when out-of-sample returns appear unlikely given random-walk assumptions. Here, our strategy did not perform well against the benchmark during the simulated 2017 out-of-sample period:'''

#########################################################
'''Summary performance statistics
pyfolio offers several analytic functions and plots. The perf_stats summary displays the annual and cumulative returns, volatility, skew, and kurtosis of returns and the SR. The following additional metrics (which can also be calculated individually) are most important:

Max drawdown: Highest percentage loss from the previous peak
Calmar ratio: Annual portfolio return relative to maximal drawdown
Omega ratio: The probability-weighted ratio of gains versus losses for a return target, zero per default
Sortino ratio: Excess return relative to downside standard deviation
Tail ratio: Size of the right tail (gains, the absolute value of the 95th percentile) relative to the size of the left tail (losses, abs. value of the 5th percentile) 
Daily value at risk (VaR): Loss corresponding to a return two standard deviations below the daily mean
Alpha: Portfolio return unexplained by the benchmark return
Beta: Exposure to the benchmark'''

from pyfolio.timeseries import perf_stats

perf_stats(returns=returns, 
           factor_returns=benchmark_rets, 
           positions=positions, 
           transactions=transactions)
'''For the simulated long-short portfolio derived from the MeanReversion factor, we obtain the following performance statistics:'''

###########################################################
'''Drawdown periods and factor exposure
The plot_drawdown_periods(returns) function plots the principal drawdown periods for the portfolio, and several other plotting functions show the rolling SR and rolling factor exposures to the market beta or the Fama French size, growth, and momentum factors:
'''
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(16, 10))
axes = ax.flatten()

plot_drawdown_periods(returns=returns, ax=axes[0])
plot_rolling_beta(returns=returns, factor_returns=benchmark_rets, 
                  ax=axes[1])
plot_drawdown_underwater(returns=returns, ax=axes[2])
plot_rolling_sharpe(returns=returns)
'''This plot, which highlights a subset of the visualization contained in the various tear sheets, illustrates how pyfolio allows us to drill down into the performance characteristics and exposure to fundamental drivers of risk and returns:'''

###########################################################
'''The minimum backtest length and the deflated SR
Marcos Lopez de Prado (http://www.quantresearch.info/) has published extensively on the risks of backtesting, and how to detect or avoid it. This includes an online simulator of backtest-overfitting (http://datagrid.lbl.gov/backtest/).'''

'''Another result includes an estimate of the minimum length of the backtest that an investor should require given the number of trials attempted, to avoid selecting a strategy with a given in-sample SR during a given number of trials that has an expected out-of-sample SR of zero. This implies that, e.g., if only two years of daily backtest data is available no more than seven strategy variations should be tried, and if only five years of daily backtest data is available, no more than 45 strategy variations should be tried. See references for implementation details.

De Lopez Prado and Bailey (2014) also derive a deflated SR to compute the probability that the SR is statistically significant while controlling for the inflationary effect of multiple testing, non-normal returns, and shorter sample lengths (see the 03_multiple_testing subdirectory for the Python implementation of deflated_sharpe_ratio.py and references for the derivation of the related formulas). '''

#########################################################
The efficient frontier in Python
We can calculate an efficient frontier using scipy.optimize.minimize and the historical estimates for asset returns, standard deviations, and the covariance matrix. The code can be found in the efficient_frontier subfolder of the repo for this chapter and implements the following sequence of steps:

The simulation generates random weights using the Dirichlet distribution, and computes the mean, standard deviation, and SR for each sample portfolio using the historical return data:
def simulate_portfolios(mean_ret, cov, rf_rate=rf_rate, short=True):
    alpha = np.full(shape=n_assets, fill_value=.01)
    weights = dirichlet(alpha=alpha, size=NUM_PF)
    weights *= choice([-1, 1], size=weights.shape)

    returns = weights @ mean_ret.values + 1
    returns = returns ** periods_per_year - 1
    std = (weights @ monthly_returns.T).std(1)
    std *= np.sqrt(periods_per_year)
    sharpe = (returns - rf_rate) / std

    return pd.DataFrame({'Annualized Standard Deviation': std,
                         'Annualized Returns': returns,
                         'Sharpe Ratio': sharpe}), weights
Set up the quadratic optimization problem to solve for the minimum standard deviation for a given return or the maximum SR. To this end, define the functions that measure the key metrics:
def portfolio_std(wt, rt=None, cov=None):
    """Annualized PF standard deviation"""
    return np.sqrt(wt @ cov @ wt * periods_per_year)

def portfolio_returns(wt, rt=None, cov=None):
    """Annualized PF returns"""
    return (wt @ rt + 1) ** periods_per_year - 1

def portfolio_performance(wt, rt, cov):
    """Annualized PF returns & standard deviation"""
    r = portfolio_returns(wt, rt=rt)
    sd = portfolio_std(wt, cov=cov)
    return r, sd 
'''Define a target function that represents the negative SR for scipy's minimize function to optimize given the constraints that the weights are bounded by, [-1, 1], and sum to one in absolute terms:'''
def neg_sharpe_ratio(weights, mean_ret, cov):
    r, sd = portfolio_performance(weights, mean_ret, cov)
    return -(r - rf_rate) / sd

weight_constraint = {'type': 'eq',
                     'fun': lambda x: np.sum(np.abs(x)) - 1}

def max_sharpe_ratio(mean_ret, cov, short=True):
    return minimize(fun=neg_sharpe_ratio,
                    x0=x0,
                    args=(mean_ret, cov),
                    method='SLSQP',
                    bounds=((-1 if short else 0, 1),) * n_assets,
                    constraints=weight_constraint,
                    options={'tol':1e-10, 'maxiter':1e4})
'''Compute the efficient frontier by iterating over a range of target returns and solving for the corresponding minimum variance portfolios. The optimization problem and the constraints on portfolio risk and return as a function of the weights can be formulated as follows: '''
def neg_sharpe_ratio(weights, mean_ret, cov):
    r, sd = pf_performance(weights, mean_ret, cov)
    return -(r - RF_RATE) / sd

def pf_volatility(w, r, c):
    return pf_performance(w, r, c)[1]

def efficient_return(mean_ret, cov, target):
    args = (mean_ret, cov)
    def ret_(weights):
        return pf_ret(weights, mean_ret)
    
constraints = [{'type': 'eq', 'fun': lambda x: ret_(x) - 
                     target},
                   {'type': 'eq', 'fun': lambda x: np.sum(x) - 1}]
    bounds = ((0.0, 1.0),) * n_assets
    return minimize(pf_volatility,
                    x0=x0,
                    args=args, method='SLSQP',
                    bounds=bounds,
                    constraints=constraints)
'''The solution requires iterating over ranges of acceptable values to identify optimal risk-return combinations:'''
def min_vol_target(mean_ret, cov, target, short=True):

    def ret_(wt):
        return portfolio_returns(wt, mean_ret)

    constraints = [{'type': 'eq', 'fun': lambda x: ret_(x) - target},
                     weight_constraint]

    bounds = ((-1 if short else 0, 1),) * n_assets
    return minimize(portfolio_std, x0=x0, args=(mean_ret, cov),
                    method='SLSQP', bounds=bounds,
                    constraints=constraints,
                    options={'tol': 1e-10, 'maxiter': 1e4})

def efficient_frontier(mean_ret, cov, ret_range):
    return [min_vol_target(mean_ret, cov, ret) for ret in ret_range]
'''The simulation yields a subset of the feasible portfolios, and the efficient frontier identifies the optimal in-sample return-risk combinations that were achievable given historic data. The below figure shows the result including the minimum variance portfolio and the portfolio that maximizes the SR and several portfolios produce by alternative optimization strategies that we discuss in the following sections.'''

######################################################################
'''How to size your bets – the Kelly rule
The Kelly rule has a long history in gambling because it provides guidance on how much to stake on each of an (infinite) sequence of bets with varying (but favorable) odds to maximize terminal wealth. It was published as A New Interpretation of the Information Rate in 1956 by John Kelly who was a colleague of Claude Shannon's at Bell Labs. He was intrigued by bets placed on candidates at the new quiz show The $64,000 Question, where a viewer on the west coast used the three-hour delay to obtain insider information about the winners. 

Kelly drew a connection to Shannon's information theory to solve for the bet that is optimal for long-term capital growth when the odds are favorable, but uncertainty remains. His rule maximizes logarithmic wealth as a function of the odds of success of each game, and includes implicit bankruptcy protection since log(0) is negative infinity so that a Kelly gambler would naturally avoid losing everything.
'''

'''The optimal size of a bet
Kelly began by analyzing games with a binary win-lose outcome. The key variables are:

b: The odds define the amount won for a $1 bet. Odds = 5/1 implies a $5 gain if the bet wins, plus recovery of the $1 capital.
p: The probability defines the likelihood of a favorable outcome.
f: The share of the current capital to bet.
V: The value of the capital as a result of betting.
The Kelly rule aims to maximize the value's growth rate, G, of infinitely-repeated bets:'''
'''When W and L are the numbers of wins and losses, then:
We can maximize the rate of growth G by maximizing G with respect to f, as illustrated using sympy as follows: 
'''
from sympy import diff, log, solve, symbols

share, odds, probability = symbols('share odds probability')
Value = probability * log(1 + odds * share) + (1 - probability) * log(1 
        - share)
solve(diff(Value, share), share)

[(odds*probability + probability - 1)/odds]
'''We arrive at the optimal share of capital to bet:'''
########################################################################
'''Basic train-test split
For a single split of your data into a training and a test set, use sklearn.model_selection.train_test_split, where the shuffle parameter, by default ensures the randomized selection of observations, which in turn can be replicated by setting random_state. There is also a stratify parameter that, for a classification problem, ensures that the train and test sets will contain approximately the same shares of each class, as shown in the following code:'''

train_test_split(data, train_size=.8)
[[8, 7, 4, 10, 1, 3, 5, 2], [6, 9]]
'''In this case, we train a model using all data except row numbers 6 and 9, which will be used to generate predictions and measure the errors given on the know labels. This method is useful for quick evaluation but is sensitive to the split, and the standard error of the test error estimate will be higher.'''

#########################################################################

'''SMB Small minus big
Nine small stock PF minus nine large stock PF
HML
High minus low
Two value PF minus two growth (with low BE/ME value) PF'''

#########################################################################
'''How to decompose time series patterns
Time series data typically contains a mix of various patterns that can be decomposed into several components, each representing an underlying pattern category. In particular, time series often consist of the systematic components trend, seasonality and cycles, and unsystematic noise. These components can be combined in an additive, linear model, in particular when fluctuations do not depend on the level of the series, or in a non-linear, multiplicative model. 

These components can be split up automatically. statsmodels includes a simple method to split the time series into a trend, seasonal, and residual component using moving averages. We can apply it to monthly data on industrial manufacturing production with both a strong trend and seasonality component, as follows:'''

import statsmodels.tsa.api as tsa

industrial_production = web.DataReader('IPGMFN', 'fred', '1988', '2017-12').squeeze()
components = tsa.seasonal_decompose(industrial_production, model='additive')
ts = (industrial_production.to_frame('Original')
      .assign(Trend=components.trend)
      .assign(Seasonality=components.seasonal)
      .assign(Residual=components.resid))
ts.plot(subplots=True, figsize=(14, 8));
'''The resulting charts show the additive components. The residual component would be the focus of additional modeling, assuming that the trend and seasonality components are more deterministic and amenable to simple extrapolation:
'''

####################################################################################
'''we can estimate a GARCH model to capture the linear relationship of past volatilities. We will use rolling 10-year windows to estimate a GARCH(p, q) model with p and q ranging from 1-4 to generate 1-step out-of-sample forecasts. We then compare the RMSE of the predicted volatility relative to the actual squared deviation of the return from its mean to identify the most predictive model. We are using winsorized data to limit the impact of extreme return values reflected in the very high positive skew of the volatility:
'''
trainsize = 10 * 252  # 10 years
data = nasdaq_returns.clip(lower=nasdaq_returns.quantile(.05),
                           upper=nasdaq_returns.quantile(.95))
T = len(nasdaq_returns)
test_results = {}
for p in range(1, 5):
    for q in range(1, 5):
        print(f'{p} | {q}')
        result = []
        for s, t in enumerate(range(trainsize, T-1)):
            train_set = data.iloc[s: t]
            test_set = data.iloc[t+1]  # 1-step ahead forecast
            model = arch_model(y=train_set, p=p, q=q).fit(disp='off')
            forecast = model.forecast(horizon=1)
            mu = forecast.mean.iloc[-1, 0]
            var = forecast.variance.iloc[-1, 0]
            result.append([(test_set-mu)**2, var])
        df = pd.DataFrame(result, columns=['y_true', 'y_pred'])
        test_results[(p, q)] = np.sqrt(mean_squared_error(df.y_true, df.y_pred))
The GARCH(2, 2) model achieves the lowest RMSE (same value as GARCH(4, 2) but with fewer parameters), so we go ahead and estimate this model to inspect the summary:

am = ConstantMean(nasdaq_returns.clip(lower=nasdaq_returns.quantile(.05),
                                      upper=nasdaq_returns.quantile(.95)))
am.volatility = GARCH(2, 0, 2)
am.distribution = Normal()
model = am.fit(update_freq=5)
print(model.summary())
'''The output shows the maximized log-likelihood as well as the AIC and BIC criteria that are commonly minimized when selecting models based on in-sample performance (see Chapter 7, Linear Models). It also displays the result for the mean model, which in this case is just a constant estimate, as well as the GARCH parameters for the constant omega, the AR parameters, α, and the MA parameters, β, all of which are statistically significant:'''

############################################################################
'''The statsmodels library implements both the Engle-Granger cointegration test and the Johansen test.

In order to estimate the spread, run a linear regression to get the coefficient for the linear combination of two integrated asset price series that produce a stationary combined series. As mentioned, using linear regression to estimate the coefficient is known as the Engle-Granger test of cointegration.'''

############################################################################
'''How to train a classification tree
We will now train, visualize, and evaluate a classification tree with up to 5 consecutive splits using 80% of the samples for training to predict the remaining 20%. We are taking a shortcut here to simplify the illustration and use the built-in train_test_split, which does not protect against lookahead bias, as our custom iterator. The tree configuration implies up to 25=32 leaf nodes that, on average in the balanced case, would contain over 4,300 of the training samples. Take a look at the following code:'''

# randomize train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y_binary, test_size=0.2, random_state=42)

# configure & train tree learner
classifier = DecisionTreeClassifier(criterion='gini',
                                    max_depth=5,
                                    random_state=42)
classifier.fit(X=X_train, y=y_train)

# Output:
DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=5,
            max_features=None, max_leaf_nodes=None,
            min_impurity_decrease=0.0, min_impurity_split=None,
            min_samples_leaf=1, min_samples_split=2,
            min_weight_fraction_leaf=0.0, presort=False, random_state=42,
            splitter='best')
'''The output after training the model displays all the DecisionTreeClassifier parameters that we will address in more detail in the next section when we discuss parameter-tuning. '''

PCA is sensitive to outliers, so we winsorize the data at the 2.5% and 97.5% quantiles:

returns = returns.clip(lower=returns.quantile(q=.025),
upper=returns.quantile(q=.975),
axis=1)
PCA does not permit missing data, so we will remove stocks that do not have data for at least 95% of the time period, and in a second step, remove trading days that do not have observations on at least 95% of the remaining stocks:

returns = returns.dropna(thresh=int(returns.shape[0] * .95), axis=1)
returns = returns.dropna(thresh=int(returns.shape[1] * .95))
We are left with 314 equity return series covering a similar period:

returns.info()
DatetimeIndex: 2070 entries, 2010-01-05 to 2018-03-27
Columns: 314 entries, A to ZBH
We impute any remaining missing values using the average return for any given trading day:

daily_avg = returns.mean(1)
returns = returns.apply(lambda x: x.fillna(daily_avg))
Now we are ready to fit the principal components model to the asset returns using default parameters to compute all components using the full SVD algorithm:

pca = PCA()
pca.fit(returns)
PCA(copy=True, iterated_power='auto', n_components=None, random_state=None,
svd_solver='auto', tol=0.0, whiten=False)


##################################################################################
'''Working with Text Data
This is the first of three chapters dedicated to extracting signals for algorithmic trading strategies from text data using natural language processing (NLP) and machine learning (ML).

Text data is very rich in content, yet unstructured in format, and hence requires more preprocessing so that an ML algorithm can extract the potential signal. The key challenge lies in converting text into a numerical format for use by an algorithm, while simultaneously expressing the semantics or meaning of the content. We will cover several techniques that capture nuances of language that are readily understandable to humans so that they can become an input for ML algorithms.

In this chapter, we introduce fundamental feature extraction techniques that focus on individual semantic units; that is, words or short groups of words called tokens. We will show how to represent documents as vectors of token counts by creating a document-term matrix that, in turn, serves as input for text classification and sentiment analysis. We will also introduce the Naive Bayes algorithm, which is popular for this purpose.

In the following two chapters, we build on these techniques and use ML algorithms such as topic modeling and word-vector embedding to capture information contained in a broader context.

In particular, in this chapter, we will cover the following:

What the fundamental NLP workflow looks like
How to build a multilingual feature extraction pipeline using spaCy and TextBlob
How to perform NLP tasks such as part-of-speech (POS) tagging or named entity recognition
How to convert tokens to numbers using the document-term matrix
How to classify text using the Naive Bayes model
How to perform sentiment analysis'''

'''How to extract features from text data
Text data can be extremely valuable given how much information humans communicate and store using natural language—the diverse set of data sources relevant to investment range from formal documents such as company statements, contracts, and patents, to news, opinion, and analyst research, and even to commentary and various types of social media posts and messages.

Numerous and diverse text data samples are available online to explore the use of NLP algorithms, many of which are listed among the references for this chapter.

To guide our journey through the techniques and Python libraries that most effectively support the realization of this goal, we will highlight NLP challenges, introduce critical elements of the NLP workflow, and illustrate applications of ML from text data to algorithmic trading.'''

'''Parsing and tokenizing text data
A token is an instance of a characters that appears in a given document and should be considered a semantic unit for further processing. The vocabulary is a set of tokens contained in a corpus deemed relevant for further processing. A key trade-off in the following decisions is the accurate reflection of the text source at the expense of a larger vocabulary that may translate into more features and higher model complexity.

Basic choices in this regard concern the treatment of punctuation and capitalization, the use of spelling correction, and whether to exclude very frequent so-called stop words (such as and or the) as meaningless noise.

An additional decision is about the inclusion of groups of n individual tokens called n-grams as semantic units (an individual token is also called a unigram). An example of a 2-gram (or bi-gram) is New York, whereas New York City is a 3-gram (or tri-gram).

The goal is to create tokens that more accurately reflect the document's meaning. The decision can rely on dictionaries or a comparison of the relative frequencies of the individual and joint usage. Including n-grams will increase the number of features because the number of unique n-grams tends to be much higher than the number of unique unigrams and will likely add noise unless filtered for significance by frequency.'''

'''Linguistic annotation
Linguistic annotations include the application of syntactic and grammatical rules to identify the boundary of a sentence despite ambiguous punctuation, and a token's role in a sentence for POS tagging and dependency parsing. It also permits the identification of common root forms for stemming and lemmatization to group related words:

POS annotations: It helps disambiguate tokens based on their function (this may be necessary when a verb and noun have the same form), which increases the vocabulary but may result in better accuracy.
Dependency parsing: It identifies hierarchical relationships among tokens, is commonly used for translation, and is important for interactive applications that require more advanced language understanding, such as chatbots.
Stemming: It uses simple rules to remove common endings, such as s, ly, ing, and ed, from a token and reduce it to its stem or root form.
Lemmatization: It uses more sophisticated rules to derive the canonical root (lemma) of a word. It can detect irregular roots, such as better and best, and more effectively condenses vocabulary, but is slower than stemming. Both approaches simplify vocabulary at the expense of semantic nuances.'''

'''Semantic annotation
Named entity recognition (NER) aims to identify tokens that represent objects of interest, such as people, countries, or companies. It can be further developed into a knowledge graph that captures semantic and hierarchical relationships among such entities. It is a critical ingredient for applications that, for example, aim to predict the impact of news events or sentiment.'''

'''Labeling
Many NLP applications learn to predict outcomes from meaningful information extracted from text. Supervised learning requires labels to teach the algorithm the true input-output relationship. With text data, establishing this relationship may be challenging and may require explicit data modeling and collection.

Data modeling decisions include how to quantify sentiments implicit in a text document like an email, a transcribed interview, or a tweet, or which aspects of a research document or news report to assign to a specific outcome.'''

'''Use cases
The use of ML with text data for algorithmic trading relies on the extraction of meaningful information in the form of features that directly or indirectly predict future price movements. Applications range from the exploitation of the short-term market impact of news to the long-term fundamental analysis of the drivers of asset valuation. Examples include the following:

The evaluation of product review sentiment to assess a company's competitive position or industry trends
The detection of anomalies in credit contracts to predict the probability or impact of a default
 The prediction of news impact in terms of direction, magnitude, and affected entities
JP Morgan, for instance, developed a predictive model based on 250,000 analyst reports that outperformed several benchmark indices and produced uncorrelated signals relative to sentiment factors formed from consensus EPS and recommendation changes.'''

'''From text to tokens – the NLP pipeline
In this section, we will demonstrate how to construct an NLP pipeline using the open source Python library, spaCy. The textacy library builds on spaCy and provides easy access to spaCy attributes and additional functionality.

Refer to the nlp_pipeline_with_spaCy notebook for the following code samples, installation instructions, and additional details.'''

'''NLP pipeline with spaCy and textacy
spaCy is a widely used Python library with a comprehensive feature set for fast text processing in multiple languages. The usage of tokenization and annotation engines requires the installation of language models. The features we will use in this chapter only require small models; larger models also include word vectors that we will cover in Chapter 15, Word Embeddings.

Once installed and linked, we can instantiate a spaCy language model and then call it on a document. As a result, spaCy produces a doc object that tokenizes the text and processes it according to configurable pipeline components that, by default, consist of a tagger, a parser, and a named-entity recognizer:
'''

nlp = spacy.load('en')
nlp.pipe_names
['tagger', 'parser', 'ner']
Let's illustrate the pipeline using a simple sentence:

sample_text = 'Apple is looking at buying U.K. startup for $1 billion'
doc = nlp(sample_text)

'''Parsing, tokenizing, and annotating a sentence
Parsed document content is iterable, and each element has numerous attributes produced by the processing pipeline. The following sample illustrates how to access the following attributes:

.text: Original word text
.lemma_: Word root
.pos_: Basic POS tag
.tag_: Detailed POS tag
.dep_: Syntactic relationship or dependency between tokens
.shape_: The shape of the word regarding capitalization, punctuation, or digits
.is alpha: Check whether the token is alphanumeric
 .is stop: Check whether the token is on a list of common words for the given language
We iterate over each token and assign its attributes to a pd.DataFrame:'''

pd.DataFrame([[t.text, t.lemma_, t.pos_, t.tag_, t.dep_, t.shape_, t.is_alpha, t.is_stop] for t in doc],
             columns=['text', 'lemma', 'pos', 'tag', 'dep', 'shape', 'is_alpha', 'is_stop'])
'''Which produces the following output:'''

We can visualize syntactic dependency in a browser or notebook using the following:

displacy.render(doc, style='dep', options=options, jupyter=True)
The result is a dependency tree:

We can get additional insights into the meaning of attributes using spacy.explain(), as here:

spacy.explain("VBZ")
verb, 3rd person singular present

Batch-processing documents
We will now read a larger set of 2,225 BBC News articles (see GitHub for data source details) that belong to five categories and are stored in individual text files. We need to do the following:

Call the .glob() method of pathlib's Path object.
Iterate over the resulting list of paths.
Read all lines of the news article excluding the heading in the first line.
Append the cleaned result to a list:
files = Path('..', 'data', 'bbc').glob('**/*.txt')
bbc_articles = []
for i, file in enumerate(files):
    _, _, _, topic, file_name = file.parts
    with file.open(encoding='latin1') as f:
        lines = f.readlines()
        body = ' '.join([l.strip() for l in lines[1:]]).strip()
        bbc_articles.append(body)
len(bbc_articles)
2225

entence boundary detection
We will illustrate sentence detection by calling the NLP object on the first of the articles:

doc = nlp(bbc_articles[0])
type(doc)
spacy.tokens.doc.Doc
spaCy computes sentence boundaries from the syntactic parse tree so that punctuation and capitalization play an important but not decisive role. As a result, boundaries will coincide with clause boundaries, even for poorly punctuated text.

We can access parsed sentences using the .sents attribute:

sentences = [s for s in doc.sents]
sentences[:3]
[Voting is under way for the annual Bloggies which recognize the best web blogs - online spaces where people publish their thoughts - of the year. ,
Nominations were announced on Sunday, but traffic to the official site was so heavy that the website was temporarily closed because of too many visitors.,
Weblogs have been nominated in 30 categories, from the top regional blog, to the best-kept-secret blog.]

Named entity recognition
spaCy enables named entity recognition using the .ent_type_ attribute:

for t in sentences[0]:
    if t.ent_type_:
        print('{} | {} | {}'.format(t.text, t.ent_type_, spacy.explain(t.ent_type_)))
annual | DATE | Absolute or relative dates or periods
the | DATE | Absolute or relative dates or periods
year | DATE | Absolute or relative dates or periods
textacy facilitates access to the named entities that appear in the first article:

from textacy.extract import named_entities
entities = [e.text for e in named_entities(doc)]
pd.Series(entities).value_counts()
year                          4
US                            2
South-East Asia Earthquake    2
annual                        2
Tsunami Blog                  2

N-grams
N-grams combine N consecutive tokens. N-grams can be useful for the BoW model because, depending on the textual context, treating something such as data scientist as a single token may be more meaningful than treating it as two distinct tokens: data and scientist.

textacy makes it easy to view the ngrams of a given length n occurring with at least min_freq times:

from textacy.extract import ngrams
pd.Series([n.text for n in ngrams(doc, n=2, min_freq=2)]).value_counts()
East Asia          2
Asia Earthquake    2
Tsunami Blog       2
annual Bloggies    2

spaCy's streaming API
To pass a larger number of documents through the processing pipeline, we can use spaCy's streaming API as follows:

iter_texts = (bbc_articles[i] for i in range(len(bbc_articles)))
for i, doc in enumerate(nlp.pipe(iter_texts, batch_size=50, n_threads=8)):
      assert doc.is_parsed

Multi-language NLP
spaCy includes trained language models for English, German, Spanish, Portuguese, French, Italian, and Dutch, as well as a multi-language model for NER. Cross-language usage is straightforward since the API does not change.

We will illustrate the Spanish language model using a parallel corpus of TED Talk subtitles (see the GitHub repo for data source references). For this purpose, we instantiate both language models:

model = {}
for language in ['en', 'es']:
    model[language] = spacy.load(language)
We then read small corresponding text samples in each model:

text = {}
path = Path('../data/TED')
for language in ['en', 'es']:
    file_name = path / 'TED2013_sample.{}'.format(language)
    text[language] = file_name.read_text()
Sentence boundary detection uses the same logic but finds a different breakdown:

parsed, sentences = {}, {}
for language in ['en', 'es']:
    parsed[language] = model[language](text[language])
    sentences[language] = list(parsed[language].sents)
print('Sentences:', language, len(sentences[language]))
Sentences: en 19
Sentences: es 22
POS tagging also works in the same way:

pos = {}
for language in ['en', 'es']:
    pos[language] = pd.DataFrame([[t.text, t.pos_, spacy.explain(t.pos_)] for t in sentences[language][0]],
    columns=['Token', 'POS Tag', 'Meaning'])
pd.concat([pos['en'], pos['es']], axis=1).head()
The result is the side-by-side token annotations for the English and Spanish documents:
     

NLP with TextBlob
TextBlob is a Python library that provides a simple API for common NLP tasks and builds on the Natural Language Toolkit (NLTK) and the Pattern web mining libraries. TextBlob facilitates POS tagging, noun phrase extraction, sentiment analysis, classification, translation, and more.

To illustrate the use of TextBlob, we sample a BBC sports article with the headline Robinson ready for difficult task. Similarly to spaCy and other libraries, the first step is to pass the document through a pipeline represented by the TextBlob object to assign annotations required for various tasks (see the nlp_with_textblob notebook for this section):

from textblob import TextBlob
article = docs.sample(1).squeeze()
parsed_body = TextBlob(article.body)

Stemming
To perform stemming, we instantiate SnowballStemmer from the nltk library, call its .stem() method on each token and display modified tokens:

from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer('english')
[(word, stemmer.stem(word)) for i, word in enumerate(parsed_body.words)
    if word.lower() != stemmer.stem(parsed_body.words[i])]
[('Andy', 'andi'),
('faces', 'face'),
('tenure', 'tenur'),
('tries', 'tri'),
('winning', 'win'),

Sentiment polarity and subjectivity
TextBlob provides polarity and subjectivity estimates for parsed documents using dictionaries provided by the Pattern library. These dictionaries map adjectives frequently found in product reviews to sentiment polarity scores, ranging from -1 to +1 (negative ↔ positive) and a similar subjectivity score (objective ↔ subjective).

The .sentiment attribute provides the average for each over the relevant tokens, whereas the .sentiment_assessments attribute lists the underlying values for each token (see notebook):

parsed_body.sentiment
Sentiment(polarity=0.088031914893617, subjectivity=0.46456433637284694)

From tokens to numbers – the document-term matrix
In this section, we first introduce how the BoW model converts text data into a numeric vector space representation that permits the comparison of documents using their distance. We then proceed to illustrate how to create a document-term matrix using the sklearn library.

The BoW model
The BoW model represents a document based on the frequency of the terms or tokens it contains. Each document becomes a vector with one entry for each token in the vocabulary that reflects the token's relevance to the document.

The document-term matrix is straightforward to compute given the vocabulary. However, it is also a crude simplification because it abstracts from word order and grammatical relationships. Nonetheless, it often achieves good results in text classification quickly and, thus, is a very useful starting point.

The following diagram (the one on the right) illustrates how this document model converts text data into a matrix with numerical entries, where each row corresponds to a document and each column to a token in the vocabulary. The resulting matrix is usually both very high-dimensional and sparse; that is, one that contains many zero entries because most documents only contain a small fraction of the overall vocabulary:

There are several ways to weigh a token's vector entry to capture its relevance to the document. We will illustrate how to use sklearn to use binary flags, which indicate presence or absence, counts, and weighted counts that account for differences in term frequencies across all documents; that is, in the corpus.

Document-term matrix with sklearn
The scikit-learn preprocessing module offers two tools to create a document-term matrix. CountVectorizer uses binary or absolute counts to measure the term frequency tf(d, t) for each document d and token t.

TfidFVectorizer, in contrast, weighs the (absolute) term frequency by the inverse document frequency (idf). As a result, a term that appears in more documents will receive a lower weight than a token with the same frequency for a given document but lower frequency across all documents. More specifically, using the default settings, tf-idf(d, t) entries for the document-term matrix are computed as tf-idf(d, t) = tf(d, t) x idf(t):



Here nd is the number of documents and df(d, t) the document frequency of term t. The resulting tf-idf vectors for each document are normalized with respect to their absolute or squared totals (see the sklearn documentation for details). The tf-idf measure was originally used in information retrieval to rank search engine results and has subsequently proven useful for text classification or clustering.

Both tools use the same interface and perform tokenization and further optional preprocessing of a list of documents before vectorizing the text by generating token counts to populate the document-term matrix.

Key parameters that affect the size of the vocabulary include the following:

stop_words: Use a built-in or provide a list of (frequent) words to exclude
ngram_range: Include n-grams in a range for n defined by a tuple of (nmin, nmax)
lowercase: Convert characters accordingly (default is True)
min_df / max_df: Ignore words that appear in less / more (int) or a smaller/larger share of documents (if float [0.0,1.0])
max_features: Limit the number of tokens in a vocabulary accordingly
binary: Set non-zero counts to 1 True
See the document_term_matrix notebook for the following code samples and additional details. We are again using the 2,225 BBC News articles for illustration.

Using CountVectorizer
The notebook contains an interactive visualization that explores the impact of the min_df and max_df settings on the size of the vocabulary. We read the articles into a DataFrame, set the CountVectorizer to produce binary flags and use all tokens, and call its .fit_transform() method to produce a document-term matrix:

binary_vectorizer = CountVectorizer(max_df=1.0,
                                    min_df=1,
                                    binary=True)

binary_dtm = binary_vectorizer.fit_transform(docs.body)
<2225x29275 sparse matrix of type '<class 'numpy.int64'>'
   with 445870 stored elements in Compressed Sparse Row format>
The output is a scipy.sparse matrix in row format that efficiently stores of the small share (<0.7%) of 445870 non-zero entries in the 2225 (document) rows and 29275 (token) columns.

Finding the most similar documents
The CountVectorizer result lets us find the most similar documents using the pdist() function for pairwise distances provided by the scipy.spatial.distance module. It returns a condensed distance matrix with entries corresponding to the upper triangle of a square matrix. We use np.triu_indices() to translate the index that minimizes the distance to the row and column indices that in turn correspond to the closest token vectors:

m = binary_dtm.todense() # pdist does not accept sparse format
pairwise_distances = pdist(m, metric='cosine')
closest = np.argmin(pairwise_distances) # index that minimizes distance
rows, cols = np.triu_indices(n_docs) # get row-col indices
rows[closest], cols[closest]
(11, 75)
Articles number 11 and 75 are closest by cosine similarity because they share 58 tokens (see notebook):

Software that can not only monitor every keystroke and action performed at a PC but can also be used as legally binding evidence of wrong-doing has been unveiled. Worries about cyber-crime and sabotage have prompted many employers to consider monitoring employees.

BT is introducing two initiatives to help beat rogue dialer scams, which can cost dial-up net users thousands. From May, dial-up net users will be able to download free software to stop computers using numbers not on a user's pre-approved list.

 

Both CountVectorizer and TfidFVectorizer can be used with spaCy; for example, to perform lemmatization and exclude certain characters during tokenization, we use the following:

nlp = spacy.load('en')
def tokenizer(doc):
    return [w.lemma_ for w in nlp(doc) 
                if not w.is_punct | w.is_space]
vectorizer = CountVectorizer(tokenizer=tokenizer, binary=True)
doc_term_matrix = vectorizer.fit_transform(docs.body)
See the notebook for additional details and more examples.

opic modeling for earnings calls
In Chapter 3, Alternative Data for Finance, we learned how to scrape earnings call data from the SeekingAlpha site. In this section, we will illustrate topic modeling using this source. I'm using a sample of some 500 earnings call transcripts from the second half of 2018. For a practical application, a larger dataset would be highly desirable. The earnings_calls directory contains several files, with examples mentioned later.

See the lda_earnings_calls notebook for details on loading, exploring, and preprocessing the data, as well as training and evaluating individual models, and the run_experiments.py file for the experiments described here.

Data preprocessing
The transcripts consist of individual statements by a company representative, an operator, and usually a question and answer session with analysts. We will treat each of these statements as separate documents, ignoring operator statements, to obtain 22,766 items with mean and median word counts of 144 and 64, respectively:

documents = []
for transcript in earnings_path.iterdir():
    content = pd.read_csv(transcript / 'content.csv')
    documents.extend(content.loc[(content.speaker!='Operator') & (content.content.str.len() > 5), 'content'].tolist())
len(documents)
22766
We use spaCy to preprocess these documents as illustrated in Chapter 13, Working with Text Data (see the notebook) and store the cleaned and lemmatized text as a new text file.

Data exploration reveals domain-specific stopwords such as year and quarter that we remove in a second step, where we also filter out statements with fewer than ten words so that some 16,150 remain.

Word Embeddings
In the two previous chapters, we applied the bag-of-words model to convert text data into a numerical format. The results were sparse, fixed-length vectors that represent documents in a high-dimensional word space. This allows evaluating the similarity of documents and creates features to train a machine learning algorithm and classify a document's content or rate the sentiment expressed in it. However, these vectors ignore the context in which a term is used so that, for example, a different sentence containing the same words would be encoded by the same vector.

In this chapter, we will introduce an alternative class of algorithms that use neural networks to learn a vector representation of individual semantic units such as a word or a paragraph. These vectors are dense rather than sparse, and have a few hundred real-valued rather than tens of thousands of binary or discrete entries. They are called embeddings because they assign each semantic unit a location in a continuous vector space.

Embeddings result from training a model to relate tokens to their context with the benefit that similar usage implies a similar vector. Moreover, we will see how the embeddings encode semantic aspects, such as relationships among words by means of their relative location. As a result, they are powerful features for use in the deep learning models that we will introduce in the following chapters.

More specifically, in this chapter, we will cover the following topics:

What word embeddings are and how they work and capture semantic information
How to use trained word vectors
Which network architectures are useful to train Word2vec models
How to train a Word2vec model using Keras, gensim, and TensorFlow
How to visualize and evaluate the quality of word vectors
How to train a Word2vec model using SEC filings
How Doc2vec extends Word2vec

How word embeddings encode semantics
The bag-of-words model represents documents as vectors that reflect the tokens they contain. Word embeddings represent tokens as lower dimensional vectors so that their relative location reflects their relationship in terms of how they are used in context. They embody the distributional hypothesis from linguistics that claims words are best defined by the company they keep.

Word vectors are capable of capturing numerous semantic aspects; not only are synonyms close to each other, but words can have multiple degrees of similarity, for example, the word driver could be similar to motorist or to cause. Furthermore, embeddings reflect relationships among pairs of words such as analogies (Tokyo is to Japan what Paris is to France, or went is to go what saw is to see) as we will illustrate later in this section.

Embeddings result from training a machine learning model to predict words from their context or vice versa. In the following section, we will introduce how these neural language models work and present successful approaches including Word2vec, Doc2vec, and fastText.

Word vectors from SEC filings using gensim
In this section, we will learn word and phrase vectors from annual US Securities and Exchange Commission (SEC) filings using gensim to illustrate the potential value of word embeddings for algorithmic trading. In the following sections, we will combine these vectors as features with price returns to train neural networks to predict equity prices from the content of security filings.

In particular, we use a dataset containing over 22,000 10-K annual reports from the period 2013-2016 that are filed by listed companies and contain both financial information and management commentary (see Chapter 3, Alternative Data for Finance). For about half of the 11-K filings for companies, we have stock prices to label the data for predictive modeling (see references about data sources and the notebooks in the sec-filings folder for details).

Sentiment analysis with Doc2vec
Text classification requires combining multiple word embeddings. A common approach is to average the embedding vectors for each word in the document. This uses information from all embeddings and effectively uses vector addition to arrive at a different location point in the embedding space. However, relevant information about the order of words is lost.

By contrast, the state-of-the-art generation of embeddings for pieces of text such as a paragraph or a product review is to use the document-embedding model Doc2vec. This model was developed by the Word2vec authors shortly after publishing their original contribution.

Similar to Word2vec, there are also two flavors of Doc2vec:

The distributed bag of words (DBOW) model corresponds to the Word2vec CBOW model. The document vectors result from training a network in the synthetic task of predicting a target word based on both the context word vectors and the document's doc vector.
The distributed memory (DM) model corresponds to the Word2vec Skip-Gram architecture. The doc vectors result from training a neural net to predict a target word using the full document's doc vector.
Gensim's Doc2vec class implements this algorithm.

Training Doc2vec on yelp sentiment data
We use a random sample of 500,000 Yelp (see Chapter 13, Working with Text Data) reviews with their associated star ratings (see notebook yelp_sentiment):

df = (pd.read_parquet('yelp_reviews.parquet', engine='fastparquet')
          .loc[:, ['stars', 'text']])
stars = range(1, 6)
sample = pd.concat([df[df.stars==s].sample(n=100000) for s in stars])
We apply use simple pre-processing to remove stopwords and punctuation using NLTK's tokenizer and drop reviews with fewer than 10 tokens:

import nltk
nltk.download('stopwords')
from nltk import RegexpTokenizer
from nltk.corpus import stopwords
tokenizer = RegexpTokenizer(r'\w+')
stopword_set = set(stopwords.words('english'))

def clean(review):
    tokens = tokenizer.tokenize(review)
    return ' '.join([t for t in tokens if t not in stopword_set])

sample.text = sample.text.str.lower().apply(clean)
sample = sample[sample.text.str.split().str.len()>10]

