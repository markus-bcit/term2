class Countdown:
    def __init__(self, start, step=1):
        self.current = start
        self.step = step
        
        if self.current <= 0:
            self.complete = True
        else:
            self.complete = False
        
    def down(self):
        self.current -= self.step
    
    @property
    def complete(self):
        if self.current <= 0:
            return True
        else:
            return False
    
    @property
    def not_complete(self):
        return not self.complete