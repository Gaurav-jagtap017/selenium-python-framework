from pages.login_page import LoginPage
import time
def test_valid_login(setup):
    driver = setup
    login = LoginPage(driver)
    login.login("Admin", "admin123")
    time.sleep(5)
    assert "dashboard" in driver.current_url.lower()
