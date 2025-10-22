# Django Forum Project

A full-featured discussion forum built with Django.

## Features

- ✅ User registration and authentication
- ✅ Categories and forums organization
- ✅ Thread creation and management
- ✅ Reply system
- ✅ Search functionality
- ✅ Pagination
- ✅ User profiles (auto-created)
- ✅ Responsive design with Bootstrap
- ✅ Permission system (owners can edit/delete own content)
- ✅ Success messages
- ✅ Breadcrumb navigation

## Technology Stack

- **Backend:** Django 5.2.7
- **Database:** SQLite
- **Frontend:** Bootstrap 5.3, Bootstrap Icons
- **Authentication:** Django built-in auth system

## Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Setup

1. Clone the repository:
```bash
git clone 
cd django-forum-project
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- **Windows:**
```bash
  venv\Scripts\activate
```
- **Mac/Linux:**
```bash
  source venv/bin/activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

8. Open your browser and go to:
```
http://127.0.0.1:8000/
```

## Usage

### Admin Panel

Access the admin panel at `http://127.0.0.1:8000/admin/` to:
- Create categories
- Create forums
- Manage threads and replies
- Manage users

### User Features

1. **Register:** Create a new account
2. **Login:** Access your account
3. **Browse Forums:** View categories and forums
4. **Create Threads:** Start new discussions
5. **Reply:** Participate in discussions
6. **Search:** Find threads by title or content
7. **Edit/Delete:** Manage your own content

## Project Structure
```
django-forum-project/
├── forum/              # Main forum app
│   ├── models.py       # Category, Forum, Thread, Reply
│   ├── views.py        # All views
│   ├── urls.py         # URL routing
│   └── admin.py        # Admin configuration
├── accounts/           # User authentication app
│   ├── models.py       # Profile model
│   ├── views.py        # Register view
│   └── urls.py         # Auth URLs
├── templates/          # HTML templates
│   ├── base.html       # Base template
│   ├── forum/          # Forum templates
│   └── accounts/       # Auth templates
├── media/              # User uploads (avatars)
├── static/             # CSS, JS, images
└── manage.py           # Django management script
```

## Models

### Category
- name
- description
- ordering

### Forum
- category (ForeignKey)
- title
- description
- ordering

### Thread
- forum (ForeignKey)
- author (ForeignKey to User)
- title
- body
- is_closed
- created_at, updated_at

### Reply
- thread (ForeignKey)
- author (ForeignKey to User)
- content
- created_at, updated_at

### Profile
- user (OneToOneField)
- bio
- avatar
- created_at

## Contributing

This is a student project created as part of an internship assignment.

## License

This project is created for educational purposes.

## Author

Created as part of Inteliate Internship Program

## Project Status

✅ **Completed:** All MVP features implemented and tested