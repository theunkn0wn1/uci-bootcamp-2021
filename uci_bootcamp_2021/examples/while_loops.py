"""
uci_bootcamp_2021/examples/while_loops.py

Demonstrate basic while loop usage
"""


def get_valid_input(
    prompt: str, valid_minimum: int = 0, valid_maximum: int = 100
) -> int:
    # initialize valid to False.
    valid = False
    result = -1

    # loop while the user hasn't given us a suitable value.
    while not valid:
        # get the user's untrusted input.
        unvalidated_input = input(prompt)
        # check if the input is numeric.
        if unvalidated_input.isnumeric():
            # if its numeric, we can safely interpret it as an integer
            result = int(unvalidated_input)
            # then we can check the bounds
            valid = valid_minimum <= result <= valid_maximum
        if not valid:
            print("invalid input, please try again!")
    return result


def main():
    valid_input = get_valid_input(
        "Enter a number between 15 and 20", valid_minimum=15, valid_maximum=20
    )
    print(valid_input)


# entry-point guard, since this example does blocking actions.
if __name__ == "__main__":
    main()
