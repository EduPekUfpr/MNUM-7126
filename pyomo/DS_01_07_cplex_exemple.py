from cplex import Cplex
from cplex.exceptions import CplexError

try:
    # Create an instance of the CPLEX problem
    problem = Cplex()

    # Set the problem type to LP
    problem.set_problem_type(Cplex.problem_type.LP)

    # Define the objective function coefficients (cost of transportation)
    # Maximize: 2*I1 + 3*I2 + 1*I3 + 4*I4 + 1*I5 + 1*I6    
    
    problem.objective.set_sense(problem.objective.sense.maximize)
    cost = [2, 3, 1, 4, 1, 1]
    
    var_names = ["I1", "I2", "I3", "I4", "I5", "I6"]
    #var_types = [problem.variables.type.integer] * len(var_names)
    var_types = [problem.variables.type.binary] * len(var_names)
    problem.variables.add(obj=cost, names=var_names, types=var_types)

    # Define the constraints
    # Capacity constraints
    capacity_coefficients = [
        [["I1", "I2", "I3", "I4", "I5", "I6"], [1, 2, 3, 1, 3, 0]],
        [["I1", "I2", "I3", "I4", "I5", "I6"], [0, 1, 2, 1, 0, 1]]
    ]
    supply_rhs = [8, 3]
    supply_senses = ["L", "L"]
    problem.linear_constraints.add(lin_expr=capacity_coefficients, 
    							   senses=supply_senses, rhs=supply_rhs)

    # Solve the problem
    problem.solve()

    # Print the results
    print("Solution status:", problem.solution.get_status())
    print("Solution value:", problem.solution.get_objective_value())
    solution_values = problem.solution.get_values()
    for var_name, val in zip(problem.variables.get_names(), solution_values):
        print(f"{var_name}: {val}")

except CplexError as exc:
    print(exc)