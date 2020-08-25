import pytest

@pytest.yield_fixture()
def setup():
    print("once before every method")
    yield
    print("once after every test method")


def testMethod1(setup):
    print("test method one")

def testMethod2(setup):
    print("test method 2")