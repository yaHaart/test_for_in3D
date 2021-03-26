import main

manager_id = int(input('Id '))
name = input('Имя ')
surname = input('Фамилия ')
job_name = input('Должность ')
department = input('Отдел ')
birthday = input('Дата рождения ')


temp_manager = main.Manager(manager_id, name, surname, job_name, department, birthday)
print(temp_manager.name)
