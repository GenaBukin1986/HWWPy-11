class Abstract:
    def __str__(self):
        return f"Это класс {self.name}"

class Water(Abstract):
    def __init__(self) -> None:
        self.name = "Вода"

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Mud()

class Fire(Abstract):
    def __init__(self) -> None:
        self.name = "Огонь"
        
    def __add__(self, other):
        if isinstance(other, Earth):
            return Lava()

class Air(Abstract):
    def __init__(self) -> None:
        self.name = "Воздух"
        
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()    
        elif isinstance(other, Earth):
            return Dust()
    

class Earth(Abstract):
    def __init__(self) -> None:
        self.name = "Земля"
        
    def __add__(self, other):
        if isinstance(other, Air):
            return Dust()

class Storm(Abstract):
    def __init__(self) -> None:
        self.name = "Шторм"

class Steam(Abstract): # Пар
    def __init__(self) -> None:
        self.name = "Пар"

class Mud(Abstract): # Грязь
    def __init__(self) -> None:
        self.name = "Грязь"

class Lightning(Abstract): # Молния
    def __init__(self) -> None:
        self.name = "Молния"

class Dust(Abstract): # Пыль
    def __init__(self) -> None:
        self.name = "Пыль"

class Lava(Abstract):
    def __init__(self) -> None:
        self.name = "Лава"


if __name__ == "__main__":
    water = Water()
    air = Air()
    print(water + air)
    
    earth = Earth()
    print(earth + air)