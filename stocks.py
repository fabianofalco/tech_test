'''
General notes:
    1 - Use Python 3 to run
    2 - Amount in pennies
    3 - I am not sure about the formula for PE Ratio. I am not clear about the "Dividend". In the document it is stated like PE Ration = Market Price / Dividend

'''

import time
from enum import Enum

class CustomListException(Exception):
    def __init__(self, message):        
        super().__init__(message)


class EnumStockTypes(Enum):
    COMMON = 'Common'
    PREF = 'Preferred'


class EnumBuySellIndicator(Enum):
    BUY = 'Buy'
    SELL = 'Sell'


class Stock():
    __type = None
    __symbol = None
    __market_price = 0
    __last_dividend = 0
    __fixed_dividend = 0
    __par_value = 0

    def __init__(self, symbol, type, market_price, last_dividend, fixed_dividend, par_value):
        self.__symbol = symbol
        self.__type = type
        self.__market_price = market_price
        self.__last_dividend = last_dividend
        self.__fixed_dividend = fixed_dividend
        self.__par_value = par_value

    @property
    def symbol(self):
        return self.__symbol

    @property
    def type(self):
        return self.__type

    @property
    def market_price(self):
        return self.__market_price

    @property
    def last_dividend(self):
        return self.__last_dividend

    @property
    def fixed_dividend(self):
        return self.__fixed_dividend

    @property
    def par_value(self):
        return self.__par_value


class Trade():
    __stock = None
    __time = None
    __quantity = 0
    __indicator = None
    __price = 0.0

    def __init__(self, stock, time, quantity, indicator, price):
        self.__stock = stock
        self.__time = time
        self.__quantity = quantity
        self.__indicator = indicator
        self.__price = price

    @property
    def stock(self):
        return self.__stock

    @property
    def time(self):
        return self.__time

    @property
    def quantity(self):
        return self.__quantity

    @property
    def indicator(self):
        return self.__indicator

    @property
    def price(self):
        return self.__price

    def return_print(self):
        return 'Stock Symbol: ' + self.stock.symbol + ' - Time: ' + str(self.time) + ' - Quantity: ' + str(self.quantity) + ' - Indicator: ' + self.indicator + ' - Price: ' + str(self.price)

    def print_trade(self):                
        print (self.return_print())



class Calculator():
    def calculate_dividend_yield(self, stock):
        '''
        Returns the dividend yield for a specific type of stock.
        In case of division by zero, returns zero.
        It returns the error description in case of other exceptions.

        For Common stocks: last_dividend / market_price
        For Preferred stocks: fixed_dividend * par_value / market_price

        Used ternary operator: (a) if condition else (b)
        where (a) = formula for Common stocks
              (b) = formula for Preferred stocks

        '''
        try:
            return stock.last_dividend / stock.market_price if stock.type == EnumStockTypes.COMMON else stock.fixed_dividend * stock.par_value / stock.par_value
        except ZeroDivisionError as e:
            return 0
        except Exception as e:
            return 'Error: ' + str(e)



    def calculate_pe_ratio(self, stock):
        '''
        Returns the PE Ration for a given stock. It is independent of the stock type.
        In case of division by zero, returns zero.
        It returns the error description in case of other exceptions.

        Formula: market_price / dividend
        
        '''

        try:
            return stock.market_price / self.calculate_dividend_yield(stock)
        except ZeroDivisionError as e:
            return 0
        except Exception as e:
            return 'Error: ' + str(e)

    

    def calculate_volume_weighted_stock_price(self, list_of_trades, now=time.time()):
        '''
        Returns the Volume Weighted Stock Price for a given list of trades and time.
        If no time is provided, then it assumes now().
        In case of division by zero and empty list, it returns zero.
        It returns the error description in case of other exceptions.
        

        Formula: Sum(trade price * quantity) / sum(quantity)
        
        '''

        try:
            #if list is not provided or is empty it raises a custom exception
            if (list_of_trades is None or len(list_of_trades) == 0):
                raise CustomListException('No list provided')

            #stores the sum of all stock prices for that specific period
            sum_trade_price_times_quantity = 0
            
            #stores the sum of all stock prices for that specific period
            count_quantity = 0
            
            #period of time to consider the stocks. Last X minutes.
            minutes = 15

            #convert the period to be considered above to seconds
            seconds = minutes * 60

            #for each trade in the list, it checks if it was registered in the last X minutes.
            #if yes, it is then sum and counted accordingly
            for trade in list_of_trades:
                time_difference_in_seconds = (now - trade.time).seconds
                if (time_difference_in_seconds <= seconds):
                    sum_trade_price_times_quantity += (trade.quantity * trade.price)
                    count_quantity += trade.quantity

            return sum_trade_price_times_quantity / count_quantity

        except ZeroDivisionError as e:
            return 0
        except CustomListException as e:
            return 0
        except Exception as e:
            return 'Error: ' + str(e)



    def calculate_gbce_all_share_index(self, list_of_trades):
        '''
        Returns the geometric mean for a given list.        
        In case of division by zero and empty list, it returns zero.
        It returns the error description in case of other exceptions.
        

        Formula: n-th square of (p1 * p2 * p3 * ... pn)
        
        '''
        try:
            #if list is not provided or is empty it raises a custom exception
            if (list_of_trades is None or len(list_of_trades) == 0):
                raise CustomListException('No list provided')

            #initial value to be used in the times operation
            prices = 1        

            #multiplies all trade prices
            for trade in list_of_trades:
                prices *= trade.price

            #returns the geometric mean
            return prices ** (1/len(list_of_trades))

        except ZeroDivisionError as e:
            return 0
        except CustomListException as e:
            return 0
        except Exception as e:
            return 'Error: ' + str(e)