import requests
import pandas as pd

def request_data(company_ticker, limit, type_of_statement ,apikey):
    """
    request financial statements from API

    Parameters
    ----------
    company_ticker : this is the abbreviation of the company that is listed on stock exchange
    limit : number of requests
    type_of_statement: which statement is needed (income statement, balance sheet, cash flow statement)
    apikey : key assigned to the user of this API
    
    Returns
    -------
    requests.models.Response
        
    Examples
    --------
    >>> resukt = request_data('AMZN',10,'income-statement','jkdahsgfjlhsygfiegfdilsa')
    >>> result
    <Response [200]>
    """
    if type_of_statement in ['income-statement', 'balance-sheet-statement', 'cash-flow-statement']: 
        base_url = 'https://financialmodelingprep.com/api/v3/'
        query_url = base_url+type_of_statement+'/'+company_ticker+'?apikey='+apikey+'&limit='+str(limit)
        return requests.get(query_url)
    else:
        print('The statements allowed are income-statement, balance-sheet-statement or cash-flow-statement')



def get_statement(raw_data):
    """
    transform result of request_data function into a pandas dataframe with easy undertand column names.

    Parameters
    ----------
    raw_data : json result from request_data()
    
    Returns
    -------
    pandas.core.frame.DataFrame
        
    Examples
    --------
    >>> resukt = request_data('AMZN',10,'income-statement','jkdahsgfjlhsygfiegfdilsa')
    >>> type(get_statement(result))
    pandas.core.frame.DataFrame
    """    
    if type(raw_data) == requests.models.Response:
        scope = range(len(raw_data.json()))
        statement = pd.DataFrame()
        for i in scope:
            d = pd.DataFrame(raw_data.json()[i],index = [i])
            d = d.drop(['fillingDate','acceptedDate','period','link','finalLink'],axis =1)
            statement = statement.append(d)
        if statement.columns[2] == "revenue":
            statement = statement.rename(columns = {'date' : 'Date', 'symbol':'Ticker', 'revenue' : 'Revenue', 'costOfRevenue' : 'Cost of Revenue', 'grossProfit' : 'Gross Profit',
           'grossProfitRatio':'Gross Profit Ratio', 'researchAndDevelopmentExpenses':'R&D Expenses',
           'generalAndAdministrativeExpenses':'General & Administraive Expenses', 'sellingAndMarketingExpenses':'Selling & Marketing Expenses',
            'otherExpenses':'Other Expenses', 'operatingExpenses':'Operating Expenses', 'costAndExpenses':'Cost & Expenses',
            'interestExpense' : 'Interest Expense', 'depreciationAndAmortization' : 'Depreciation & Amortization', 'ebitda' : 'EBIDTA',
           'ebitdaratio':'EBITDA Ratio', 'operatingIncome':'Operating Income/Loss', 'operatingIncomeRatio' : 'Operating Income/Loss Ratio',
           'totalOtherIncomeExpensesNet':'Total Other Income Expenses', 'incomeBeforeTax':'Income Before Tax',
           'incomeBeforeTaxRatio':'Income Before Tax Ratio', 'incomeTaxExpense':'Income Tax', 'netIncome':'Net Income',
           'netIncomeRatio':'Net Income Ratio', 'eps':'EPS', 'epsdiluted':'Diluted EPS', 'weightedAverageShsOut':'Weighted Average Shares Outstanding',
           'weightedAverageShsOutDil' : 'Diluted Weighted Average Shares Outstanding'})
        elif statement.columns[2] == 'cashAndCashEquivalents':
            statement = statement.rename(columns = {'date':'Date', 'symbol':'Ticker', 'cashAndCashEquivalents':'Cash & Cash Equivalents', 'shortTermInvestments':'Short Term Investments',
           'cashAndShortTermInvestments':'Cash and Shortterm Investment', 'netReceivables':'Account Receivables', 'inventory':'Inventory',
           'otherCurrentAssets':'Other Current Assets', 'totalCurrentAssets':'Total Current Assets', 'propertyPlantEquipmentNet':'PP&E',
           'goodwill':'Goodwill', 'intangibleAssets':'Intangible Assets', 'goodwillAndIntangibleAssets':'Goodwill & Intangible Assets',
           'longTermInvestments':'Long Term Investments', 'taxAssets':'Tax Assets', 'otherNonCurrentAssets':'Other Noncurrent Assets',
            'totalNonCurrentAssets':'Total Noncurrent Assets', 'otherAssets':'Other Assets', 'totalAssets':'Total Assets',
           'accountPayables':'Account Payables', 'shortTermDebt':'Short Term Debt', 'taxPayables':'Tax Payables', 'deferredRevenue':'Deferred Revenue',
           'otherCurrentLiabilities':'Other Current Liabilities', 'totalCurrentLiabilities':'Total Current Liabilities', 'longTermDebt':'Long Term Debt',
           'deferredRevenueNonCurrent':'Deferred Revenue Noncurrent', 'deferredTaxLiabilitiesNonCurrent':'Deferred Tax Liabilities Noncurrent',
           'otherNonCurrentLiabilities':'Other Non Current Liabilities', 'totalNonCurrentLiabilities':'Total Noncurrent Liabilities',
           'otherLiabilities':'Other Liabilities', 'totalLiabilities':'Total Liabilities', 'commonStock':'Common Stock',
           'retainedEarnings':'Retained Earnings', 'accumulatedOtherComprehensiveIncomeLoss':'Accumulated Other Comprehensive Income/Loss',
           'othertotalStockholdersEquity':'Other Total Stockholders Equity', 'totalStockholdersEquity':'Total Stockholders Equity',
           'totalLiabilitiesAndStockholdersEquity':'Total Liabilies and Stockholders Equity', 'totalInvestments':'Total Investments',
           'totalDebt':'Total Debt', 'netDebt':'Net Debt'})
        else:
            statement = statement.rename(columns = {'date':'Date', 'symbol':'Ticker', 'netIncome':'Net Income', 'depreciationAndAmortization':'Depreciation & Amortization',
           'deferredIncomeTax':'Deferred Income Tax', 'stockBasedCompensation':'Stock Based Compensation', 'changeInWorkingCapital':'Change in Working Captial',
           'accountsReceivables':'Account Receivables', 'inventory':'Inventory', 'accountsPayables':'Accounts Paybales',
           'otherWorkingCapital':'Other Working Captial', 'otherNonCashItems':'Other NonCash Items',
           'netCashProvidedByOperatingActivities':'Cash FLow from Operation',
           'investmentsInPropertyPlantAndEquipment':'PP&E Investmetn', 'acquisitionsNet':'Net Acquisition',
           'purchasesOfInvestments':'Purchase of Investment', 'salesMaturitiesOfInvestments':'Sales of Matuities',
           'otherInvestingActivites':'Other Investing Activities', 'netCashUsedForInvestingActivites':'Cash Flow from Investment',
           'debtRepayment':'Debt Repayment', 'commonStockIssued':'Common Stock Issued', 'commonStockRepurchased':'Common Stock Repurchased',
           'dividendsPaid':'Dividends Paid', 'otherFinancingActivites':'Other Financing Activities',
           'netCashUsedProvidedByFinancingActivities':'Cash Flow from Financing Activities',
           'effectOfForexChangesOnCash':'Effect of Foreign Currency Exchange', 'netChangeInCash':'Net Change in Cash', 'cashAtEndOfPeriod':'Cash at the end of Period',
           'cashAtBeginningOfPeriod':'Cash at Beginning of Period', 'operatingCashFlow':'Operating Cash Flow', 'capitalExpenditure':'Capital Expenditure',
           'freeCashFlow':'Free Cash Flow'})
        return statement
    # taking the potential input error into account. this function only process json data
    else:
        print('Raw_data type should be json')
        
        
        
