def average(nums):

    if len(nums) ==0:
        return None
    total = 0
    for n in nums:
        total += n
    
    length = len(nums)

    return total/ length

print(average([1,5,4]))









## GAMLE ØVELSER ##
"""
def min_nums(nums):
    min_num = nums[0]
    for n in nums:
        if n < min_num:
            min_num = n 
    return min_num

print(min_nums([1, 2, 3]))


class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str) -> None:
        task = task.strip()
        if not task:
            raise ValueError("Task må ikke være tom.")
        self.tasks.append(task)


    def show_tasks(self):
        return self.tasks
    
    def show_tasks_numbered(self) -> str:
        if not self.tasks:
            return "Ingen opgaver endnu."
        return "\n".join(f"{i+1}. {t}" for i, t in enumerate(self.tasks))
    
    def remove_task(self, index: int) -> str:
        #Fjerner task ved 1-baseret index og returnerer teksten.
        if index < 1 or index > len(self.tasks):
            raise IndexError("Ugyldigt task-nummer.")
        return self.tasks.pop(index - 1)

    def complete_task(self, index: int) -> None:
        #Markerer en task som færdig ved at tilføje '✅' foran.
        if index < 1 or index > len(self.tasks):
            raise IndexError("Ugyldigt task-nummer.")
        self.tasks[index - 1] = "✅ " + self.tasks[index - 1]

    
todo = TodoList()
todo.add_task("Buy groceries")
todo.add_task("Walk the dog")
todo.complete_task(1)
print(todo.show_tasks_numbered())




def sum_list(numbers):
    
    total = 0
    for i in numbers:
        total += i
    return total

print(sum_list([1, 2, 3, 4, 5]))

def greet(name):
    return f"Hello, {name}!"

print(greet("Malthe"))
print(greet("Mette"))


class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        return f"{self.name} says Woof!"
    
dog1 = Dog("Buddy")
print(dog1.bark())
dog2 = Dog("Max")
print(dog2.bark())


def double (x):
    return x * 2
print(double(5))

class Car:
    def __init__ (self, brand):
        self.brand = brand

    def drive(self):
        return f"The {self.brand} is driving!"

car1 = Car("Toyota")
print(car1.drive())
car2 = Car("Honda")
print(car2.drive())

"""