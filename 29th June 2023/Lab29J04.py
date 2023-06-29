# class BasePage:
#     def __init__(self, driver):
#         self.driver = driver
#
# class LoginPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#
#     def enter_username(self, username):
#         # Code to enter username
#         pass
#
#     def enter_password(self, password):
#         # Code to enter password
#         pass
#
#     def click_login_button(self):
#         # Code to click login button
#         pass
#
# class HomePage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver) #Parent Constructor
#
#     def verify_login_success(self):
#         # Code to verify successful login
#         pass
#
#     def click_logout_button(self):
#         # Code to click logout button
#         pass
#
#
# # # Example usage
# # from selenium import webdriver
# #
# # # Create a webdriver instance (assuming Selenium WebDriver is being used)
# # driver = webdriver.Chrome()
# #
# # # Create LoginPage object
# # login_page = LoginPage(driver)
# #
# # # Perform login actions
# # login_page.enter_username("username")
# # login_page.enter_password("password")
# # login_page.click_login_button()
# #
# # # Create HomePage object
# # home_page = HomePage(driver)
# #
# # # Perform actions on the home page
# # home_page.verify_login_success()
# # home_page.click_logout_button()
# #
# # # Close the browser
# # driver.quit()
