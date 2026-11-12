from calculator import add, divide, multiply, power, subtract


def main():
    print("Калькулятор")
    print(f"2 + 3 = {add(2, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"3 * 4 = {multiply(3, 4)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"2 ** 3 = {power(2, 3)}")


if __name__ == "__main__":
    main()
