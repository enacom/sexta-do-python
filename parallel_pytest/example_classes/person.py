class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        message = f"{self.name} tem {self.age} anos"
        return message


if __name__ == '__main__':
    brian = Person(name="Brian", age=25)
    print(brian)
