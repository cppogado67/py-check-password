from app.main import check_password


def test_valid_password():
	assert check_password("Pass@word1") is True


def test_password_is_too_short():
	assert check_password("Pass@1") is False


def test_password_is_too_long():
	assert check_password("Password@123456789") is False


def test_password_requires_a_digit():
	assert check_password("Password@") is False


def test_password_requires_a_special_character():
	assert check_password("Password1") is False


def test_password_requires_an_uppercase_letter():
	assert check_password("password@1") is False


def test_password_rejects_invalid_characters():
	assert check_password("Pass word1") is False
	assert check_password("Pass%word1") is False
