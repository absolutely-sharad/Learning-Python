# Nested if..else Chain for Multiple Conditions
# if..else chain statement

letter = "D"

if letter == "B":
    print("letter is B")
else:
    if letter == "C":
        print("letter is C")
    else:
        if letter == "A":
            print("letter is A")
        else:
            print("letter is none of A, B and C")
            
# Output : letter is none of A, B and C