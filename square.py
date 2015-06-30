# file squares.py

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

if __name__ == '__main__':
    S = Squares(1,5)
    Q = Squares(1,5)
    for i in S:
        for j in Q:
            print("%s:%s" % (i,j), end=' ')