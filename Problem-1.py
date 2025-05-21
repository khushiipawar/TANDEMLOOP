class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b == 0:
                return "Error: Division by zero is not allowed."
            return self.a / self.b
        else:
            return "Error: Invalid operation. Please use 'add', 'subtract', 'multiply', or 'divide'."

def main():
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

            calc = Calculator(a, b, operation)
            result = calc.calculate()
            print(f"The result of {operation}ing {a} and {b} is: {result}")

            continue_choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
            if continue_choice != 'yes':
                print("Exiting the calculator. Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
