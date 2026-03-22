from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (NumericProperty , ReferenceListProperty, ObjectProperty, ColorProperty)
from kivy.vector import Vector
from random import randint
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.core.audio import SoundLoader




class Ball(Widget):
    color = ColorProperty((1,1,1,1)) #set to white for now



    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)


    velocity = ReferenceListProperty(velocity_x, velocity_y) #This makes it easier to control the ball as the x and y axis vel can be called together


    #move function will move the ball one step and this will be called in equal interbvals to animate the ball 

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos





class Paddle(Widget): 
    score = NumericProperty(0)
    color = ColorProperty((1, 1, 1, 1)) #For now the color is set to white


    def bounce_ball(self, ball):  # self refers to current object instance and ball is another parameter passed
        if self.collide_widget(ball):    #collide_wid is a built in kivy method
            vx, vy = ball.velocity 
            offset = (ball.center_y-self.center)/(self.height/2)
            bounced = Vector(-1*vx,vy)
            vel = bounced * 1.20
            ball.velocity = vel.x, vel.y + offset
            





class BrickGame(Widget):
    ball = ObjectProperty(None) # ball = ObjectProperty(None) creates a reference to the ball object.ObjectProperty is a Kivy property 
                                #used to link widgets together None means it starts empty until assigned later ususally from a .kv file.
                                #once linked you can access it as self.ball inside the class

    player = ObjectProperty(None)
    color = ColorProperty((1,1,1,1)) # white



    def serve_ball(self, vel=(4,0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        #This function moves the ball, dt is delta time passed by kivy clock and updates game
        #dt is not a built in python method and is just a parameter name, in kivy it is automatically passed by Clock.schedule_interval() 
        #it represents delta time = time sinxe laste framce in seconds 



        self.ball.move()


    #Bounce off paddle

        self.player.bounce_ball(self.ball)


        #bounce off top and bottom of the screen logic. Will be updated later!!

        if (self.ball.y < 0) or (self.ball.top > self.height): #height is the top of the window and top is the top of the ball widget
            self.ball.velocity_y *= -1

        #bounce of top and bottom, This part will be updated later!!

        if (self.ball.x < self.x) or (self.ball.right > self.width):
            self.ball.velocity_x *= -1




class BrickApp(App):



    def build(self):
        game = BrickGame()
        game.serve_ball()




        #This is where the game updated regularly using kivy built in clock. (Need to know more!)

        Clock.schedule_interval(game.update, 1.0/60.0)


        return game
    

if __name__ == "__main__":

    BrickApp().run()


        











