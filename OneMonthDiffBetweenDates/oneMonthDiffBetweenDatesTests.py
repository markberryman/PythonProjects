import oneMonthDiffBetweenDates
import unittest


#class SmallerDateTests(unittest.TestCase):
#    def test_DiffYear(self):
#        date1 = oneMonthDiffBetweenDates.date(1, 1, 10)
#        date2 = oneMonthDiffBetweenDates.date(1, 1, 12)
#        expected = 1

#        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

#        self.assertEqual(expected, actual)

class MonthDiffBwDatesTests(unittest.TestCase):
    def test_DiffYearGreaterThanOne(self):
        date1 = oneMonthDiffBetweenDates.date(1, 1, 10)
        date2 = oneMonthDiffBetweenDates.date(1, 1, 12)
        expected = 1

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

    def test_YearBoundaryMoreThanMonthApart(self):
        date1 = oneMonthDiffBetweenDates.date(12, 1, 10)
        date2 = oneMonthDiffBetweenDates.date(1, 2, 11)
        expected = 1

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

    def test_YearBoundaryExactlyOneMonthApart(self):
        date1 = oneMonthDiffBetweenDates.date(12, 5, 10)
        date2 = oneMonthDiffBetweenDates.date(1, 5, 11)
        expected = 0

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

    def test_YearBoundaryLessThanOneMonthApart(self):
        date1 = oneMonthDiffBetweenDates.date(12, 5, 10)
        date2 = oneMonthDiffBetweenDates.date(1, 4, 11)
        expected = -1

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

    def test_SameYearNonConsecutiveMonths(self):
        date1 = oneMonthDiffBetweenDates.date(1, 1, 11)
        date2 = oneMonthDiffBetweenDates.date(3, 1, 11)
        expected = 1

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

    def test_SameYearConsecutiveMonthAndMoreThanAMonth(self):
        date1 = oneMonthDiffBetweenDates.date(1, 1, 11)
        date2 = oneMonthDiffBetweenDates.date(2, 2, 11)
        expected = 1

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

    def test_SameYearConsecutiveMonthAndExactlyAMonthApart(self):
        date1 = oneMonthDiffBetweenDates.date(1, 1, 11)
        date2 = oneMonthDiffBetweenDates.date(2, 1, 11)
        expected = 0

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

    def test_SameYearSameMonthThereforeLessThanOneMonthApart(self):
        date1 = oneMonthDiffBetweenDates.date(1, 1, 11)
        date2 = oneMonthDiffBetweenDates.date(1, 31, 11)
        expected = -1

        actual = oneMonthDiffBetweenDates.month_diff_bw_dates(date1, date2)

        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
