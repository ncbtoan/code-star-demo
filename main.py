def question1(a, n):
    sum = 0
    for number in range(n + 1):
        sum += number / (a ** number)
    print(f"Sum: {sum}")


question1(3, 3)