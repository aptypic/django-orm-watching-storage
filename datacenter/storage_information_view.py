from datetime import timezone
from datacenter.models import Passcard
from datacenter.models import Visit, get_duration, format_duration, is_visit_long
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_list = []
    for visit in Visit.objects.filter(leaved_at__isnull=True):
    #     print(i)
    #     total_seconds = (localtime() - i.entered_at.astimezone()).total_seconds()
    #     rest_of_seconds = (localtime() - i.entered_at.astimezone()).seconds
    #     hours = total_seconds // 3600
    #     minutes = (total_seconds % 3600) // 60
    #     non_closed_visits = {
    #             'who_entered': '{}'.format(i.passcard),
    #             'entered_at': '{}'.format(i.entered_at.astimezone()),
    #             'duration': '{}:{}:{}'.format(round(hours), round(minutes), rest_of_seconds % 60),
    #         }
    #     non_closed_list.append(non_closed_visits)
    # context = {
    #     'non_closed_visits': non_closed_list,  # не закрытые посещения
    # }
    # return render(request, 'storage_information.html', context)
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
            "non_closed_visits": non_closed_list,  # не закрытые посещения
        }

    # for i in Visit.objects.all():
    #     print(Visit.objects.filter(passcard__passcode__contains=Visit.objects.all()[i].passcard.passcode))
    return render(request, 'storage_information.html', context)
