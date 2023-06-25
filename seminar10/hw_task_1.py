'''Доработаем задачи 5-6. Создайте класс-фабрику.
Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.'''

class Animal:
    def __init__(self, name: str, weight: int, age: int):
        self.name = name
        self.weight = weight
        self.age = age

    def move(self):
        pass

    def say(self): 
        pass

    def __str__(self):
        return f'{self.name} {self.weight} {self.age}'

class Bird(Animal):
    def __init__(self, name: str, weight: int, age: int, bird_type: str, sound: str):
        super().__init__(name, weight, age)
        self.bird_type = bird_type
        self._sound = sound

    def move(self):
        return 'Fly'
    
    def say(self):
        return self._sound
    
    def __str__(self):
        return f'{super().__str__()} {self.bird_type} {self._sound}'
    
class Dog(Animal):
    def __init__(self, name: str, weight: int, age: int, dog_type: str):
        super().__init__(name, weight, age)
        self.dog_type = dog_type

    def move(self):
        return 'Run'
    
    def say(self):
        return 'Gov'
    
    def __str__(self):
        return f'{super().__str__()} {self.dog_type}'
    
class Fish(Animal):
    def __init__(self, name: str, weight: int, age: int, fish_type: str):
        super().__init__(name, weight, age)
        self.fish_type = fish_type

    def move(self):
        return 'Swim'
    
    def say(self):
        return '' 
    
    def __str__(self):
        return f'{super().__str__()} {self.fish_type}'


'''if __name__ == '__main__':
    dog = Dog('Рэкс', 40, 5, 'Овчарка')
    bird = Bird('Лола', 1, 3, 'Попугай', 'Ку-ку')
    fish = Fish('Джо', 10, 5, 'Карп')

    print(dog)
    print(bird)
    print(fish)'''


class AnimalFactory:
    def create_animal(animal_type: str, name: str, weight: int, age: int, **kwargs):
        if animal_type == 'bird':
            return Bird(name, weight, age, **kwargs)
        elif animal_type == 'dog':
            return Dog(name, weight, age, **kwargs)
        elif animal_type == 'fish':
            return Fish(name, weight, age, **kwargs)

if __name__ == '__main__':
    dog = AnimalFactory.create_animal('dog', 'Рэкс', 40, 5, dog_type='Овчарка')
    bird = AnimalFactory.create_animal('bird', 'Лола', 1, 3, bird_type='Попугай', sound='Ку-ку')
    fish = AnimalFactory.create_animal('fish', 'Джо', 10, 5, fish_type='Карп')

    print(dog)
    print(bird)
    print(fish)
