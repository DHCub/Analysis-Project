from AuxClasses import *

class FunctionData:
    def __init__(self, definitionInterval: Interval, 
                 discontinuities: list[Point], 
                 XIntercepts: list[Point], 
                 YIntercepts: list[Point], 
                 isEven: bool,
                 obliqueAsymptotes: list[LinearAsymptote],
                 verticalAsymptotes: list[LinearAsymptote],
                 firstDerivativeStr: str,
                 monotonyIntervals: list[MonotonyInterval],
                 localExtremes: list[Extreme],
                 secondDerivativeStr: str,
                 concavityIntervals: list[MonotonyInterval],
                 inflectionPoints: list[Point],
                 plotFunction: callable
                 ):
        self.definitionInterval = definitionInterval
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