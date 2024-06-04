from funcs import sum_function, subtract_function

a = int(input("a = "))
b = int(input("b = "))


def main():
    print('press "1" to sum, press "2" to subtract\n')
    if int(input('Press "1" to sum, press "2" to subtract\n')) == 1:
        result = sum_function(a, b)
    else:
        result = subtract_function(a, b)
    print(result)


if __name__ == "__main__":
    main()
