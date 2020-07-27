import requests
import pytest

class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.headers)
        print(r.json())
        assert r.status_code == 200
    def test_query(self):
        payload = {
            "a":1,
            "name":'mjx'
        }
        r = requests.get('http://httpbin.testing-studio.com/get',params=payload)
        print(r.text)
        assert r.status_code == 200
    def test_form(self):
        payload = {
            "level":1,
            "name":'mjx'
        }
        r = requests.post('http://httpbin.testing-studio.com/post_post',data=payload)
        print(r.text)
        assert r.status_code == 200
    def test_headers(self):
        r = requests.get('http://httpbin.testing-studio.com/get',headers={"h":"demo"})

        print(r.status_code)
        print(r.headers)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == 'demo'


