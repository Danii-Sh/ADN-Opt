

import cvxpy as cvx

# Create two scalar optimization variables.
x1 = cvx.Variable()
x2 = cvx.Variable()
x3 = cvx.Variable()

# Create two constraints.
constraints = [x1 + x2 +x3 <= 4,
               x2 + x3 <= 2,
	       x1 <= 2, x2 <=2, x3 <=2,
	       x1 >= 0, x2 >=0, x3 >=0]

# Form objective.
obj = cvx.Maximize(cvx.log(x1)+cvx.log(x2)+cvx.log(x3))

# Form and solve problem.
prob = cvx.Problem(obj, constraints)
prob.solve()  # Returns the optimal value.
print "status:", prob.status
print "optimal value", prob.value
print "optimal var", x1.value, x2.value, x3.value
