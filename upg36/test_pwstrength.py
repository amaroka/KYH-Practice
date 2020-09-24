from upg36.pwstrength import compute_strength


def test_password_with_length_11_gives_1_point():
    pw = "1" * 11
    assert compute_strength(pw) == 1

def test_password_with_alphanumeric_gives_1_point():
    pw = "abc123"
    assert compute_strength(pw) == 1

def test_password_with_symbols_gives_1_point():
    pw = "#%&"
    assert compute_strength(pw) == 1

def test_password_with_any_other_symbols_gives_0_points():
    pw = "a1asfhaslfh#/()"
    assert compute_strength(pw) == 0

def test_password_with_length_and_alphanumeric_gives_2_points():
    pw = "a1" * 11
    assert compute_strength(pw) == 2

def test_password_with_length_and_symbols_gives_2_points():
    pw = "a#" * 11
    assert compute_strength(pw) == 2

def test_password_with_alphanumeric_and_symbols_gives_2_points():
    pw = "a1#"
    assert compute_strength(pw) == 2

def test_password_with_all_rules_gives_3_points():
    pw = "a1#" * 5
    assert compute_strength(pw) == 3
