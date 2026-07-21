from scanner.filters import validate_filter


def test_valid_filter():

    assert validate_filter("tcp") == "tcp"


def test_dns_filter():

    assert validate_filter("dns") == "dns"