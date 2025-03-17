import random


class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(self.attack_power // 2, self.attack_power)
        other.health -= damage
        print(f"{self.name} атакует {other.name} и наносит {damage} урона!")

    def is_alive(self):
        return self.health > 0


class Game:
    def __init__(self, player_name):
        self.player = Hero(player_name)
        self.computer = Hero("Компьютер")

    def start(self):
        print("Начинаем битву героев!")
        while self.player.is_alive() and self.computer.is_alive():
            input("Нажмите Enter, чтобы совершить ход...")
            self.player.attack(self.computer)
            if not self.computer.is_alive():
                print(f"{self.computer.name} побежден! {self.player.name} выиграл!")
                break

            input("Нажмите Enter, чтобы продолжить...")
            self.computer.attack(self.player)
            if not self.player.is_alive():
                print(f"{self.player.name} побежден! {self.computer.name} выиграл!")
                break

            print(f"{self.player.name}: {self.player.health} HP | {self.computer.name}: {self.computer.health} HP\n")


if __name__ == "__main__":
    name = input("Введите имя вашего героя: ")
    game = Game(name)
    game.start()