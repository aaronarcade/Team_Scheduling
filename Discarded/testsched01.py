from gurobipy import *

# Create model
m = Model("assignment")

#Add variables
w1 = m.addVar(name='w1')
w2 = m.addVar(name='w2')
w3 = m.addVar(name='w3')
w4 = m.addVar(name='w4')

t1=m.addVar(name='t1')
t2=m.addVar(name='t2')

# Add constraints
m.addConstr(w1<=1, name='p1')
m.addConstr(w2<=1, name='p2')
m.addConstr(w3<=1, name='p3')
m.addConstr(w4<=1, name='p4')

m.addConstr(w4<=1, name='p4')

# Number of workers required for each shift
shifts, shiftRequirements = multidict({
  "T1":  2,
  "T2":  2 })

# Amount each worker is paid to work one shift
workers, pay = multidict({
    "Amy":   1,
    "Bob":   2,
    "Cat":   3,
    "Dan":   1 })

# Worker availability
availability = tuplelist([
('Amy', 'T2'), ('Bob', 'T1'), ('Amy', 'T1'), ('Cat', 'T2')])

# Assignment variables: x[w,s] == 1 if worker w is assigned to shift s.
# Since an assignment model always produces integer solutions, we use
# continuous variables and solve as an LP.
x = m.addVars(availability, ub=1, name="x")

# The objective is to minimize the total pay costs
m.setObjective(quicksum(pay[w]*x[w,s] for w,s in availability), GRB.MAXIMIZE)

# Constraints: assign exactly shiftRequirements[s] workers to each shift s
reqCts = m.addConstrs((x.sum('*', s) <= shiftRequirements[s]
                      for s in shifts), "_")

# Save model
m.write('workforce1.lp')

# Optimize
m.optimize()
status = m.status
for i in x:
    #print(i)
    if x[i].x == 1:
        n = x[i].varName[1::].strip("[").strip("]").split(",")
        print(n[0], n[1])
