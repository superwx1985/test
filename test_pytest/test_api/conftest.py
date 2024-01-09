import pytest



users = [
    {"name": "abc", "pwd": "123", "status_code": 200, "msg": "Log Out"},
    {"name": "vic", "pwd": "123", "status_code": 200, "msg": "Incorrect password."}
]


@pytest.fixture()
def domain():
    return '127.0.0.1:8080'


@pytest.fixture(params=users)
def user(request):
    return request.param

