from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
from model import RaiderAdd_call


def shopact(self):
    yuans = RaiderAdd_call.raider_datas()[1][0]
    self.driver.find_element(By.NAME, "snatch_name").send_keys(yuans)
    self.driver.find_element(By.NAME, "keywords").send_keys("宝马xxx")
    self.driver.find_element(By.CSS_SELECTOR, "input[value=' 搜索 ']").click()
    sleep(2)
    xiala_locator = self.driver.find_element(By.NAME, "goods_id")
    select = Select(xiala_locator)
    select.select_by_index(0)  # 为活动商品名找到商品
    dd = self.driver.find_element_by_name("goods_id").text
    dd = str(dd).strip()
    return dd
