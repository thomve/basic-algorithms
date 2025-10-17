import threading


def printFirst():
    print("first")

def printSecond():
    print("second")

def printThird():
    print("third")


class Foo:
    def __init__(self):
        self.first_done = threading.Event()
        self.second_done = threading.Event()

    def first(self, printFirst):
        # printFirst() outputs "first"
        printFirst()
        # signal that first() is done
        self.first_done.set()

    def second(self, printSecond):
        # wait until first() is done
        self.first_done.wait()
        # printSecond() outputs "second"
        printSecond()
        # signal that second() is done
        self.second_done.set()

    def third(self, printThird):
        # wait until second() is done
        self.second_done.wait()
        # printThird() outputs "third"
        printThird()
