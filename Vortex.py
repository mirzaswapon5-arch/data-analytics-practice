class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.__health = health  # Private
        self.attack_power = attack_power

    def get_health(self):
        return self.__health

    def take_damage(self, damage):
        self.__health -= damage
        if self.__health < 0:
            self.__health = 0

    def attack(self, target):
        # Override করার জন্য মূল কাঠামো
        pass


class Hero(Character):
    def attack(self, target):
        print(f"⚔️ {self.name} তরবারি দিয়ে {target.name}-কে আঘাত করল!")
        target.take_damage(self.attack_power)


class Monster(Character):
    def attack(self, target):
        print(f"🔥 {target.name}-এর ওপর {self.name} আগুন দিয়ে আক্রমণ করল!")
        target.take_damage(self.attack_power)