def export(data,filename):
    """
    export the financial statement data to a csv file for potential valuation analysis in excel

    Parameters
    ----------
    data : pd.DataFrame of the financial statements
    filename : the filename user wants the file to be
    
    Returns
    -------
        
    Examples
    --------
    >>> resukt = request_data('AMZN',10,'income-statement','jkdahsgfjlhsygfiegfdilsa')
    >>> data = get_statement(result)
    >>> export(data,'income statement')
    """ 
    if isinstance(filename, str):
        data.transpose().to_csv(filename+'.csv')
    else: 
        print('filename needs to be a string')
        
        
        
def request_stock_price(company_ticker, limit ,apikey):
    """
    request stock price information of this company of user's choice from API

    Parameters
    ----------
    company_ticker : this is the abbreviation of the company that is listed on stock exchange
    limit : number of requests
    apikey :  assigned key of user for this API
    
    Returns
    -------
    requests.models.Response
        
    Examples
    --------
    >>> resukt = request_stock_price('AMZN',10,'jkdahsgfjlhsygfiegfdilsa')
    >>> type(result)
    requests.models.Response
    """ 
    base_url = 'https://financialmodelingprep.com/api/v3/quote'
    query_url = base_url+'/'+company_ticker+'?apikey='+apikey+'&limit='+str(limit)
    return requests.get(query_url)
   


def valuation(company_ticker,limit,apikey):
    """
    get essetial valuation ratios that is neceesary to conduct valuation analysis in form of panads data frame

    Parameters
    ----------
    company_ticker : this is the abbreviation of the company that is listed on stock exchange
    limit : number of requests
    apikey :  assigned key of user for this API
    
    Returns
    -------
    pandas.core.frame.DataFrame
    
    Examples
    --------
    >>> data = valuation('AMZN,10,'skahdfdahfiodshlfa')
    >>> type(data)
    pandas.core.frame.DataFrame
    """ 
    a_is = request_data(company_ticker,limit,'income-statement',apikey)
    a_is_d = get_statement(a_is)
    a_bs = request_data(company_ticker,limit,'balance-sheet-statement',apikey)
    a_bs_d = get_statement(a_bs)
    a_cf = request_data(company_ticker,limit,'cash-flow-statement',apikey)
    a_cf_d = get_statement(a_cf)
    q = request_stock_price(company_ticker,limit,apikey).json()
    d ={}
    d['Price'] = [q[0]['price']]
    d['Market Cap'] = [d['Price'][0] * a_is_d['Weighted Average Shares Outstanding'][0]]
    d['EV'] = [d['Market Cap'][0] + a_bs_d['Total Liabilities'][0] - a_bs_d['Cash & Cash Equivalents'][0]]
    d['Sales'] = [a_is_d['Revenue'][0]]
    d['EBIDTA'] = [a_is_d['EBIDTA'][0]]
    d['EBIT'] = [d['EBIDTA'][0] - a_cf_d['Depreciation & Amortization'][0]]
    d['Earnings'] = [a_is_d['Net Income'][0]]
    d['EV/Sales'] = [d['EV'][0]/d['Sales'][0]]
    d['EV/EBIDTA'] = [d['EV'][0]/d['EBIDTA'][0]]
    d['EV/EBIT'] = [d['EV'][0]/d['EBIT'][0]]
    d['P/E'] = [d['Price'][0]/a_is_d['EPS'][0]]
    return d
