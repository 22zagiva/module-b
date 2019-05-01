def main():
    def add(x, y):
        return x + y

    def sub(x, y):
        return x - y

    def mult(x, y):
        return x * y

    def divid(x, y):
        return x / y

    print("1.addition")
    print("2.subtraction")
    print("3.multiplication")
    print("4.division")
    print()

    choice = input("choose a option(1, 2, 3, 4) or quit(q): ")

    while choice !='q':
        if choice == '1':
            print("you chose addition")
            num1 = float(input("enter your first number: "))
            num2 = float(input("enter your second number: "))
            print(num1, "+", num2, "=", round(add(num1, num2), 3))
            print()
            choice = input("choose a option(1, 2, 3, 4) or quit(q): ")

        elif choice == '2':
            print("you chose subtraction")
            num1 = float(input("enter your first number: "))
            num2 = float(input("enter your second number: "))
            print(num1, "-", num2, "=", sub(num1, num2))
            print()
            choice = input("choose a option(1, 2, 3, 4) or quit(q): ")

        elif choice == '3':
            print("you chose multiplication")
            num1 = float(input("enter your first number: "))
            num2 = float(input("enter your second number: "))
            print(num1, "*", num2, "=", mult(num1, num2))
            print()
            choice = input("choose a option(1, 2, 3, 4) or quit(q): ")

        elif choice == '4':
            print("you chose division")
            num1 = float(input("enter your first number: "))
            num2 = float(input("enter your second number: "))
            print(num1, "/", num2, "=", divid(num1, num2))
            print()
            choice = input("choose a option(1, 2, 3, 4) or quit(q): ")

        elif choice != '1' and '2' and '3' and '4':
            print("please enter valid number")
            print()
            choice = input("choose a option(1, 2, 3, 4) or quit(q): ")
            
    print("thank you for using my program")

main()