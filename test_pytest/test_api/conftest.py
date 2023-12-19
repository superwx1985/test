import pytest


users = [["123", "abc", 200], ["abc", "456", 200], ["abc", "111", 401]]


@pytest.fixture(params=users)
def get_user(request):
    return request.param

