# Base page and Two Child Class

class BasePage:
    def __init__(self,driver):
        self.driver = driver
        print("Default Cons")

    def go_to_url(self,url):
        pass

    def read_file(self):
        pass

    def write_file(self):
        pass


class LoginPage(BasePage):
    def __init__(self,driver):
        super().__init__(driver) # Call my parent constructor

    def enter_username(self, username):
        # Code to enter username
        pass

    def enter_password(self, password):
        # Code to enter password
        pass

    def click_login_button(self):
        # Code to click login button
        pass

class Homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_login_success(self):
        # Code to verify successful login
        pass

    def click_logout_button(self):
        # Code to click logout button
        pass



# driver = ChromeDriver()
#
# login = LoginPage(driver)
# login.go_to_url("http://app.vwo.com")
# login.enter_password("admin")
# login.enter_username("admin")
# login.click_login_button()

