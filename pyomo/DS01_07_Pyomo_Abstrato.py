from pyomo.environ import *

model = AbstractModel()

model.I = Set()
model.J = Set()

model.name = "Knapsack"

model.a = Param(model.I, model.J)
model.b = Param(model.I)
model.custo = Param(model.J)

# the next line declares a variable indexed by the set J

#model.x = Var(model.J, domain=Binary)
model.x = Var(model.J, domain=NonNegativeIntegers)

def obj_expression(model):
    return summation(model.custo, model.x)


model.OBJ = Objective(rule=obj_expression, sense= maximize)


def ax_constraint_rule(model, i):
    # return the expression for the constraint for i
    return sum(model.a[i, j] * model.x[j] for j in model.J) <= model.b[i]


# the next line creates one constraint for each member of the set model.I
model.AxbConstraint = Constraint(model.I, rule=ax_constraint_rule)


# https://pyomo.readthedocs.io/en/stable/pyomo_modeling_components/Sets.html
