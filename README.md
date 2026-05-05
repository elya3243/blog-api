# Blog API (Django REST Framework)

A scalable RESTful API built with Django REST Framework, featuring authentication, post management, comments, likes, filtering, pagination, and optimized database queries.

---

## Features

* JWT Authentication (Register / Login)
* Post CRUD (Create, Read, Update, Delete)
* Comment System
* Like / Unlike System
* Search & Filtering
* Pagination
* Query Optimization (select_related, prefetch_related)
* Permission System (Only owners can edit/delete)

---

## Tech Stack

* Python
* Django
* Django REST Framework
* Simple JWT

---

## API Endpoints

### Auth

* POST `/api/v1/token/`
* POST `/api/v1/register/`

### Posts

* GET `/api/v1/posts/`
* POST `/api/v1/posts/`
* GET `/api/v1/posts/<id>/`
* PATCH `/api/v1/posts/<id>/`
* DELETE `/api/v1/posts/<id>/`

### Comments

* GET `/api/v1/comments/`
* POST `/api/v1/comments/`

### Likes

* POST `/api/v1/posts/<id>/like/`

---

## Installation

```bash
git clone https://github.com/yourusername/blog-api.git
cd blog-api

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```
SECRET_KEY=your_secret_key
DEBUG=True
```

---

## Run the Project

```bash
python manage.py migrate
python manage.py runserver
```

---

## Example Request

### Create a Post

```json
POST /api/v1/posts/

{
  "title": "My First Post",
  "content": "This is a test post"
}
```

---

## What I Learned

* Building RESTful APIs with Django REST Framework
* Authentication & Authorization using JWT
* Query optimization techniques
* Clean architecture (separating serializers and views)
* Designing scalable APIs

---

## Author

Elyas Derakhshanfar
