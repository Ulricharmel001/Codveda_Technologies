"""Creating a class with different method that perform different calculations """

class BasicMath:
    def Addition(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return f"The sum of {num1} and {num2} is {num1 + num2}"
        except ValueError:
            return "Invalid input, please enter numbers only"

    def Multiply(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return f"The product of {num1} and {num2} is {num1 * num2}"
        except ValueError:
            return "Invalid input, please enter numbers only"

    def Subtract(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return f"The difference between {num1} and {num2} is {num1 - num2}"
        except ValueError:
            return "Invalid input, please enter numbers only"

    def Division(self):
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if num2 == 0:
                return "Cannot divide by 0"
            return f"The division of {num1} by {num2} is {num1 / num2}"
        except ValueError:
            return "Invalid input, please enter numbers only"

    def run(self):
        while True:
            print('\nChoose the operation:')
            print('1. Add')
            print('2. Subtract')
            print('3. Divide')
            print('4. Multiply')
            print('5. Exit')

            choice = input("Enter choice (1-5): ")

            if choice == "1":
                print("Result:", self.Addition())
            elif choice == "2":
                print("Result:", self.Subtract())
            elif choice == "3":
                print("Result:", self.Division())
            elif choice == "4":
                print("Result:", self.Multiply())
            elif choice == "5":
                print("Goodbye")
                break
            else:
                print("Invalid choice, try again!")

if __name__ == "__main__":
    calc = BasicMath()
    calc.run()
