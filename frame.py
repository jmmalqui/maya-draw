import pygame as pg
from ui_manager import UIChild, UIComponent, UIContainer, UIManager


class FrameHandler(UIContainer):
    def __init__(self, manager: UIManager, position: pg.Vector2) -> None:
        super().__init__(manager, position)
        self.position: pg.Vector2 = position
        self.margin = pg.Vector2(10, 0)
        self.frame1 = Frame(self, pg.Vector2(16, 16))
        self.frame2 = Frame(self, pg.Vector2(16, 16))
        self.frame3 = Frame(self, pg.Vector2(16, 16))
        self.frame4 = Frame(self, pg.Vector2(16, 16))
        self.generate_child_rects()

    def generate_child_rects(self):
        for child_id, child in enumerate(self.ui_elements):
            child.absolute_position = self.position + child_id * (
                pg.Vector2(child.size.x, 0) + self.margin
            )
        return super().generate_child_rects()

    def container_update(self):
        for event in self.get_events():
            if event.type == pg.MOUSEWHEEL:
                self.margin.x += event.y
                self.generate_child_rects()

    def container_render(self):
        for index, e in enumerate(self.ui_elements):
            e.render()
            self.display.blit(e.surface, e.absolute_position)


class Frame(UIChild):
    def __init__(self, container: UIContainer, size: pg.Vector2) -> None:
        super().__init__(container, size)
        ...

    def child_update(self):
        for event in self.get_events():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.is_hovered():
                    ...
        return super().child_update()

    def child_render(self):
        self.surface.fill("red")
        return super().child_render()
