from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
    
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as file:
            self.highest_score = int(file.read())
        self.hideturtle()
        self.penup()
        self.color("#884AB5")
        self.goto(0, 260)
        self.write(f"Score: {self.score}  Highest Score: {self.highest_score}", align="center", font=("Arial", 24, "normal"))
    

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}  Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)
    

    def is_hit_score(self): # edit it later.
        if self.highest_score < self.score:
            with open("highest_score.txt", "w") as file:
                file.write(str(self.score))
            return True
        return False

    def game_over(self):
        self.goto(0, 0)
        if self.is_hit_score():
            self.write(f"You hit the highest score 🥳\nNew highest score: {self.score}", align=ALIGNMENT, font=FONT)
        else:
            self.write(f"Game Over", align=ALIGNMENT, font=FONT)