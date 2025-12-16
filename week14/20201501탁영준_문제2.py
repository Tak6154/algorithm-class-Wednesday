def knapSack_dp(W, wt, val, n):
    # (n+1) x (W+1) DP 테이블 생성 및 0으로 초기화
    A = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # bottom-up 채우기
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] > w:
                A[i][w] = A[i - 1][w]
            else:
                valWith = val[i - 1] + A[i - 1][w - wt[i - 1]]
                valWithout = A[i - 1][w]
                A[i][w] = max(valWith, valWithout)

    return A  # 역추적을 위해 테이블 전체 반환


def traceback_items(A, wt, val, name, W, n):
    # A 테이블을 이용해 어떤 물건을 선택했는지 역추적
    picked = []
    w = W

    for i in range(n, 0, -1):
        # i번째 물건을 선택했다면 값이 달라짐
        if A[i][w] != A[i - 1][w]:
            picked.append(name[i - 1])
            w -= wt[i - 1]  # 선택했으니 용량 감소

    picked.reverse()
    return picked


# ----- 고정 데이터(문제 표 그대로) -----
name = ["노트북", "카메라", "책", "옷", "휴대용 충전기"]
wt   = [3, 1, 2, 2, 1]
val  = [12, 10, 6, 7, 4]
n = len(wt)

W = int(input("배낭 용량을 입력 하세요 : "))

A = knapSack_dp(W, wt, val, n)
bestVal = A[n][W]
picked_items = traceback_items(A, wt, val, name, W, n)

print(f"최대 만족도: {bestVal}")
print(f"선택된 물건: {picked_items}")
