class Todo:

    COMPLETE = 'X'
    INCOMPLETE = ' '

    def __init__(self, title):
        self._title = title
        self.done = False

    @property
    def title(self):
        return self._title
    
    @property
    def done(self):
        return self._done
    
    @done.setter
    def done(self, value):
        self._done = value

    def __str__(self):
        mark = Todo.COMPLETE if self.done else Todo.INCOMPLETE
        return f'[{mark}] {self.title}'
    
    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        
        return self.title == other.title and self.done == other.done
