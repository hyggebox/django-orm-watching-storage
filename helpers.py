def format_duration(duration):
    hours = int(duration // 3600)
    min = int((duration % 3600) // 60)
    return f'{hours}ч {min}мин'


def is_visit_long(duration):
    long_visit_sec = 3600
    return duration > long_visit_sec