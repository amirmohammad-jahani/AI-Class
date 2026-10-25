class Character:
    def __init__(self,name,power,health,coins):
        self.name = name
        self.power = power
        self.health = health
        self.coins = coins
        self.level = 1

    def show_info(self):
        print(f"{self.name} | Level : {self.level} | Power : {self.power} | Health : {self.health} | Coins : {self.coins}")

    def is_alive(self):
        if self.health > 0:
            return True
        else:
            return False

    def attack(self,other):
        other.health -= self.power
        print(f"{self.name} attacked {other.name} , {other.name}s health : {other.health}")

    def earn_coins(self,amount):
        self.coins += amount

    def buy_potion(self):
        if self.coins >= 20:
            self.health += 30
        else:
            print("Not enough coins")

    def level_up(self):
        self.level += 1
        self.power += 5
        print(f"{self.name} reached level : {self.level} New power : {self.power}")

arya = Character("Arya",10,100,200)
bran = Character("Bran",7,120,180)

arya.attack(bran)
bran.attack(arya)
arya.attack(bran)
arya.attack(bran)
bran.attack(arya)

bran.buy_potion()

arya.level_up()

arya.show_info()
bran.show_info()

