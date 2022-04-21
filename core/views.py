from django.shortcuts import render

from core.models import CloudFunctions, HostProduct, AboutUs


def host_list(request):
    host_list = HostProduct.objects.all()
    cloud_list = CloudFunctions.objects.all()
    aboutus_list = AboutUs.objects.all()
    context = {
        'host_list': host_list,
        'cloud_list': cloud_list,
        'aboutus_list': aboutus_list,
    }
    return render(request, 'index.html', context)
