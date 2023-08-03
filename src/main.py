from scenes.main_scene.main_scene import MainScene

gameapp = MainScene()

gameapp.setup()

while True:
    gameapp.update()