data = [4, -30, 100, -100, 123, 1, 0, -1, -4]

if __name__ == '__main__':
    print(data)
    result = sorted(data, key = abs, reverse = True)
    print(result)

    f = lambda x: sorted(x, key = abs, reverse = True)
    result_with_lambda = f(data)
    print(result_with_lambda)
