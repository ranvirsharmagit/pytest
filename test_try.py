#file name must be start with test_ for pytest or end with _test
#any code wrapped in method
#to run in terminal use "py.test" after enter path or use "py.test -v" or "py.test -v -s
# "py.test -k secondone -v -s" use specific file when you have multiple test case in single file "secondone" is METHOD name which is used after -k
# -K stands for method name execution -s for logs in out put  -v statds for more infor metadata
# run specific file with py.test <filename>
# -m stands for mark to run marked tc with @pytest.Mark.anytext
#smoke use for mark this method to (can use any text) , now this method is marked so you can mark may TC in that wayand run those only
import pytest


@pytest.mark.smoke
def test_firstprogram():   #pytest method name should be start with test
    print("hello")

def test_secondone():
    print("Good morning")
    msg = "hello"
    assert msg == "hello"