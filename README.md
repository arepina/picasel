REST API для проекта, содержащего две основные сущности — пользователи и задачи. 
Свойства пользователя: имя и должность, город. Свойства задачи: название и описание. 


Основные возможности API:

0)curl http://localhost:8000/ - список возможных запросов

1)
curl http://localhost:8000/users/ - все пользователи

curl http://localhost:8000/users/{id}/ - пользователь с id

curl http://localhost:8000/users/ -d "username={username}&position={position}&city={city}" - создание пользователя

curl -X DELETE http://localhost:8000/users/{id}/ - удаление пользователя с id

curl -X PUT http://localhost:8000/users/ -d "username={username}&position={position}&city={city}" - обновление пользователя

2)
curl http://localhost:8000/tasks/ - все задачи

curl http://localhost:8000/tasks/{id}/ - задача с id

curl --user anastasia:123456 -X POST http://localhost:8000/tasks/  "name={name}&definition={definition}" - создание задачи

curl --user anastasia:123456 -X DELETE http://localhost:8000/tasks/{id}/ - удаление задачи с id

curl --user anastasia:123456 -X PUT http://localhost:8000/tasks/  "name={name}&definition={definition}" - обновление задачи
3)curl http://127.0.0.1:8000/users/?position={position} - поиск и фильтрация пользователей по должности
4)curl http://127.0.0.1:8000/tasks/?name={name}- поиск и фильтрация задач по названию
5) назначение/снятие назначения задачи на пользователя
6) назначение пользователя, который сможет проверить выполнение конкретной задачи конкретным пользователем (саму проверку и статусы выполнения задачи реализовывать не нужно)
7) получение всех задач, назначенных пользователю — с проверяющими, когда они есть
8) получение всех пользователей, кому назначена задача



