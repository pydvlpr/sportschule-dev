import datetime

"""
    Funktion für Vergleich Zeitangaben
"""
def time_in_range(start, end, x):
    """Gibt True zurück, wenn x ist in der range[start,end]"""

    if start <= end:
        return start <= x <= end
    else:
        return start <= x or x <= end
