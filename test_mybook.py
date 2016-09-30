import unittest
import xlwings as xw


class TestSum(unittest.TestCase):
    def setUp(self):
        self.wb = xw.Book('mybook.xlsm')

        # Map functions
        self.mysum = self.wb.macro('Module1.mysum')

    def tearDown(self):
        pass
        # self.wb.close()

    def test_mysum(self):
        result = self.mysum(1, 2)
        self.assertAlmostEqual(3, result)

    def test_mysum_alternative(self):
        arg1, arg2 = 1, 2
        self.assertAlmostEqual(self.mysum(arg1, arg2), sum((arg1, arg2)))

    def test_sum_table(self):
        # expand() automatically gets the dimensions of dynamic tables
        table = self.wb.sheets(1).range('B1').expand()
        for col in range(table.columns.count):
            self.assertAlmostEqual(table.value[3][col],
                                   table.value[1][col] + table.value[2][col])


if __name__ == '__main__':
    unittest.main()
