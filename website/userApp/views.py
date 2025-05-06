from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


def motion_status(request):
    try:
        with open("/home/zain/TeamProject/motion_status.txt", "r") as f:
            status = f.read().strip()
        return HttpResponse(f"Motion status: {status}")
    except FileNotFoundError:
        return HttpResponse("No motion data found.")


def live_page(request):
    return render(request, 'live.html')