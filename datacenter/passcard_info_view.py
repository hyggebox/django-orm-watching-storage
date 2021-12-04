from datacenter.models import Visit
from django.shortcuts import render

from datacenter.helpers import format_duration, is_visit_long, get_duration
from datacenter.models import Passcard



def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    this_passcard_visits = []

    all_visits = Visit.objects.filter(passcard=passcard)
    for visit in all_visits:
        visit_duration = get_duration(visit.leaved_at, visit.entered_at)
        this_passcard_visits.append({
                'entered_at': visit.entered_at,
                'duration': format_duration(visit_duration),
                'is_strange': is_visit_long(visit_duration)
            })

    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
