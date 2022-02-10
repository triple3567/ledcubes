import threading
import Shelf as shelf

class EventSequence(threading.Thread):
    def __init__(self):
        # calling parent class constructor
        threading.Thread.__init__(self)
        self.shelf = shelf.Shelf()
        self.red = self.Red()


    def run(self):
        self.shelf.setAll(255,255,255)
        self.shelf.update()

    class Red:

        def __init__(self):
            super().__init__()
        
        def run(self):
            self.shelf.setAll(200, 30, 0)
            self.shelf.update()


    