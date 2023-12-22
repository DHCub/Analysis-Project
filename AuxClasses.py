INFINITY_STR = float('inf').__str__()

class Interval:
    def Reals(): return Interval(None, None, None, None)

    def __init__(self, start: float, startClosed: bool, end: float, endClosed: bool) -> None:
        self.start = start
        self.startClosed = startClosed
        self.end = end
        self.endClosed = endClosed

    def __str__(self) -> str:
        if (self.start == None or not self.startClosed): opener = "("
        else: opener = "["

        if (self.start == None): start = INFINITY_STR
        else: start = self.start.__str__()

        if (self.end == None): end =  INFINITY_STR
        else: end = self.end.__str__()

        if (self.end == None or not self.endClosed): closer = ")"
        else: closer = "]"
        
        return "{0}{1}, {2}{3}".format(opener, start, end, closer)

class MonotonyInterval(Interval): 
    def __init__(self, interval: Interval, growing : bool) -> None:
        super().__init__(interval.start, interval.startClosed, interval.end, interval.endClosed)
        self.growing = growing

    def GetAsMonotony(self) -> str:
        grow = None
        if (self.growing): grow = "Creciente"
        else: grow = "Decreciente"
        
        return grow + " en " + super().__str__()

    def GetAsConvexity(self) -> str:
        if (self.growing): grow = "Convexa"
        else: grow = "Cóncava"

        return grow + " en " + super().__str__()

class Point:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "({0}, {1})".format(self.x, self.y)

class Extreme(Point):
    def __init__(self, x, y, maximum: bool) -> None:
        super().__init__(x, y)
        self.maximum = maximum

    def __str__(self) -> str:
        if(self.maximum): mx = "Máximo"
        else: mx = "Mínimo"

        return mx + " local en " + super().__str__()

class LinearAsymptote:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return "{0}x + {1}y + {2}".format(self.a, self.b, self.c)
