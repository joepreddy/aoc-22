from utils import readfile

def test_readfile():
    assert(readfile('test_inputs/readfile.txt') == ['this\n', 'is\n', 'a\n', 'test'])