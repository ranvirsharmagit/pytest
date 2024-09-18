import pytest
@pytest.mark.usefixtures("setup")
class Testexample:
    def test_fixturedemo(self):
        print("fixturedemo print tst")
    def test_fixturedemo1(self):
        print("fixturedemo print tst1")
    def test_fixturedemo2(self):
        print("fixturedemo print tst2")

