from foobar import app 

def test_app():
    client = app.test_client()
    foo = client.get('/foo')
    bar = client.get('/bar')
    assert foo.data == b'foo'
    assert bar.data == b'bar'
