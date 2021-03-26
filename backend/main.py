class Manager:
    def __init__(self, id, name, surname, job_name, department, birthday):
        self.id = id
        self.name = name
        self.surname = surname
        self.job_name = job_name
        self.department = department
        self.birthday = birthday



class Worker(Manager):
    def __init__(self, boss_id, id, name, surname, job_name, department, birthday):
        self.boss_id = boss_id
        super().__init__(id, name, surname, job_name, department, birthday)


manager1 = Manager(id=1, name='ИВан', surname='Иванов', job_name='Руководитель отдела', department='Департамент продаж', birthday='01.01.2080')
manager1.name = 'Иван'
print(manager1.name)

worker1 = Worker(boss_id=1, id=1, name='ПЕтр', surname='Петров', job_name='Руководитель отдела', department='Департамент продаж', birthday='01.01.2080')
print(worker1.name)
