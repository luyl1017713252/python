import re

from django.template import Library

register = Library()

@register.inclusion_tag('menu.html')
def get_menu_style(request):
    '''
        创建一个自定义标签用来把已登录的用户对应的权限拿到，并且对页面判断点击选中项
        :param request:
        :return: 返回一个字典给menu.html页面
        '''
    permissions_menu_dict = request.session.get('permissions_menu_dict')
    # for permission_menu in permissions_menu_dict:
    #     if re.search('^{}$'.format(permission_menu['url']), request.path):
    #         permission_menu['class'] = 'active'
    for permission_menu in permissions_menu_dict.values():
        permission_menu['selected'] = ''
        for item in permission_menu['children']:
            item['class'] = ''
            # permission_menu['class'] = 'hide'
            if re.search('^{}$'.format(item['url']), request.path):
                permission_menu['selected'] = 'active'
                item['class'] = 'active'
            # if item['pk'] == request.show_id:
            #     permission_menu['class'] = ''
    return {'permissions_menu_dict': permissions_menu_dict}