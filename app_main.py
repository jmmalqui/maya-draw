import pygame as pg
from canvas import Canvas
from color_picker import ColorPicker, ColorShower, ColorHandler
from ui_manager import UIManager
from frame import FrameHandler
import settings


class MayaDraw:
    def __init__(self) -> None:
        pg.init()
        self.display = pg.display.set_mode(settings.SIZE, pg.RESIZABLE | pg.SCALED)
        self.clock = pg.Clock()
        self.ui_manager = UIManager(self)
        self.color_picker = ColorPicker(
            self.ui_manager, pg.Vector2(150, 10), pg.Vector2(50, 50)
        )
        self.color_shower = ColorShower(
            self.ui_manager,
            self.color_picker.position
            + pg.Vector2(0, self.color_picker.size.y)
            + pg.Vector2(0, 2),
            pg.Vector2(self.color_picker.size.x, 5),
            self.color_picker,
        )
        self.color_handler_red = ColorHandler(
            self.ui_manager,
            self.color_picker.position
            + pg.Vector2(self.color_picker.size.x, 0)
            + pg.Vector2(5, 0),
            pg.Vector2(5, 50),
            [255, 0, 0],
            self.color_picker,
            0,
        )
        self.color_handler_green = ColorHandler(
            self.ui_manager,
            self.color_picker.position
            + pg.Vector2(self.color_picker.size.x, 0)
            + pg.Vector2(12, 0),
            pg.Vector2(5, 50),
            [0, 255, 0],
            self.color_picker,
            1,
        )
        self.color_handler_blue = ColorHandler(
            self.ui_manager,
            self.color_picker.position
            + pg.Vector2(self.color_picker.size.x, 0)
            + pg.Vector2(19, 0),
            pg.Vector2(5, 50),
            [0, 0, 255],
            self.color_picker,
            2,
        )
        self.canvas = Canvas(
            self.ui_manager, pg.Vector2(10, 10), pg.Vector2(60, 60), self.color_picker
        )
        self.frame_handler = FrameHandler(self.ui_manager, pg.Vector2(10, 100))
        self.delta_time = 0

    def check_events(self):
        self.ui_manager.pump(None)
        for event in pg.event.get():
            self.ui_manager.pump(event)
            if event.type == pg.QUIT:
                exit()

    def update(self):
        self.ui_manager.update()

    def render(self):
        self.display.fill("black")
        self.ui_manager.render()
        pg.display.update()

    def run(self):
        while self.run:
            self.delta_time = self.clock.tick(60)
            self.check_events()
            self.update()
            self.render()
