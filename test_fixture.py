import pytest
#fixture functions are setup/provide resources, objects, or data to test functions can say provide prerequsite



@pytest.fixture()   #after fixture() every thing is for pre reqisite or post excution of PYtest test case

def fsetup(): #its pre requsite
    print("run first")
    yield   #yield keyword used for post execution "when yu use this keyword then after this keywrd everything is for post excution work"
    print("i will be executed last")

def test_fixturedemo(setup):
    print("fixturedemo print tst")

def test_fixturedemo1(setup):
    print("fixturedemo print tst1")

def test_fixturedemo2(setup):
    print("fixturedemo print tst2")

