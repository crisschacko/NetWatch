def format_bytes(value):
    units = ["B", "KB", "MB", "GB", "TB"]

    value = float(value)
    index = 0

    while value >= 1024 and index < len(units) - 1:
        value /= 1024
        index += 1

    return f"{value:.2f} {units[index]}"


def format_speed(value):
    return format_bytes(value) + "/s"


def calculate_percentage(value, total):
    if total == 0:
        return 0

    return round((value / total) * 100, 2)
