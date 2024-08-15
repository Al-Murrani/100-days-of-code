from turtle import Turtle

ALIGN = "center"
FONT = ("Courier ", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highest_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def read_highest_score(self):
        with open("data.txt") as file:
            self.high_score = file.read()
        return int(self.high_score)

    def write_highest_score(self, highest_score):
        with open("data.txt", "w") as file:
            file.write(str(highest_score))
        return self.high_score

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highest_score(self.high_score)
            self.update_scoreboard()
        self.score = 0

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
