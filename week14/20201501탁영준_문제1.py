def count_stairs(n):
    # dp[i] = i개의 계단을 오르는 방법의 수
    # 1칸 또는 2칸만 가능 => dp[i] = dp[i-1] + dp[i-2]
    if n < 0:
        return 0

    f = [0] * (n + 1)
    f[0] = 1  # 0칸은 "아무 것도 안 함" 1가지
    if n >= 1:
        f[1] = 1

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]

    return f[n]


def main():
    n_str = input("계단의 개수를 입력하시오: ").strip()
    n = int(n_str)

    A = count_stairs(n)
    print(f"{n}개의 계단을 오르는 방법의 수는 {A}가지입니다.")


if __name__ == "__main__":
    main()
