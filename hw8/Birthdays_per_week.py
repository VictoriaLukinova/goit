from datetime import datetime, timedelta

users = [
    {'name': "Anna", "birthday": datetime(year= 1993, month= 11, day= 12, hour= 0)},
    {'name': "Nat", "birthday": datetime(year= 1993, month= 11, day= 8, hour= 0)},
    {'name': "Yegor", "birthday": datetime(year= 1993, month= 11, day= 8, hour= 0)},
    {'name': "Nik", "birthday": datetime(year= 1993, month= 11, day= 11, hour= 0)}
]

def get_birthdays_per_week(users):
    current_date = datetime.now()
    delta = timedelta(days= 1)
    birthdays_dict_int = {
        0 : [],
        1 : [],
        2 : [],
        3 : [],
        4 : []
    }
    for i in range(6):
        day = current_date + delta*i
        for collegue in users:
            if collegue['birthday'].month == day.month and collegue['birthday'].day == day.day:
                weekday = day.weekday()
                try:
                    birthdays_dict_int[weekday].append(collegue['name'])
                except KeyError:
                    birthdays_dict_int[0].append(collegue['name'])
    birthdays_dict_str = {
        "Monday" : ', '.join(birthdays_dict_int[0]),
        'Tuesday' : ', '.join(birthdays_dict_int[1]),
        'Wednesday' : ', '.join(birthdays_dict_int[2]),
        'Thursday' : ', '.join(birthdays_dict_int[3]),
        'Friday' : ', '.join(birthdays_dict_int[4])
    }
    for key, value in birthdays_dict_str.items():
        if value:
            print(key, ':', value)

get_birthdays_per_week(users)