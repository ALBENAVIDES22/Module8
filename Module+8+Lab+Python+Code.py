#Alberto Benavides
#11-23-2021
#Choosing options during the game and creating it 


class character:
    def __init__(self, nickname, weapons, weaknesses):
        self.nickname = nickname
        self.weapons = weapons
        self.weaknesses = weaknesses

    def get_nickname(self):
        return self.nickname

    def get_weapons(self):
        return self.weapons

    def get_weaknesses(self):
        return self.weaknesses

    def profile(self):
        return self.nickname +' ', self.weapons +' ', self.weaknesses

    def check_equipment(self, taskL, state):
        missing_item = []
        for item in range(len(taskL)):
            if taskL[item] not in self.weapons:
                missing_item.append(taskL[item])
                print('{} is not ready' .format(taskL[item]))
        if len(missing_item) == 0:
            print("confirmed all items are prepared")

        if state in self.weaknesses:
            print("Player status is {}, which is not allowed condition".format(state))
        else:
            print('Player is good condition')


player1 = character('','','')
player1.nickname = 'Dragon Slayer'
player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
player1.weaknesses = ['slow']

for item in player1.weapons:
    print("Item: ", item)

for debuff in player1.weaknesses:
    print("Debuff: ", debuff)

#display the option name
print("There are three task you can choose.")
print("Task1 - CLimb a mountain")
print("Task2 - Cooks a seal")
print("Task3 - write a book")

option = input("please enter one of the following option (1-3)")
#option 1
if option == '1':
    task =['rope', 'coat', 'first aid kits']
    not_allowed_state = 'slow'

#option 2
if option == '2':
    task = ['pan', 'groceries']
    not_allowed_state = 'small'

#option 3
if option == '3':
    task = ['pen', 'paper']
    not_allowed_state = 'confusion'


#call check_equipment and weakness
player1.check_equipment(task,not_allowed_state)
