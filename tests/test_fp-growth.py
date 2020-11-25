import unittest
from data_mining import pyfpgrowth
from data_mining.pyfpgrowth import FPNode, FPTree
import csv


class FPGrowthTests(unittest.TestCase):

    def read_csv_file(self, file_name):
        """
        Transaction 데이터(사용자 정보)를 csv 파일에서 불러옴
        :param file_name: csv 파일 이름
        :return: 사용자 정보를 담은 list
        """
        with open(file_name, 'r') as f:
            reader = csv.reader(f)
            user_list = []
            max_val = 0
            next(reader)  # skip the first line a CSV file
            for row in reader:
                set_row = set(row[1:])
                if '' in set_row:
                    set_row.remove('')
                user_list.append(set_row)
                max_val = max(len(user_list[-1]), max_val)
            print('the maximum number of items {} '.format(max_val))
        self.assertEqual(1,1)
        return user_list

    def print(self):
        REAL = True
        threshold = 0.01
        if REAL:
            path = '../input/groceries - groceries.csv'
            users = self.read_csv_file(path)
        else:
            users = [[1, 2, 5],
                     [2, 4],
                     [2, 3],
                     [1, 2, 4],
                     [1, 3],
                     [2, 3],
                     [1, 3],
                     [1, 2, 3, 5],
                     [1, 2, 3]]

        answer = pyfpgrowth.find_frequent_patterns(users, 0.2)
        print(answer)
        self.assertEqual('e', answer)


class TestArray(unittest.TestCase):
    """
    Test that the result sum of all numbers
    """

    def test_sum(self):
        result = sum([1, 2, 3, 4])
        self.assertEqual(result, 31)


# th_as_num = int(threshold * len(users))
# fp_tree = FPTree(users, th_as_num)
# result = fp_tree.find_combinations(th_as_num)
# print result

if __name__ == '__main__':
    import sys

    sys.exit(unittest.main())
