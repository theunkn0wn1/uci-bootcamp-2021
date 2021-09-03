from uci_bootcamp_2021.examples.pathlib_example import main


def test_pathlib_example():
    # the expected value should be known at the time the test is written.
    # Therefore, we will not pull this from a file we assert constant.
    expected = "Provider      ,Nov-12,Dec-12,Jan-13,Feb-13,Mar-13,Apr-13,May-13,Jun-13,Jul-13,Aug-13,Sep-13,Oct-13,Nov-13,Dec-13,Jan-14,Feb-14,Mar-14,Apr-14,May-14,Jun-14,Jul-14,Aug-14,Sep-14,Oct-14,Nov-14,Dec-14,Jan-15,Feb-15"

    result = main()

    actual = result[0]
    assert expected == actual
