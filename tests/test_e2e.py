import os

BASE_PATH = "file://" + os.path.abspath("module13-fastapi-jwt/Frontend/") + "/"


# ✅ REGISTER
def test_register(page):

    page.goto(BASE_PATH + "register.html")

    page.fill("#email", "test@test.com")
    page.fill("#password", "123456")

    page.click("button")

    page.wait_for_timeout(2000)

    assert "success" in page.inner_text("#msg").lower()


# ✅ LOGIN
def test_login(page):

    page.goto(BASE_PATH + "login.html")

    page.fill("#email", "test@test.com")
    page.fill("#password", "123456")

    page.click("button")

    page.wait_for_timeout(2000)

    text = page.inner_text("#msg").lower()

    assert "success" in text

    # ✅ token exists
    token = page.evaluate("localStorage.getItem('token')")

    assert token is not None


# ✅ CALCULATION FLOW
def test_calculation_flow(page):

    # 🔐 LOGIN FIRST
    page.goto(BASE_PATH + "login.html")

    page.fill("#email", "test@test.com")
    page.fill("#password", "123456")

    page.click("button")

    page.wait_for_timeout(2000)

    token = page.evaluate("localStorage.getItem('token')")

    assert token is not None

    # 👉 OPEN CALCULATOR PAGE
    page.goto(BASE_PATH + "index.html")

    # 👉 SET TOKEN
    page.fill("#token", token)

    # ➕ NORMAL ADD
    page.fill("#op1", "5")
    page.fill("#op2", "3")

    page.select_option("#operation", "add")

    page.click("#addBtn")

    page.wait_for_timeout(2000)

    # 📄 LOAD
    page.click("#loadBtn")

    page.wait_for_timeout(2000)

    content = page.content()

    assert "8" in content

    # ✅ POWER TEST
    page.fill("#op1", "2")
    page.fill("#op2", "3")

    page.select_option("#operation", "power")

    page.click("#addBtn")

    page.wait_for_timeout(2000)

    assert "8" in page.content()

    # ✅ MOD TEST
    page.fill("#op1", "10")
    page.fill("#op2", "3")

    page.select_option("#operation", "mod")

    page.click("#addBtn")

    page.wait_for_timeout(2000)

    assert "1" in page.content()

    # ❌ DELETE
    page.click("text=Delete")

    page.wait_for_timeout(2000)