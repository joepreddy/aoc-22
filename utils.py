def readfile(path):
    with open(path) as f:
        return f.readlines()

def readfile_strip(path):
    with open(path) as f:
        return f.read().splitlines()