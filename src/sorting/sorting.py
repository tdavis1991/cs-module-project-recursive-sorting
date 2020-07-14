# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    # Your code here


    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]

        merge_sort(left)
        merge_sort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
              myList[k] = left[i]
              i += 1
            else:
                myList[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k]=right[j]
            j += 1
            k += 1
    return myList

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
# def merge_in_place(arr, start, mid, end):
#     # Your code here


# def merge_sort_in_place(arr, l, r):
#     # Your code here

import unittest
import random


class RecursiveSortingTests(unittest.TestCase):
    def test_merge_sort(self):
        arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
        arr2 = []
        arr3 = [2]
        arr4 = [0, 1, 2, 3, 4, 5]
        arr5 = random.sample(range(200), 50)

        self.assertEqual(merge_sort(arr1), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(merge_sort(arr2), [])
        self.assertEqual(merge_sort(arr3), [2])
        self.assertEqual(merge_sort(arr4), [0, 1, 2, 3, 4, 5])
        self.assertEqual(merge_sort(arr5), sorted(arr5))

    # Uncomment this test to test your in-place merge sort implementation
    # def test_in_place_merge_sort(self):
    #     arr1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
    #     arr2 = []
    #     arr3 = [2]
    #     arr4 = [0, 1, 2, 3, 4, 5]
    #     arr5 = random.sample(range(200), 50)
    #     arr5_copy = [x for x in arr5]

    #     merge_sort_in_place(arr1, 0, len(arr1)-1)
    #     self.assertEqual(arr1, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    #     merge_sort_in_place(arr2, 0, len(arr2)-1)
    #     self.assertEqual(arr2, [])
        
    #     merge_sort_in_place(arr3, 0, len(arr3)-1)
    #     self.assertEqual(arr3, [2])

    #     merge_sort_in_place(arr4, 0, len(arr4)-1)
    #     self.assertEqual(arr4, [0, 1, 2, 3, 4, 5])

    #     merge_sort_in_place(arr5, 0, len(arr5)-1)
    #     self.assertEqual(arr5, sorted(arr5_copy))


if __name__ == '__main__':
    unittest.main()
