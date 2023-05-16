# SOCKS5 Proxy Sockets tests

Creates a very simple infrastructure with:
- `client.py`: Craft packet and implements SOCKS5 socket connection
- `main.py`: Very simple dockerized socket listener
- The SOCKS5 proxy docker is `ghcr.io/httptoolkit/docker-socks-tunnel:latest`

## How to run

:warning: Don't forget to change the server IPAddress in `client.py`

```bash
HOSTNAME$ docker inspect server | grep IPAddress
            "SecondaryIPAddresses": null,
            "IPAddress": "",
                    "IPAddress": "172.18.0.3",
```

```bash
HOSTNAME$ pip install scapy PySocks
HOSTNAME$ docker-compose up -d
HOSTNAME$ python client.py
```

## How to test

```bash
HOSTNAME$ pip install --user pytest
HOSTNAME$ pytest -sv tests
========================================= test session starts ==========================================
platform linux -- Python 3.9.9, pytest-7.3.1, pluggy-1.0.0 -- /home/fedora/.pyenv/versions/3.9.9/bin/python3
cachedir: .pytest_cache
rootdir: /home/fedora/Documents/git-repos/test-archi/endpoint
collected 1 item

tests/socks_test.py::test_server_response PASSED

========================================== 1 passed in 0.01s ===========================================
```

