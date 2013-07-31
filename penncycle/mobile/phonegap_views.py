# import re
# import datetime
import json

from django.http import HttpResponse

from app.models import Student # Bike, Ride  # , Station

from penncycle.util.util import email_razzi
from .forms import SignupForm

def check_for_student(request):
    email_razzi("Got request: {}".format(request))
    penncard = request.GET.get("penncard")
    try:
        student = Student.objects.get(penncard=penncard)
        reply = {'student': student.name}
        return json.dumps(reply)
    except Student.DoesNotExist:
        reply = {'penncard': penncard}
        return json.dumps(reply)


def mobile_signup(request):
    form = SignupForm(request.POST)
    if form.is_valid():
        form.save()
        reply = {
            'success': True,
            'form_valid': True
        }
    else:
        reply = {
            'success': True,
            'form_valid': False,
            'new_form': str(form)
        }
    return HttpResponse(json.dumps(reply), content_type="application/json")


def verify(request):
    data = request.POST
    penncard = data.get("penncard")
    pin = data.get("pin")
    try:
        student = Student.objects.get(penncard=penncard)
    except Student.DoesNotExist:
        return "failure"
    if student.pin != pin:
        return "bad pin"