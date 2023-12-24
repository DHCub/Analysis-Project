from AuxClasses import *

class FunctionData:
    definitionIntervals: list[Interval]
    discontinuities: list[Discontinuity] 
    XIntercepts: list[Point]
    YIntercepts: list[Point] 
    isEven: bool
    obliqueAsymptotes: list[LinearAsymptote]
    verticalAsymptotes: list[LinearAsymptote]
    firstDerivativeStr: str
    monotonyIntervals: list[PositivityInterval]
    localExtremes: list[Extreme]
    secondDerivativeStr: str
    concavityIntervals: list[PositivityInterval]
    inflectionPoints: list[Point]


    def __init__(self, definitionIntervals: list[Interval], 
                 discontinuities: list[Discontinuity], 
                 XIntercepts: list[Point], 
                 YIntercepts: list[Point], 
                 isEven: bool,
                 obliqueAsymptotes: list[LinearAsymptote],
                 verticalAsymptotes: list[LinearAsymptote],
                 firstDerivativeStr: str,
                 monotonyIntervals: list[PositivityInterval],
                 localExtremes: list[Extreme],
                 secondDerivativeStr: str,
                 concavityIntervals: list[PositivityInterval],
                 inflectionPoints: list[Point],
                 plotFunction: callable
                 ):
        self.definitionIntervals = definitionIntervals
        self.discontinuities = discontinuities
        self.XIntercepts = XIntercepts
        self.YIntercepts = YIntercepts
        self.isEven = isEven
        self.obliqueAsymptotes = obliqueAsymptotes
        self.verticalAsymptotes = verticalAsymptotes
        self.firstDerivativeStr = firstDerivativeStr
        self.secondDerivativeStr = secondDerivativeStr
        self.monotonyIntervals = monotonyIntervals
        self.localExtremes = localExtremes
        self.concavityIntervals = concavityIntervals
        self.inflectionPoints = inflectionPoints
        self.plotFunction = plotFunction

    def evaluate(self, x): return self.plotFunction(x)