import pytest

@pytest.fixture()
def setup():
    print("once before every method")

def testmethod1(setup):
    print("this is method one")

def testmethod2(setup):
    print("this is method two")

# to excute:
# 1 open terminal
# 2 enter pytest -v -s name of the file if you have multiple pytest testcases.