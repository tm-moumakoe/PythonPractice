try:
    Value = int(input("Type a number between 1 and 10: "))
except (ValueError, KeyboardInterrupt):
    print("You must type a value between 1 and 10!")
else:
    if (Value > 0) and (Value <= 10):
        print("You typed:", Value)
    else:
        print("The value you typed is incorrect!")
