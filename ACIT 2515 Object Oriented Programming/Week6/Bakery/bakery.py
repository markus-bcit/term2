
class Bakery:
    def __init__(self, name, croissants=0, money=0):
        self.name = name
        self.croissants = croissants
        self.money = money
        
    def bake(self, number):
        if not isinstance(int(number), int) or (type(number) is float) or (int(number) <= 0):
            raise ValueError
        self.croissants += int(number)
        return self.croissants
    def sell(self, number=1):
        
        if not isinstance(int(number), int) or (type(number) is float) or (int(number) <= 0) or (type(number) is str):
            raise ValueError
        elif int(number) > self.croissants:
            raise RuntimeError
        else:
            self.croissants -= int(number)
            self.money += int(number)*3
            
    def __str__(self):
        return self.name

def main():
    a = Bakery('name')
    # # print(a.bake(1.5))
    # print(a.bake('-100'))
    
    
if __name__ == '__main__':
    main()