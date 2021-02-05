# #                     ...................................... class / object ................................
# class PlayerCharacter:
#     membership = True       # class object attributes
#     def __init__(self,name,age):
#         if self.membership:
#             self.name = name       # attributes
#             self.age =age
#
#     def shout(self):
#         print(f'my name is {self.name}')
#
#
# player1 = PlayerCharacter('Akash',26)
# player2 = PlayerCharacter('Arif', 26)
#
# print(f'{player1.name} is {player1.age} years old')
# print(f'{player2.name} is {player2.age} years old')
#
# print(player1.shout())
# print(player2.shout())

#                     ...................................... init ................................
# class PlayerCharacter:
#     def __init__(self,name,age):
#         if age>18:
#             self.name = name       # attributes
#             self.age =age
#
#     def shout(self):
#         print(f'my name is {self.name}')
#
#
# player1 = PlayerCharacter('Akash',0)
# player2 = PlayerCharacter('Arif', 26)
#
# print(f'{player1.name} is {player1.age} years old')       #  name error
# print(f'{player2.name} is {player2.age} years old')

#                     ...................................... Exercise ................................
#

# # Given the below class:
# class Cat:
#     species = 'mammal'
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# # 1 Instantiate the Cat object with 3 cats
# cat1 = Cat('p1', 20)
# cat2 = Cat('p2', 30)
# cat3 = Cat('p3', 20)
#
# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
#
# def oldest_cat(*args):
#     return max(*args)
#
#
# print(f'The age of oldest cat {oldest_cat(cat1.age, cat2.age, cat3.age)} year')

#                     ...................................... Exercise ................................
#
#
# class PlayerCharacter:
#     def __init__(self,name,age):
#         self.name = name       # attributes
#         self.age =age
#
#     @classmethod
#     def add(cls,num1,num2):
#         return num1+num2
#
#
# p1 = PlayerCharacter('aaa',20)
# print(p1.add(2,3))
#
# # calling add method without declaring PlayerCharacter object so it is called @classmethod
# print(PlayerCharacter.add(2,5))

# # ...............
#
# class PlayerCharacter:
#     def __init__(self,name,age):
#         self.name = name       # attributes
#         self.age =age
#
#     @classmethod
#     def add(cls,num1,num2):
#         return cls('akash',num1+num2)
#
#     @staticmethod                 #      almost same but not adding cls parameter
#     def add2(num1,num2):
#         return num1+num2
#
#
# p2 = PlayerCharacter.add(2,5)
# print(p2.age)

#                     ...................................... private ................................
# class PlayerCharacter:
#     def __init__(self,name,age):
#         self._name = name       #  _ is use for private
#         self._age =age
#
#     def shout(self):
#         print(f'my name is {self._name} and age {self._age} ')
#
#
# p1 = PlayerCharacter('ass', 40)
# p1.shout()
#
# p1.shout = 'booo'
# print(p1.shout)      # do not use shout() method....because of private attribute

# #                     ...................................... inheritance ................................
# class User():
#     def sign_in(self):
#         print('sign in')
#
# class Wizard(User):
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(f'attacking with power of self {self.power}')
#
# class Archer(User):
#     def __init__(self,name,num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#     def attack(self):
#         print(f'attacking with arrows:  {self.num_arrows}')
#
# wizard1 = Wizard('AAA',40)
# archer1 = Archer('bbA',400)
#
# print(wizard1.attack())
# print(archer1.attack())
# # wizard1 and archer1 both call sign_in method of User class -> for the reason of inheritance

#                     ...................................... polymorphism ................................
# class User():
#     def sign_in(self):
#         print('sign in')
#
# class Wizard(User):
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(f'attacking with power of self {self.power}')
#
# class Archer(User):
#     def __init__(self,name,num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#     def attack(self):
#         print(f'attacking with arrows:  {self.num_arrows}')
#
# wizard1 = Wizard('AAA',40)
# archer1 = Archer('bbA',400)
#
# def player_attack(char):     # same func give different out ...
#     char.attack()
#
# player_attack(wizard1)
# player_attack(archer1)
#
# for char in [wizard1,archer1]:
#     char.attack()                   #  give different out ...
# ....................
# class User():
#     def sign_in(self):
#         print('sign in')
#     def attack(self):
#         print('do nothing')
#
# class Wizard(User):
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         User.attack(self)
#         print(f'attacking with power of self {self.power}')
#
# class Archer(User):
#     def __init__(self,name,num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#     def attack(self):
#         print(f'attacking with arrows:  {self.num_arrows}')
#
# wizard1 = Wizard('AAA',40)
# print(wizard1.attack())

#                .......................................... Exercise .............................................
# class Pets():
#     animals = []
#     def __init__(self, animals):
#         self.animals = animals
#
#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())
#
# class Cat():
#     is_lazy = True
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def walk(self):
#         return f'{self.name} is just walking around'
#
# class Simon(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# class Sally(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
# # 1 Add nother Cat
# class Pussy(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
#
#
# # 2 Create a list of all of the pets (create 3 cat instances from the above)
# my_cats = [Simon('si', 20),Sally('sa', 22),Pussy('ps', 10)]
#
# # 3 Instantiate the Pet class with all your cats use variable my_pets
# my_pets = Pets(my_cats)
#
# # 4 Output all of the cats walking using the my_pets instance
# my_pets.walk()

#                      ................................ super ..................................

# class User():
#     def __init__(self, email):
#         self.email = email
#     def sign_in(self):
#         print('sign in')
#
# class Wizard(User):
#     def __init__(self,name,power,email):
#         # User.__init__(self,email)
#         super().__init__(email)
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(f'attacking with power of self {self.power}')
#
#
# wizard1 = Wizard('AAA',40,'aaa@gmail.com')
# print(wizard1.email)
#
# # print(wizard1.email)               #   wrong answer

#                      ................................ introspection ..................................
# print(dir(wizard1))         #  show all func , attribute which is access


#                      ................................ multiple inh ..................................
#
# class User():
#     def sign_in(self):
#         print('sign in')
#
# class Wizard(User):
#     def __init__(self,name,power):
#         self.name = name
#         self.power = power
#     def attack(self):
#         print(f'attacking with power of self {self.power}')
#
# class Archer(User):
#     def __init__(self,name,num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#     def check_arrows(self):
#         print(f'{self.num_arrows} remaining')
#
#     def run(self):
#         print('run really fast')
#
# class HybridBorg(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self,name, arrows)
#         Wizard.__init__(self,name, power)
#
# hb1 = HybridBorg('aaa', 40, 100)
#
# print(hb1.check_arrows())
# print(hb1.run())
# print(hb1.attack())
# print(hb1.sign_in())


#                      ................................ method resolution order ..................................
# mro check the order of inheritance class...
# print(d.mro())




