## Тестовая работа для собеседования в компанию "TL Group"
Создано приложение, отображающее оргструктуру со следующими требованиями:

1. Информация о каждом сотруднике должна храниться в базе данных и содержать следующие данные
 * ФИО;
* Должность;
* Дата приема на работу;
* Размер заработной платы;
* Подразделение - подразделения имеют структуру до 5 уровней;
 
Дерево отображается в свернутом виде. 
Закоментирован код для отображения в развернутом виде.
 
База данных более 50 000 сотрудников и 25 подразделений в 5 уровнях иерархий
Заполнение базы реализовано из скрипта
Для заполнения пустой база `python manage.py runscript  db_faker`

Управление записями CRUD через административную часть Django.
В админке реализован просмотре дерева в режиме таблицы и режиме дерева

**Технологии:** 
Django, Python, SQLite
Базовые стили Bootstrap.


