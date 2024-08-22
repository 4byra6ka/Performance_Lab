import math
import os
from statistics import median


def task4(file_name: str) -> int:
    nums = []
    min_num_move_1 = 0
    min_num_move_2 = 0
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as r_file:
            while True:
                line = r_file.readline()
                if not line:
                    break
                nums.append(int(line.strip()))
    median_num_min = math.floor(sum(nums) / len(nums))
    median_num_max = math.ceil(sum(nums) / len(nums))
    for num in nums:
        min_num_move_1 += abs(num - median_num_max)
    for num in nums:
        min_num_move_2 += abs(num - median_num_min)
    return min_num_move_1 if min_num_move_1 < min_num_move_2 else min_num_move_2


if __name__ == '__main__':
    print(task4('numbers.txt'))
