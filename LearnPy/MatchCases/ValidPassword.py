def validate_password(password):
    match password:
        case p if len(p) < 6:
            print("Weak password: Too short")
        case p if p.isnumeric():
            print("Weak password: Numeric only")
        case p if p.isalpha():
            print("Weak password: Alphabetical only")
        case p if p.islower():
            print("Weak password: All lowercase")
        case p if p.isupper():
            print("Weak password: All uppercase")
        case _:
            print("Strong password")

validate_password("2349999oP")