from page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class FrameAdd(BasePage):
    snat_locator = (By.NAME, "menu")
    pro_locator = (By.XPATH, "/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a")
    add_loactor = (By.CSS_SELECTOR, "body > h1 > span.action-span")
    def menu_frame(self):
        self.driver.switch_to.frame("menu-frame")
    def snat_loact(self):
        self.driver.find_element(*self.snat_locator).click()
        sleep(2)
    def pro_loac(self):
        self.driver.find_element(*self.pro_locator).click()
        sleep(2)
    def defa_content(self):
        self.driver.switch_to.default_content()
    def main_frame(self):
        self.driver.switch_to.frame("main-frame")
    def add_loca(self):
        self.driver.find_element(*self.add_loactor).click()
        sleep(2)
    def add(self):
        self.menu_frame()
        self.snat_loact()
        self.pro_loac()
        self.defa_content()
        self.main_frame()
        self.add_loca()
