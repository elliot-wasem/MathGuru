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
        if n < 0:
            result = "N/A"
        else:
            result = factorial_function(n)
    elif choice == 3:
        if n < 0:
            result = "N/A"
        else:
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


def factorial_function(n):
    """Compute factorial of number n. n must be greater than or equal to 0."""
    # TODO Calc n! here. Return int
    if n == 0 or n == 1:
        return 1
    return n * factorial_function(n - 1)


def fab_function(n):
    """
    We use the modern Fibonacci sequence which start from 0.
    https://en.wikipedia.org/wiki/Fibonacci_number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fab_function(n - 1) + fab_function(n - 2)


if __name__ == '__main__':
    try:
        print("Welcome to MathGuru\n")
        start_math_guru()
    except KeyboardInterrupt:
        print("Keyboard interrupt")
        sys.exit(0)
