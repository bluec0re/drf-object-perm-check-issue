from guardian.shortcuts import assign_perm
from django.shortcuts import redirect
from .models import Foo
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate


def init(request):
    try:
        user = User.objects.create_user('test', 'test@example.com', 'qwertz1290')
        user.save()
    except Exception:
        pass
    user = authenticate(username='test', password='qwertz1290')
    login(request, user)

    f = Foo()
    f.bar = 'object 1'
    f.save()
    assign_perm(perm='change_foo',
                user_or_group=user,
                obj=f)
    assign_perm(perm='view_foo',
                user_or_group=user,
                obj=f)

    f = Foo()
    f.bar = 'object 2'
    f.save()
    assign_perm(perm='view_foo',
                user_or_group=user,
                obj=f)

    return redirect('/api/foo/')
