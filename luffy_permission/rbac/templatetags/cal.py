import re

from django.template import Library

register = Library()


@register.filter
def mul(x, y):
    return x * y


#
# def tag(val):
#     return


@register.filter
def lowerse(val):
    return val.lower()


@register.simple_tag
def mul_tag(x, y, z):
    return x * y * z


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
        print(permission_menu)
        for item in permission_menu['children']:
            permission_menu['class'] = 'hide'
            if item['pk'] == request.show_id:
                permission_menu['class'] = ''
    return {'permissions_menu_dict': permissions_menu_dict}


# @register.inclusion_tag('btn.html')
# def get_btn_style(request, url):
#     permissions_list = request.session.get('permissions_list')
#
#     # print(permissions_list)
#     return {'permissions_list': permissions_list, 'url': url}


@register.filter
def has_permissions(url, request):
    permissions_names = request.session.get('permissions_names')
    return url in permissions_names
