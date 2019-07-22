import csv, pprint

noprojects=9

def clean(noprojects):
    members = []
    with open('DummyApplicationResponses_preclean.csv', 'r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        headers = next(reader, None)
        teamlist = {}
        for h in headers[20:20+noprojects]:
            teamlist[h] = [0,0,0,[]]
        avg_year = 0
        for row in reader:

            #make dict of preferences *****be sure to change number of projects, no projects = 2nd number in 2nd param of range
            proj_pref = {}
            for proj in range(20, 20+noprojects):
                if 'VERY' in row[proj]:
                    proj_pref[headers[proj]] = 3
                    teamlist[headers[proj]][2]+=1
                elif 'Interested' in row[proj]:
                    proj_pref[headers[proj]] = 2
                    teamlist[headers[proj]][1]+=1
                elif 'Mildly' in row[proj]:
                    proj_pref[headers[proj]] = 1
                    teamlist[headers[proj]][0]+=1

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
    return members, teamlist, avg_year
members, teamlist, avg_year = clean(9)

def firstchoices(members, teamlist):
    #find smallest first choice list
    todel = []
    m = (min([teamlist[t][0] for t in teamlist]))
    target = ([t for t in teamlist if teamlist[t][0] == m][0])
    for p in range(0,len(members)):
        if target in members[p]['projects']:
            if members[p]['projects'][target]==1:
                todel.append(p)
                teamlist[target][3].append(str(members[p]['name'])[2:-1])
    #print(todel)
    newmembers = []
    for p in range(0,len(members)):
        if p not in todel:
            newmembers.append(members[p])
    teamlist[target][0] = 999
    return(newmembers, teamlist)

def secondchoices(members, teamlist):
    #find smallest first choice list
    todel = []
    m = (min([len(teamlist[t][3]) for t in teamlist]))
    target = ([t for t in teamlist if len(teamlist[t][3]) == m][0])
    #print(target,m)
    for p in range(0,len(members)):
            if target in members[p]['projects']:
                if members[p]['projects'][target]==2:
                    todel.append(p)
                    teamlist[target][3].append(str(members[p]['name'])[2:-1])
    newmembers = []
    for p in range(0,len(members)):
        if p not in todel:
            newmembers.append(members[p])
    teamlist[target][1] = 999
    return(newmembers, teamlist)

def thirdchoices(members, teamlist):
    #find smallest first choice list
    todel = []
    m = (min([len(teamlist[t][3]) for t in teamlist]))
    target = ([t for t in teamlist if len(teamlist[t][3]) == m][0])
    #print(target,m)
    for p in range(0,len(members)):
            if target in members[p]['projects']:
                if members[p]['projects'][target]==3:
                    todel.append(p)
                    teamlist[target][3].append(str(members[p]['name'])[2:-1])
    newmembers = []
    for p in range(0,len(members)):
        if p not in todel:
            newmembers.append(members[p])
    teamlist[target][2] = 999
    return(newmembers, teamlist)

def lastchoice(members, teamlist):
    todel = []
    p = members[0]
    m = (min([len(teamlist[t][3]) for t in p['projects']]))
    target = ([t for t in teamlist if len(teamlist[t][3]) == m][0])
    #print(target)

    for p in range(0,len(members)):
        todel.append(p)
        teamlist[target][3].append(str(members[p]['name'])[2:-1])
    newmembers = []
    for p in range(0,len(members)):
        if p not in todel:
            newmembers.append(members[p])
    return(newmembers, teamlist)



members, teamlist, avg_year = clean(noprojects)
for i in range(noprojects):
    members, teamlist = firstchoices(members, teamlist)
#pprint.pprint(teamlist)
if len(members)!=0:
    # print(len(members))
    for i in range(noprojects):
        members, teamlist = secondchoices(members, teamlist)
if len(members)!=0:
    # print(len(members))
    for i in range(noprojects):
        members, teamlist = thirdchoices(members, teamlist)
while len(members)!=0:
    members, teamlist = lastchoice(members, teamlist)
# pprint.pprint(teamlist)

for t in teamlist:
    throw it back in a csv

