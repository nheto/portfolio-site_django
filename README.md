# 🧰 Ernesto's Django Portfolio Site

A dynamic, Bootstrap-styled portfolio built with Django to showcase web projects, team leadership, and content migration expertise. Designed for job applications and professional growth in IT/web leadership roles.

## 🚀 Features

- Responsive homepage with clean Bootstrap design
- Dynamic portfolio section powered by Django models
- Admin panel for easy project management
- Secure settings via `python-decouple`
- Static and media file handling for production-ready deployment

## 🛠️ Tech Stack

- **Backend**: Django 4.x
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **Tools**: Python-decouple, SQLite (default), Git
- **Deployment**: Localhost, with production-ready structure

## 📦 Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   cd your-repo-name
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate on Windows
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Configure .env using python-decouple
   DEBUG=True
   SECRET_KEY=your-secret-key
5. Run migrations and start the server:
   ```bash
   python manage.py migrate
   python manage.py runserver

## 📁 Project Structure
```text
portfolio_site/
│
├── static/         # CSS, JS, images
├── media/          # Uploaded files
├── templates/      # HTML templates
│
├── portfolio/      # Project showcase app
│   ├── models.py
│   ├── views.py
│   └── admin.py
│
├── about/          # Personal bio app
│
├── manage.py
└── requirements.txt

## 🧪 Testing & Deployment

- Media and static files configured for local and production use
- Admin panel tested for dynamic content updates
- Deployment-ready with secure settings and modular structure

## 🙋 About the Author

Ernesto is a Web Content Migration Specialist transitioning into IT/web leadership roles. Passionate about clean design, scalable workflows, and collaborative development






   
