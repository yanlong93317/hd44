from page.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class FramePage22(BasePage):
    def act_alter(self, dd):
        """
        修改活动名称
        :param dd:
        :return:
        """
        NAmeAct = self.driver.find_element(By.NAME, "snatch_name")  # 定位到输入框
        NAmeAct.clear()  # 清空输入框
        NAmeAct.send_keys(dd)  # 输入数据
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "body > div.main-div >"
                                                  " form > table > tbody > tr:nth-child(11) "
                                                  "> td > input:nth-child(1)").click()  # 点击确定按钮
        assert_text = self.driver.find_element_by_xpath('//*[@id="listDiv"]/table/tbody/tr[2]/td[2]')
        sleep(3)
        return assert_text

    def remove_activity(self):
        """
        删除
        :return:
        """
        assert_text = self.driver.find_element_by_xpath("//*[@id='listDiv']/table/tbody/tr[2]/td[2]")
        sleep(2)
        return assert_text

    def aver(self, dd):
        """
        寻找用于断言的数据
        :param dd:
        :return:
        """
        self.driver.get("http://192.168.1.134:8080/upload")
        self.driver.refresh()
        sleep(2)
        self.driver.find_element(By.NAME, "keywords").send_keys(dd)
        self.driver.find_element(By.NAME, "imageField").click()
        sleep(2)
        self.driver.refresh()
        self.driver.find_element(By.CSS_SELECTOR, "#compareForm > div > div").click()
        sleep(3)
        text1 = self.driver.find_element(By.CSS_SELECTOR, "#ECS_FORMBUY > div > a:nth-child(2)").text
        return text1
