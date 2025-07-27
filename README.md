# 🔧 SkillStack – Backend

SkillStack is a personal skill-tracking system that helps users track progress in online courses, tutorials, and certifications.

This is the **Django REST Framework** backend that powers the SkillStack app.

---

## ⚙️ Features

- ✅ User registration and login 
- ✅ Add, update, delete, and view skills
- ✅ Track status: Started, In-progress, Completed
- ✅ Store platform, resource type, hours, difficulty, and notes

---

## 🛠️ Tech Stack

- Python + Django + Django REST Framework
- SQLite 
- CORS Headers for frontend access

---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/your-username/SkillStack-Backend.git
cd SkillStack-Backend

# Create virtual environment
python -m venv env
source env/bin/activate  # For Windows: env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations and start server
python manage.py migrate
python manage.py runserver

---

🔗 Frontend Repo
👉 SkillStack Frontend (React)