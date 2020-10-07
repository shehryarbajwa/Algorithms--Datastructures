def meeting_rooms(intervals):
    if not intervals or len(intervals) == 1:
            return True
    intervals = sorted(intervals)
    first_interval = intervals[0]

    for interval in intervals[1:]:
        current_start = interval[0]
        first_interval_end = first_interval[1]
        if current_start < first_interval_end:
            return False
        else:
            first_interval = interval
    return True

        