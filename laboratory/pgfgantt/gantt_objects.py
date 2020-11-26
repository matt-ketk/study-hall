import datetime as dt

class Event:
    def __init__(self, preceding, succeeding, name, group):
        self.preceding = preceding
        self.succeeding = succeeding
        
        self.name = name
        self.group = group

class Group:
    def __init__(self, group_name):
        self.events = []
        self.name = group_name
        self.start = None
        self.length = dt.timedelta(days=0)

    def get_end(self):
        return self.start + self.length

    def add_event(self, event):
        if event.group == self.name:
            self.events.append(event)
            if self.start == None or (self.start - event.start).days > 0:
                self.start = event.start

            # check event type first!
            if type(event) == Task:
                if (self.get_end() - event.get_end()).days < 0:
                    self.length = event.get_end() - self.start

class Milestone(Event):
    def __init__(self, preceding, succeeding, name, group, date):
        super().__init__(preceding, succeeding, name, group)
        self.start = date

class Task(Milestone):
    def __init__(self, preceding, succeeding, name, group, date, length):
        super().__init__(preceding, succeeding, name, group, date)
        self.length = length

    def get_end(self):
        return self.length + self.start
