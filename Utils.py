from numpy import poly1d

def stringifyPoly(poly: poly1d) -> str:
    if (poly.order == 0): return poly.coef[0].__str__()
    answ = ""
    answ += "{0}x^{1}".format(poly.coef[0], poly.order)
    orderCtr = poly.order - 1
    for coef in poly.coef[1:]:
        
        if coef == 0:
            orderCtr -= 1
            continue
        elif (coef < 0): answ += " - "
        else: answ += " + "
        
        if orderCtr == 1: answ += "{0}x".format(abs(coef))
        elif orderCtr != 0: answ += "{0}x^{1}".format(abs(coef), orderCtr)
        else: answ += abs(coef).__str__()
        
        orderCtr -= 1
    return answ

def apply(collection: list, func: callable) -> list:
    answ = []
    for item in collection:
        answ += [func(item)]
    return answ