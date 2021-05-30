from app01.models import Role


def is_permission(user, request):
    permissions_list = []
    ret = Role.objects.filter(user=user).values('permissions__url').distinct()
    for i in ret:
        permissions_list.append(i['permissions__url'])
    request.session['permissions_list'] = permissions_list