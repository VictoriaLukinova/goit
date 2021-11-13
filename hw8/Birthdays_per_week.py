from datetime import datetime, timedelta

users = [
    {'name': "Anna", "birthday": datetime(year= 1993, month= 11, day= 14, hour= 0)},
    {'name': "Nat", "birthday": datetime(year= 1993, month= 11, day= 18, hour= 0)},
    {'name': "Yegor", "birthday": datetime(year= 1993, month= 11, day= 18, hour= 0)},
    {'name': "Nik", "birthday": datetime(year= 1993, month= 11, day= 16, hour= 0)}
]

def get_birthdays_per_week(users):
    current_date = datetime.now()
    delta = timedelta(days= 1)
    birthdays_list =[[], [], [], [], [],]
    for i in range(6):
        date = current_date + delta*i
        for collegue in users:
            if collegue['birthday'].month == date.month and collegue['birthday'].day == date.day:
                weekday = date.weekday()
                try:
                    birthdays_list[weekday].append(collegue['name'])
                except IndexError:
                    birthdays_list[0].append(collegue['name'])
    collegues_birthdays= {
        "Monday" : ', '.join(birthdays_list[0]),
        'Tuesday' : ', '.join(birthdays_list[1]),
        'Wednesday' : ', '.join(birthdays_list[2]),
        'Thursday' : ', '.join(birthdays_list[3]),
        'Friday' : ', '.join(birthdays_list[4]),
    }
    for key, value in collegues_birthdays.items():
        if value:
            print(key, ':', value)

get_birthdays_per_week(users)
