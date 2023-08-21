from datetime import datetime, timedelta


class CommentTimeFormatter:
    @staticmethod
    def time_since(value):
        if not isinstance(value, datetime):
            return str(value)

        now = datetime.now()
        time_difference = now - value

        if time_difference.total_seconds() < 60:
            # 1분 미만일 경우
            return f"{int(time_difference.total_seconds())}초 전"
        elif time_difference.total_seconds() < 3600:
            # 1시간 미만일 경우
            return f"{int(time_difference.total_seconds() / 60)}분 전"
        elif time_difference.total_seconds() < 86400:
            # 1일 미만일 경우
            return f"{int(time_difference.total_seconds() / 3600)}시간 전"
        elif time_difference.total_seconds() < 2592000:  # 30일 이하
            # 30일 미만일 경우
            return f"{int(time_difference.total_seconds() / 86400)}일 전"
        else:
            # 30일 이상일 경우
            return value.strftime('%Y.%m.%d')