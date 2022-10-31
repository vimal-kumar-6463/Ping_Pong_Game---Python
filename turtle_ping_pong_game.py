from cmath import pi
from turtle import Turtle , Screen 
import time
import math
import random

S = Screen()
S.setup(height = 600 , width = 600)
S.tracer(0)
S.bgcolor("black")


class Board :
    def __init__(self,init_pos) :
        self.init_pos = init_pos
        self.segments = []
        for i in range(4):
            T = Turtle(shape = 'square')
            T.color('white')
            T.penup()
            T.goto(self.init_pos[i][0],self.init_pos[i][1])
            self.segments.append(T)
        S.update()
         
    def move_up(self):
        for i in self.segments:
            i.goto(i.pos()[0],i.pos()[1]+10)  
        S.update()      
    
    def move_down(self):
        for i in self.segments:
            i.goto(i.pos()[0],i.pos()[1]-10)        
        S.update()    
        
class ScoreBoard(Turtle) :
    def __init__(self):
        super().__init__()               
        self.color('yellow')
        self.penup()
        self.goto(0,260)
        self.pendown()
        self.hideturtle()   
        S.update()
        
class Line(Turtle) :
    def __init__(self):
        super().__init__()
        self.color("white")
        self.left(90)
        self.forward(200)
        self.backward(400)
        self.hideturtle()  
        S.update()      
        
class Ball(Turtle) :
    def __init__(self):
        super().__init__()
        self.init_angle = 25
        self.color("red")
        self.shape('circle')
        self.shapesize(stretch_len=0.7,stretch_wid=0.7)
        self.penup()
        S.update()   
        
                
            
class PingPong :
    def __init__(self):
        self.initial_positions1 = [(-260,-260),(-260,-240),(-260,-220),(-260,-200)]
        self.initial_positions2 = [(260,-260),(260,-240),(260,-220),(260,-200)]
        self.score = 0
        self.board1 = Board(self.initial_positions1)
        self.board2 = Board(self.initial_positions2)
        self.scoreboard = ScoreBoard()
        self.display_score()
        self.line = Line()
        self.ball = Ball()
        self.ball.left(self.ball.init_angle)
        self.game_status = True
        self.motion_dir = ('right','up')
        self.new_x = random.choice([8,-8,5,-5,6,-6,7,-7,9,-9])
        self.new_y = random.choice([8,-8,5,-5,6,-6,7,-7,9,-9])
    
    def display_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(arg = f"SCORE : {self.score}",font=('impact',20),align="center")
        return True
    
    def set_listener(self):
        S.listen()
        S.onkeypress(key = 'o' , fun = self.start)
        S.onkeypress(key = 'p' , fun = self.stop)
        S.onkeypress(key = 'w' , fun = self.board1.move_up)
        S.onkeypress(key = 's' , fun = self.board1.move_down)
        S.onkeypress(key = 'Up' , fun = self.board2.move_up)
        S.onkeypress(key = 'Down' , fun = self.board2.move_down)
            
        
    def dist_btw(self,t1,t2) :
        return ((t1.pos()[0]-t2.pos()[0])**2)+((t1.pos()[1]-t2.pos()[1])**2)**1/2
    
    def move(self):
        while self.game_status :
            self.is_out_of_boundary()
            self.is_collided()
            self.ball.speed(10)
            self.ball.goto(self.ball.pos()[0]+self.new_x,self.ball.pos()[1]+self.new_y)
            self.display_score()
            S.update()
            time.sleep(0.05)   
    
    def start(self):
        self.game_status = True
        self.move()
        
    def stop(self):
        self.game_status = False    
        
    def is_collided(self):
        
        
        for i in self.board1.segments :
            if self.dist_btw(self.ball,i) < 50 :
                self.score += 1
                print("collied")
                self.new_x = random.choice([8,5,6,7,9])
    
        
        for i in self.board2.segments :
            if self.dist_btw(self.ball,i) < 30 :
                self.score += 1
                print("collied")
                self.new_x = random.choice([-8,-5,-6,-7,-9]) 
      
                
        position = self.ball.pos()
        if position[1] >= 260 :
                print("collied")
                self.new_y = random.choice([-8,-5,-6,-7,-9]) 

        if position[1] <= -260 :
                print('collied')
                self.new_y = random.choice([8,5,6,7,9])
                
         
            
    def is_out_of_boundary(self):
        position = self.ball.pos()
        if position[0] >= 300 or position[0] <= -300  :
            self.game_status = False
            print(f"you have lost and your score is {self.score}")
            S.bye()   
        
        
    
        
game = PingPong()
game.set_listener()
















S.exitonclick()            