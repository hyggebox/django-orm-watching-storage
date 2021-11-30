from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from helpers import format_duration, is_visit_long


def get_duration(visit):
    time_delta = visit.leaved_at - visit.entered_at
    delta_sec = time_delta.total_seconds()
    return delta_sec


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.filter(passcode=passcode)[0]
    this_passcard_visits = []

    all_visits = Visit.objects.filter(passcard=passcard)
    for visit in all_visits:
        this_passcard_visits.append({
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
                'is_strange': is_visit_long(get_duration(visit))
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
