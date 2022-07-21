def solution(n: int) -> int:
    answer: int
    d: list = [0 for x in range(n+1)]
    d[1] = 0
    for i in range(2, n+1):
        d[i] = d[i-1] + 1
        if i % 3 == 0 :
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 2 == 0 :
            d[i] = min(d[i], d[i // 2] + 1)
    return d[n]


if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline().strip())
    print(solution(n))