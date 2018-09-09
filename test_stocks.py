'''
Unit tests
'''

import unittest
import time
from datetime import datetime
from stocks import Stock, Calculator, Trade, EnumStockTypes, EnumBuySellIndicator



class Test_test_stocks(unittest.TestCase):
    common_stock = None
    preferred_stock = None
    calculator = None
    common_trade = None
    preferred_trade = None
    list_of_trades = list()



    def setUp(self):
        '''
        Setting data for unit tests
        '''

        self.common_stock = Stock('ABCD', EnumStockTypes.COMMON, 100, 8, None, 100)
        self.preferred_stock = Stock('EFGH', EnumStockTypes.PREF, 100, 8, 0.02, 100)

        self.common_stock_division_by_zero = Stock('ABCD', EnumStockTypes.COMMON, 0, 8, None, 100)
        self.preferred_stock_division_by_zero = Stock('EFGH', EnumStockTypes.PREF, 100, 8, 0.02, 0)

        self.calculator = Calculator()
        self.common_trade = Trade(self.common_stock, datetime.strptime("09/09/18 16:30:31", "%d/%m/%y %H:%M:%S") , 200, EnumBuySellIndicator.BUY.value , 150)
        self.preferred_trade = Trade(self.preferred_stock, datetime.strptime("09/09/18 16:30:32", "%d/%m/%y %H:%M:%S"), 300, EnumBuySellIndicator.SELL.value, 200)
        
        
        self.list_of_trades.append(Trade(self.common_stock, datetime.strptime("09/09/18 16:30:29", "%d/%m/%y %H:%M:%S") , 200, EnumBuySellIndicator.BUY, 150))
        self.list_of_trades.append(Trade(self.common_stock, datetime.strptime("09/09/18 16:30:30", "%d/%m/%y %H:%M:%S") , 200, EnumBuySellIndicator.BUY, 150))
        self.list_of_trades.append(Trade(self.common_stock, datetime.strptime("09/09/18 16:30:31", "%d/%m/%y %H:%M:%S") , 200, EnumBuySellIndicator.BUY, 150))
        self.list_of_trades.append(Trade(self.preferred_stock, datetime.strptime("09/09/18 16:45:30", "%d/%m/%y %H:%M:%S"), 300, EnumBuySellIndicator.SELL, 200))
        self.list_of_trades.append(Trade(self.preferred_stock, datetime.strptime("09/09/18 16:45:30", "%d/%m/%y %H:%M:%S"), 300, EnumBuySellIndicator.SELL, 200))
        self.list_of_trades.append(Trade(self.preferred_stock, datetime.strptime("09/09/18 16:45:30", "%d/%m/%y %H:%M:%S"), 300, EnumBuySellIndicator.SELL, 200))
        
        

        
    def test_calculate_divident_yield_for_common_stock(self):
        #expected result
        expected_result = 0.08
                
        #actual result
        actual_result = self.calculator.calculate_dividend_yield(self.common_stock)

        #assertion
        self.assertEqual(actual_result, expected_result, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))



    def test_calculate_divident_yield_for_preferred_stock(self):
        #expected result
        expected_result = 0.02
        
        #actual result
        actual_result = self.calculator.calculate_dividend_yield(self.preferred_stock)

        #assertion
        self.assertEqual(actual_result, expected_result, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))



    def test_calculate_divident_yield_division_by_zero(self):
        #expected result
        expected_result = 0
                
        #actual result
        actual_result_for_common = self.calculator.calculate_dividend_yield(self.common_stock_division_by_zero)
        actual_result_for_preferred = self.calculator.calculate_dividend_yield(self.common_stock_division_by_zero)
        
        #assertion
        self.assertEqual(actual_result_for_common, expected_result, msg='FAIL. Actual value: ' + str(actual_result_for_common) + 'Expected: ' + str(expected_result))
        self.assertEqual(actual_result_for_preferred, expected_result, msg='FAIL. Actual value: ' + str(actual_result_for_preferred) + 'Expected: ' + str(expected_result))


    def test_calculate_pe_ratio(self):
        #expected result
        expected_result_for_common_stock = 1250
        expected_result_for_preferred_stock = 5000
        
        #actual result
        actual_result_for_common_stock = self.calculator.calculate_pe_ratio(self.common_stock)
        actual_result_for_preferred_stock = self.calculator.calculate_pe_ratio(self.preferred_stock)

        #assertion
        self.assertEqual(actual_result_for_common_stock, expected_result_for_common_stock, msg='FAIL. Actual value: ' + str(actual_result_for_common_stock) + 'Expected: ' + str(expected_result_for_common_stock))
        self.assertEqual(actual_result_for_preferred_stock, expected_result_for_preferred_stock, msg='FAIL. Actual value: ' + str(actual_result_for_preferred_stock) + 'Expected: ' + str(expected_result_for_preferred_stock))
        


    def test_calculate_pe_ratio_division_by_zero(self):
        #expected result
        expected_result = 0
        
        #actual result
        actual_result_for_common_stock = self.calculator.calculate_pe_ratio(self.common_stock_division_by_zero)
        actual_result_for_preferred_stock = self.calculator.calculate_pe_ratio(self.common_stock_division_by_zero)
        
        #assertion
        self.assertEqual(actual_result_for_common_stock, expected_result, msg='FAIL. Actual value: ' + str(actual_result_for_common_stock) + 'Expected: ' + str(expected_result))
        self.assertEqual(actual_result_for_preferred_stock, expected_result, msg='FAIL. Actual value: ' + str(actual_result_for_preferred_stock) + 'Expected: ' + str(expected_result))



    def test_record_trade(self):
        #expected result
        expected_result_for_common_stock = 'Stock Symbol: ABCD - Time: 2018-09-09 16:30:31 - Quantity: 200 - Indicator: Buy - Price: 150'
        expected_result_for_preferred_stock = 'Stock Symbol: EFGH - Time: 2018-09-09 16:30:32 - Quantity: 300 - Indicator: Sell - Price: 200'

        #actual result
        actual_result_for_common_stock = self.common_trade.return_print()
        actual_result_for_preferred_stock = self.preferred_trade.return_print()

        #assertion
        self.assertEqual(actual_result_for_common_stock, expected_result_for_common_stock, msg='FAIL. Actual value: ' + actual_result_for_common_stock + 'Expected: ' + expected_result_for_common_stock)
        self.assertEqual(actual_result_for_preferred_stock, expected_result_for_preferred_stock, msg='FAIL. Actual value: ' + actual_result_for_preferred_stock + 'Expected: ' + expected_result_for_preferred_stock)



    def test_calculate_volume_weighted_stock_price(self):
        #expected result
        expected_result = 184.62

        #actual result
        actual_result = self.calculator.calculate_volume_weighted_stock_price(self.list_of_trades, datetime.strptime("09/09/18 16:45:30", "%d/%m/%y %H:%M:%S"))

        #assertion
        self.assertAlmostEqual(actual_result, expected_result, 2, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))



    def test_calculate_volume_weighted_stock_price_with_empty_list(self):
        #expected result
        expected_result = 0
        actual_result = self.calculator.calculate_volume_weighted_stock_price(list(), datetime.strptime("09/09/18 16:45:30", "%d/%m/%y %H:%M:%S"))

        #actual result
        self.assertAlmostEqual(actual_result, expected_result, 2, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))



    def test_calculate_volume_weighted_stock_price_no_list(self):
        #expected result
        expected_result = 0
        
        #actual result
        actual_result = self.calculator.calculate_volume_weighted_stock_price(None, datetime.strptime("09/09/18 16:45:30", "%d/%m/%y %H:%M:%S"))

        #assertion
        self.assertAlmostEqual(actual_result, expected_result, 2, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))



    def test_calculate_gbce_all_share_index(self):
        #expected result
        expected_result = 173.21

        #actual result
        actual_result = self.calculator.calculate_gbce_all_share_index(self.list_of_trades)

        #assertion
        self.assertAlmostEqual(actual_result, expected_result, 2, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))        



    def test_calculate_gbce_all_share_index_with_empty_list(self):
        #expected result
        expected_result = 0
      
        #actual result
        actual_result = self.calculator.calculate_gbce_all_share_index(list())

        #assertion
        self.assertAlmostEqual(actual_result, expected_result, 2, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))



    def test_calculate_gbce_all_share_index_with_no_list(self):
        #expected result
        expected_result = 0
      
        #actual result
        actual_result = self.calculator.calculate_gbce_all_share_index(None)

        #assertion
        self.assertAlmostEqual(actual_result, expected_result, 2, msg='FAIL. Actual value: ' + str(actual_result) + 'Expected: ' + str(expected_result))



if __name__ == '__main__':
    unittest.main()
