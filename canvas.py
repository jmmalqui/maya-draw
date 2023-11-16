import pygame as pg
import settings
from ui_manager import UIComponent, UIManager


class Canvas(UIComponent):
    def __init__(
        self, manager: UIManager, position: pg.Vector2, size: pg.Vector2, color_picker
    ) -> None:
        super().__init__(manager, position, size)
        self.surface.fill("white")
        self.color_picker = color_picker

    def update(self):
        for event in self.get_events():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_DELETE:
                    self.surface.fill("white")
        return super().update()

    def render(self):
        if self.is_hovered() and pg.mouse.get_pressed(3)[0]:
            self.surface.set_at(
                pg.Vector2(pg.mouse.get_pos() - self.position),
                self.color_picker.get_color(),
            )
        self.blit_surf()
        return super().render()
