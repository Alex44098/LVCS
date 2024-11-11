from typing import Callable, TypeVar, Any

Self = TypeVar("Self", bound="EventListener")


class EventListener:
    def __init__(self):
        self.listeners: dict[str, list[Callable[[Any], None]]] = {}

    def add_listener(self, event: str, func: Callable[[Self], None]) -> Callable:
        try:
            self.listeners[event].append(func)
        except:
            self.listeners[event] = [func]

    def trigger_event(self, event):
        if event not in self.listeners.keys():
            return

        for func in self.listeners[event]:
            func()
