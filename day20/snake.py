from turtle import Turtle

START_POSITION = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN =270
LEFT = 180
RIGHT = 0


class Snake():
    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]

    def createsnake(self):
        for position in START_POSITION:
            self.add_segments(position)

    def add_segments(self,position):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(position)
        self.segments.append(tim)

    def extend(self):
        self.add_segments(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            seg_x = self.segments[seg_num - 1].xcor()
            seg_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(seg_x, seg_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
