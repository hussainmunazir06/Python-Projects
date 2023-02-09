import turtle

class Snake:
    def __init__(self):
        self.all_turtles = []
        self.x_axis = 0
        self.create_snake()
    def create_snake(self):
        for turtles in range(3):
            self.tom = turtle.Turtle(shape="circle")
            self.tom.color("white")
            self.tom.penup()
            self.tom.goto((self.x_axis, 0))
            self.all_turtles.append(self.tom)
            self.x_axis -= 20

    def move(self):
        for turtles in range(len(self.all_turtles)-1, 0, -1):
            new_x = self.all_turtles[turtles-1].xcor()
            new_y = self.all_turtles[turtles-1].ycor()
            self.all_turtles[turtles].goto(new_x, new_y)
        self.all_turtles[0].forward(20)

    
    def add_tail(self):
        self.tom = turtle.Turtle(shape="circle")
        self.all_turtles.append(self.tom)
        self.tom.penup()
        self.tom.color("white")
        self.tom.speed("fastest")

    def forward_move(self):
        if self.all_turtles[0].heading() == 180.0:
            self.all_turtles[0].right(90)
        elif self.all_turtles[0].heading() == 90.0 or self.all_turtles[0].heading() == 270.0:
            # all_turtles[0].forward(1)
            None
        else:
            self.all_turtles[0].left(90)
        self.all_turtles[0].forward(1)

    def left_move(self):
        if self.all_turtles[0].heading() == 270.0:
            self.all_turtles[0].right(90)
        elif self.all_turtles[0].heading() == 180.0 or self.all_turtles[0].heading() == 0.0:
            self.all_turtles[0].forward(1)
        else:
            self.all_turtles[0].left(90)

    def right_move(self):
        if self.all_turtles[0].heading() == 270.0:
            self.all_turtles[0].left(90)
        elif self.all_turtles[0].heading() == 0.0 or self.all_turtles[0].heading() == 180.0:
            self.all_turtles[0].forward(1)
        else:
            self.all_turtles[0].right(90)

    def down_move(self):
        if self.all_turtles[0].heading() == 180.0:
            self.all_turtles[0].left(90)
        elif self.all_turtles[0].heading() == 90.0 or self.all_turtles[0].heading() == 270.0:
            self.all_turtles[0].forward(1)

        else:
            self.all_turtles[0].right(90)
        self.all_turtles[0].forward(1)

        