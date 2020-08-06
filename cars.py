class car:
    def __init__(self, diesel, color, age):
        self.diesel = diesel
        self.color = color
        self.age = age
    def __init_subclass__(cls, electric, color, age):
        cls.electric = electric
        cls.blue = color
        cls.six = age

