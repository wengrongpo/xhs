# -*- coding: utf-8 -*-
# @Time    : 2023/6/20 10:24
# @Author  : XuLei
# @FileName: ForumPage.py
# @Software: PyCharm

import time
import allure
from PageEle.BasePage import Page
from PageEle.selector.ForumSelector import *
from Common.set import Set
from Common.Tools import Tools
from Common.mail import GetCode
from Common.data_deal import DataDeal


class ForumPage(Page):
    @allure.step("点击Gotcha！按钮")
    def click_gotcha(self):
        if self.find_element(ForumSelector.GOTCHA_LAB, model='assert', timeout=10):
            self.slip_find_click(ForumSelector.GOTCHA_LAB)
        else:
            Tools.step_log("已经点击过gotcha")
        self.assert_ele(ForumSelector.FORUM_TAB, "进入Forum页面")

    @allure.step("修改并验证国家站点为Japan")
    def modify_site_to_japan(self):
        self.find_element(ForumSelector.COUNTRY_SHOW).click()
        self.assert_ele(ForumSelector.COUNTRY_LAB, "跳转至切换国家站点界面")
        self.find_element(ForumSelector.JAPAN_LAB).click()
        self.find_element(ForumSelector.SAVE_BUTTON).click()
        self.find_element(ForumSelector.SEARCH_BUTTON).click()
        self.assert_ele(ForumSelector.SEARCH_BOX, "跳转至搜索界面")
        self.find_element(ForumSelector.SEARCH_BOX).send_keys('をスマートになる')
        if Set.client == "android":
            self.driver.execute_script('mobile:performEditorAction', {"action": "search"})
        elif Set.client == "ios":
            self.find_element(ForumSelector.SEARCH_BOX).click()
            self.find_element(ForumSelector.SEARCH_BOX_KEYBOARD).click()
        time.sleep(3)
        post_content = self.find_element(ForumSelector.SEARCH_JAPAN_CONTENT)
        assert 'をスマートになる' in post_content.text, "站点切换成Japan失败"
        logger.info('国家站点切换成Japan成功')
        self.find_element(ForumSelector.RETURN_BUTTON).click()
        self.find_element(ForumSelector.COUNTRY_SHOW).click()
        self.find_element(ForumSelector.US_LAB).click()
        self.find_element(ForumSelector.SAVE_BUTTON).click()
        logger.info('国家站点切换回US成功')

    @allure.step("搜索框搜索Meross正确")
    def modify_search_function(self):
        self.find_element(ForumSelector.SEARCH_BUTTON).click()
        self.assert_ele(ForumSelector.SEARCH_BOX, "跳转至搜索界面")
        self.find_element(ForumSelector.SEARCH_BOX).send_keys('Meross')
        if Set.client == "android":
            self.driver.execute_script('mobile:performEditorAction', {"action": "search"})
        elif Set.client == "ios":
            self.find_element(ForumSelector.SEARCH_BOX).click()
            self.find_element(ForumSelector.SEARCH_BOX_KEYBOARD).click()
        time.sleep(3)
        post_content = self.find_element(ForumSelector.SEARCH_PAGE_CONTENT)
        assert 'Meross' in post_content.text, "没有包含'Meross'关键字的帖子"
        logger.info('搜索出来的帖子中包含"Meross"关键字')
        self.find_element(ForumSelector.RETURN_BUTTON).click()

    @allure.step("Forum页面tag标签显示正确")
    def modify_forum_tag_with_login_in(self):
        global user_time1, user_time2
        self.assert_ele(ForumSelector.ALL_TAG, 'All标签默认显示')
        self.assert_ele(ForumSelector.NEWS_TAG, 'News标签默认显示')
        self.assert_ele(ForumSelector.INVOLVED_POSTS_TAG, 'InvolvedPosts标签可显示')
        self.assert_ele(ForumSelector.LATEST_TAG, '帖子排序默认显示Latest')
        # Latest标签验证
        # 代码备注：这里的外层try代表找到第二个group组的用户名为'Meross Official'时，下滑一次并直接重新判断用户名
        # 当用户名不为'Meross Official'时，第二层的try代表判断当前的帖子是否为热度贴，是的话再次下滑，否则取当前普通帖子的时间
        # if Set.client == "android":
        #     Tools.swipe_down(self)
        #     time.sleep(3)
        #     retry_times = 10
        #     for i in range(1, retry_times):
        #         try:
        #             if self.find_element(ForumSelector.USER_NAME).text is 'Meross Official':
        #                 Tools.swipe_down(self)
        #             else:
        #                 try:
        #                     if self.find_element(ForumSelector.HOT_TAGE):
        #                         Tools.swipe_down(self)
        #                 except Exception as e:
        #                     user_time1 = self.find_element(ForumSelector.USER_TIME).text
        #                     all_time1 = Tools.time_to_timestamp(user_time1)
        #                     print('all_time1=',all_time1)
        #                     break
        #         except Exception as e:
        #             Tools.swipe_down(self)
        #             continue
        #     Tools.swipe_down(self)
        #     user_time2 = self.find_element(ForumSelector.USER_TIME).text
        #     all_time2 = Tools.time_to_timestamp(user_time2)
        #     print('all_time2=', all_time2)
        #     assert all_time1 > all_time2, 'All标签的帖子默认未按照Latest格式排序'
        #     logger.info('All标签的帖子默认按Latest排序正确')
        #
        #     self.find_element(ForumSelector.NEWS_TAG).click()
        #     time.sleep(2)
        #     Tools.swipe_down(self)
        #     time.sleep(1)
        #     for i in range(1, retry_times):
        #         try:
        #             if self.find_element(ForumSelector.USER_NAME).text is 'Meross Official':
        #                 Tools.swipe_down(self)
        #             else:
        #                 try:
        #                     if self.find_element(ForumSelector.HOT_TAGE):
        #                         Tools.swipe_down(self)
        #                 except Exception as e:
        #                     user_time1 = self.find_element(ForumSelector.USER_TIME).text
        #                     new_time1 = Tools.time_to_timestamp(user_time1)
        #                     print('new_time1=', new_time1)
        #                     break
        #         except Exception as e:
        #             Tools.swipe_down(self)
        #             continue
        #     Tools.swipe_down(self)
        #     user_time2 = self.find_element(ForumSelector.USER_TIME).text
        #     new_time2 = Tools.time_to_timestamp(user_time2)
        #     print('new_time2=', new_time2)
        #     assert new_time1 > new_time2, 'News标签的帖子默认未按照Latest格式排序'
        #     logger.info('News标签的帖子默认按Latest排序正确')
            # Hottest标签验证
            # self.find_element(ForumSelector.ALL_TAG).click()
            # time.sleep(1)
            # self.find_element(ForumSelector.LATEST_TAG).click()
            # self.find_element(ForumSelector.HOTTEST_TAG).click()
            # time.sleep(1)
            # user1_browsing_data = self.find_element(ForumSelector.USER_BROWSING_DATA1).text
            # Tools.swipe_down(self)
            # time.sleep(1)
            # user2_browsing_data = self.find_element(ForumSelector.USER_BROWSING_DATA2).text
            # if 'k' in user1_browsing_data:
            #     user1_browsing_data = float(user1_browsing_data[0:-1])*1000
            # if 'k' in user2_browsing_data:
            #     user2_browsing_data = float(user2_browsing_data[0:-1])*1000
            # assert user1_browsing_data > user2_browsing_data, 'Forum帖子切换成Hottest模式，All标签的帖子未按照Hottest格式排序'
            # logger.info('Forum帖子切换成Hottest模式，All标签的帖子按Hottest排序正确')
            # self.find_element(ForumSelector.NEWS_TAG).click()
            # time.sleep(1)
            # user1_browsing_data = self.find_element(ForumSelector.USER_BROWSING_DATA1).text
            # Tools.swipe_down(self)
            # time.sleep(1)
            # user2_browsing_data = self.find_element(ForumSelector.USER_BROWSING_DATA2).text
            # if 'k' in user1_browsing_data:
            #     user1_browsing_data = float(user1_browsing_data[0:-1])*1000
            # if 'k' in user2_browsing_data:
            #     user2_browsing_data = float(user2_browsing_data[0:-1])*1000
            # assert user1_browsing_data > user2_browsing_data, 'Forum帖子切换成Hottest模式，New标签的帖子未按照Hottest格式排序'
            # logger.info('Forum帖子切换成Hottest模式，New标签的帖子按Hottest排序正确')
            # # Official only标签验证
            # self.find_element(ForumSelector.ALL_TAG).click()
            # time.sleep(1)
            # self.find_element(ForumSelector.LATEST_TAG).click()
            # self.find_element(ForumSelector.OFFICIAL_ONLY_TAG).click()
            # official_title1 = self.find_element(ForumSelector.OFFICIAL_TITLE).text
            # Tools.swipe_down(self)
            # time.sleep(1)
            # official_title2 = self.find_element(ForumSelector.OFFICIAL_TITLE).text
            # Tools.swipe_down(self)
            # time.sleep(1)
            # official_title3 = self.find_element(ForumSelector.OFFICIAL_TITLE).text
            # assert official_title1 == official_title2 == official_title3 == 'Meross Official', 'Forum帖子切换成Official only模式，All标签的帖子不全是官方贴子'
            # logger.info('Forum帖子切换成Official only模式,All标签的帖子全是官方贴子正确')
            # # 恢复环境
            # self.find_element(ForumSelector.ALL_TAG).click()
            # time.sleep(1)
            # self.find_element(ForumSelector.LATEST_TAG).click()
            # self.find_element(ForumSelector.LATEST_TAG).click()
            # logger.info('Forum页面标签环境恢复正确')
        #
        # elif Set.client == "ios":
        #     all_comment_time1 = self.find_element(ForumSelector.COMMENT_TIME1).text
        #     all_comment_time2 = self.find_element(ForumSelector.COMMENT_TIME2).text
        #     time1 = Tools.time_to_timestamp(all_comment_time1)
        #     time2 = Tools.time_to_timestamp(all_comment_time2)
        #     assert time1 > time2, 'All标签的帖子默认未按照Latest格式排序'
        #     logger.info('All标签的帖子默认按Latest排序正确')
        #     self.find_element(ForumSelector.NEWS_TAG).click()
        #     time.sleep(1)
        #     news_comment_time1 = self.find_element(ForumSelector.COMMENT_TIME1).text
        #     news_comment_time2 = self.find_element(ForumSelector.COMMENT_TIME2).text
        #     time1 = Tools.time_to_timestamp(news_comment_time1)
        #     time2 = Tools.time_to_timestamp(news_comment_time2)
        #     assert time1 > time2, 'News标签的帖子默认未按照Latest格式排序'
        #     logger.info('News标签的帖子默认按Latest排序正确')
        #     # Hottest标签验证
        #     self.find_element(ForumSelector.ALL_TAG).click()
        #     time.sleep(1)
        #     self.find_element(ForumSelector.LATEST_TAG).click()
        #     self.find_element(ForumSelector.HOTTEST_TAG).click()
        #     all_brow_data1 = self.find_element(ForumSelector.ALL_BROW_DATA1).text
        #     all_brow_data2 = self.find_element(ForumSelector.ALL_BROW_DATA2).text
        #     if 'k' in all_brow_data1:
        #         all_brow_data1 = float(all_brow_data1[0:-1])*1000
        #     if 'k' in all_brow_data2:
        #         all_brow_data2 = float(all_brow_data2[0:-1])*1000
        #     assert all_brow_data1 > all_brow_data2, 'Forum帖子切换成Hottest模式，All标签的帖子未按照Hottest格式排序'
        #     logger.info('Forum帖子切换成Hottest模式，All标签的帖子按Hottest排序正确')
        #     self.find_element(ForumSelector.NEWS_TAG).click()
        #     time.sleep(1)
        #     new_brow_data1 = self.find_element(ForumSelector.NEWS_BROW_DATA1).text
        #     new_brow_data2 = self.find_element(ForumSelector.NEWS_BROW_DATA2).text
        #     if 'k' in new_brow_data1:
        #         new_brow_data1 = float(new_brow_data1[0:-1])*1000
        #     if 'k' in new_brow_data2:
        #         new_brow_data2 = float(new_brow_data2[0:-1])*1000
        #     assert new_brow_data1 > new_brow_data2, 'Forum帖子切换成Hottest模式，New标签的帖子未按照Hottest格式排序'
        #     logger.info('Forum帖子切换成Hottest模式，New标签的帖子按Hottest排序正确')
        #     # Official only标签验证
        #     self.find_element(ForumSelector.ALL_TAG).click()
        #     time.sleep(1)
        #     self.find_element(ForumSelector.HOTTEST_TAG).click()
        #     self.find_element(ForumSelector.OFFICIAL_ONLY_TAG).click()
        #     time.sleep(1)
        #     official_title1 = self.find_element(ForumSelector.OFFICIAL_TITLE1).text
        #     Tools.swipe_down(self)
        #     official_title9 = self.find_element(ForumSelector.OFFICIAL_TITLE9).text
        #     assert official_title1 == official_title9 == 'Meross Official', 'Forum帖子切换成Official only模式，All标签的帖子不全是官方贴子'
        #     logger.info('Forum帖子切换成Official only模式,All标签的帖子全是官方贴子正确')
        #     # 恢复环境
        #     self.find_element(ForumSelector.NEWS_TAG).click()
        #     time.sleep(1)
        #     self.find_element(ForumSelector.OFFICIAL_ONLY_TAG).click()
        #     self.find_element(ForumSelector.LATEST_TAG).click()
        #     logger.info('Forum页面标签环境恢复正确')

    @allure.step("未登录时Forum页面验证")
    def modify_forum_tag_with_logout(self):
        # 未登录时对帖子进行点赞
        self.assert_ele(ForumSelector.ALL_TAG, 'All标签验证')
        self.assert_ele(ForumSelector.NEWS_TAG, 'News标签验证')
        self.find_element(ForumSelector.LIKE_BUTTON).click()
        self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时对帖子进行点赞跳转至登录注册界面正确')
        self.find_element(ForumSelector.CLOSE_BUTTON).click()
        # 未登录时对帖子进行投诉
        if Set.client == "android":
            # 未登录时对帖子进行投诉
            self.find_element(ForumSelector.SEARCH_BUTTON).click()
            self.assert_ele(ForumSelector.SEARCH_BOX, "跳转至搜索界面")
            self.find_element(ForumSelector.SEARCH_BOX).send_keys('Hello')
            self.driver.execute_script('mobile:performEditorAction', {"action": "search"})
            self.find_element(ForumSelector.SEARCH_PAGE_CONTENT).click()
            self.find_element(ForumSelector.ICD_ELE_BUTTON).click()
            self.find_element(ForumSelector.REPORT_THIS_POST).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时对帖子进行投诉跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            # 未登录时对无评论对帖子进行评论
            self.find_element(ForumSelector.SEARCH_BUTTON).click()
            self.assert_ele(ForumSelector.SEARCH_BOX, "跳转至搜索界面")
            self.find_element(ForumSelector.SEARCH_BOX).send_keys('Hello')
            self.driver.execute_script('mobile:performEditorAction', {"action": "search"})
            self.find_element(ForumSelector.NO_COMMENT_BUTTON).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时对无评论对帖子进行评论跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            # 未登录时对有评论对帖子进行评论
            self.find_element(ForumSelector.HAS_COMMENT_BUTTON).click()
            self.find_element(ForumSelector.POST_BUTTON).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时对有评论对帖子进行评论跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            # 点击用户头像投诉和屏蔽
            Tools.swipe_down(self)
            time.sleep(1)
            for i in range(1, 5):
                try:
                    if self.find_element(ForumSelector.USER_NAME).text is 'Meross Official':
                        Tools.swipe_down(self)
                    else:
                        # 验证投诉
                        self.find_element(ForumSelector.USER_HEAD_PORTRAIT).click()
                        self.find_element(ForumSelector.APOSTROPHE_BUTTON).click()
                        self.find_element(ForumSelector.REPORT_USER).click()
                        self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时点击用户头像投诉跳转至登录注册界面正确')
                        self.find_element(ForumSelector.CLOSE_BUTTON).click()
                        # 验证屏蔽
                        self.find_element(ForumSelector.APOSTROPHE_BUTTON).click()
                        self.find_element(ForumSelector.BLOCK_USER).click()
                        self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时点击用户头像屏蔽跳转至登录注册界面正确')
                        self.find_element(ForumSelector.CLOSE_BUTTON).click()
                        self.find_element(ForumSelector.USER_RETURN_BUTTON).click()
                        break
                except Exception as e:
                    Tools.swipe_down(self)
                    continue

        elif Set.client == "ios":
            self.find_element(ForumSelector.ALL_BROW_DATA1).click()
            self.find_element(ForumSelector.ICD_ELE_BUTTON).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时对帖子进行投诉跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            self.find_element(ForumSelector.ALL_BROW_DATA1).click()
            self.find_element(ForumSelector.POST_BUTTON).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时对有评论对帖子进行评论跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            # 点击用户头像投诉
            self.find_element(ForumSelector.USER_HEAD_PORTRAIT).click()
            # 第一次页面滑动到第六个用户，第二次点击用户头像
            self.find_element(ForumSelector.USER_HEAD_PORTRAIT).click()
            self.find_element(ForumSelector.ICMORE_BUTTON).click()
            self.find_element(ForumSelector.REPORT_USER).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时点击用户头像投诉跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            # 点击用户头像屏蔽
            self.find_element(ForumSelector.ICMORE_BUTTON).click()
            self.find_element(ForumSelector.BLOCK_USER).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时点击用户头像屏蔽跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()
            # 验证无评论帖子
            self.find_element(ForumSelector.SEARCH_BUTTON).click()
            self.assert_ele(ForumSelector.SEARCH_BOX, "跳转至搜索界面")
            self.find_element(ForumSelector.SEARCH_BOX).send_keys('Hello')
            self.find_element(ForumSelector.SEARCH_BOX_KEYBOARD).click()
            self.find_element(ForumSelector.NO_COMMENT_BUTTON).click()
            self.assert_ele(ForumSelector.LOGIN_BUTTON, '验证未登录时对无评论对帖子进行评论跳转至登录注册界面正确')
            self.find_element(ForumSelector.CLOSE_BUTTON).click()
            self.find_element(ForumSelector.RETURN_BUTTON).click()