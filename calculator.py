def main():
    try:
        a = float(input("Enter a value: "))
        b = float(input("Enter b value: "))
    except ValueError:
        print("Error: Please enter numeric values.")
        return

    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")
    if b != 0:
        print(f"Quotient: {a / b}")
    else:
        print("Error: Division by zero")

if __name__ == "__main__":
    main()
