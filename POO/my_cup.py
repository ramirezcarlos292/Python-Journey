from typing import Union
from dataclasses import dataclass

class Cup:
    def __init__(self, liquid, volume, temperature):
        self.liquid = liquid
        self.volume = volume
        self.temperature = temperature
    
    def __str__(self):
        return f"I want a cup of {self.temperature} {self.liquid}, size {self.volume} ml."
        
@dataclass
class Cup2:
    liquid: str
    volume: int
    temperature: str
    
    def __str__(self):
        return f"I want a cup of {self.temperature} {self.liquid}, size {self.volume} ml."
        
        
my_coffee = Cup('coffee', 355, 'hot')
print(my_coffee)

my_tea = Cup('mint tea', 500, 'cold')
print(my_tea)

my_coffee = Cup2('coffee', 500, 'hot')
print(my_coffee)

my_tea = Cup2('mint tea', 1000, 'cold')
print(my_tea)