import math
import os


def task2(circle: str, dot: str) -> str:
    text_return = ''
    if os.path.exists(circle):
        with open(circle, 'r', encoding='utf-8') as r_file:
            circle_dot = r_file.readline().strip().split()
            circle_x = int(circle_dot[0])
            circle_y = int(circle_dot[1])
            circle_r = int(r_file.readline().strip())
    if os.path.exists(dot):
        with open(dot, 'r', encoding='utf-8') as r_file:
            while True:
                dot_xy = r_file.readline()
                if not dot_xy:
                    break
                dot_x = int(dot_xy[0])
                dot_y = int(dot_xy[2])
                line_length = math.sqrt((circle_x - dot_x) ** 2 + (circle_y - dot_y) ** 2)
                if line_length > circle_r:
                    text_return += '2\n'
                elif line_length < circle_r:
                    text_return += '1\n'
                elif line_length == circle_r:
                    text_return += '0\n'
    return text_return


if __name__ == '__main__':
    print(task2('circle.txt', 'dot.txt'))
