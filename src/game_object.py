from visual.drawer import Drawer

class GameObject:
    __game_objects = []

    @staticmethod
    def global_setup():
        for obj in GameObject.__game_objects:
            obj.setup()
    
    @staticmethod
    def global_update():
        for obj in GameObject.__game_objects:
            obj.update()
    
    @staticmethod
    def global_render(drawer: Drawer):
        for obj in GameObject.__game_objects:
            obj.render(drawer)
    
    @staticmethod
    def clear_objects():
        GameObject.__game_objects.clear()

    @staticmethod
    def get_type(T):
        on_type = []
        for g in GameObject.__game_objects:
            if type(g) == T:
                on_type.append(g)
        return on_type

    def __init__(self):
        GameObject.__game_objects.append(self)

    def destroy(self):
        if self in self.__game_objects:
            self.__game_objects.remove(self)
            del self

    def setup(self):
        pass
    
    def update(self):
        pass

    def render(self, drawer: Drawer):
        pass