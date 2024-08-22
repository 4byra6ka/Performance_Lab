def task1(n: int, m: int) -> str:
    i = 0
    m_i = 0
    track = '1'
    while True:
        i += 1
        m_i += 1
        if i == 1 and m_i == m:
            break
        elif m_i == m:
            m_i = 1
            track += str(i)
        if i == n:
            i = 0
    return track


if __name__ == '__main__':
    print(task1(4, 3))
    print(task1(5, 4))

