# Micro-Shop #

Micro-Shop - это интернет витрина ориентированная на небольшой бизнес не требующий интернет магазина с корзиной и онлайн оплатой.

## Особенности витрины ##

* Прямая связи с продавцом по средствам мессенджеров WhatsApp или Telegram.

* Возможность совершения телефонного звонка без необходимости набирать номер вручную.

* Конфигуратор главной страницы.

* Редактор категорий.

* 10 цветовых схем для стилизации сайта.

* Брендирование витрины. Вместо кнопки "Главная" в меню сайта может отображаться любой текст.

* Доступно несколько символов валют: ₽, ₴, Br, $, €.

* Кнопки профилей социальных сетей в подвале сайта.

* Простая система управления контентом не требующая специальных знаний.

* Максимальное количество товаров - 500 единиц.

* Возможность помещения товаров в архив.

* Административный интерфейс совмещён с основным меню сайта.

## Установка и запуск на локальном сервере ##

Консольные команды могут быть специфичными для операционных систем симейства Linux.

* Копируем репозиторий: ```git clone https://github.com/YuriyCherniy/micro-shop.git```

* Переходим в папку с содержимым: ```cd micro-shop/```

* Создаём виртуальное окружение стандартными средствами Python: ```python3 -m venv venv```

* Активируем виртуальное окружение: ```source venv/bin/activate```

* Устанавливаем зависимости: ```pip3 install -r requirements.txt```

* Переходим в папку с проектом: ```cd micro_shop/```

* Применяем миграции: ```./manage.py migrate```

* Создаём суперюзера: ```./manage.py createsuperuser```

* Создаём профиль для суперюзера (команда специфичная для проекта): ```./manage.py createsuperuserprofile```

* Запускаем локальный сервер: ```./manage.py runserver```

Если всё сделанно правильно сайт будет доступен по адресу ```http://127.0.0.1:8000/```

## Технологии ##

* Micro-shop на бекенде использует язык программирования Python 3 и фреймворк Django 2.2 версии, на фронтенде применяется Bootstrap 4, в качестве базы данных используется sqlite3

## Как принять участие в проекте ##

### Структура проекта для понимания общей картины ###

#### Проект состоит из нескольких приложений ####

* **showcase** - отвечает за отображение товаров, кроме товаров на главной странице, а также здесь находится CRUD функционал.

* **mainpage** - отвечает за отображение товаров на главной странице, а также содержит логику редактирования товаров на главной, добавление, удаление и изменение позиции.

* **staff** - отвечает за профиль администратора, через который настраиваются контакты для связи, способы связи, профили социальных сетей, брендирование витрины и выбор знака валюты для карточек товаров.

* **category_manager** - отвечает за создание и редактирование категорий товаров.

* **color_theme** - отвечает за изменение цветовой схемы сайта.

### Как сделать pull request ###

* В общем случае вот так: [first-contributions](https://github.com/firstcontributions/first-contributions)

* Сюда в проект по тому же принципу. Детали обсудим в обсуждениях.
