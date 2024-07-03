### [Описание на русском языке](#русский)

### [Description in English](#english)

---

## <a name="русский"></a>Описание на русском языке

### Описание проекта

Проект DJ03_models_BD представляет собой веб-приложение на Django для управления новостями. В рамках этого проекта была создана база данных, включающая все необходимые поля, а также поле с именем пользователя, выкладывающего новость. Проект использует современный стиль Material Design с помощью MDBootstrap.

### Шаги по выполнению задания

#### 1. Создание модели News_post

1. В приложении `news` была создана модель `News_post` с полями:
   - `title` (Заголовок новости)
   - `short_description` (Краткое описание)
   - `content` (Текст новости)
   - `created_at` (Дата создания)
   - `creator` (Автор)
2. Поле `creator` было добавлено для хранения имени пользователя, выкладывающего новость.

#### 2. Создание и применение миграций

1. Выполнены команды `makemigrations` и `migrate` для создания и применения миграций, обновляющих базу данных.

#### 3. Создание представлений для отображения новостей

1. В файле `views.py` были созданы представления:
   - `news` для отображения списка новостей.
   - `news_detail` для отображения подробной информации о конкретной новости.

#### 4. Настройка URL-маршрутов

1. В файле `urls.py` приложения `news` были добавлены маршруты для списка новостей и подробного отображения.
2. В файле `urls.py` основного проекта были подключены маршруты приложения `news`.

#### 5. Создание шаблонов для новостей

1. Создан шаблон `news.html` для отображения списка новостей.
2. Создан шаблон `news_detail.html` для отображения подробной информации о новости.
3. Шаблоны используют компоненты MDBootstrap для реализации современного дизайна.

#### 6. Настройка основного шаблона и меню

1. В файле `base.html` были подключены стили и скрипты MDBootstrap.
2. Создано меню `menu.html` с навигацией по разделам сайта.

#### 7. Обновление стиля и дизайна

1. Использованы компоненты MDBootstrap для реализации современного стиля Material Design.
2. Обновлены все шаблоны для использования стилизованных компонентов.

### Заключение

Проект успешно реализован с использованием Django и MDBootstrap, включает все необходимые поля в базе данных, а также дополнительное поле для имени пользователя, выкладывающего новость. Созданы представления, маршруты и шаблоны для отображения списка новостей и подробной информации о них.

---

## <a name="english"></a>Description in English

### Project Description

The DJ03_models_BD project is a Django web application for managing news. As part of this project, a database was created that includes all necessary fields, plus a field for the username of the person posting the news. The project uses modern Material Design styling with MDBootstrap.

### Steps to Complete the Assignment

#### 1. Creating the News_post Model

1. In the `news` app, the `News_post` model was created with the following fields:
   - `title` (News title)
   - `short_description` (Short description)
   - `content` (News content)
   - `created_at` (Creation date)
   - `creator` (Author)
2. The `creator` field was added to store the username of the person posting the news.

#### 2. Creating and Applying Migrations

1. Ran `makemigrations` and `migrate` commands to create and apply migrations updating the database.

#### 3. Creating Views to Display News

1. In the `views.py` file, the following views were created:
   - `news` to display the list of news.
   - `news_detail` to display detailed information about a specific news item.

#### 4. Setting Up URL Routes

1. In the `urls.py` file of the `news` app, routes were added for the news list and detailed views.
2. In the main project's `urls.py` file, routes from the `news` app were included.

#### 5. Creating Templates for News

1. Created a `news.html` template to display the list of news.
2. Created a `news_detail.html` template to display detailed information about a news item.
3. Templates use MDBootstrap components to implement modern design.

#### 6. Setting Up the Base Template and Menu

1. In the `base.html` file, MDBootstrap styles and scripts were included.
2. Created a `menu.html` with navigation across the site sections.

#### 7. Updating Style and Design

1. Used MDBootstrap components to implement a modern Material Design style.
2. Updated all templates to use stylized components.

### Conclusion

The project was successfully implemented using Django and MDBootstrap, including all necessary fields in the database, as well as an additional field for the username of the person posting the news. Views, routes, and templates were created to display the list of news and detailed information about them.
