# Django view wich is just an Ajax endpoint to recive the user agent from the FE

import json
from pprint import pprint

from django.http import HttpResponse
from ipware import get_client_ip
from ua_parser.user_agent_parser import Parse

from django_concierge.models import Visit


def get_client_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def ajax_recive_client_intel(request):

    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        ua = Parse(data["userAgent"])

        Visit.objects.create(
            ip_address=request.META["REMOTE_ADDR"],
            user_agent=data["userAgent"],
            referrer=data["referrer"],
            screen_width=data["screenWidth"],
            screen_height=data["screenHeight"],
            user_agent_family=ua["user_agent"]["family"],
            user_agent_major=ua["user_agent"]["major"],
            user_agent_minor=ua["user_agent"]["minor"],
            os_family=ua["os"]["family"],
            os_major=ua["os"]["major"],
            device_family=ua["device"]["family"],
            device_brand=ua["device"]["brand"],
            device_model=ua["device"]["model"],
        )

        return HttpResponse(200)
