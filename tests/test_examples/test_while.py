from io import StringIO

from uci_bootcamp_2021.examples.while_loops import get_valid_input


def test_get_valid_input_basic(monkeypatch):
    ###
    # Test setup
    ##

    # A file-like object to patch the standard input with.
    mocked_stdin = StringIO()
    # prepare an input that starts with an invalid input, followed by a valid input.
    mocked_stdin.write("garbage\n42\n")
    # reset stdin's position to the start of the mocked data.
    mocked_stdin.seek(0)
    # patch the standard input to temporarially point at the mocked object, so the test doesn't require human-interaction.
    monkeypatch.setattr("sys.stdin", mocked_stdin)

    ###
    # Test execution
    ##

    # Call the unit under test.
    result = get_valid_input("enter a number: ", valid_minimum=0, valid_maximum=50)

    ###
    # Test validation
    ##

    # assert it returned the expected value
    assert 42 == result
