from scanner.parser import HOST_CACHE


def test_host_cache_exists():

    assert isinstance(HOST_CACHE, dict)