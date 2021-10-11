import random


class Attack:
    def __init__(self):
        pass

    def drone_damage(self):
        randnum = random.randrange(2, 7)
        drone_d = randnum + 1
        return drone_d

    def warrior_damage(self):
        randnum = random.randrange(6, 14)
        warrior_d = randnum + 1
        return warrior_d

    def tank_damage(self):
        randnum = random.randrange(1, 10)
        tank_d = randnum + 1
        return tank_d

    def attack_drone(self, hp):
        return hp - Attack.drone_damage(Attack)

    def attack_warrior(self, hp):
        return hp - Attack.warrior_damage(Attack)

    def attack_tank(self, hp):

        d_hp = hp - Attack.tank_damage(Attack)
        return d_hp

    def drone_at_tank(self, hp):
        if hp >= 70:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 30:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 0:
            return False
        return hp

    def drone_at_warrior(self, hp):
        if hp >= 70:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 69:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 69:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 30:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 0:
            return False
        return hp

    def warrior_at_tank(self, hp):
        if hp >= 70:
            hp -= Attack.warrior_damage(Attack) - 2
        elif hp <= 69:
            hp -= Attack.warrior_damage(Attack) - 1
        elif hp <= 69:
            hp -= Attack.warrior_damage(Attack) - 1
        elif hp <= 30:
            hp -= Attack.warrior_damage(Attack) - 1
        elif hp <= 0:
            return False
        return hp

    def warrior_at_drone(self, hp):
        if hp >= 70:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 30:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 0:
            return False
        return hp

    def tank_at_drone(self, hp):
        if hp >= 70:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 30:
            hp -= Attack.tank_damage(Attack) - 1
        elif hp <= 0:
            return False
        return hp

    def tank_at_tank(self, hp):
        if hp >= 70:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 69:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 30:
            hp -= Attack.tank_damage(Attack)
        elif hp <= 0:
            return False
        return hp

    def warrior_at_warrior(self, hp):
        if hp >= 70:
            hp -= Attack.warrior_damage(Attack)
        elif hp <= 69:
            hp -= Attack.warrior_damage(Attack)
        elif hp <= 69:
            hp -= Attack.warrior_damage(Attack)
        elif hp <= 30:
            hp -= Attack.warrior_damage(Attack)
        elif hp <= 0:
            return False
        return hp

    def drone_at_drone(self, hp):
        if hp >= 70:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 69:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 69:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 30:
            hp -= Attack.drone_damage(Attack)
        elif hp <= 0:
            return False
        return hp
