class User:

    def __init__(self):

        self.plans_counter = 0
        self.plans = {}
        self.schedule = {
                'Понедельник': {},
                'Вторник': {},
                'Среда': {},
                'Четверг': {},
                'Пятница': {},
                'Суббота': {},
                'Воскресенье': {},
            }

    def plans_str(self) -> str:
        plan = '<b>Ваши заметки:</b>'
        for key, value in self.plans.items():
            plan += f'\n{key}. <em>{value}</em>'
        return plan

    def schedule_str(self)-> str:
        schedule = '<b>Ваше текущее расписание:</b>'
        for day, daily in self.schedule.items():
            schedule += f'\n{day}:'
            for time, event in daily.items():
                schedule += f'\n        →{time} | <em>{event}</em>'
        return schedule

    def __str__(self):
        return f'{self.plans_str()}\n\n{self.schedule_str()}'

    def plans_clear(self):
        self.plans = {}

    def schedule_clear(self):
        self.schedule = {
                'Понедельник' : {},
                'Вторник': {},
                'Среда': {},
                'Четверг': {},
                'Пятница': {},
                'Суббота': {},
                'Воскресенье': {},
        }

    def schedule_add(self, day, time, text):
        self.schedule[day][time] = text
        self.schedule[day] = dict(sorted(self.schedule[day].items()))

    def plans_add(self, text):
        self.plans_counter += 1
        self.plans[str(self.plans_counter)] = text


if __name__ == '__main__':
    user = User()
    print(user.plans)