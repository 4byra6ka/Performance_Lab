def task1(n: int, m: int) -> str:
    n_i = 0
    m_i = 0
    track = '1'
    # log = ''
    while True:
        n_i += 1
        m_i += 1
        # log += str(n_i)
        if n_i == 1 and m_i == m:
            break
        elif m_i == m and n_i != 1:
            # log += f',{n_i}'
            m_i = 1
            track += str(n_i)
        if n_i == n:
            n_i = 0
    # print(log)
    return track


if __name__ == '__main__':
    print(task1(4, 3))
    print(task1(5, 4))

