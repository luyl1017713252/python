from rbac.models import Role


def is_permission(user_obj, request):
    permissions_list = []
    permissions_names = []
    permissions_menu_dict = {}
    ret = Role.objects.filter(userinfo=user_obj).values('permissions__url',
                                                        'permissions__title',
                                                        'permissions__name',
                                                        'permissions__pk',
                                                        'permissions__pid',
                                                        'permissions__menus__icon',
                                                        'permissions__menus__title',
                                                        'permissions__menus__pk',
                                                        ).distinct()
    for i in ret:
        permissions_list.append(
            {
                'url': i['permissions__url'],
                'id': i['permissions__pk'],
                'pid': i['permissions__pid']
            }
        )
        permissions_names.append(i['permissions__name'])
        menu_pk = i['permissions__menus__pk']
        if menu_pk:
            if menu_pk not in permissions_menu_dict:
                permissions_menu_dict[menu_pk] = {
                    'title': i['permissions__menus__title'],
                    'icon': i['permissions__menus__icon'],
                    'children': [
                        {
                            'title': i['permissions__title'],
                            'url': i['permissions__url'],
                            'pk': i['permissions__pk']
                        }
                    ],
                }
            else:
                permissions_menu_dict[menu_pk]['children'].append({
                    'title': i['permissions__title'],
                    'url': i['permissions__url']
                })
    print(permissions_menu_dict)
    request.session['permissions_list'] = permissions_list
    request.session['permissions_names'] = permissions_names
    request.session['permissions_menu_dict'] = permissions_menu_dict