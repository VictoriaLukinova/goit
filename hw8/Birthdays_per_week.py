from datetime import datetime, timedelta

users = [
    {'name': "Anna", "birthday": datetime(year= 1993, month= 11, day= 15, hour= 0)},
    {'name': "Nat", "birthday": datetime(year= 1993, month= 11, day= 18, hour= 0)},
    {'name': "Yegor", "birthday": datetime(year= 1993, month= 11, day= 18, hour= 0)},
    {'name': "Nik", "birthday": datetime(year= 1993, month= 11, day= 19, hour= 0)}
]

def get_birthdays_per_week(users):
    current_date = datetime.now()
    delta = timedelta(days= 1)
    birthdays_list =['', '', '', '', '',]
    for i in range(6):
        date = current_date + delta*i
        for colleague in users:
            if colleague['birthday'].month == date.month and colleague['birthday'].day == date.day:
                weekday = date.weekday()
                try:
                    birthdays_list[weekday] = birthdays_list[weekday] + colleague['name'] + ', '
                except IndexError:
                    birthdays_list[0] = birthdays_list[0] + colleague['name'] + ', '
    colleagues_birthdays= {
        "Monday" : birthdays_list[0].removesuffix(', '),
        'Tuesday' : birthdays_list[1].removesuffix(', '),
        'Wednesday' : birthdays_list[2].removesuffix(', '),
        'Thursday' : birthdays_list[3].removesuffix(', '),
        'Friday' : birthdays_list[4].removesuffix(', '),
    }
    for key, value in colleagues_birthdays.items():
        if value:
            print(key, ':', value)

get_birthdays_per_week(users)
