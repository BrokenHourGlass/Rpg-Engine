import sys, pygame, time, random, math
pygame.init()

#CONSTANTS
BLACK = pygame.Color(0,0,0)
WHITE = pygame.Color(255,255,255)
GREEN = pygame.Color(0,255,0)
GAME_FONT = pygame.font.SysFont('Comic Sans', 30)

#Classes
class Window:
    screen = None
    width, height = 0,0
    tile_size = 0

    def __init__(self, x, y):
        self.screen = pygame.display.set_mode((x,y))
        self.width, self.height = self.screen.get_size()
        self.tile_size = 60*(self.width/1920)

    def getScreen(self):
        return self.screen

    def getDim(self):
        return (self.width, self.height)

    def getSize(self):
        return self.tile_size

class Battle_sys:

    hero_list = []
    enemy_list = []
    battle_order = []

    def turn_order(self, hero, enemy):
        organize_list = []

        #enters hero and enemy list to be numerated and organized
        for i in range(len(hero)):
            organize_list.append((hero[i], self.roll()+hero[i].get_mod(hero[i].get_dex())))
        for i in range(len(enemy)):
            organize_list.append((enemy[i], self.roll()+enemy[i].get_mod(enemy[i].get_dex())))

        organize_list = sorted(organize_list, key = lambda x: x[1], reverse = True)

    def add_to_list(self, list, var):
        #list being battle_sys variable, var being actor
        pass

    def roll(self):
        return random.randint(1,20)

    def advantage(self):
        return max([self.roll(), self.roll()])

    def disadvantage(self):
        return min([self.roll(), self.roll()])

class Actor:
    health = 0
    weapon = None
    armor = None
    ac = None
    inventory = []
    str = 0
    dex = 0
    con = 0
    int = 0
    wis = 0
    cha = 0

    defense = False
    dead = False

    def __init__(self, hp=10, wp=None, arm=None, strength=10, dexterity=10, constitution = 10, intelligence=10, wisdom=10, charisma=10):
        self.health = hp
        self.weapon = wp
        self.armor = arm
        self.str = strength
        self.dex = dexterity
        self.int = intelligence
        self.wis = wisdom
        self.cha = charisma
        self.ac = self.calculate_ac()

    def get_ac(self):
        return self.ac

    def calculate_ac(self):
        return self.armor + self.get_mod(self.dex)

    def get_mod(self, stat):
        return math.floor((stat-10)/2)

    def is_dead(self):
        return self.dead

    def is_defending(self):
        return self.defense

    def defending(self):
        self.defense = True

    def get_health(self):
        return self.health

    def set_health(self, hp):
        self.health = hp

    def get_weapon(self):
        return self.weapon

    def set_weapon(self, wp):
        self.weapon = wp

    def get_armor(self):
        return self.armor

    def set_armor(self, arm):
        self.armor = arm

    def get_inventory(self):
        return self.inventory

    def set_inventory(self):
        pass

    def get_str(self):
        return self.str

    def set_str(self, num):
        self.str = num

    def get_dex(self):
        return self.dex

    def set_dex(self, num):
        self.dex = num

    def get_con(self):
        return self.con

    def set_con(self, num):
        self.con = num

    def get_int(self):
        return self.int

    def set_int(self, num):
        self.int = num

    def get_wis(self):
        return self.wis

    def set_wis(self, num):
        self.wis = num

    def get_cha(self):
        return self.cha

    def set_cha(self, num):
        self.cha = num

    def attack(self, target):
        defense = target.get_ac()
        if(target.is_defending()):
            defense = defense + 5
        if(random.randint(1,20)+self.get_mod(self.str))>defense:
            target.set_health(target.get_health()-(random.randint(1,6)+self.get_mod(self.str)))

class Player(Actor):
    pass

class Enemy(Actor):
    pass

class Board:
    pass

test = Window(960, 540)
battle = Battle_sys()

#Variables
bg = pygame.transform.scale(pygame.image.load("background/60checker.png"), test.getDim())

act = [Player(100, None, 15, 18, 15)]
nemesis = [Enemy(100, None, 10, 12)]
#nemesis.defending()

battle.turn_order(act, nemesis)

while True:
    test.getScreen().blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    #act.attack(nemesis)
    #print(nemesis.get_health())
    pygame.display.update()
