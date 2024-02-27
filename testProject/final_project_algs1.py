import math
import time
from random import seed, randint


def merge(a, b):
    i, j = 0, 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            result.append(a[i])
            i += 1
        else:
            result.append(b[j])
            j += 1
    while i < len(a):
        result.append(a[i])
        i += 1
    while j < len(b):
        result.append(b[j])
        j += 1
    return result


def merge_sort(a):
    if len(a) <= 1:
        return a
    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])
    return merge(left, right)


"""Complexity is O(n) + O(nlogn), which is O(nlogn)"""


def find_percentile(a, b, p=0):
    merged_arrays = merge(a, b)
    sorted_array = merge_sort(merged_arrays)

    print("Input arrays:")
    print("merged_arrays:", merged_arrays)
    print("sorted_array:", sorted_array)

    if len(sorted_array) != 0:
        print("Sorted array length:", len(sorted_array))
        K = len(sorted_array)
        k = math.ceil((p / 100) * K)
        print("k:", k)
        k_element = sorted_array[k - 1]
        print("k_element:", k_element)
        return k_element
    else:
        print("Merged array is empty. Cannot calculate percentile.")
        return None


def test_find_percentile(a, b, p=0, correct_answer=0):
    solution_p = find_percentile(a, b, p)
    assert solution_p == correct_answer, f'{solution_p} != {correct_answer}'
    print('test passed')


def run_unit_tests():
    test1 = test_find_percentile(a=[1, 2, 7, 8, 10], b=[6, 12], p=50, correct_answer=7)
    test2 = test_find_percentile(a=[1, 2, 7, 8], b=[6, 12], p=50, correct_answer=6)
    test3 = test_find_percentile(a=[15, 20], b=[25, 40, 50], p=40, correct_answer=20)
    print('all unit tests passed')


def reference_solution(a, b, p=0):
    print("Input arrays:")
    print("a:", a)
    print("b:", b)
    sorted_array = list(a)
    sorted_array.extend(b)
    sorted_array.sort()
    if len(sorted_array) != 0:
        print("Merged and sorted array:", sorted_array)
        K = len(sorted_array)
        k = math.ceil((p / 100) * K)
        print("k:", k)
        k_element = sorted_array[k - 1]
        print("k_element:", k_element)
        return k_element
    else:
        return None


def get_random_test(test_size, right_border):
    a = []
    b = []
    for i in range(test_size):
        a.append(randint(0, right_border))
        b.append(randint(0, right_border))
    p = randint(1, 100)
    return a, b, p


def run_stress_test(max_test_size=10, max_attemps=1000, max_right_border=10):
    seed(100)
    for test_size in range(max_test_size):
        for right_border in range(0, max_right_border):
            for attempt in range(max_attemps):
                a, b, p = get_random_test(test_size, right_border)
                reference_p = reference_solution(a, b, p)
                test_find_percentile(a, b, p, correct_answer=reference_p)
    print('Stress test passed')

def max_run_stress_test():
    seed(100)
    a,b,p = get_random_test(100000, 100000000)
    reference_p = reference_solution(a,b,p)
    start_time = time.time()
    test_find_percentile(a,b,p, correct_answer=reference_p)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Time used:", elapsed_time)

max_run_stress_test()
# print(find_percentile(a,b,p = 50))
# test_find_percentile(a,b,50,10)
