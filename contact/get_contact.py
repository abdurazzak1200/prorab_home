from .models import Info


def get_info(request):
    infos = Info.objects.all()
    context = {'infos': infos}
    return context