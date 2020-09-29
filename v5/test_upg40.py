from v5.upg40 import reverse, upper, in_range


def test_string_rev_v1():
    expected = "54321"
    got = reverse("12345")
    assert expected == got


def test_string_rev_v2():
    expected = "cba"
    got = reverse("abc")
    assert expected == got

def test_string_rev_v3():
    expected = "54321"
    got = reverse("1345")
    assert expected != got

def test_stor_bokstav_v1():
    expected = 2
    got = upper("Hej Hej")
    assert expected == got

def test_stor_bokstav_v2():
    expected = 3
    got = upper("Hej Hej")
    assert expected != got

def test_stor_bokstav_3():
    expected = 3
    got = upper("HEJ Hej")
    assert expected <= got


def test_in_range_v1():
    min = 1
    max = 3
    value = 2
    assert in_range(value,min,max) == True
def test_in_range_v2():
    min = 1
    max = 3
    value = 4
    assert in_range(value,min,max) != True
def test_in_range_v3():
    min = 1
    max = 3
    value = 0
    assert in_range(value,min,max) == False