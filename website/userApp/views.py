from django.http import StreamingHttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View


from django.core.mail import send_mail


import os
from django.conf import settings
from django.shortcuts import render


import requests
from django.shortcuts import render


class Home(View):
    def get(self, request):
        return render(request, 'home.html')


def motion_status(request):
    try:
        with open("/home/zain/TeamProject/shared_logs/motion_status.txt", "r") as f:
            status = f.read().strip()
        return HttpResponse(f"Motion status: {status}")
    except FileNotFoundError:
        return HttpResponse("No motion data found.")


def live_page(request):
    return render(request, 'live.html')


def notifications_page(request):
    return render(request, 'Notifications.html')





def read_log(request):
    log_path = os.path.join(settings.BASE_DIR, 'smoke_log.txt')  # or wherever your log is stored
    log_entries = []

    with open(log_path, 'r') as file:
        for line in file:
            if "Smoke Detected!!!" in line:
                try:
                    # Example line: Smoke Detected!!! Date: 07_05_2025 and Time: 00_23_05
                    date_part = line.split("Date:")[1].split("and")[0].strip()
                    time_part = line.split("Time:")[1].strip()
                    log_entries.append({
                        'message': 'Smoke Detected!!!',
                        'date': date_part.replace('_', '-'),
                        'time': time_part.replace('_', ':')
                    })
                except (IndexError, ValueError):
                    continue  # skip malformed lines

    return render(request, 'logs.html', {'logs': log_entries})












def motion_log_view(request):
    LOG_URL = 'http://192.168.123.153:8001/motion_status.txt'

    try:
        resp = requests.get(LOG_URL, timeout=2)
        resp.raise_for_status()
        lines = resp.text.splitlines()
    except requests.RequestException:
        lines = []

    logs = []
    for line in lines:
        if "Intruder!!!" in line:
            try:
                date = line.split("Date:")[1].split("and")[0].strip().replace('_', '-')
                time = line.split("Time:")[1].strip().replace('_', ':')
                logs.append({
                    'message': 'Motion Detected!!!',
                    'date': date,
                    'time': time
                })
            except (IndexError, ValueError):
                continue

    return render(request, 'motion_logs.html', {'logs': logs})



def smoke_log(request):
    LOG_URL = 'http://192.168.123.153:8001/smoke_status.txt'

    try:
        resp = requests.get(LOG_URL, timeout=2)
        resp.raise_for_status()
        lines = resp.text.splitlines()
    except requests.RequestException:
        lines = []

    logs = []
    for line in lines:
        if "Intruder!!!" in line:
            try:
                date = line.split("Date:")[1].split("and")[0].strip().replace('_', '-')
                time = line.split("Time:")[1].strip().replace('_', ':')
                logs.append({
                    'message': 'Motion Detected!!!',
                    'date': date,
                    'time': time
                })
            except (IndexError, ValueError):
                continue

    return render(request, 'motion_logs.html', {'logs': logs})






























def send_email_to(email):
    subject = 'Order confirmation'
    message = 'Thanks for placing a Pizza Order Using My Website! Your Food will arrive shortly'
    from_email = 'setting.EMAIL_HOST'
    to_email = email

    send_mail(
        subject,
        message,
        from_email,
        [to_email],
        fail_silently=False)
