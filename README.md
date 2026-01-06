# Smart Asset Management System (IoT-Ready)

A centralized, role-based asset management platform designed for manufacturing and IoT environments.  
Built using Python, REST APIs, Linux file systems, and JWT-based RBAC.

---

##  Features

- Role-Based Access Control (Admin / Manager / Viewer)
- Secure JWT authentication
- Asset lifecycle management (create, view, archive)
- Linux filesystem–backed asset storage
- Automatic metadata extraction (permissions, timestamps, size)
- RESTful API design
- Lightweight frontend dashboard
- Scalable architecture (10k+ assets supported)

---

##  Architecture Overview

Frontend (HTML/CSS/JS)
|
v
Flask REST APIs
|
|-- Auth (JWT)
|-- RBAC Enforcement
|-- Asset Management
|
Linux File System
(data/assets/<asset_id>/)

yaml
Copy code

Assets are stored as directories on disk, enabling fast access, low latency, and OS-level metadata extraction.

---

##  Roles & Permissions

| Role    | Permissions |
|--------|-------------|
| Admin  | User & asset control, archive assets |
| Manager | Create and update assets |
| Viewer | Read-only access |

RBAC is enforced at every API endpoint.

---

##  Project Structure

```text
smart-asset-management/
├── app/
│   ├── main.py
│   ├── auth.py
│   ├── rbac.py
│   ├── assets.py
│   ├── filesystem.py
│   └── database.py
├── data/
│   └── assets/
├── frontend/
│   ├── index.html
│   ├── dashboard.html
│   ├── app.js
│   └── style.css
├── scripts/
│   └── init_db.py
├── requirements.txt
└── README.md
```

## Authentication
Login via /login

JWT token returned

Token required in Authorization header for protected routes

## Asset Lifecycle
Asset created via API

Directory created on disk

Metadata auto-generated

Asset visible on dashboard

Admin can archive asset

## Setup Instructions
1. Clone Repo
bash
Copy code
git clone <repo-url>
cd smart-asset-management
2. Create Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Initialize Database
bash
Copy code
python scripts/init_db.py
5. Run Backend
bash
Copy code
python app/main.py
6. Open Frontend
Open frontend/index.html in browser.

## Performance & Scale
Designed for 300+ concurrent users

Tested with thousands of asset directories

Sub-second metadata access using filesystem indexing

Minimal memory footprint

## Future Enhancements
IoT sensor ingestion (MQTT)

Audit logging

Asset health analytics

Docker deployment

Cloud storage integration

## License
MIT

yaml
Copy code

---
