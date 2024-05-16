# The if-elif statement is shortcut of if..else chain. While using if-elif statement at the end else block is added which is performed if none of the above if-elif statement is true.
# Syntax: if (condition): statementelif (condition): statement..else: statement

letter = "C"
if(letter == "A"):
    print("letter is A")
elif letter == "B":
    print("letter is B")
elif letter == "C":
    print("letter is C")
else:
    print("letter is none of A,B or C")