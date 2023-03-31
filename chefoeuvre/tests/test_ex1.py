import pytest

@pytest.fixture(scope="session")
#session : on ne run qu'une seule fois la fixture même si elle est utilisée dans plusieurs tests
def fixture_1():
    print("run_fixture_1")
    return 1

def test_exemple(fixture_1):
    print("run_exemple_1")
    num = fixture_1
    assert num==1

def test_exemple_2(fixture_1):
    print("run_exemple_2")
    num = fixture_1
    assert num==1

