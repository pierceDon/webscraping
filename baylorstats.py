from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from plotly.graph_objects import Bar
from plotly import offline

url = 'https://cfbstats.com/2024/team/51/index.html'
# Request in case 404 Forbidden error



years = [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016]


team_statistics = {

}

rival_attendance = {

}

rival_attendance_total = {

}



for x in range (0, len(years)):
    url = f'https://cfbstats.com/{years[x]}/team/51/index.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    tr = soup.findAll('tr')
    year = years[x]
    for row in tr[1:34]:
        td = row.findAll('td')
        name = str(td[0].text.replace("  "," "))
        value = str(td[1].text)
        if name in team_statistics.keys():
            try: 
                team_statistics[name].append([year, float(value)])
            except ValueError:
                team_statistics[name].append([year, value])
        else:
            team_statistics[name] = []
            try: 
                team_statistics[name].append([year, float(value)])
            except ValueError:
                team_statistics[name].append([year, value])

for x in range(0, len(years)):
    url = f'https://cfbstats.com/{years[x]}/team/51/index.html'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
    req = Request(url, headers=headers)
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    schedule = soup.find("div", attrs={"class":"team-schedule"})
    tr = schedule.findAll('tr')
    year = years[x]
    attendance = []
    for row in tr[1:13]:
        try: 
            ls_count = 0
            td = row.findAll('td')
            school = str(td[1].text)
            school = ''.join([x for x in school if not x.isdigit()])
            school = school.replace('@ ','')
            school = school.replace(" ","")
            school = school.replace("+","")
            attnd = int(td[4].text.replace(",",""))
            attendance.append([school, attnd])
            ls_count += 1
            if school in rival_attendance_total.keys():
                rival_attendance_total[f'{school}'] += attnd
            else:
                rival_attendance_total[f'{school}'] = attnd
        except IndexError:
            pass
    max_attn = max(list(map(lambda x: x[1], attendance)))
    for x, y in attendance:
        if y == max_attn:
            rival_attendance[f'{year}'] = [x,y]
# print(rival_attendance)
# print(rival_attendance_total)

sorted_attendance = list(sorted(rival_attendance_total.items(), key=lambda x: x[1], reverse=True)[:5])
sorted_schools = list(map(lambda x: x[0], sorted_attendance))
sorted_num = list(map(lambda x: x[1], sorted_attendance))



    



#print(team_statistics)
score = (team_statistics['Scoring: Points/Game'])
passing = (team_statistics['Passing: Yards'])
conversion = (team_statistics["3rd Down Conversions: Conversion %"])
field_goal = (team_statistics['Field Goals: Success %'])


def best(arg):
    value = max(list(map(lambda x: x[1], arg)))
    for [x, y] in arg:
        if y == value:
            year = x 
        else:
            pass
    return value, year
    
def worst(arg):
    value = min(list(map(lambda x: x[1], arg)))
    for [x, y] in arg:
        if y == value:
            year = x 
        else:
            pass
    return value, year

print(f'''
Best Years:
    1) Scoring Points/Game - {(best(score))[1]}
    2) Passing Yards - {(best(passing))[1]}
    3) 3rd Down Conversion - {(best(conversion))[1]}
    4) Field Goal Success - {(best(field_goal))[1]}

Worst Years:
    1) Scoring Points/Game - {(worst(score))[1]}
    2) Passing Yards - {(worst(passing))[1]}
    3) 3rd Down Conversion - {(worst(conversion))[1]}
    4) Field Goal Success - {(worst(field_goal))[1]}
''')

# counter = 16


# while counter <= 24:
#     index_counter = 0
#     att_list = []
#     for x, y in rival_attendance[f'20{counter}']: 
#         att_list.append(y)
#     year_max = max(att_list)
#     max_att.append(year_max)
#     counter += 1

# print(max_att)


# for x in max_att:
#     if x in rival_attendance[]


data = [
    {
        "type":"bar",
        "x":sorted_schools,
        "y":sorted_num,
        "marker": {
            "color": "rgb(60,100,150)",
            "line": {"width":1.5,"color": "rgb(25,25,25)"},
        },
        "opacity": 0.6
    }
]

my_layout = {
    "title": "Biggest Baylor Football Rivalry Based on Attendence",
    "xaxis": {"title": "Teams"},
    "yaxis": {"title": "Attendance"},
}

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="baylorstats.html")












