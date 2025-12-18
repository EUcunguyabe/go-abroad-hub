from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_success():
    res = client.post(
        "/auth/register",
        json={"full_name": "Blandine", "email": "blandine@test.com", "password": "secret123"},
    )
    assert res.status_code == 200
    body = res.json()
    assert "id" in body
    assert body["email"] == "blandine@test.com"


def test_register_duplicate_email_fails():
    client.post(
        "/auth/register",
        json={"full_name": "User1", "email": "dup@test.com", "password": "secret123"},
    )
    res = client.post(
        "/auth/register",
        json={"full_name": "User2", "email": "dup@test.com", "password": "secret123"},
    )
    assert res.status_code == 400
    assert "error" in res.json()


def test_login_success_and_fail():
    client.post(
        "/auth/register",
        json={"full_name": "LoginUser", "email": "login@test.com", "password": "pass1234"},
    )

    ok = client.post("/auth/login", json={"email": "login@test.com", "password": "pass1234"})
    assert ok.status_code == 200
    assert ok.json()["message"] == "Login successful"

    bad = client.post("/auth/login", json={"email": "login@test.com", "password": "wrong"})
    assert bad.status_code == 400


def test_create_opportunity_and_apply():
    user_res = client.post(
        "/auth/register",
        json={"full_name": "Applicant", "email": "applicant@test.com", "password": "secret123"},
    )
    user_id = user_res.json()["id"]

    opp_res = client.post(
        "/opportunities",
        json={"title": "Erasmus Germany", "country": "Germany", "type": "STUDY", "deadline": "2026-01-31"},
    )
    assert opp_res.status_code == 200
    opp_id = opp_res.json()["id"]

    app_res = client.post("/applications", json={"user_id": user_id, "opportunity_id": opp_id})
    assert app_res.status_code == 200
    assert app_res.json()["status"] == "SUBMITTED"
