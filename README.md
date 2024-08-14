# ZeroCoder VD01-09
## VD01. Введение в веб-разработку. Основы HTML
Виды HTML тегов<br>
_**VD01/VD01_les_ex_01.html**_

Основные теги для работы с встроенным контентом на странице<br>
_**VD01/VD01_les_ex_02.html**_

### ДЗ VD01
Создай таблицу с рейтингом ваших любимых/нелюбимых блюд. 
В таблице должно быть минимум 5 рядов и 4 столбца: 
* Первый столбец - название блюда;
* Второй столбец - ваша оценка от 1 до 10;
* Третий столбец - ссылка на рецепт;
* Четвертый столбец - фото блюда.

_**VD01/VD01_home_ex_01.html**_

<hr>

## VD02. Основы CSS
Запись стилей для элементов сайта. <br> Какие бывают стили<br>
_**VD02/VD02_les_ex_01.html**<br>
**VD02/VD02_les_ex_style_01.css**_

Как позиционировать элементы<br>
**VD02/VD02_les_ex_02.html**


Псевдоэлементы и псевдоклассы
_**VD02/VD02_les_ex_03.html**<br>
**VD02/VD02_les_ex_style_02.css**_


Практика. Создадим карточку с персонажем<br>
_**VD02/VD02_les_ex_04.html**<br>
**VD02/VD02_les_ex_style_03.css**_


### ДЗ VD02
Создать минимум три карточки с информацией о пользователях. 
На карточке должно быть 
- фото, 
- ФИО, 
- e-mail, 
- дата рождения, 
- город.

Стили обязательно нужно применить к самой карточке и к фото, также примените <br>
псевдокласс hover для карточки и сделайте стили при наведении на карточку.

_**VD02/VD02_home_ex_01.html**<br>
**VD02/VD02_home_ex_style_01.css**_

<hr>

## VD03. Работа с фреймворком Bootstrap
Работа с компонентами Bootstrap<br>
_**[VD03/VD03_les_ex_01.html](VD03%2FVD03_home_ex_01.html)**_

Работа с сеткой Bootstrap<br>
_**VD03/VD03_les_ex_02.html**_

### ДЗ VD03
Создайте базовую структуру страницы с использованием компонентов бутстрапа
* Шапка сайта(содержит название сайта и навигационное меню)
* Основной контент содержит три секции, 
  - в первой слайдер с минимум 3 фото, 
  - во второй три карточки, расположенные в три колонки для больших экранов 
  и в один столбец для маленьких экранов, 
  - в третьей аккордеон с информацией.
* Футер(содержит контактную информацию и ссылки на социальные сети

_**VD03/VD03_home_ex_01.html**_

<hr>

## VD04. Знакомство с фреймворком Flask для веб-разработки
Что будет на уроке. Flask. Декорирование

**_VD04_les_ex_01.py<br>
templates/VD04_les_ex_01.html<br>
templates/VD04_les_ex_02.html_**

### ДЗ VD04
Задание 1
Создайте новое приложение Flask, которое будет отображать текущие дату и время на главной странице.<br>
_**VD04_home_ex_01.py**_


Задание 2
Создайте новое приложение Flask, создайте структуру проекта с папками static и templates, 
в папке templates должны быть 3 html файла: index, blog, contacts (главная страница, 
страница блога и контакты). Заполните их информацией и выведите силами flask сервера, 
используя функцию render_template()

Обязательно на всех страницах сделайте меню, которое будет работать именно при запуске 
проекта через flask

_**VD04_home_ex_02.py**_<br>
_**VD04_home_ex_index.html**_<br>
_**VD04_home_ex_blog.html**_<br>
_**VD04_home_ex_contacts.html**_