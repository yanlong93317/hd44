from cases.base_case import BaseCase  # 调用自己所写的类
from time import sleep
from model.login_page import loginpage
from model import bacKlogin_datas
from page.RaiderAdd import AddRaider
from model import RaiderAdd_call
from page.frame import FrameAdd
from page.frame_edit import FrameEdit
from page.frame_aver import FramePage22
import unittest  # 引入自动化测试框架


class TestLogin(BaseCase):  # 定义一个类用于测试
    def test_1raideradd(self):  # 定义一个函数用于登录
        lp = loginpage(self.driver)  # 调用类用于输入数据
        username, password = bacKlogin_datas.login()[3]  # 获取数据
        lp.login(username, password)  # 填入获取到的数据
        sleep(2)
        fp = FrameAdd(self.driver)
        fp.add()
        # FramePage(self.driver)
        pp = AddRaider(self.driver)
        huodongm, shanp, miaoshu = RaiderAdd_call.raider_datas()[3]  # 获取添加活动需要的数据
        pp.input(huodongm, shanp, miaoshu)  # 填入数据
        sleep(2)
        nameActivity = RaiderAdd_call.raider_datas()[3][1]  # 定义变量并赋值
        nameAct = str(RaiderAdd_call.raider_datas()[3][0])
        ll = FramePage22(self.driver)
        sleep(2)
        assert_text = ll.aver(nameActivity)
        if assert_text == nameAct:
            print("成功")
        else:
            raise AssertionError("失败")

    # def test_2editRaider(self):
    #     lp = loginpage(self.driver)  # 调用类用于输入数据
    #     username, password = bacKlogin_datas.login()[3]  # 获取数据
    #     lp.login(username, password)  # 填入获取到的数据
    #     sleep(2)
    #     fp = FrameEdit(self.driver)
    #     fp.degr()
    #     nameActivity = RaiderAdd_call.raider_datas()[1][1]  # 定义变量并赋值
    #     ll = FramePage22(self.driver)
    #     sleep(2)
    #     assert_text = ll.act_alter(nameActivity)
    #     if assert_text.text == nameActivity:
    #         print("成功")
    #     else:
    #         raise AssertionError("失败")

    # def test_3delRaider(self):
    #     lp = loginpage(self.driver)  # 调用类用于输入数据
    #     username, password = bacKlogin_datas.login()[4]  # 获取数据
    #     lp.login(username, password)  # 填入获取到的数据
    #     sleep(2)
    #     fp = FramePage(self.driver)
    #     fp.delll()
    #     sleep(2)
    #     nameRaider_text = self.driver.find_element_by_xpath("//*[@id='listDiv']/table/tbody/tr[2]/td[2]")
    #     ll = FramePage22(self.driver)
    #     sleep(2)
    #     assert_text = ll.remove_activity()
    #     if assert_text.text != nameRaider_text:
    #         print("成功")
    #     else:
    #         raise AssertionError("失败")


if __name__ == "__main__":
    unittest.main()  # 开始执行用例
