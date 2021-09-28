
class base:
    base_val = 10
    def __init__(self):
        self.noVar = 1012

class dolittle(base):
    def __init__(self, i):
        self.i = i
        self.data = {}
        super().__init__()

    def __repr__(self):
        return "for developer {0}".format(self.i)

    def __str__(self):
        return "for user: {0}".format(self.i)

    def __len__(self):
        return 1
    
    def __setitem__(self, key, value):
        print(key, value)
        self.data[key] = value
    
    def __getitem__(self, key):
        return self.data.get(key, None)
    
    def __delitem__(self, key):
        if key in self.data.keys():
            del(self.data[key])
    
    def __add__(self, value):
        self.i += value
    
    def __iadd__(self, value):
        self.i += value
    
    def __sub__(self, value):
        self.i -= value
    
    def __isub__(self, value):
        self.i -= value
        
d = dolittle(1)
print(d)
print(len(d))

d[1] = 2
print(d[3])
del(d[1])

e = dolittle(2)
e.noVar = 1
print(d.noVar)