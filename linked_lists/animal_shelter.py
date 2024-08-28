import unittest


class Animal:
    def __init__(self, name):
        self.name = name
        self.__order = 0

    def set_order(self, order):
        self.__order = order

    def get_order(self):
        return self.__order

    def is_older_than(self, animal):
        return self.__order < animal.get_order()
    

class AnimalQueue:
    def __init__(self):
        self.dogs = []
        self.cats = []
        self.__order = 0

    def enqueue(self, animal):
        animal.set_order(self.__order)
        self.__order += 1

        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)

    def dequeue_any(self):
        if not self.dogs:
            return self.dequeue_cat()
        elif not self.cats:
            return self.dequeue_dog()

        dog = self.dogs[0]
        cat = self.cats[0]

        if dog.is_older_than(cat):
            return self.dequeue_dog()
        else:
            return self.dequeue_cat()

    def dequeue_dog(self):
        return self.dogs.pop(0)

    def dequeue_cat(self):
        return self.cats.pop(0)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)


class TestAnimalQueue(unittest.TestCase):
    def setUp(self):
        self.queue = AnimalQueue()
        self.dog1 = Dog("Rex")
        self.dog2 = Dog("Buddy")
        self.cat1 = Cat("Whiskers")
        self.cat2 = Cat("Garfield")

    def test_enqueue_dog(self):
        self.queue.enqueue(self.dog1)
        self.assertEqual(len(self.queue.dogs), 1)
        self.assertEqual(self.queue.dogs[0].name, "Rex")

    def test_enqueue_cat(self):
        self.queue.enqueue(self.cat1)
        self.assertEqual(len(self.queue.cats), 1)
        self.assertEqual(self.queue.cats[0].name, "Whiskers")

    def test_dequeue_any(self):
        self.queue.enqueue(self.dog1)
        self.queue.enqueue(self.cat1)
        self.queue.enqueue(self.dog2)
        self.queue.enqueue(self.cat2)

        animal = self.queue.dequeue_any()
        self.assertEqual(animal.name, "Rex")

        animal = self.queue.dequeue_any()
        self.assertEqual(animal.name, "Whiskers")

    def test_dequeue_dog(self):
        self.queue.enqueue(self.dog1)
        self.queue.enqueue(self.dog2)
        self.queue.enqueue(self.cat1)

        animal = self.queue.dequeue_dog()
        self.assertEqual(animal.name, "Rex")
        self.assertEqual(len(self.queue.dogs), 1)

    def test_dequeue_cat(self):
        self.queue.enqueue(self.cat1)
        self.queue.enqueue(self.cat2)
        self.queue.enqueue(self.dog1)

        animal = self.queue.dequeue_cat()
        self.assertEqual(animal.name, "Whiskers")
        self.assertEqual(len(self.queue.cats), 1)

    def test_is_older_than(self):
        self.dog1.set_order(1)
        self.cat1.set_order(2)
        self.assertTrue(self.dog1.is_older_than(self.cat1))
        self.assertFalse(self.cat1.is_older_than(self.dog1))

if __name__ == "__main__":
    unittest.main()
