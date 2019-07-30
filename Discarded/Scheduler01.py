# Imports------------------------------------
from gurobipy import GRB,Model
import pprint, csv


# clean csv


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
    member_list.append(str(mem['name']).replace(" ","").strip('b'))

#addvars teams and members in list vars
team_v = m.addVars(team_list, vtype=GRB.CONTINUOUS,lb = -999, name="teamvars")
members_v = m.addVars(member_list, vtype=GRB.BINARY, name="membervars")

# Add constraints------------------------------------

#make list of arcs max caps
for t in team_list:
    m.addConstr(team_v[t]<=10, "maxmembers")

#other stuff
# time = 0
# for i  in arcs:
# 	time += 3* fixed[i] + bolts[i]
# m.addConstr(time >= 0,"time")

# #make list of relations
# values = []
# for node in nodes:
#     pos = []
#     neg = []
#     exp = 0
#     for a in arcs:
#         land = int(a.split("x")[2])
#         send = int(a.split("x")[1])
#         send_n = int(node[1:])
#         if land == send_n:
#             exp+=v[a]
#         if send == send_n:
#             exp-=v[a]
#     m.addConstr(v[node]==exp, name="a"+node)

# #set max and min constraints for nodes
# for i in v:
#     if i[0] == "y":
#         m.addConstr(v[i]>=0, name="l"+i)
#         m.addConstr(v[i]<=demand[int(i[1])], name="u"+i)

#set total demand satisfied to be greater than or equal to a percent of 99
obj = 0
for i in range(0,len(team_list)):
    obj+=team_v[team_list[i]]

# m.setObjective(v["a"], GRB.MAXIMIZE)
m.setObjective(obj, GRB.MAXIMIZE)

#optimize model function
m.write("B4.lp")
m.optimize()

#print results
status_code = {1:'LOADED', 2:'OPTIMAL', 3:'INFEASIBLE', 4:'INF_OR_UNBD', 5:'UNBOUNDED'}
status = m.status
print('The optimization status is {}'.format(status_code[status]))
if status == 2:
    # Retrieve variables value
    print('Optimal solution:')
    for v in m.getVars():
        print('%s = %g' % (v.varName, v.x))
        if v.varname == "x0x1":
        	source = v.x

time = 0
for i  in arcs:
	time += 3* fixed[i].X + bolts[i].X
print("Demand Satisfied:")
print(source) #returns 154 units of demand satisfied
print("Hours Spent:")
print(time) #returns 77 minimum man hours spent to hit max demand satisfied
