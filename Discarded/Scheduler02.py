# Imports------------------------------------
from gurobipy import GRB,Model
import pprint, csv

#===================
#==== clean csv ====
#===================


members = []
with open('DummyApplicationResponses_preclean.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    headers = next(reader, None)
    avg_year = 0
    for row in reader:


        #make dict of preferences *****be sure to change number of projects, no projects = 2nd number in 2nd param of range
        proj_pref = {}
        for proj in range(20, 20+9):
            if 'VERY' in row[proj]:
                proj_pref[headers[proj]] = 3
            elif 'Interested' in row[proj]:
                proj_pref[headers[proj]] = 2
            elif 'Mildly' in row[proj]:
                proj_pref[headers[proj]] = 1

        #make year numeric
        if 'First' in row[9]:
            temp_year = 1
        elif 'Second' in row[9]:
            temp_year = 2
        elif 'Third' in row[9]:
            temp_year = 3
        elif 'Fourth' in row[9]:
            temp_year = 4
        else:
            temp_year = 5

        #add year to total years
        avg_year+=temp_year

        #add member to list of dictionaries of all members
        members.append({
            'name':row[2].encode('ascii', 'ignore'),
            'year':temp_year,
            'projects':proj_pref
            })
#pprint.pprint(members[0])
#solve for average year among all members
avg_year = round(avg_year/len(members),4)

# Create the model------------------------------------
m = Model('EI')

# Set parameters
m.setParam('OutputFlag',True)

# Add variables------------------------------------

#make list of teams (removing spaces)
team_list = []
for p in members[0]['projects'].keys():
    team_list.append(str(p).replace(" ",""))

#make list of members
member_list = []
for mem in members:
    #print(str(mem['name']).replace(" ","").strip('b')) #list of names
    member_list.append(str(mem['name']).replace(" ","").strip('b').strip("'"))



#=============================
#==== optimization script ====
#=============================

from gurobipy import *

# Number of workers required for each shift
projects = ["T1","T2"]
recs = [2,2]

proj_requirements = {}
for i in range(0,len(projects)):
    proj_requirements[projects[i]] = recs[i]

# Amount each worker is paid to work one shift # need to associate with a team
workers, pay = multidict({
  "Amy":   1,
  "Bob":   2 })

# Worker availability
availability = tuplelist([('Amy', 'T2'), ('Bob', 'T1'), ('Amy', 'T1')])

# Model
m = Model("assignment")

# Assignment variables: x[w,s] == 1 if worker w is assigned to shift s.
# Since an assignment model always produces integer solutions, we use
# continuous variables and solve as an LP.
x = m.addVars(availability, ub=1, name="x")

# The objective is to minimize the total pay costs
m.setObjective(quicksum(pay[w]*x[w,s] for w,s in availability), GRB.MAXIMIZE)

# Constraints: assign exactly shiftRequirements[s] workers to each shift s
reqCts = m.addConstrs((x.sum('*', s) <= proj_requirements[s] for s in proj_requirements.keys()), "_")

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
