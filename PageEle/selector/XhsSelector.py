from PageEle.selector.NaviSelector import NaviSelector
from Common.set import Set
from Common.log import logger


class UserSelector:
    USER_TITLE = NaviSelector.USER_TITLE
    if Set.client == "android":
        SEARCH= f'by.accessibility_id|搜索'
        SEARCH_AGAIN= f'by.id|com.xingin.xhs:id/evv'
        TEXT_BOX= f'by.class_name|android.widget.EditText'
        PRODUCT= f'by.id|com.xingin.xhs:id/zt'
        WAYS= f'by.id|com.xingin.xhs:id/evh'
        NAME= f'by.name|com.xingin.xhs:id/chh'
        SHOP_NAME= f'by.id|com.xingin.xhs:id/clg'
        ENTRY= f'by.id|com.xingin.xhs:id/ckr'
        NUMBER= f'by.id|com.xingin.xhs:id/gfn'
    elif Set.client == "ios":
        LINK_BACK= f'by.id|{Set.Apk}:id/iv_back'
    else:
        logger.error(f"client异常:{Set.client}")
