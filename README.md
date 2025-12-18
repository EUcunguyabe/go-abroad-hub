# Go Abroad Hub

A simple web application that helps students discover opportunities abroad
(study, work, volunteer) and track their applications.

This project is developed for the **Final Exam – Best Programming Practices and Design Patterns**.

---

## 1. Project Overview

**Problem**  
Students often struggle to find and track international opportunities because information is scattered across many platforms.

**Solution**  
Go Abroad Hub centralizes opportunities and allows users to:
- Register and log in
- View opportunities
- Apply for opportunities
- Track application status

---

## 2. Technology Stack

- **Language:** Python  
- **Framework:** FastAPI  
- **Architecture:** MVC-style (Controllers, Services, Models)  
- **Design Pattern:** Singleton  
- **Testing:** Pytest  
- **Containerization:** Docker  
- **Version Control:** GitHub  

---

## 3. Project Structure

go-abroad-hub/
│
├── app/
│ ├── main.py # Application entry point
│ ├── controllers.py # API routes
│ ├── services.py # Business logic
│ ├── models.py # Data models (OOP)
│ ├── singleton.py # Singleton pattern (in-memory database)
│ ├── exceptions.py # Custom exceptions
│ └── init.py
│
├── tests/
│ ├── test_api.py # Automated test cases
│ └── init.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md


---

## 4. Design Pattern Used

### Singleton Pattern

The **Singleton** pattern is used to manage a single shared in-memory database instance.

- Ensures only one database instance exists
- Avoids inconsistent data across services
- Implemented in `singleton.py`

---

## 5. API Endpoints

### Authentication
- `POST /auth/register` – Register a new user
- `POST /auth/login` – Login user

### Opportunities
- `GET /opportunities` – List all opportunities
- `POST /opportunities` – Create a new opportunity

### Applications
- `POST /applications` – Apply for an opportunity
- `GET /applications` – List all applications

Swagger UI:
http://127.0.0.1:8000/docs


---

## 6. How to Run the Application (Local)

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload

http://127.0.0.1:8000/docs

7. Testing
Run automated tests
$env:PYTHONPATH="."
pytest -q

Testing Plan
| Test ID | Scenario               | Expected Result           |
| ------- | ---------------------- | ------------------------- |
| TC-01   | Register user          | User created successfully |
| TC-02   | Duplicate registration | Error returned            |
| TC-03   | Login success          | Login successful          |
| TC-04   | Login failure          | Error returned            |
| TC-05   | Create opportunity     | Opportunity saved         |
| TC-06   | Apply for opportunity  | Status = SUBMITTED        |

8. Dockerization
Files

Dockerfile

docker-compose.yml

Run with Docker
docker compose up --build

Application will be available at:
http://localhost:8000/docs

9. Version Control

The project is version-controlled using GitHub.
Multiple commits demonstrate incremental development.

10. Conclusion

This project demonstrates:

Clean code and best practices

OOP and layered architecture

Design pattern usage

Automated testing

Dockerization

Professional documentation
