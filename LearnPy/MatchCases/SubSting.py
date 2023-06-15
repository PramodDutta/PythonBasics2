if "x" in "xyz":
    print("True")

string = "XYZ"
substring = "X"
match string:
    case x if substring in x:
        print("String contains the substring")
        # Perform actions for matching substring
    case _:
        print("String does not contain the substring")
        # Perform actions for non-matching substring
