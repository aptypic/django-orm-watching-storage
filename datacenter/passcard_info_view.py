from django.utils.timezone import localtime

from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render


def passcard_info_view(request, passcode):
    this_passcard_visits_list = []
    passcard = Passcard.objects.get(passcode=passcode)
    for visit in Visit.objects.filter(passcard=passcard, leaved_at__isnull=False):
        duration = get_duration(visit.entered_at, visit.leaved_at)
        this_passcard_visits = {
            'entered_at': visit.entered_at,
            'duration': format_duration(duration),
            'is_strange': is_visit_long(duration)
        }
        this_passcard_visits_list.append(this_passcard_visits)
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits_list,
    }
    return render(request, 'passcard_info.html', context)
