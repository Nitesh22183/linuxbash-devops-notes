user_input = input("Enter a number:")
try :
    number =int(user_input)
    if number >10 :
        print("number is greater than 10")
    elif number == 10:
            print("number is equal to 10")
    else:
        print("number is lesser than 10")

except ValueError:
    print("It is anot avalid number")

