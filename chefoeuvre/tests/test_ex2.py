import pytest

@pytest.fixture
def yield_fixture():
    print("Start test phase")
    yield 6
    print("End test phase")

def test_exemple_yield(yield_fixture):
    print("run yield test")
    assert yield_fixture==6