# Django backend project

This is a backend development assignment project built with Django, Django REST Framework (DRF), Celery, Redis, and a Telegram bot. It demonstrates your ability to build a production-ready backend with APIs, background task processing, authentication, and external API integration.

---

## 🚀 Features

* ✅ Django + DRF backend setup
* 🔐 Token-based authentication
* 🌐 Public and protected API endpoints
* 📬 Celery + Redis for background email sending
* 🤖 Telegram Bot that registers users using /start command
* 🛡 Environment variable security
* 🧹 Clean code with GitHub version control

---

## 🧱 Tech Stack

* **Python 3.8+**
* **Django 4+**
* **Django REST Framework**
* **Redis** (as message broker for Celery)
* **Celery** (for background tasks)
* **Telegram Bot API**
* **SQLite** (default DB, can be swapped with Postgres)

---

## 📂 Project Structure

```
myproject/
├── core/
│   ├── models.py        # Telegram user model
│   ├── views.py         # API views
│   ├── tasks.py         # Celery task (email)
│   ├── urls.py          # App URLs
├── myproject/
│   ├── settings.py      # Main settings
│   ├── urls.py          # Root URLs
│   ├── celery.py        # Celery setup
├── bot.py               # Telegram bot script
├── manage.py            # Django management script
├── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/your-username/django-intern-assignment.git
cd django-intern-assignment
```

### 2. Create & Activate Virtual Environment

```bash
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create `.env` File

```
SECRET_KEY=your-secret-key
DEBUG=False
BOT_TOKEN=your-telegram-bot-token
```

### 5. Run Migrations

```bash
python manage.py migrate
python manage.py createsuperuser
```

### 6. Run Redis

```bash
redis-server
```

### 7. Run Celery Worker

```bash
celery -A myproject worker --loglevel=info
```

### 8. Start Django Server

```bash
python manage.py runserver
```

### 9. Start Telegram Bot

```bash
python bot.py
```

---

## 🧪 API Endpoints

| Method | Endpoint          | Auth Required | Description             |
| ------ | ----------------- | ------------- | ----------------------- |
| GET    | `/api/public/`    | No            | Public test endpoint    |
| GET    | `/api/protected/` | Yes (Token)   | Protected user endpoint |

To get token:

```bash
POST /api-token-auth/ with username and password
```

Use in header:

```
Authorization: Token <your-token>
```

---

## 🤖 Telegram Bot

* Go to Telegram and search your bot.
* Type `/start`
* Your username will be stored in the database.

---


