from pages.common_page import BasePage
from selenium.webdriver.common.by import By
class LoginPage(BasePage):
    userName=(By.NAME,"username")
    passWord=(By.NAME,"password")
    LoginButton=(By.XPATH,'//button["submit"]')
    def login(self, username, password):
        self.enter_text(self.userName, username)
        self.enter_text(self.passWord, password)
        self.click(self.LoginButton)
                        

