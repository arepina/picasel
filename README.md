REST API для проекта, содержащего две основные сущности — пользователи и задачи. 
Свойства пользователя: имя и должность, город. Свойства задачи: название и описание. 


Основные возможности API:

0)curl http://localhost:8000/ - список возможных запросов
1)
curl http://localhost:8000/users/ - все пользователи
curl http://localhost:8000/users/{id}/ - пользователь с id
curl http://localhost:8000/users/ -d "username={username}&position={position}&city={city}" - создание пользователя
curl -X DELETE http://localhost:8000/users/{id}/ - удаление пользователя с id
curl -X PUT http://localhost:8000/users/{id}/ -d "username={username}&position={position}&city={city}" - обновление пользователя
2)
curl http://localhost:8000/tasks/ - все задачи
curl http://localhost:8000/tasks/{id}/ - задача с id
curl --user anastasia:123456 http://localhost:8000/tasks/ -d "name={name}&definition={definition}" - создание задачи (назначение задачи на пользователя anastasia:123456)
curl --user anastasia:123456 -X DELETE http://localhost:8000/tasks/{id}/ - удаление задачи с id (снятие назначения задачи с пользователя anastasia:123456)
curl --user anastasia:123456 -X PUT http://localhost:8000/tasks/{id}/ -d "name={name}&definition={definition}" - обновление задачи
3) curl http://127.0.0.1:8000/users/?position={position} - поиск и фильтрация пользователей по должности
4) curl http://127.0.0.1:8000/tasks/?name={name} - поиск и фильтрация задач по названию
5) curl -X PUT http://127.0.0.1:8000/check_assign/{task_id}/{username} - назначение пользователя (username - имя пользователя), который сможет проверить выполнение конкретной задачи (task_id - id задачи) конкретным пользователем 
6) curl http://127.0.0.1:8000/user_tasks/{user_id}/ - получение всех задач, назначенных пользователю c user_id
7) curl http://127.0.0.1:8000/task_users/{task_id}/ - получение всех пользователей, кому назначена задача c task_id



