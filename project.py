try:
    age=int(input("Enter your age: "))
    if age%2==0:
        print("The age entered is even.")
    else:
        print("The age entered is odd.")
    print(age)
except ValueError:
    print("Check the values!")
except NameError:
    print("Check The name!")
finally:
    print("done")