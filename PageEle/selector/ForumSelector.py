# -*- coding: utf-8 -*-
# @Time    : 2023/6/20 09:54
# @Author  : XuLei
# @FileName: ForumSelector.py
# @Software: PyCharm
from Common.set import Set
from Common.log import logger


class ForumSelector:
    if Set.client == "android":
        GOTCHA_LAB = f'by.id|{Set.Apk}:id/tv_got'
        FORUM_TAB = f'by.id|{Set.Apk}:id/tv_title_info'
        COUNTRY_SHOW = f'by.id|{Set.Apk}:id/iv_country'
        COUNTRY_LAB = f'by.id|{Set.Apk}:id/tv_title_info'
        JAPAN_LAB = "by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[6]"
        US_LAB = "by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[9]"
        SAVE_BUTTON = f'by.id|{Set.Apk}:id/tv_right'
        SEARCH_BUTTON = f'by.id|{Set.Apk}:id/iv_left_gone'
        SEARCH_BOX = f'by.id|{Set.Apk}:id/et_search'
        SEARCH_BOX_KEYBOARD = f'by.id|{Set.Apk}:id/et_search'
        SEARCH_PAGE_CONTENT = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[4]'
        SEARCH_JAPAN_CONTENT = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup/android.widget.TextView[3]'
        USER_RETURN_BUTTON = f'by.id|{Set.Apk}:id/iv_left_gone'
        RETURN_BUTTON = f'by.id|{Set.Apk}:id/iv_back'
        ALL_TAG = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.LinearLayout'
        NEWS_TAG = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.LinearLayout'
        INVOLVED_POSTS_TAG = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.HorizontalScrollView/android.widget.LinearLayout/android.widget.FrameLayout[3]/android.view.ViewGroup/android.widget.LinearLayout'
        LATEST_TAG = f'by.id|{Set.Apk}:id/tv_latest'
        HOTTEST_TAG = f'by.id|{Set.Apk}:id/tv_hotest'
        OFFICIAL_ONLY_TAG = f'by.id|{Set.Apk}:id/tv_official'
        USER_NAME = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[1]'

        USER_TIME = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[2]'
        USER_HEAD_PORTRAIT = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.widget.ImageView'
        USER_BROWSING_DATA1 = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout[1]/android.widget.TextView'
        USER_BROWSING_DATA2 = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.LinearLayout[1]/android.widget.TextView'
        OFFICIAL_TITLE = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.TextView[1]'
        LIKE_BUTTON = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout[3]/android.widget.TextView'
        LOGIN_BUTTON = f'by.id|{Set.Apk}:id/bt_sign_in'
        ALL_BROW_DATA1 = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.TextView[3]'
        CLOSE_BUTTON = f'by.id|{Set.Apk}:id/iv_left_gone'
        ICD_ELE_BUTTON = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup[1]/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.ImageView[2]'
        REPORT_THIS_POST = f'by.id|{Set.Apk}:id/tv_report_post'
        NO_COMMENT_BUTTON = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.TextView'
        HAS_COMMENT_BUTTON = 'by.xpath|/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/android.view.ViewGroup/android.view.ViewGroup/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.LinearLayout[2]/android.widget.TextView'
        POST_BUTTON = f'by.id|{Set.Apk}:id/tv_post'
        APOSTROPHE_BUTTON = f'by.id|{Set.Apk}:id/iv_right'
        REPORT_USER = f'by.id|{Set.Apk}:id/tv_report_user'
        BLOCK_USER = f'by.id|{Set.Apk}:id/tv_block_user'
        HOT_TAGE = f'by.id|{Set.Apk}:id/iv_hot'
    elif Set.client == "ios":
        GOTCHA_LAB = 'by.ios_predicate|label == "Gotcha!" AND name == "Gotcha!" AND value == "Gotcha!"'
        FORUM_TAB = 'by.ios_predicate|label == "Forum" AND name == "Forum" AND value == "Forum"'
        COUNTRY_SHOW = 'by.ios_class_chain|**/XCUIElementTypeNavigationBar[`name == "Forum"`]/XCUIElementTypeButton[2]'
        COUNTRY_LAB = 'by.ios_predicate|label == "Country"'
        JAPAN_LAB = 'by.ios_predicate|label == "Japan"'
        US_LAB = 'by.ios_predicate|label == "United States "'
        SAVE_BUTTON = 'by.ios_predicate|label == "Save"'
        SEARCH_BUTTON = 'by.ios_predicate|label == "icSearch"'
        SEARCH_BOX = 'by.ios_predicate|label == "Search with keywords"'
        SEARCH_BOX_KEYBOARD = 'by.ios_predicate|label == "search"'
        SEARCH_PAGE_CONTENT = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[2]'
        SEARCH_JAPAN_CONTENT = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeStaticText[1]'
        ALL_TAG = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "All"`]'
        NEWS_TAG = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "News"`]'
        OFFICIAL_ONLY_TAG = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Official Only"`]'
        INVOLVED_POSTS_TAG = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "InvolvedPosts"`]'
        LATEST_TAG = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Latest"`]'
        HOTTEST_TAG = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Hottest"`]'
        COMMENT_TIME1 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther' \
                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeStaticText[2]'
        COMMENT_TIME2 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther' \
                        '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[10]/XCUIElementTypeStaticText[2]'
        ALL_BROW_DATA1 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther' \
                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]'
        ALL_BROW_DATA2 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther' \
                         '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]'
        NEWS_BROW_DATA1 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther' \
                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[1]'
        NEWS_BROW_DATA2 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther' \
                          '/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]'
        OFFICIAL_TITLE1 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[3]'
        OFFICIAL_TITLE9 = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[9]/XCUIElementTypeButton[3]'
        LIKE_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[1]/XCUIElementTypeButton[5]'
        LOGIN_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Log in"`]'
        CLOSE_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "close"`]'
        ICD_ELE_BUTTON = 'by.xpath|//XCUIElementTypeButton[@name="icMore"]'
        POST_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]'
        RETURN_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "return"`]'
        USER_HEAD_PORTRAIT = 'by.ios_class_chain|**/XCUIElementTypeWindow[1]/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther[2]/XCUIElementTypeTable/XCUIElementTypeCell/XCUIElementTypeTable/XCUIElementTypeCell[6]/XCUIElementTypeButton[3]'
        WRITE_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "icWrite"`]'
        ICMORE_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "icMore"`]'
        REPORT_USER = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Report this user"`]'
        BLOCK_USER = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Block this user"`]'
        TITLE_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeTextField[`value == "Theme"`]'
        NEWS_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "News"`]'
        CONTENT_BOX = 'by.ios_class_chain|**/XCUIElementTypeStaticText[`label == "Tell the community more…"`]'
        TALCK_POST_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "Post"`]'
        NO_COMMENT_BUTTON = 'by.ios_class_chain|**/XCUIElementTypeButton[`label == "0"`][2]'