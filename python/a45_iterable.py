from collections.abc import Iterable

class Simpleiter:
    def __init__(self, start, end):
        self.current = start
        self.end = end

    # These methods must be indented inside the class
    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        value = self.current
        self.current += 1
        return value


def main():
    # Note: Avoid using 'iter' as a variable name as it shadows the built-in iter() function
    my_iter = Simpleiter(0, 10)
    
    print(isinstance(my_iter, Iterable))  # Now returns True!
    print(isinstance("aa", str))          # Returns True
    print(isinstance("aa", object))       # Returns True
    
    for v in my_iter:
        print(v)


if __name__ == "__main__":
    main()