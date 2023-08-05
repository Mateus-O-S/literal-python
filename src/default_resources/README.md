# development guide

This is the development guide section for introducing the default resources

The default resources folder in the project contains all the resources used by more than one scene and are not specific for the scenes content. The visual folder contains the drawer(render) class, the window class, and the visual class that wraps both and is used as parameter to other classes

There are two default resources in this project: input_server and window_closing_handler. Both handle window events. The input server handles keyboard inputs coming from the window event, if there is some key event on it, it will be thrown to the rest of the componets as a KeyBoardEvent. The window closing handler will check if there is a request to close the window; And if there is, it will exit the program.