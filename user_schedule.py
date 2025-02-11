class User:

    def __init__(self):
        self.plans_counter = 0 #Нужен для нумерации заметок. Нумерация нужна для реализации метода удаления по выбору пункта
        self.plans = {} #Словарь для заметок
        self.schedule = {
                'Понедельник': {},
                'Вторник': {},
                'Среда': {},
                'Четверг': {},
                'Пятница': {},
                'Суббота': {},
                'Воскресенье': {},
            } #Словарь для расписания

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
        self.plans_counter = 0

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

    def plans_remove(self, message):
        msg = message.text.split('&')[1]
        if msg in self.plans:
            del self.plans[msg]
        else:
            pass

    def schedule_remove_by_time(self,message):
        day, time = message.text.split('&&')[1], message.text.split('&&')[2]
        if day in self.schedule:
            if time in self.schedule[day]:
                del self.schedule[day][time]

    def schedule_remove_by_day(self,message):
        day = message.text.split('&&')[1]
        if day in self.schedule:
            self.schedule[day] = {}

if __name__ == '__main__':
    user = User()
    print(user.plans)