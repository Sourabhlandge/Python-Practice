class MyIterator:
    def __init__(self, max):
        self.max = max
    def __iter__(self):
        self.no=0
        return self
    def __next__(self):
        if self.no> = self.max:
            raise StopIteration
        else:
            self.no+=1
            return self.no
    my=MyIterator(5)
    for x in my:
        print(x)