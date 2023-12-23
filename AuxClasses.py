INFINITY_STR = float('inf').__str__()

class Interval:
    def Reals(): return Interval(None, None, None, None)

    def __init__(self, start: float, startClosed: bool, end: float, endClosed: bool) -> None:
        self.start = start
        self.startClosed = startClosed
        self.end = end
        self.endClosed = endClosed

    def __str__(self) -> str:
        opener = "(" if (self.start == None or not self.startClosed) else "[" 
        start = INFINITY_STR if self.start == None else self.start.__str__()

        end = INFINITY_STR if self.end == None else self.end.__str__()
        closer = ")" if self.end == None or not self.endClosed else "]"
        
        return "{0}{1}, {2}{3}".format(opener, start, end, closer)

class MonotonyInterval(Interval): 
    def __init__(self, interval: Interval, growing : bool) -> None:
        super().__init__(interval.start, interval.startClosed, interval.end, interval.endClosed)
        self.growing = growing

    def GetAsMonotony(self) -> str:
        grow = "Creciente" if self.growing else "Decreciente"
        
        return grow + " en " + super().__str__()

    def GetAsConvexity(self) -> str:
        grow = "Convexa" if self.growing else "Cóncava"

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
        type = "Máximo" if self.maximum else "Mínimo"

        return type + " local en " + super().__str__()

class LinearAsymptote:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c

    def __str__(self) -> str:
        return "{0}x + {1}y + {2}".format(self.a, self.b, self.c)
