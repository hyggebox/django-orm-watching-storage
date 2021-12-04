def format_duration(duration):
    hours = int(duration // 3600)
    min = int((duration % 3600) // 60)
    return f'{hours}ч {min}мин'


def is_visit_long(duration):
    long_visit_sec = 3600
    return duration > long_visit_sec


def get_duration(left_at, entered_at):
    time_delta = left_at - entered_at
    delta_sec = time_delta.total_seconds()
    return delta_sec