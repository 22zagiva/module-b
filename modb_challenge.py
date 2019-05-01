def main():
    #greeting them with full name
    first_name = input("what is your first name: ")
    last_name = input("what is your last name: ")
    print("hello, %s %s!"%(first_name,last_name))
    print()

    #food list
    food = ['cookie', 'steak', 'ice cream', 'apples']
    for food in food:
        print (food)

    #showing age in days, weeks and months
    print()
    aiy = float(input("how old are you: "))
    diy = aiy * 365
    wiy = aiy * 52.143
    miy = aiy * 12
    print("you're at least", diy, "days old.")
    print("you,re at least", wiy, "weeks old.")
    print("you're at least", miy, "months old.")

    #makes funny sentence
    noun = input("enter a noun: ")
    verb = input("enter a verb: ")
    ad = input("enter a adjective: ")
    place = input("enter a place: ")
    print("Take your %s %s and %s it at the %s"%(ad, noun, verb, place))

main()
