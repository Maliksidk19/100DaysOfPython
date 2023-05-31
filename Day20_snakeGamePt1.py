from turtle import Screen
from Files.snakegame_data import Snake, Food, ScoreBoard
import time

def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0) # Turns off animation on screen
 
    snake = Snake()
    food = Food()
    score = ScoreBoard()
        
    screen.listen()

    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")    
        
    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        if snake.segments[0].distance(food) < 15:
            food.refresh()
            snake.extend()
            score.increase_score()
            
        if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
            game_is_on = False
            score.game_over()    
        
    screen.exitonclick()
   
if __name__ == "__main__":
    main()   
    