"""

Demonstrate basic while loop usage

"""


def main():
    ...


def get_valid_input(
    prompt: str, valid_minimum: int = 0, valid_maximum: int = 100
) -> int:
    # initialize valid to False.
    valid = False
    result = -1

    # loop while the user hasn't given us a suitable value.
    while not valid:
        unvalidated_input = input(prompt)
        # check if the input is numeric.
        if unvalidated_input.isnumeric():
            # if its numeric, we can safely interpret it as an integer
            result = int(unvalidated_input)
            # the we can check the bounds
            valid = valid_maximum >= result >= valid_minimum
        if not valid:
            print("invalid input, please try again!")
    return result


# entry-point guard, since this example does blocking actions.
if __name__ == "__main__":
    main()
