from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from helpers import format_duration, is_visit_long


def get_duration(visitor):
    time_delta = localtime() - localtime(visitor.entered_at)
    delta_sec = time_delta.total_seconds()
    return delta_sec


def storage_information_view(request):
    visitors_at_storage = Visit.objects.filter(leaved_at__isnull=True)
    non_closed_visits = []

    for visitor in visitors_at_storage:
        visit_duration = get_duration(visitor)
        formated_time = format_duration(visit_duration)

        non_closed_visits.append({
            'who_entered': visitor.passcard.owner_name,
            'entered_at': localtime(visitor.entered_at),
            'duration': formated_time,
            'is_strange': is_visit_long(visit_duration)
        })

    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
