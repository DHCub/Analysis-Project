from AuxClasses import *
from numpy import poly1d
from numpy import polydiv
from FunctionData import *
from typing_extensions import Self
from Utils import *
from math import isclose

# (definitionIntervals: list[Interval], 
# discontinuities: list[Discontinuity], 
# XIntercepts: list[Point], 
# YIntercepts: list[Point], 
# isEven: bool, 
# obliqueAsymptotes: list[LinearAsymptote], 
# verticalAsymptotes: list[LinearAsymptote], 
# firstDerivativeStr: str, 
# monotonyIntervals: list[PositivityInterval], 
# localExtremes: list[Extreme], 
# secondDerivativeStr: str, 
# concavityIntervals: list[PositivityInterval], 
# inflectionPoints: list[Point], 
# plotFunction: Any) -> None

def flipPoly(poly: poly1d) -> poly1d:

    evenExp = True
    newCoefs = []
    for i in range(poly.coef.__len__()):
        coef = poly.coef[-i-1]
        if evenExp: newCoefs += [coef]
        else: newCoefs += [-coef]
        evenExp = not evenExp
    newCoefs = list(reversed(newCoefs))
    return poly1d(newCoefs)


class PolyQuotient:
    numPoly: poly1d
    denPoly: poly1d
    numRoots: list[float]
    denRoots: list[float]
    discontinuities: list[Discontinuity]
    roots: list[float]
    parity: bool
    obliqueAsymtote: LinearAsymptote
    verticalAsymptotes: list[LinearAsymptote]
    positivityIntervals: list[PositivityInterval]
    evaluate: callable

    def __init__(self, numPoly: poly1d, denPoly: poly1d) -> None:
        self.numPoly = numPoly
        self.denPoly = denPoly
        self.numRoots = numPoly.roots
        self.denRoots = denPoly.roots
        self.evaluate = lambda x: numPoly(x)/denPoly(x)

        self.discontinuities = []

        #region Getting Discontinuities

        for denRoot in self.denRoots:
            if not isclose(denRoot.imag, 0): continue
            
            lim = self.limit(denRoot)
            if lim is None:
                self.discontinuities += [InfiniteJumpDiscontinuity(denRoot)]
            else:
                self.discontinuities += [AvoidableDiscontinuity(denRoot, lim)]

        #endregion
        #region Getting Roots
        self.roots = []
        for root in self.numRoots:
            if not isclose(root.imag, 0): continue
            if not contains(self.denRoots, root): self.roots += [root]
        
        #endregion
        #region Getting Parity

        if numPoly*flipPoly(denPoly) == flipPoly(numPoly)*denPoly: self.parity = True
        elif numPoly*flipPoly(denPoly) == -flipPoly(numPoly)*denPoly: self.parity = False
        else: self.parity = None

        #endregion
        #region Getting asymptotes

        if self.numPoly.order == 1: self.obliqueAsymtote = None
        elif self.numPoly.order != self.denPoly.order + 1: self.obliqueAsymtote = None
        else:
            quot = polydiv(self.numPoly, self.denPoly)
            a = quot[0].coef[0]
            b = quot[0].coef[1]
            self.obliqueAsymtote = LinearAsymptote(-a, 1, -b)
        
        self.verticalAsymptotes = []
        if not (numPoly.order == 0 and isclose(numPoly.coef[0], 0)):
            for denRoot in filter(lambda x: isclose(x.imag, 0), self.denRoots):
                if contains(self.numRoots, denRoot): continue
                self.verticalAsymptotes += [LinearAsymptote(1, 0, -denRoot)]

        #endregion
        #region Getting Positivity Intervals

        if not (numPoly.order == 0 and isclose(numPoly.coef[0], 0)):
            criticalPoints = self.roots + apply(self.discontinuities, lambda x: x.x)
            criticalPoints = getApproxUnique(criticalPoints)
            criticalPoints.sort()
            
            print(apply(self.discontinuities, lambda x: x.x))

            if criticalPoints.__len__() == 0:
                self.positivityIntervals = [PositivityInterval(
                    Interval.Reals(),
                    self.evaluate(0) > 0
                )]
            else:
                prevCrit = criticalPoints[0]
                self.positivityIntervals = [PositivityInterval(
                    Interval(None, None, prevCrit, False),
                    self.evaluate(prevCrit - 10) > 0
                )]
                
                for crit in criticalPoints[1:]:
                    self.positivityIntervals += [PositivityInterval(
                        Interval(prevCrit, False, crit, False),
                        self.evaluate((prevCrit + crit)/2) > 0
                    )]
                    prevCrit = crit
                
                self.positivityIntervals += [PositivityInterval(
                    Interval(criticalPoints[-1], False, None, None),
                    self.evaluate(criticalPoints[-1] + 10) > 0
                )]

        #endregion


        
    def limit(self, x: float) -> float:
        if (not contains(self.denRoots, x)): return self.numPoly(x)/self.denPoly(x)
    
        if (self.numPoly.order == 0): return 0
        if (not contains(self.numRoots, x)): return None

        lim = 1

        for root in self.numPoly.roots:
            if isclose(x, root): continue
            lim*=(x - root)
        
        for root in self.denPoly.roots:
            if isclose(x, root): continue
            lim/=(x - root)

        lim*= (self.numPoly.coefficients[0]/self.denPoly.coefficients[0])

        return lim  

    def deriv(self) -> Self:
        return PolyQuotient(self.numPoly.deriv()*self.denPoly - self.numPoly*self.denPoly.deriv(), self.denPoly*self.denPoly)

    def __str__(self) -> str:
        return "( {0} )/( {1} )".format(stringifyPoly(self.numPoly), stringifyPoly(self.denPoly))

    def hasDiscontinuityAt(self, x: float) -> bool:
        if not isclose(x.imag, 0): return False
        for disc in self.discontinuities:
            if isclose(disc.x, x): return True
        return False



