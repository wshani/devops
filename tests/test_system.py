import requests 

url = 'http://127.0.0.1:8000/'

def test_system_app():
    foo = requests.get(url + 'foo')
    bar = requests.get(url + 'bar')
    assert foo.text == 'foo'
    assert bar.text == 'bar'
