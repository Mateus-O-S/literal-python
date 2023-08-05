# development guide
This is a development guide section introducing the events

There are two tipes of events: Events that carry a value and the ones that alert of an action. The naming convenction is that the ones that carry an value should have "{value_name}_event.py" while the ones that alert from an action should have "{action_name}_event.py"

All the events derive the Event class in the event.py and all the operations with events are done through the Event server in the event.py