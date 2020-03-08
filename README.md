# devtest
Шаблон проекта django - "Тестовое задание для веб-разработчика".

## Требования
Django 2.2.10

Python >= 3.5

СУБД - любая на выбор.

Прочее по необходимости.

Для шаблонов можно использовать CSS-фреймворки (например bootstrap) и Jquery.

## Задание 
1. Клонировать проект
2. Установить требуемое ПО в виртуальное окружение
3. Настроить settings.py
4. Настроить модели - добавить названия полей на русском языке в соответствии с комментариями в коде.
5. Настроить шаблон base - меню расрянуть горизонтально, убрать метки списка.
###  6. Доработать Раздел "Заявки"
Сделать горизонтально растянутую форму фильтра по номеру заявки, контрагенту, диапазону дат ("с" и "по").

Фильтр по контрагенту - с выбором из списка, включающего значение "все", которое выбирается по умолчанию.

Для пользователя,выполнившего вход, в поле "Номер заявки" появляется гиперссылка для открытия формы редактирования заявки.

В таблице сделать разделители для ячеек.

### 7. Доработать форму создания заявки
Функция доступна только пользователям, выполнившим вход.

### 8. Реализовать форму редактирования заявки
Вид - аналогичный форме создания новой заявки.

Функция доступна только пользователям, выполнившим вход.

Редирект при успешной обработке - на '/'.

### 9. Реализовать отчет по поданным заявкам на получение ту (раздел "Отчет")
Примерный макет:

Данные о заявках
----------------
|Арендодатель|ТУ получено|Отказ|В работе|ИТОГО|
|------------|-----------|-----|--------|-----|
|**Контрагент 1**|"" или целое число > 0|"" или целое число > 0|"" или целое число > 0|"" или целое число > 0|
|...|...|...|...|...|
|**Контрагент N**|"" или целое число > 0|"" или целое число > 0|"" или целое число > 0|"" или целое число > 0|
|**ИТОГО**|"" или целое число > 0|"" или целое число > 0|"" или целое число > 0|"" или целое число > 0|

В ячейках отчета - количество заявок, сгруппированное по резолюциям и арендодателям.
