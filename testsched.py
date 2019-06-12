#!/usr/bin/python

# Copyright 2019, Gurobi Optimization, LLC

# Assign workers to shifts; each worker may or may not be available on a
# particular day. If the problem cannot be solved, use IIS to find a set of
# conflicting constraints. Note that there may be additional conflicts besides
# what is reported via IIS.

from gurobipy import *

# Number of workers required for each shift
shifts, shiftRequirements = multidict({
  "T1":  2,
  "T2":  2 })

# Amount each worker is paid to work one shift
workers, pay = multidict({
  "Amy":   1,
  "Bob":   2 })

# Worker availability
availability = tuplelist([
('Amy', 'T2'), ('Bob', 'T1'), ('Amy', 'T1')])

# Model
m = Model("assignment")

# Assignment variables: x[w,s] == 1 if worker w is assigned to shift s.
# Since an assignment model always produces integer solutions, we use
# continuous variables and solve as an LP.
x = m.addVars(availability, ub=1, name="x")

# The objective is to minimize the total pay costs
m.setObjective(quicksum(pay[w]*x[w,s] for w,s in availability), GRB.MAXIMIZE)

# Constraints: assign exactly shiftRequirements[s] workers to each shift s
reqCts = m.addConstrs((x.sum('*', s) <= shiftRequirements[s]
                      for s in shifts), "_")

# Using Python looping constructs, the preceding statement would be...
#
# reqCts = {}
# for s in shifts:
#   reqCts[s] = m.addConstr(
#        quicksum(x[w,s] for w,s in availability.select('*', s)) ==
#        shiftRequirements[s], s)

# Save model
m.write('workforce1.lp')

# Optimize
m.optimize()
status = m.status
for i in x:
  if x[i].x == 1:
    n = x[i].varName[1::].strip("[").strip("]").split(",")
    print(n[0], n[1])
if status == GRB.Status.UNBOUNDED:
    print('The model cannot be solved because it is unbounded')
    exit(0)
if status == GRB.Status.OPTIMAL:
    print('The optimal objective is %g' % m.objVal)
    exit(0)
if status != GRB.Status.INF_OR_UNBD and status != GRB.Status.INFEASIBLE:
    print('Optimization was stopped with status %d' % status)
    exit(0)

# do IIS
print('The model is infeasible; computing IIS')
m.computeIIS()
if m.IISMinimal:
  print('IIS is minimal\n')
else:
  print('IIS is not minimal\n')
print('\nThe following constraint(s) cannot be satisfied:')
for c in m.getConstrs():
    if c.IISConstr:
        print('%s' % c.constrName)
