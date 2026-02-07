# 🚀 Blog API - FastAPI Social Platform

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)

Полнофункциональный REST API для социальной блог-платформы с аутентификацией, постами, комментариями и лайками. Построен на современном асинхронном стеке FastAPI.

## ✨ Особенности

- ✅ **JWT аутентификация** с ролями (user/admin)
- ✅ **Полный CRUD** для постов, комментариев, лайков
- ✅ **Асинхронные операции** базы данных
- ✅ **Автоматическая документация** OpenAPI/Swagger
- ✅ **Пагинация и фильтрация** данных
- ✅ **Валидация данных** через Pydantic
- ✅ **Связи между моделями** с каскадным удалением
- ✅ **Защита эндпоинтов** по ролям пользователей

## 🏗️ Архитектура
app/
├── core/ # Конфигурация и зависимости
├── database/ # Модели и подключение к БД
├── schemas/ # Pydantic схемы
├── crud/ # Операции с БД
├── routers/ # Маршруты API
├── security/ # Аутентификация и хеширование
├── validate/ # Валидация и зависимости
└── deps.py # FastAPI зависимости

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.10+
- PostgreSQL (или SQLite для разработки)
- pip (менеджер пакетов Python)

### Установка

1. **Клонируйте репозиторий:**
```bash
git clone https://github.com/ваш-username/BLOG-API.git
cd BLOG-API
```
2. **Создайте виртуальное окружение:**
python -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate     # Windows

3. **Установите зависимости:**
pip install -r requirements.txt

4. **Настройте переменные окружения:**
Измените файл config.py в корне проекта

5. **Запустите приложение:**
uvicorn app.main:app --reload

Приложение будет доступно по адресу: http://localhost:8000


📚 Документация API
После запуска приложения документация доступна по адресам:
Swagger UI: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc

🔐 Аутентификация
API использует JWT (JSON Web Tokens) для аутентификации:
Регистрация: POST /auth/register
Логин: POST /auth/login (получите access token)
Использование: Добавьте заголовок Authorization: Bearer <token>

📋 Основные эндпоинты
👤 Аутентификация
Метод	Эндпоинт	Описание
POST	/auth/register	Регистрация нового пользователя
POST	/auth/login	Вход и получение токена

📝 Посты
Метод	Эндпоинт	Описание
GET	/posts/	Получить все посты (с пагинацией)
GET	/posts/{post_id}	Получить конкретный пост
POST	/posts/create	Создать новый пост
PUT	/posts/update/{post_id}	Обновить пост
DELETE	/posts/delete/{post_id}	Удалить пост

💬 Комментарии
Метод	Эндпоинт	Описание
GET	/posts/{post_id}/comments/	Комментарии к посту
POST	/posts/{post_id}/comments/	Добавить комментарий
PUT	/posts/{post_id}/comments/{comment_id}	Обновить комментарий
DELETE	/posts/{post_id}/comments/{comment_id}	Удалить комментарий

❤️ Лайки
Метод	Эндпоинт	Описание
POST	/posts/{post_id}/like	Поставить лайк
DELETE	/posts/{post_id}/like	Убрать лайк
GET	/posts/{post_id}/like/check	Проверить лайк
GET	/posts/{post_id}/like/count	Количество лайков

👥 Пользователи
Метод	Эндпоинт	Описание
GET	/users/profile	Профиль текущего пользователя
PUT	/users/profile/update	Обновить профиль
DELETE	/users/profile/delete	Удалить аккаунт
GET	/users/get_all	Все пользователи (admin)
GET	/users/{user_id}	Профиль пользователя по ID

🗄️ Модели базы данных
**User**
id: Integer (PK)
username: String(15), unique
hashed_password: String
role: String (user/admin)
created_at: DateTime
description: String (nullable)
date_of_birth: DateTime (nullable)
**Post**
id: Integer (PK)
title: String
content: String
author_id: Integer (FK → User)
created_at: DateTime
updated_at: DateTime
is_published: Boolean
**Comment**
id: Integer (PK)
text: String
post_id: Integer (FK → Post)
author_id: Integer (FK → User)
created_at: DateTime
updated_at: DateTime
**Like**
id: Integer (PK)
author_id: Integer (FK → User)
post_id: Integer (FK → Post)
created_at: DateTime
UNIQUE(author_id, post_id)  # один лайк на пост от пользователя


🔧 **Технологии**
FastAPI - современный, быстрый веб-фреймворк
SQLAlchemy 2.0 - асинхронный ORM
Pydantic - валидация данных и сериализация
JWT - аутентификация и авторизация
Python-jose - работа с JWT токенами
Passlib - хеширование паролей
Uvicorn - ASGI сервер

👤 **Автор**
GitHub: @OneSummon
