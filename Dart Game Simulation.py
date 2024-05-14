import math
import random

class Point:
    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.distance = math.sqrt((coord_x ** 2) + (coord_y ** 2))

        if self.distance <= 1:
            self.score = 100
        elif 1 < self.distance <= 2:
            self.score = 50
        elif 2 < self.distance <= 3:
            self.score = 20
        elif 3 < self.distance <= 4:
            self.score = 10
        else:
            self.score = 0

    def get_score(self):
        return self.score

    def __str__(self):
        return f"({self.coord_x}, {self.coord_y})"

class Player:
    def __init__(self, name, seed=30):
        self.name = name
        self.points = []
        self.seed = seed
        random.seed(self.seed)

    def make_throw(self):
        x = random.randint(-5, 5)
        y = random.randint(-5, 5)
        point = Point(x, y)
        self.points.append(point)
        print(f"{self.name}: The score for a dart throw at position {point} is {point.get_score()}.")

    def get_score(self):
        if not self.points:
            return 0
        new_point = self.points[-1]
        return new_point.get_score()

    def get_total_score(self):
        return sum(point.get_score() for point in self.points)

    def get_name(self):
        return self.name

    def __str__(self):
        result = f"{self.name}'s total score is {self.get_total_score()}.\n"
        for point in self.points:
            result += f"{self.name}: The score for a dart throw at position {point} is {point.get_score()}.\n"
        return result.strip()

class DartGame:
    def __init__(self, seed=30, max_score=51):
        self.seed = seed
        random.seed(seed)
        self.max_score = max_score
        self.rounds = 0
        print("*" * 47)
        print("Welcome to the simplified dart game simulation!")
        print("*" * 47)
        self.get_player_name("player1")
        self.get_player_name("player2")

    def get_player_name(self, player_num):
        while True:
            name = input(f"Enter {player_num} name: ").strip()
            if name:
                break
        if player_num == "player1":
            self.player1 = Player(name, seed = self.seed)
        else:
            self.player2 = Player(name, seed = self.seed)

    def play_game(self):
        print()
        while True:
            self.rounds += 1
            self.player1.make_throw()
            self.player2.make_throw()

            if self.player1.get_total_score() >= self.max_score or self.player2.get_total_score() >= self.max_score:
                break

    def congratulate_player(self):
        score1 = self.player1.get_total_score()
        score2 = self.player2.get_total_score()

        if score1 >= self.max_score and score2 >= self.max_score:
            print("*" * 11)
            print("It's a tie!")
            print("*" * 11)
        elif score1 >= self.max_score:
            print("*" * (32 + len(self.player1.name)))
            print(f"Congratulations! The winner is {self.player1.name}.")
            print("*" * (32 + len(self.player1.name)))
        elif score2 >= self.max_score:
            print("*" * (32 + len(self.player2.name)))
            print(f"Congratulations! The winner is {self.player2.name}.")
            print("*" * (32 + len(self.player2.name)))

        print(f"The number of rounds required is {self.rounds}.")
        print(f"The total score of {self.player1.name} is {score1}.")
        print(f"The total score of {self.player2.name} is {score2}.")
