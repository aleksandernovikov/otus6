# Цель: Сделать модели данных для сайта. 
На сайте есть список курсов, 
каждый курс ведет преподаватель, 
студент может записаться на курс. 
На курсе есть некоторое количество занятий по расписанию.


#### Для запуска проекта нужно клонировать репозиторий
* выполнить миграции используя `manage.py migrate`
* загрузить fixture коммандой `manage.py loaddata auth university`
* скомпилировать перевод `manage.py compilemessages`
* админка доступна по стандартному адресу, пользователь user, пароль 123
---
#### студент может записаться на курс используя метод enroll_in_a_course() модели Student


#Продолжение: 
### Страницы для создания, удаления, редактирования, просмотра 1-го курса и списка курсов