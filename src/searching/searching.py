# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    middle_index = (start + end) // 2
    if(len(arr) == 0):
        return -1
    if (arr[middle_index] == target):
        return middle_index
    else:
        if(arr[middle_index] > target):
            end_index = middle_index - 1
            return binary_search(arr, target, start, end_index)
        if(arr[middle_index] < target):
            start_index = middle_index + 1
            return binary_search(arr, target, start_index, end)
    return -1


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
#     # Your code here

import unittest
import random
# from searching import *

class RecursiveSortingTests(unittest.TestCase):
    def test_binary_search(self):
        arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
        arr2 = []

        self.assertEqual(binary_search(arr1, -8, 0, len(arr1)-1), 1)
        self.assertEqual(binary_search(arr1, 0, 0, len(arr1)-1), 6)
        self.assertEqual(binary_search(arr2, 6, 0, len(arr2)-1), -1)
        self.assertEqual(binary_search(arr2, 0, 0, len(arr2)-1), -1)

    # Uncomment this test to test your agnostic binary search implementation
    # def test_agnostic_binary_search(self):
    #     ascending = [2, 4, 12, 14, 17, 30, 46, 47, 51, 54, 61]
    #     descending = [101, 98, 57, 49, 45, 13, -3, -17, -61]

    #     self.assertEqual(agnostic_binary_search(ascending, 12), 2)
    #     self.assertEqual(agnostic_binary_search(ascending, 54), 9)
    #     self.assertEqual(agnostic_binary_search(ascending, 31), -1)

    #     self.assertEqual(agnostic_binary_search(descending, 49), 3)
    #     self.assertEqual(agnostic_binary_search(descending, -17), 7)
    #     self.assertEqual(agnostic_binary_search(descending, -1), -1)

if __name__ == '__main__':
    unittest.main()
