import pytest
#you should create file in same file with name conftest.py and create fixture in it then it will execute can any file undr same folder
#@pytest.fixture(scope="class") #use scope="class when you want to run one time for full class"
@pytest.fixture() #TO RUN AFTER OR BEFORE EVERY TEST CASE
def setup():
    print("configure for all file setup")
    yield
    print("after tc execution")


@pytest.fixture()
def dataloade():
    print("user profile data is being created")
    return ["rahul","sharma","xyz@gmail.com"]