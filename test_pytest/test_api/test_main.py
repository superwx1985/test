import pytest
import requests
import tempfile
from test_data import TestData


def test_register(domain):
    username = "abc"
    password = "123"
    path = "auth/register"
    # url = f"http://{domain}/{path}"
    url = f"http://{TestData.domain}/{path}"
    res = requests.request(method="POST", url=url, data={'username': username, 'password': password})
    assert 200 == res.status_code


def test_login(domain, user):
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
        # user["cookie"] = cookie
        user["session"] = session
    else:
        assert not res.request.headers.get("cookie")


def test_file_upload(domain, user):
    # cookie = user.get("cookie")
    session = user.get("session")
    if session:
        path = "file/file_upload"
        url = f"http://{domain}/{path}"

        filename = "test.jpg"
        f = tempfile.NamedTemporaryFile()
        f.name = filename
        data = {
            "file": f
        }
        # session = requests.session()
        # session.cookies = cookie
        res = session.request(method="POST", url=url, files=data)
        assert 200 == res.status_code
        assert filename in res.url


if __name__ == '__main__':
    # pytest.main([f'{__file__}::test_file_upload'])
    pytest.main([__file__, '-v'])
    pass
