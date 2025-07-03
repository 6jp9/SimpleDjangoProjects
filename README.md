# 🧠 Django Quiz App

A full-featured, login-protected multiple-choice quiz application built with Django and MySQL/SQLite. Users can select subjects like Python, Java, or Front-End Technologies, choose difficulty levels (Beginner, Intermediate, Expert), take exams, and get instant results with answer feedback.

---

## 🚀 Features

- 🔐 User registration with email OTP verification
- 📧 Email sending using Gmail SMTP (via Django)
- 📚 Quiz Subjects: Python, Java, Front-End Technologies
- 🎯 Levels: Beginner, Intermediate, Expert
- ✅ Real-time result evaluation with answer feedback
- 📊 Score summary with correct/incorrect answers
- 🗃️ MySQL (or SQLite for deployment) with 180+ questions
- 🌐 Deployment-ready on platforms like Render, Railway, etc.

---

## 🛠️ Tech Stack

- **Framework:** Django 5.x
- **Database:** MySQL (development), SQLite (deployment optional)
- **Frontend:** HTML, Bootstrap 4
- **Auth:** Django’s built-in authentication
- **Email:** Gmail SMTP for OTP
- **Deployment:** Can be deployed with Gunicorn + Nginx or cloud platforms

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/6jp9/SimpleDjangoProjects.git
cd SimpleDjangoProjects/Quiz_App
```

### 2. Install Dependencies Globally

Make sure Django and the database client are installed:

```bash
pip install django
pip install mysqlclient  # or use pymysql if preferred
```

> 💡 If you want to use a virtual environment, that's even better (but optional).

---

## ⚙️ Database Setup

### Option A: Using MySQL (For development)

1. Create a MySQL database:
   ```sql
   CREATE DATABASE quiz_app_db CHARACTER SET UTF8;
   ```

2. Update `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'quiz_app_db',
           'USER': 'root',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '3306',
       }
   }
   ```

3. Load your data:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   python manage.py loaddata py_questions.json
   ```

### Option B: Use SQLite (For easier deployment)

In `settings.py`, switch to:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

Then run:

```bash
python manage.py migrate
python manage.py loaddata py_questions.json
```

---

## ✉️ Setup Gmail OTP Email (Required)

In `settings.py`, add your Gmail SMTP settings:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@gmail.com'
EMAIL_HOST_PASSWORD = 'your_app_password'  # Generated from Google Account > Security > App Passwords
```

> ⚠️ Make sure to enable **2-Step Verification** in your Google account and create an **App Password**.

---

## 🧪 Run the Server

```bash
python manage.py runserver
```

Then visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## ✅ How the App Works

1. User signs up with email and password
2. OTP is sent to email via Gmail SMTP
3. User verifies OTP to complete registration
4. After login, user selects subject and level
5. Quiz is loaded and responses are submitted
6. App calculates score and shows results with answers

---

## 📁 Project Structure

```
Quiz_App/
├── testapp/
│   ├── migrations/
│   ├── templates/
│   │   └── testapp/
│   │       ├── signup.html
│   │       ├── otpverify.html
│   │       ├── exam.html
│   │       └── result.html
│   ├── views.py
│   ├── models.py
│   └── forms.py
├── py_questions.json
├── db.sqlite3
├── manage.py
└── TestProject/
    ├── settings.py
    └── urls.py
```

---

## 🔐 Admin Access (Optional)

Create superuser:

```bash
python manage.py createsuperuser
```

Access admin panel at: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 📦 Future Enhancements

- Pagination for questions
- Timer for exams
- PDF certificate generation
- Export results via email
- Dashboard for progress tracking

---

## 💡 Tips

- Make sure to keep your `.json` fixtures clean and UTF-8 encoded
- Always validate OTP and sanitize user inputs
- You can disable `fail_silently=False` in production

---

## 📬 Contact

For queries or feedback:  
📧 Email: [jayaprakash.peddi619@gmail.com](mailto:jayaprakash.peddi619@gmail.com)  
GitHub: [https://github.com/6jp9](https://github.com/6jp9)

---

> 🚧 Built with 💙 using Django and caffeine.
