import math
import os


def task2(circle_file: str = 'circle.txt', dot_file: str = 'dot.txt') -> None:
    if os.path.exists(circle_file):
        with open(circle_file, 'r', encoding='utf-8') as r_file:
            circle_dot = r_file.readline().strip().split()
            circle_x = float(circle_dot[0])
            circle_y = float(circle_dot[1])
            circle_r = float(r_file.readline().strip())
    if os.path.exists(dot_file):
        with open(dot_file, 'r', encoding='utf-8') as r_file:
            while True:
                dot_xy = r_file.readline().strip().split()
                if not dot_xy:
                    break
                dot_x = float(dot_xy[0])
                dot_y = float(dot_xy[1])
                line_length = math.sqrt((circle_x - dot_x) ** 2 + (circle_y - dot_y) ** 2)
                if line_length == circle_r:
                    print('0')
                elif line_length < circle_r:
                    print('1')
                elif line_length > circle_r:
                    print('2')


if __name__ == '__main__':
    circle_file_ = input('Введите путь до файла координатов центра окружности и радиуса:')
    dot_file_ = input('Введите путь до файла координатов точек:')
    task2(circle_file_ if circle_file_ != '' else 'circle.txt', dot_file_ if dot_file_ != '' else 'dot.txt')
