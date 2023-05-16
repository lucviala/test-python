import pytest
import socks

sock = socks.socksocket()

@pytest.fixture
def setup():
    global sock
    sock.set_proxy(socks.SOCKS5, "localhost", 1080)
    sock.connect(('172.18.0.3', 8080))
    yield
    sock.close()

def test_server_response(setup):
    data = b'hello'
    sock.send(data)
    assert sock.recv(5) == data
