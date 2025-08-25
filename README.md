# Dashboard App

Проект — это таск-менеджер с real-time синхронизацией, вдохновлённый эстетикой олдскульных видеоигр.
Минимализм, тёмная палитра и строгие контрасты создают атмосферу ретро-интерфейсов, но с современными технологиями под капотом.

## Архитектура

### Frontend — Vue 3 + Pinia + Vite:

- Компонентный подход
- Pinia store для управления состоянием
- WebSocket для моментального обновления задач
- Стилизация через Sass с переменными и миксинами (адаптивные отступы через clamp)

### Backend — FastAPI

- REST API для CRUD-операций над задачами
- WebSocket для push-уведомлений об изменениях
- Асинхронная работа с БД
- Database — PostgreSQL (через asyncpg)

### Docker

- Контейнеризация фронта, бэка и базы данных
- Автоматическая сборка и запуск через docker-compose

## Особенности дизайна

**Тёмная палитра с акцентными цветами** 

**Адаптивность —** размеры (отступы, шрифты) рассчитаны через clamp(), чтобы интерфейс выглядел органично на экранах от 320px до 1440px.

**Ретро-вайб:**

- строгие границы ($border-radius: 12px)
- резкие переходы и мягкие тени (--shadow)
- минимализм, вдохновлённый интерфейсами из игр 90-х.

## Установка и запуск

> git clone https://github.com/Lapidusa/Dashboard

> cd Kanban

#### Копируем env

В Windows PowerShell:
>Copy-Item .\backend\.env.example .\backend\.env <br />
>Copy-Item .\frontend\.env.example .\frontend\.env

В Linux/macOS (bash):
>cp backend/.env.example backend/.env <br />
>cp frontend/.env.example frontend/.env

Для frontend:
>pnpm install

Для backend:
>pip install

### Запуск
Для frontend:
> pnpm run dev

Для backend:
> uvicorn main:app --reload

#### Приложение поднимется на:

> Фронтенд: http://localhost:5173/

> Бэкенд: http://127.0.0.1:8000

## Фичи

- Создание, редактирование, удаление и восстановление задач
- Скрытые задачи (архив)
- Автоматическая синхронизация между вкладками/устройствами через WebSocket
- Адаптивный дизайн