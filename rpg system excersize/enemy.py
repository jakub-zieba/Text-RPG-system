import random

class Enemy:
    min_atk = 200
    max_atk = 300

    description = '''
        This is a base enemy, fill in the description when instantiating
    '''
    
    def __init__(self, min_atk, max_atk, description, *args):
        self.min_atk = min_atk
        self.max_atk = max_atk
        self.description = description

        # this dict should be then transformed into some descriptive field (maby?)
        self.__dict__.update(args)

    # add some methods like combat handling and loot drop maby

    def attack(self):
        return(random.randint(self.min_atk, self.max_atk))