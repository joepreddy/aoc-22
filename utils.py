def readfile(path):
    with open(path) as f:
        return f.readlines()

def readfile_strip(path):
    with open(path) as f:
        return f.read().splitlines()

def split(list, chunk_size):
    for i in range(0, len(list), chunk_size):
        yield list[i:i + chunk_size]