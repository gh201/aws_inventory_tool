import datetime


class TimeConverter:
    last_time_function_called = datetime.datetime.now()

    @staticmethod
    def time_ago_seconds_to_text(time_in_seconds):
        second = 1
        minute = 60 * second
        hour = 60 * minute

        if time_in_seconds < second:
            return "less than second"

        elif time_in_seconds == second:
            return "1 second"

        elif time_in_seconds < minute:
            return "{} seconds".format(time_in_seconds)

        elif time_in_seconds > minute and time_in_seconds < (minute * 2):
            return "about a minute"

        elif time_in_seconds > (minute * 2) and time_in_seconds < hour:
            minutes = int(time_in_seconds / minute)
            return "{} minutes".format(minutes)

        elif time_in_seconds > hour and time_in_seconds < (hour * 2):
            return "more than hour"

        elif time_in_seconds > (hour * 2) and time_in_seconds < (hour * 24):
            hours = int(time_in_seconds / hour)
            return "{} hours".format(hours)

        else:
            return "way too long"

    @staticmethod
    def get_last_usage_string():
        current_time = datetime.datetime.now()

        time_delta_since_last_call = datetime.datetime.now() - TimeConverter.last_time_function_called
        TimeConverter.last_time_function_called = current_time

        text = TimeConverter.time_ago_seconds_to_text(time_delta_since_last_call.seconds) + " ago"

        return text
