import sys


def start_math_guru():
    print("Choose 1 for '2^n'\nChoose 2 for 'n!'\nChoose 3 for 'fab(n)'\n")
    try:
        choice = int(input())
    except ValueError:
        print("Please enter an integer. Bye!")
        sys.exit(0)

    while choice != 1 and choice != 2 and choice != 3:
        try:
            choice = int(input("Sorry, you have to choose 1, 2, or 3!\n"))
        except ValueError:
            print("Please enter an integer. Bye!")
            sys.exit(0)

    try:
        n = int(input("What is n?\n"))
    except ValueError:
        print("Please enter an integer. Bye!")
        sys.exit(0)
    while n > 20:
        try:
            n = int(input("n has to be below 20.\n"))
        except ValueError:
            print("Please enter an integer. Bye!")
            sys.exit(0)

    if choice == 1:
        result = power_function(n)
    elif choice == 2:
        result = faculty_function(n)
    elif choice == 3:
        result = fab_function(n)
    print("The result is: " + str(result))

    yes_no = input("Do you want to go again? Yes/No\n")
    if yes_no.lower() == "yes":
        start_math_guru()
    else:
        print("Ok bye\n")


def power_function(n):
    # TODO: Calc 2^n1 here. Return int
    return 5


def faculty_function(n):
    # TODO Calc n! here. Return int
    return 5


def fab_function(n):
    # TODO: Calc fab(n) here. Return int
    return 5


if __name__ == '__main__':
    try:
        print("Welcome to MathGuru\n")
        start_math_guru()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        sys.exit(0)
