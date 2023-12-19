import uuid
import pytest
import requests
import tempfile


domain = '127.0.0.1:8080'
users = [
    {"name": "abc", "pwd": "123", "status_code": 200, "msg": "Log Out"},
    {"name": "vic", "pwd": "123", "status_code": 200, "msg": "Incorrect password."}
]


def test_register():
    username = "abc"
    password = "123"
    path = "auth/register"
    url = f"http://{domain}/{path}"
    res = requests.request(method="POST", url=url, data={'username': username, 'password': password})
    assert 200 == res.status_code


@pytest.mark.parametrize("user", users)
def test_login(user):
    username = user["name"]
    password = user["pwd"]
    path = "auth/login"
    url = f"http://{domain}/{path}"
    session = requests.session()
    res = session.request(method="POST", url=url, data={'username': username, 'password': password})
    assert user["status_code"] == res.status_code
    assert user["msg"] in res.text
    if user["msg"] == "Log Out":
        cookie = session.cookies
        assert cookie
        user["cookie"] = cookie
    else:
        assert not res.request.headers.get("cookie")


@pytest.mark.parametrize("user", users)
def test_file_upload(user):
    cookie = user.get("cookie")
    if cookie:
        path = "file/file_upload"
        url = f"http://{domain}/{path}"

        filename = "test.jpg"
        f = tempfile.NamedTemporaryFile()
        f.name = filename
        data = {
            "file": f
        }
        session = requests.session()
        session.cookies = cookie
        res = session.request(method="POST", url=url, files=data)
        assert 200 == res.status_code
        assert filename in res.url


if __name__ == '__main__':
    # pytest.main([f'{__file__}::test_file_upload'])
    pytest.main([f'{__file__}'])
    pass
