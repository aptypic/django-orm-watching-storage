from datetime import timezone
from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_list = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
        duration = get_duration(visit.entered_at, localtime())
        formatted_duration = format_duration(duration)
        is_strange = is_visit_long(duration)
        non_closed_visits = {
                "who_entered": visit.passcard,
                "entered_at": visit.entered_at,
                "duration": formatted_duration,
                "is_strange": is_strange,
            }
        non_closed_list.append(non_closed_visits)
        context = {
            "non_closed_visits": non_closed_list,
        }
    return render(request, 'storage_information.html', context)
