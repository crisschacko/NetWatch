def format_bytes(value):
    value = float(value)

    units = [
        "B",
        "KB",
        "MB",
        "GB",
        "TB"
    ]

    index = 0

    while value >= 1024 and index < len(units) - 1:
        value /= 1024
        index += 1

    return f"{value:.2f} {units[index]}"


def format_speed(value):
    return f"{format_bytes(value)}/s"


def percentage(value, total):
    if total <= 0:
        return 0

    return round((value / total) * 100, 2)


def clamp(value, minimum=0, maximum=100):
    return max(minimum, min(value, maximum))