def PolyDivision(p1: list[float], p2: list[float]) -> FunctionData:
    if all(apply(p2, lambda x: x == 0)): return None
    quotient = PolyQuotient(poly1d(p1), poly1d(p2))

    defIntervals: list[Interval]
    defIntervals = []

    realDenRoots = list(filter(lambda x: isclose(x.imag, 0), quotient.denRoots))

    if (realDenRoots.__len__() == 0):
        defIntervals = [Interval.Reals()]
    else:
        prevRoot = realDenRoots[0]
        defIntervals += [Interval(None, None, prevRoot, False)]
        
        for root in realDenRoots[1:]:
            defIntervals += [Interval(prevRoot, False, root, False)]
            prevRoot = root
        
        defIntervals += [Interval(realDenRoots[-1], False, None, None)]

    XIntercepts: list[Point]
    XIntercepts = []
    for root in quotient.roots:
        XIntercepts += [Point(root, 0)]

    YIntercepts: list[Point]
    if contains(quotient.denRoots, 0): YIntercepts = []
    else: YIntercepts = [Point(0, quotient.limit(0))]

    firstDer = quotient.deriv()
    monotonyIntervals = firstDer.positivityIntervals
    
    localExtremes: list[Extreme]
    localExtremes = []
    for i in range(monotonyIntervals.__len__() - 1):
        if (monotonyIntervals[i].positive == monotonyIntervals[i + 1].positive): continue
        
        x = monotonyIntervals[i].end
        if quotient.hasDiscontinuityAt(x): continue
        
        localExtremes += [Extreme(
            x, quotient.evaluate(x),
            monotonyIntervals[i].positive
        )]
    
    secondDer = firstDer.deriv()
    concavityIntervals = secondDer.positivityIntervals
    inflectionPoints: list[Point]
    inflectionPoints = []
    for i in range(concavityIntervals.__len__() - 1):
        if (concavityIntervals[i].positive == concavityIntervals[i + 1].positive): continue

        x = concavityIntervals[i].end
        if quotient.hasDiscontinuityAt(x): continue

        inflectionPoints += [Point(x, quotient.evaluate(x))]

    return FunctionData(
        defIntervals,
        quotient.discontinuities,
        XIntercepts,
        YIntercepts,
        quotient.parity,
        [] if quotient.obliqueAsymtote == None else [quotient.obliqueAsymtote],
        quotient.verticalAsymptotes,
        firstDer.__str__(),
        monotonyIntervals,
        localExtremes,
        secondDer.__str__(),
        concavityIntervals,
        inflectionPoints,
        quotient.evaluate
    )
    

