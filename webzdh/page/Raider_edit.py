from selenium.webdriver.common.by import By
# from selenium import webdriver
from page.base_page import BasePage
from time import sleep
class AddRaider(BasePage):
    """
    类的定位器
    """
    nameActivity_locator=(By.XPATH,"/html/body/div[1]/form/table/tbody/tr[1]/td[2]/input")