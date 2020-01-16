from abc import ABC, abstractmethod

class geometric_figure(ABC):
    @abstractmethod
    def area(self):
        pass