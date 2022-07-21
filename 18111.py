def solution(n: int, m: int, b: int, lst: list) -> None:
    min_value: int = min([min(x) for x in lst])
    max_value: int = max([max(x) for x in lst])

    for r in range(n):
        for c in range(m):
            lst[r][c] -= min_value

    answer_time: int = -1
    answer_height: int = -1

    for curr in range(max_value-min_value+1) :
        time: int = 0
        count: int = 0
        for l in lst:
            for i in l:
                gap: int = i - curr
                # 양수라면 인벤토리에 집어넣어야하는거. 2초 소요
                if gap > 0:
                    time += gap*2
                    count += gap
                # 음수라면 쌓아 올려야한다는거. 1초 소요.
                elif gap < 0:
                    time += abs(gap)
                    count += gap
        if count+b >= 0 and (answer_time == -1 or answer_time >= time):
            answer_time = time
            answer_height = curr
    print(answer_time, answer_height+min_value)

if __name__ == "__main__":
    import sys
    n, m, b = map(int, sys.stdin.readline().split())
    lst: list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    solution(n, m, b, lst)