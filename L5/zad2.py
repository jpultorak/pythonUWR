from itertools import product

class Formula:
    def __add__(self, f2):
        return Or(self, f2)
    def __mul__(self, f2):
        return And(self, f2) 
    
    def tautology(self):
        if self.is_tautology is not None:
            return self.is_tautology
        
        for vals in product((0, 1), repeat=len(self.vars)):
            if not self.eval(dict(zip(self.vars, vals))):  
                self.is_tautology = False
                return False
        self.is_tautology = True
        return True

class BinOp(Formula):
    def __init__(self, f1, f2):
        self.f1 = f1
        self.f2 = f2
        self.vars = f1.vars + f2.vars
        self.is_tautology = None

    def __str__(self):
        return f"({str(self.f1)} {self.op} {str(self.f2)})" 

class Impl(BinOp):
    def eval(self, vars):
        if self.f1.eval(vars):
            return True
        else: 
            return self.f2.eval(vars)
            
    def __str__(self):
        return f"({str(self.f1)} → {str(self.f2)})" 
 
class Or(BinOp):
    op = '∨'
    def eval(self, vars):
        if self.f1.eval(vars):
            return True
        else: 
            return self.f2.eval(vars)

class And(BinOp):
    op = '∧'
    def eval(self, vars):
        if not self.f1.eval(vars):
            return False
        else: 
            return self.f2.eval(vars)

class Not(Formula):

    def __init__(self, f1):
        self.f1 = f1
        self.vars = f1.vars
        self.is_tautology = None

    def eval(self, vars):
        return not self.f1.eval(vars)

    def __str__(self):
        return "¬" + str(self.f1)

class Var(Formula):
    def __init__(self, name):
        self.vars = [name]
        self.is_tautology = False

    def eval(self, vars):
        return vars[self.vars[0]]

    def __str__(self):
        return self.vars[0]

class Const(Formula):
    def __init__(self, val):
        self.val = val
        self.vars = []
        self.is_tautology = True if val else False

    def eval(self, vars):
        return self.val

    def __str__(self):
        if self.val:
            return '⊤'
        return '⊥'

x = Impl(Const(True), Const(False))
y = Or(Not(Var("x")), And(Var("y"), Const(True)))

t1 = Or(Not(Var('x')), Var('x'))
print(t1)
print(t1.tautology())

# does not calculate for the second time
print(t1.tautology())
