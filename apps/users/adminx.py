from users.models import VerifyCode
from xadmin import views

import xadmin


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "后台管理系统"
    site_footer = '1234'
    menu_style = 'accordion'


class VerifyCodeAdmin(object):
    list_display = ['code', 'mobile', "add_time"]


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)
xadmin.site.register(VerifyCode, VerifyCodeAdmin)
