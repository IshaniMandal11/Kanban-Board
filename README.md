# Kanban Board — Django

A task management board built with Django, HTML, and CSS. Organise work across **Todo**, **In Progress**, and **Done** columns.

**Live Demo:** [kanban-board.onrender.com](https://kanban-board.onrender.com) *(update this link after deploy)*

---

## Features

- Add tasks with a title and optional description to any column
- Move cards left or right across columns with one click
- Delete tasks with a confirmation prompt
- Card count badge per column
- Clean, responsive CSS layout — no external frameworks
- Persistent storage via SQLite

## Tech Stack

| Layer | Technology |
|---|---|
| Backend | Python 3.13, Django 6.0 |
| Frontend | HTML5, CSS3 (Grid, Flexbox) |
| Database | SQLite |
| Deployment | Render |

## Run Locally

```bash
# 1. Clone
git clone https://github.com/IshaniMandal11/Kanban-Board.git
cd Kanban-Board/django_series/isha

# 2. Install dependencies
pip install -r requirements.txt

# 3. Migrate and seed columns
python manage.py migrate
python manage.py setup_kanban

# 4. Start the dev server
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser.

## Project Structure

```
django_series/isha/
├── isha/               # Project settings & URLs
├── kanban/             # Kanban app
│   ├── models.py       # Column, Task models
│   ├── views.py        # add / move / delete views
│   ├── urls.py
│   ├── admin.py
│   ├── templates/
│   │   └── kanban/board.html   # All HTML + CSS
│   └── management/commands/setup_kanban.py
├── manage.py
└── requirements.txt
```
