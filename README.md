# 🏆 Sports Tournament Management Backend  

This is the **backend** for a sports tournament management app, built using **Django, Django REST Framework (DRF), and SQLite3**. It provides APIs to manage teams, players, and matches efficiently.  

---

## 🌍 Live Demo  
🚧 *(unfortunatly it's backend what do want me to show you. (that's why I like backendj))*  

---

## 📜 About  

This project simplifies the management of sports tournaments by providing an intuitive system to:  
- ✅ **Create and manage teams**  
- ✅ **Register and track players**  
- ✅ **Schedule and manage matches**  
- ✅ **Keep track of scores and rankings**  

The API follows **RESTful principles** and is designed to be easily integrated with a frontend or mobile application.  

---

## ⚙️ Installation Guide  

### 🔹 Prerequisites  
Ensure you have the following installed:  
- Python 3.12+  
- Django & Django REST Framework  
- SQLite3 (default Django database)  
- Docker

### 🔹 Setup Instructions  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/thenew-programer/sportify.git
   cd sportify
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py createsuperuser
   python manage.py runserver
    ```
#### 🐳 Running with Docker
##### Build and Run the container
1. **Build the docker image**
    ```bash
    docker build -t sportify .
    ```
1. **Run The container**
    ```bash
    docker run -p 8000:8000 sportify

    ```

## API Endpoints
### Authentification
- `POST /api/auth/token` - Get access and refresh token (login)
- `POST /api/auth/token/refresh` - Refresh expired access token
- `POST /api/auth/token/verify` - Verify access token

### Team Management
- `GET /api/teams` - Retrieve all teams
- `POST /api/teams/create/` - Create a team

### Player Management
- `GET /api/players` - Retrieve all players
- `POST /api/players/create` - Create a player

### Match Management
- `GET /api/matches` - Retrieve all matches
- `POST /api/matches/create/` - Create a match

## 📷 Screenshots
`backend can be seen only by blind people`

## 🛠️ Technologies Used
- Django & Django Rest Framework (Backend)
- Sqlite3 (database)
- JWT Authentication
- Docker (optional for deployment)

## 🔥 Contributing
If you’d like to contribute, feel free to open an issue or submit a pull request!

## 📄 License

MIT License © 2025 Joseph Bouryal

### 📌 Notes:  
- Replace **YOUR_USERNAME** and **YOUR_REPO** with your actual GitHub details.  
- Add **a live demo URL** if deployed.  
- Include **API screenshots** (Swagger UI or Postman tests).  

This **README** is structured, professional, and ready for your **hackathon project! 🚀**
