import pygame as pg
import settings


class UIFont:
    def __init__(self) -> None:
        self.font_name = settings.FONTNAME
        self.font_list = pg.font.get_fonts()
        self.font_big = pg.font.Font(self.font_name, 12)
        self.font_normal = pg.font.Font(self.font_name, 10)


class UIManager:
    def __init__(self, app) -> None:
        self.app = app
        self.ui_font = UIFont()
        self.ui_events = []
        self.ui_elements = []
        self.ui_containers = []

    def pump(self, event):
        if event:
            self.ui_events.append(event)
        else:
            self.ui_events.clear()

    def update(self):
        for e in self.ui_elements:
            e.update()
        for e in self.ui_containers:
            e.update()

    def render(self):
        for e in self.ui_elements:
            e.render()
        for e in self.ui_containers:
            e.render()


class UIContainer:
    def __init__(self, manager: UIManager, position: pg.Vector2) -> None:
        self.position = position
        self.manager = manager
        self.manager.ui_containers.append(self)
        self.display: pg.Surface = self.manager.app.display
        self.ui_elements: list[UIChild] = []

    def get_events(self):
        return self.manager.ui_events

    def generate_child_rects(self):
        ...

    def container_update(self):
        ...

    def container_render(self):
        ...

    def update(self):
        self.container_update()
        for e in self.ui_elements:
            e.update()

    def render(self):
        for e in self.ui_elements:
            e.render()
        self.container_render()


class UIChild:
    def __init__(self, container: UIContainer, size: pg.Vector2) -> None:
        self.container = container
        self.container.ui_elements.append(self)
        self.size = size
        self.surface = pg.Surface(size)
        self.absolute_position = self.container.position
        self.rect = pg.Rect(self.absolute_position, self.size)

    def is_hovered(self):
        return self.rect.collidepoint(pg.mouse.get_pos())

    def get_events(self):
        return self.container.get_events()

    def update_rect(self):
        self.rect = pg.Rect(self.absolute_position, self.size)

    def child_update(self):
        ...

    def child_render(self):
        ...

    def update(self):
        self.update_rect()
        self.child_update()

    def render(self):
        self.child_render()


class UIComponent:
    def __init__(
        self, manager: UIManager, position: pg.Vector2, size: pg.Vector2
    ) -> None:
        self.position = position
        self.size = size
        self.surface = pg.Surface(self.size)
        self.rect = pg.Rect(self.position, self.size)
        self.manager = manager
        self.manager.ui_elements.append(self)
        self.display = self.manager.app.display

    def is_hovered(self):
        return self.rect.collidepoint(pg.mouse.get_pos())

    def blit_surf(self):
        self.display.blit(self.surface, self.position)

    def update(self):
        ...

    def render(self):
        ...

    def get_events(self):
        return self.manager.ui_events
