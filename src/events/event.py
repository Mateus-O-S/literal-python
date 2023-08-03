class Event:
    pass

class EventServer:
    __listeners = {}

    @staticmethod
    def bind(command, type):
        if type not in EventServer.__listeners.keys():
            EventServer.__listeners[type] = []
        EventServer.__listeners[type].append(command)

    @staticmethod
    def pool(event: Event):
        if type(event) not in EventServer.__listeners.keys():
            return
        for l in EventServer.__listeners[type(event)]:
            l(event)