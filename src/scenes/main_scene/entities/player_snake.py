from scenes.main_scene.entities.snake import Snake
from scenes.main_scene.resources.growth_function import growth
from events.keyboard_event import KeyBoardEvent
from events.event import EventServer
from events.snake_coord_event import SnakeCoordEvent
from events.keyboard_event import KeyBoardEvent
from events.snake_body_event import SnakeBodyEvent
from events.snake_size_event import SnakeSizeEvent
from events.destroy_enemy_part_event import DestroyEnemyPartEvent
import pygame

class PlayerSnake(Snake):
    def __init__(self):
        super().__init__()
        self.color = (229, 180, 2)
        self.inputThreatement = _Snake_InputThreatement(self)
    
    def setup(self):
        super().setup()
        EventServer.bind(self.inputThreatement.threat, KeyBoardEvent)
        EventServer.bind(self.speed_up, SnakeSizeEvent)
        EventServer.bind(self.grow, DestroyEnemyPartEvent)



    def speed_up(self, event: SnakeSizeEvent):
        self.speed = 10 + growth(event.size, 55, 20)

    def update(self):
        super().update()
        EventServer.pool(SnakeCoordEvent(self.body[0][0], self.body[0][1]))
        EventServer.pool(SnakeSizeEvent(len(self.body)))
        EventServer.pool(SnakeBodyEvent(self.body))


class _Snake_InputThreatement:
    def __init__(self, snake: Snake) -> None:
        self.snake = snake

    def threat(self, event: KeyBoardEvent):
        self.snake.input = [0, 0]
        if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
            self.snake.input[0] = 1

        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
            self.snake.input[0] = -1
        
        if event.key == pygame.K_w or event.key == pygame.K_UP:
            self.snake.input[1] = -1
        
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
            self.snake.input[1] = 1