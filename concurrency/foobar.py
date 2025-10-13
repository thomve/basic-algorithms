from threading import Lock

"""
Suppose you are given the following code:

class FooBar {
  public void foo() {
    for (int i = 0; i < n; i++) {
      print("foo");
    }
  }

  public void bar() {
    for (int i = 0; i < n; i++) {
      print("bar");
    }
  }
}
The same instance of FooBar will be passed to two different threads:

thread A will call foo(), while
thread B will call bar().
Modify the given program to output "foobar" n times.
"""
class FooBar:
    def __init__(self, n):
        self.n = n
        self.l1 = Lock()
        self.l2 = Lock()
        self.l2.acquire()

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.l1.acquire()
            printFoo()
            self.l2.release()

    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            self.l2.acquire()
            printBar()
            self.l1.release()