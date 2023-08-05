# Snake
This is a little project that copies the classic snake game. This project is made up in python.

## development guide
The project uses terinology inspired by Unity (e.g, game object) and ECS (e.g, resources, entities). The resources in this project mean "managers", a component responsable for a part of the project. The entities are responsable for itself and have solid presence in the game (e.g, the snake class is a component that is rendered in the screen and is only responsable for itself).

The default resources folder in the project contains all the resources used by more than one scene and are not specific for the scenes content. The visual folder contains the drawer(render) class, the window class, and the visual class that wraps both and is used as parameter to other classes

This project uses a event system to decouple the parts of the project. This event system and its components are present in the events folder. Each class deriving the Event class is a event and can be received by its listeners

The project's sections are divided by scenes. Every scene derives from the scene class and is responsable for managing it's entities and resources.

The game adds to concepts to the original snake game: The snake goes faster as it grows and the map grows when the snake grows.