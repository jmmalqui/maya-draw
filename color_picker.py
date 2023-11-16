import pygame as pg
from ui_manager import UIComponent, UIManager
from transform import color_picker, color_lerp


class ColorHandler(UIComponent):
    def __init__(
        self,
        manager: UIManager,
        position: pg.Vector2,
        size: pg.Vector2,
        color,
        _color_picker,
        index,
    ) -> None:
        super().__init__(manager, position, size)
        self.color_picker: ColorPicker = _color_picker
        self.color = color
        self.index = index
        self.make_strip()
        self.strip = self.surface.copy()
        self.picked = [0, 0, 0]
        self.y_pick = 98

    def add_to_picker(self, index):
        self.color_picker.base_colors[index] = pg.Vector3(
            self.picked.r, self.picked.g, self.picked.b
        )

    def update(self):
        if pg.mouse.get_pressed(3)[0]:
            if self.is_hovered():
                self.y_pick = (pg.Vector2(pg.mouse.get_pos()) - self.position).y
                self.picked = self.surface.get_at(
                    pg.Vector2(pg.mouse.get_pos()) - self.position
                )
                self.add_to_picker(self.index)
                self.color_picker.remake_surface()

    def make_strip(self):
        colors = []
        for i in range(int(self.size.y) - 2):
            colors.append(color_lerp(self.color, [0, 0, 0], i, self.size.y))
        pg.draw.rect(self.surface, "white", pg.Rect([0, 0], self.size), 0)
        for i, color in enumerate(colors):
            pg.draw.rect(self.surface, color, pg.Rect(1, i + 1, 3, 1), 0)

    def render(self):
        self.surface.blit(self.strip, [0, 0])
        pg.draw.rect(self.surface, "yellow", pg.Rect(1, self.y_pick + 1, 3, 1), 0)
        self.blit_surf()


class ColorShower(UIComponent):
    def __init__(
        self, manager: UIManager, position: pg.Vector2, size: pg.Vector2, color_picker
    ) -> None:
        super().__init__(manager, position, size)
        self.color_picker: ColorPicker = color_picker

    def update(self):
        return super().update()

    def render(self):
        self.surface.fill(self.color_picker.get_color())
        pg.draw.rect(self.surface, "white", pg.Rect([0, 0], self.size), 1)
        self.blit_surf()


class ColorPicker(UIComponent):
    def __init__(
        self, manager: UIManager, position: pg.Vector2, size: pg.Vector2
    ) -> None:
        super().__init__(manager, position, size)
        self.base_colors = [
            pg.Vector3(255, 0, 0),
            pg.Vector3(0, 25, 0),
            pg.Vector3(0, 0, 192),
        ]
        self.color = self.merge_color()

        self.surface = color_picker(self.color, self.size.x, 5)

        self.picked = [255, 0, 0]

    def remake_surface(self):
        self.color = self.merge_color()
        self.surface = color_picker(self.color, self.size.x, 5)

    def merge_color(self):
        _color = [0, 0, 0]
        for color in self.base_colors:
            _color[0] += int(color.x)
            _color[1] += int(color.y)
            _color[2] += int(color.z)
            _color[0] %= 256
            _color[1] %= 256
            _color[2] %= 256
        return _color.copy()

    def get_color(self):
        return self.picked

    def update(self):
        for event in self.get_events():
            if event.type == pg.MOUSEBUTTONDOWN:
                if self.is_hovered():
                    self.picked = self.surface.get_at(
                        pg.Vector2(pg.mouse.get_pos()) - self.position
                    )
                    if self.picked == [255, 255, 255]:
                        self.picked = self.last_picked

    def render(self):
        self.blit_surf()
