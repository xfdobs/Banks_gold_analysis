from random import shuffle, choice

class Player():
    door_selected = None
    door_opened = None
    non_switch_door = None

    def __init__(self):
        self.doors = [0, 1, 0]
        shuffle(self.doors)


    def switch_door(self):
        if self.doors[self.door_selected] == 1:
            return True
        else:
            return False

    def check_switch_door(self):
        if self.doors[self.door_selected] == 1:
            return True
        else:
            return False


    def choose_door(self,door):
        self.door_selected = door


    def check_remaining_door(self):
        remaining_door = set([0, 1, 2]).difference([self.door_selected, self.door_opened])
        remaining_door = remaining_door.pop()
        if self.doors[remaining_door] == 1:
            return True
        else:
            return False

    def open_non_car_doors(self):
        non_car_doors = list()
        for i, d in enumerate(self.doors):
            if d == 0 and i != self.door_selected: non_car_doors.append(i)
        self.door_opened = choice(non_car_doors)


class Game():

    def play_game(self):
        player = Player()
        door_selected = choice([0,1,2])
        player.choose_door(door_selected)
        player.open_non_car_doors()
        non_switch_success =  player.check_switch_door()
        remaining_door = player.check_remaining_door()
        return non_switch_success, remaining_door


    def run_simulation(self,n):
        non_switch_success = 0
        switch_success = 0

        for i in range(n):
            ns, ss = self.play_game()
            non_switch_success += ns
            switch_success += ss

        print(f"Total plays: {n}")
        print(f"Total of success - Switch: {switch_success} - {round( (switch_success / n) * 100 ,2)}%")
        print(f"Total of success - Non-Switch: {non_switch_success} - {round( (non_switch_success / n) * 100,2)}%")



game = Game()
game.run_simulation(500000)










