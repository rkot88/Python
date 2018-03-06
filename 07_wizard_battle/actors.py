import random


class Creature:
    def __init__(self, name, the_level):  # self is a pointer to an object created in init
        self.name = name
        self.level = the_level

    def __repr__(self):
        return "Creature {} of level {}".format(
            self.name, self.level
        )

    def get_defensive_roll(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):
    '''def __init__(self, name, level):  # self is a pointer to an object created in init
    super().__init__(name, level) # access to direct methods on creature'''  # actually we don't need that

    def attack(self, creature):
        print("The wizard {} attacks {}!".format(
            self.name, creature.name
        ))

        my_roll = self.get_defensive_roll()
        # creature_roll = random.randint(1, 12) * creature.level
        creature_roll = creature.get_defensive_roll()

        print("You roll {}...".format(my_roll))
        print("{} rolls {}...".format(creature.name, creature_roll))

        if my_roll >= creature_roll:
            print("The wizard has destroyed a {}".format(creature.name))
            return True
        else:
            print("The wizard has been defeated")
            return False


class SmallAnimal(Creature):
    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.breaths_fire = breaths_fire
        self.scaliness = scaliness

    def get_defensive_roll(self):
        base_roll = super().get_defensive_roll()
        # fire_modifier = None
        # if self.breaths_fire:
        #     fire_modifier = 5
        # else:
        #     fire_modifier = 1

        # fire_modifier = VALUE_IF_TRUE if SOME_TEST else VALUE_IF_FALSE
        fire_modifier = 5 if self.breaths_fire else 1
        scale_modifier = self.scaliness / 10

        return base_roll * fire_modifier * scale_modifier