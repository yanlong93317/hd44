from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.select import Select  #引入select类
from model import bacKlogin_datas
import unittest
class CuXiao(unittest.TestCase):
    def test_cuxiao(self):
        driver=webdriver.Chrome()
        driver.get("http://192.168.1.134:8080/upload/admin")  #打开网址
        username,password=bacKlogin_datas.login()[2]   #输入用户名和密码进行登录
        # driver.find_element(By.NAME,"username").send_keys("huachuan")
        # sleep(2)
        # driver.find_element(By.NAME,"password").send_keys("admin123456")
        # sleep(2)

        driver.find_element(By.CSS_SELECTOR,"input[value='进入管理中心']").click()
        sleep(3)
        driver.switch_to.frame("menu-frame")  #定位到menu-frame
        driver.find_element(By.NAME,"menu").click()
        driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/ul/li[1]/ul/li[1]/a").click()
        driver.switch_to.default_content() #返回到最外层
        driver.switch_to.frame("main-frame")
        driver.find_element(By.CSS_SELECTOR,"body > h1 > span.action-span").click()
        sleep(1)
        yuans="hello1"
        driver.find_element(By.NAME,"snatch_name").send_keys(yuans)
        driver.find_element(By.NAME,"keywords").send_keys("宝马xxx")
        driver.find_element(By.CSS_SELECTOR,"input[value=' 搜索 ']").click()
        sleep(2)

        xiala_locator=driver.find_element(By.NAME,"goods_id")
        select=Select(xiala_locator)
        select.select_by_index(0)   #为活动商品名找到商品
        dd=driver.find_element_by_name("goods_id").text
        dd=str(dd).strip()
        print(dd)
        miaoshu=driver.find_element(By.CSS_SELECTOR,"body > div.main-div >"
                                     " form > table > tbody > tr:nth-child(10) "
                                    "> td:nth-child(2) > textarea").send_keys("我们的毛衣很暖和")
        driver.find_element(By.CSS_SELECTOR,"input[value=' 确定 ']").click()
        sleep(4)

        driver.get("http://192.168.1.134:8080/upload")
        driver.refresh()
        sleep(2)
        driver.find_element(By.NAME,"keywords").send_keys(dd)
        driver.find_element(By.NAME,"imageField").click()
        sleep(2)
        driver.refresh()
        tupian=driver.find_element(By.CSS_SELECTOR,"#compareForm > div > div").click()
        sleep(3)
        text1=driver.find_element(By.XPATH,"//*[@id='ECS_FORMBUY']/div/a[6]").text
        print(text1)
        if text1==yuans:
            print("成功")
        else:
            raise AssertionError("错误")
    # def test_cuxiao2(self):
    #     driver=webdriver.Chrome()
    #     driver.get("http://192.168.1.134:8080/upload/admin")  #打开网址
    #     # username,password=houtai_logon.hou_login()[3]    #输入用户名和密码进行登录
    #     username=driver.find_element(By.NAME,"username").send_keys("huachuan")
    #     sleep(2)
    #     password=driver.find_element(By.NAME,"password").send_keys("admin123456")
    #     sleep(2)
    #     driver.find_element(By.CSS_SELECTOR,"input[value='进入管理中心']").click()
    #     sleep(2)
    #     driver.switch_to.frame("menu-frame")  #定位到menu-frame
    #     cuxiao_locator=driver.find_element(By.NAME,"menu").click()
    #     duobao_locaot=driver.find_element(By.CSS_SELECTOR,"#menu-ul > "
    #                                             "li.explode.lis.ico2_1 > ul > li:nth-child(1) > a").click()
    #     driver.switch_to.default_content() #返回到最外层
    #     driver.switch_to.frame("main-frame")
    #     #定位器
    #     table_loc=(By.CSS_SELECTOR,"#listDiv > table > tbody")
    #     table_lelement=driver.find_element(*table_loc)
    #     tr_loc=(By.CSS_SELECTOR,"#listDiv > table > tbody > tr:nth-child(2)")  #找到行
    #     tr_lists=table_lelement.find_elements(*tr_loc)
    #     for tr in tr_lists:
    #         tr.find_element_by_xpath('//td[8]/a[2]/img').click()  #利用绝对路径找到编辑按钮并点击
    #         sleep(1)
    #     huod="我的中国"
    #     tt=driver.find_element(By.NAME,"snatch_name")
    #     tt.clear()
    #     tt.send_keys(huod)
    #     sleep(2)
    #     driver.find_element(By.CSS_SELECTOR,"body > div.main-div >"
    #                                         " form > table > tbody > tr:nth-child(11) "
    #                                         "> td > input:nth-child(1)").click()
    #     sleep(3)
    #     yy=driver.find_element_by_xpath("/html/body/form/div/table/tbody/tr[2]/td[2]")
    #     if yy.text==huod:
    #         print("成功")
    #     else:
    #         raise AssertionError("失败")
    # def test_cuxiao3(self):
    #     driver=webdriver.Chrome()
    #     driver.get("http://192.168.1.134:8080/upload/admin")  #打开网址
    #     # username,password=houtai_logon.hou_login()[3]    #输入用户名和密码进行登录
    #     username=driver.find_element(By.NAME,"username").send_keys("admin")
    #     sleep(2)
    #     password=driver.find_element(By.NAME,"password").send_keys("admin123456")
    #     sleep(2)
    #     driver.find_element(By.CSS_SELECTOR,"input[value='进入管理中心']").click()
    #     sleep(3)
    #     driver.switch_to.frame("menu-frame")  #定位到menu-frame
    #     driver.find_element(By.XPATH,"//*[@id='menu-ul']/li[2]").click()
    #     driver.find_element(By.XPATH,"//*[@id='menu-ul']/li[2]/ul/li[1]/a").click()
    #     driver.switch_to.default_content() #返回到最外层
    #     driver.switch_to.frame("main-frame")
    #     # 定位器
    #     table_del = (By.CSS_SELECTOR, "#listDiv > table > tbody")
    #     driver.find_element(*table_del)
    #     tr_loc = (By.CSS_SELECTOR, "#listDiv > table > tbody > tr:nth-child(2)")  # 找到行
    #     driver.find_element(By.XPATH,"//*[@id='listDiv']/table/tbody/tr[2]/td[8]/a[3]").click()
    #     sleep(5)
    #     driver.switch_to.alert.accept()
if __name__=="__main__":
    unittest.main()




