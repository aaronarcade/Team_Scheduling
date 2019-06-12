import csv, pprint

def clean():
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
    return members, avg_year
