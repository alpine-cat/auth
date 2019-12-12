from django.contrib.auth.decorators import permission_required


@permission_required('polls.can_vote')
def my_view(request):
    ...



from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('polls.can_vote', raise_exception=True)
def my_view(request):
    ...
