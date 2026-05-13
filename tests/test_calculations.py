from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# 🔐 GET TOKEN DYNAMICALLY
def get_token():

    # register (ignore if already exists)
    client.post("/users/register", json={
        "email": "test@test.com",
        "password": "123456"
    })

    # login
    res = client.post(
        "/users/login",
        data={
            "username": "test@test.com",
            "password": "123456"
        }
    )

    token = res.json()["access_token"]
    return token


def get_headers():
    token = get_token()
    return {"Authorization": f"Bearer {token}"}


# ✅ CREATE → READ → UPDATE → DELETE
def test_crud():

    headers = get_headers()

    # ➕ CREATE
    res = client.post("/calculations", json={
        "operand1": 2,
        "operand2": 2,
        "operation": "add"
    }, headers=headers)

    assert res.status_code == 200

    data = res.json()
    calc_id = data["id"]

    # 📄 READ
    res = client.get(f"/calculations/{calc_id}", headers=headers)

    assert res.status_code == 200
    assert res.json()["result"] == 4

    # ✏️ UPDATE
    res = client.put(f"/calculations/{calc_id}", json={
        "operand1": 3,
        "operand2": 3,
        "operation": "add"
    }, headers=headers)

    assert res.status_code == 200
    assert res.json()["result"] == 6

    # ❌ DELETE
    res = client.delete(f"/calculations/{calc_id}", headers=headers)

    assert res.status_code == 200

    # 🔁 VERIFY DELETE
    res = client.get(f"/calculations/{calc_id}", headers=headers)

    assert res.status_code == 404


# ❌ INVALID OPERATION
def test_invalid_operation():

    headers = get_headers()

    res = client.post("/calculations", json={
        "operand1": 5,
        "operand2": 2,
        "operation": "wrong"
    }, headers=headers)

    # Pydantic validation error
    assert res.status_code == 422


# ❌ DIVIDE BY ZERO
def test_divide_by_zero():

    headers = get_headers()

    res = client.post("/calculations", json={
        "operand1": 5,
        "operand2": 0,
        "operation": "divide"
    }, headers=headers)

    assert res.status_code == 400


# 🔒 UNAUTHORIZED ACCESS
def test_unauthorized():

    res = client.get("/calculations")

    assert res.status_code == 401


# ✅ POWER OPERATION
def test_power():

    headers = get_headers()

    res = client.post("/calculations", json={
        "operand1": 2,
        "operand2": 3,
        "operation": "power"
    }, headers=headers)

    assert res.status_code == 200
    assert res.json()["result"] == 8


# ✅ MODULUS OPERATION
def test_modulus():

    headers = get_headers()

    res = client.post("/calculations", json={
        "operand1": 10,
        "operand2": 3,
        "operation": "mod"
    }, headers=headers)

    assert res.status_code == 200
    assert res.json()["result"] == 1