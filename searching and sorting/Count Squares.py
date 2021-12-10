def sol(n):
    if n == 1:
        return 0
    n = n ** 0.5
    if int(n) < n:
        n = int(n)
        return n
    else:
        return int(n - 1)


if __name__ == '__main__':
    n=9
    print(sol(n))