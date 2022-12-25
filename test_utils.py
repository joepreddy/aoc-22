from utils import readfile, split

def test_readfile():
    assert(readfile('test_inputs/readfile.txt') == ['this\n', 'is\n', 'a\n', 'test'])

def test_split():
    assert(list(split(['a','b','c','d','e','f'], 2)) == [['a','b'],['c','d'],['e','f']])