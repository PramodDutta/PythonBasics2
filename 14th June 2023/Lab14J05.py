#Substring in the String

if "x" in "xyz":
    print("True")


string = input("Enter a String")
subString = "mod"

match string:
    case string if subString in string:
        print("Present")
    case _:
        print("Not present")


full_string = "pramod"
sub_String = "mod" #Part of the word

if sub_String in full_string:
    print("True!!!!")