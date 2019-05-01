# convert.py
# by: Valeriy Z.

def main():
    print("this program converts celsius to fahrenheit")
    print("and converts fahrenheit to celsius")
    print()
    print("Celsius temperature\tfahrenheit temperature")
    for c in range (0, 101, 10):
        f = 9/5 * c + 32
        print(c,"°C","\t\t\t\t", f,"°F")
        if c == 101:
            break

    #converts celsius to fahrenheit
    def ctf():
        for i in range(5):
            cel = eval(input("What is the Celsius temperature? "))
            fah = 9 / 5 * cel + 32
            print("The temperature is", fah, "degrees Fahrenheit.")
            print(" ")
            if i == 6:
                break

    #converts fahrenheit to celsius
    def ftc():
        for i in range(5):
            fah = eval(input("What is the fahrenheit temperature? "))
            cel = (fah-32)*5/9
            print("The temperature is", cel, "degrees celsius.")
            print(" ")
            if i == 6:
                break

    #asks what action the user would like to take
    uc = input("do you wat to convert C-->F(c) or F-->C(f) or quit(q):")
    while uc !='q':
        if uc == 'c': 
            ctf()
            uc = input("do you wat to convert C-->F(c) or F-->C(f) or quit(q):")

        elif uc == 'f':
            ftc()
            uc = input("do you wat to convert C-->F(c) or F-->C(f) or quit(q):")    

        elif uc !='c' and uc !='f':
            print("please put valid input")
            uc = input("do you wat to convert C-->F(c) or F-->C(f) or quit(q):")
           
    #just prints now exiting when exiting
    print("now exiting")

main()
