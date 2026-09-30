# ticktock.py

import datetime
from lunarcalendar import Converter, Solar
from functools import lru_cache

# 控制报错语言的变量（True=英文，False=中文）
error_is_english = False

@lru_cache(maxsize=8)
def _get_festival_dates(year: int):
    """算某年所有传统节日的公历日期，返回 ((月, 日), ...)，带缓存"""
    from lunarcalendar import Converter, Lunar

    festivals = [
        (1, 1),   # 春节
        (1, 15),  # 元宵节
        (5, 5),   # 端午节
        (7, 7),   # 七夕节
        (7, 15),  # 中元节
        (8, 15),  # 中秋节
        (9, 9),   # 重阳节
        (12, 8),  # 腊八节
    ]
    result = []
    for (m, d) in festivals:
        try:
            solar = Converter.Lunar2Solar(Lunar(year, m, d))
            result.append((solar.month, solar.day))
        except Exception:
            continue
    return tuple(result)

class TimeError(Exception):
    """时间相关的自定义异常基类"""
    pass


class MonthError(TimeError):
    """月份输入错误（1-12以外）"""
    pass


class DayError(TimeError):
    """日期输入错误（超出当月天数）"""
    pass

def get_festival() -> str:
    """判断当前是不是中国传统节日，不是则返回提示"""
    today = datetime.now().date()
    solar = Solar(today.year, today.month, today.day)
    lunar = Converter.Solar2Lunar(solar)

    # 农历日期对应的节日
    lunar_festivals = {
        (1, 1): "春节",
        (1, 15): "元宵节",
        (5, 5): "端午节",
        (7, 7): "七夕节",
        (7, 15): "中元节",
        (8, 15): "中秋节",
        (9, 9): "重阳节",
        (12, 8): "腊八节",
        (12, 30): "除夕",
    }

    # 农历月/日
    lunar_month = lunar.month
    lunar_day = lunar.day

    # 如果是除夕（腊月最后一天），需要特殊处理
    if lunar_month == 12 and lunar_day == 29 or lunar_month == 12 and lunar_day == 30:
        # 小月29，大月30，具体需检查下个月是不是春节
        next_day = Converter.Solar2Lunar(Solar(today.year, today.month, today.day + 1))
        if next_day.month == 1 and next_day.day == 1:
            return "除夕"

    if (lunar_month, lunar_day) in lunar_festivals:
        return lunar_festivals[(lunar_month, lunar_day)]

    return "现在不是传统节日"

def get_ymd():
    """获取当前的年月日，返回格式为 (年, 月, 日)"""
    today = datetime.date.today()
    return today.year, today.month, today.day

def get_hms():
    """获取当前的时分秒，返回 (时, 分, 秒)"""
    now = datetime.datetime.now()
    return now.hour, now.minute, now.second

def get_now():
    """获取完整的日期时间对象"""
    return datetime.datetime.now()

def is_leap_year(year: int) -> bool:
    """判断是否为闰年"""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def get_days_in_month(year: int, month: int) -> int:
    """返回某年某月有多少天"""
    if month < 1 or month > 12:
        if error_is_english:
            raise MonthError(f"Month must be 1~12, you input {month}")
        else:
            raise MonthError(f"月份必须是 1~12，你输入了 {month}")
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in [4, 6, 9, 11]:
        return 30
    return 31

def format_date(fmt: str = "%Y-%m-%d"):
    """返回当前日期的格式化字符串，默认 '2026-09-01'"""
    return datetime.datetime.now().strftime(fmt)

def validate_date(year: int, month: int, day: int) -> bool:
    if month < 1 or month > 12:
        if error_is_english:
            raise MonthError(f"Month must be 1~12, you input {month}")
        else:
            raise MonthError(f"月份必须是 1~12，你输入了 {month}")
    max_day = get_days_in_month(year, month)
    if day < 1 or day > max_day:
        if error_is_english:
            raise DayError(f"Day must be 1~{max_day}, you input {day}")
        else:
            raise DayError(f"日期必须在 1~{max_day} 之间，你输入了 {day}")
    return True

def get_weekday() -> int:
    """返回今天是星期几（0=周一，6=周日）"""
    return datetime.datetime.now().weekday()

def is_weekend() -> bool:
    """判断今天是否为周末（周六或周日）"""
    return get_weekday() >= 5  # 5 是周六，6 是周日

def days_until_weekend() -> int:
    """计算距离下一个周末还有几天（如果是周末，返回0）"""
    today = get_weekday()
    days_to_saturday = (5 - today) % 7
    return days_to_saturday

def get_period_of_day() -> str:
    """返回当前时间段（早晨、上午、中午、下午、傍晚、深夜）"""
    current_hour = datetime.datetime.now().hour
    if 6 <= current_hour < 9:
        return "早晨"
    if 9 <= current_hour < 12:
        return "上午"
    if 12 <= current_hour < 14:
        return "中午"
    if 14 <= current_hour < 18:
        return "下午"
    if 18 <= current_hour < 21:
        return "傍晚"
    return "深夜"

def is_past_date(target_date: str) -> bool:
    """判断目标日期是否已经过去"""
    from datetime import date
    target = date.fromisoformat(target_date)
    return target < date.today()

def time_difference(start: str, end: str) -> str:
    from datetime import datetime
    start_time = datetime.fromisoformat(start)
    end_time = datetime.fromisoformat(end)
    diff = end_time - start_time
    seconds = diff.total_seconds()
    days = int(seconds // 86400)
    hours = int((seconds % 86400) // 3600)
    minutes = int((seconds % 3600) // 60)
    return f"{days}天{hours}小时{minutes}分钟"

def date_to_timestamp(date_str: str) -> int:
    """将日期字符串转换为 Unix 时间戳"""
    from datetime import datetime
    date_obj = datetime.fromisoformat(date_str)
    return int(date_obj.timestamp())


def get_week_of_month() -> str:
    """判断今天是本月的第几周（默认只有4周，不考虑31天的特殊情况）"""
    today = datetime.date.today()

    # 如果今天是28号之后，返回“今天不在计算内”
    if today.day > 28:
        return "今天不在计算内(如果你现在是比28日后的日期，这属于不在我们的计算内)"

    # 计算今天是第几周（1~4）
    week = (today.day - 1) // 7 + 1
    return f"今天是本月的第{week}周"


import time as time_module
import tkinter as tk
from tkinter import messagebox


def rest_reminder(interval: float = 20.0, max_times: int = 5):
    """每隔 interval 分钟提示一次休息，最多提醒 max_times 次"""
    if interval <= 0:
        raise ValueError("时间间隔必须大于0")
    for _ in range(max_times):
        time_module.sleep(interval * 60)
        print(f"⏰ 该休息了！已经连续工作 {interval} 分钟了。")
        root = tk.Tk()
        root.withdraw()
        messagebox.showinfo("休息提醒", f"该休息了！已经连续工作 {interval} 分钟了。")
        root.destroy()

from datetime import datetime, timedelta
#days_until_month_end
def countdown_to_next_hour() -> str:
    """计算距离下一个整点还有多少分钟（比如距离下午3点还有多久）"""
    now = datetime.now()
    next_hour = now.replace(minute=0, second=0, microsecond=0) + timedelta(hours=1)
    minutes_left = int((next_hour - now).total_seconds() // 60)
    return f"距离下一个整点还有 {minutes_left} 分钟"

def days_between(date1: str, date2: str) -> int:
    """计算两个日期之间相差的天数（date2 - date1）"""
    from datetime import date
    d1 = date.fromisoformat(date1)
    d2 = date.fromisoformat(date2)
    return (d2 - d1).days

def format_duration(seconds: int) -> str:
    """把秒数转成人类可读的格式，如 '1天2小时3分'"""
    days = seconds // 86400
    hours = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60

    parts = []
    if days:
        parts.append(f"{days}天")
    if hours:
        parts.append(f"{hours}小时")
    if minutes:
        parts.append(f"{minutes}分")
    if secs:
        parts.append(f"{secs}秒")

    return "".join(parts) if parts else "0秒"

def is_same_day(date1: str, date2: str) -> bool:
    """判断两个日期是不是同一天"""
    from datetime import date
    d1 = date.fromisoformat(date1)
    d2 = date.fromisoformat(date2)
    return d1 == d2

import random

def zhuangge_quote() -> str:
    """随机返回一条装哥语录（彩蛋）"""
    quotes = [
        "我会 C++。",
        "我爸爸是程序员，我知道变量，所以你们都是辣鸡。",
        "我装的是 Python 4.0 绿色免安装版。",
        "我用的是在线编译器。",
        "我写代码不用 IDE，用记事本。",
        "我用脑子跑算法，不用编译器。",
        "我其实学过汇编，只是忘了。",
        "这次我肯定赢。",
        "这不是筛子，这是正宗应用。",
        "我会 Vim。……:q!",
    ]
    return random.choice(quotes)

def time_ago(dt_str: str) -> str:
    """把过去的时间点转成'多久之前'的说法"""
    from datetime import datetime
    target = datetime.fromisoformat(dt_str)
    now = datetime.now()
    diff = now - target

    seconds = int(diff.total_seconds())

    if seconds < 60:
        return f"{seconds}秒前"
    if seconds < 3600:
        return f"{seconds // 60}分钟前"
    if seconds < 86400:
        return f"{seconds // 3600}小时前"
    if seconds < 2592000:
        return f"{seconds // 86400}天前"
    if seconds < 31536000:
        return f"{seconds // 2592000}个月前"
    return f"{seconds // 31536000}年前"

def countdown_to_date(target_date: str) -> str:
    """算距离某个日期还有几天"""
    from datetime import date
    target = date.fromisoformat(target_date)
    today = date.today()
    diff = (target - today).days

    if diff > 0:
        return f"距离 {target_date} 还有 {diff} 天"
    if diff == 0:
        return "就是今天"
    return f"{target_date} 已经过去 {abs(diff)} 天了"

def get_season(date_str: str = None) -> str:
    """根据日期返回季节（春/夏/秋/冬），默认今天"""
    from datetime import date
    if date_str is None:
        d = date.today()
    else:
        d = date.fromisoformat(date_str)

    month = d.month
    day = d.day

    # 按北半球节气大致划分
    if (month == 3 and day >= 20) or month in (4, 5) or (month == 6 and day < 21):
        return "春"
    if (month == 6 and day >= 21) or month in (7, 8) or (month == 9 and day < 23):
        return "夏"
    if (month == 9 and day >= 23) or month in (10, 11) or (month == 12 and day < 21):
        return "秋"
    return "冬"

def is_same_week(date1: str, date2: str) -> bool:
    """判断两个日期是否在同一周（按 ISO 周，周一为一周开始）"""
    from datetime import date
    d1 = date.fromisoformat(date1)
    d2 = date.fromisoformat(date2)
    return d1.isocalendar()[:2] == d2.isocalendar()[:2]

def is_workday() -> bool:
    """判断今天是不是工作日（周一到周五）"""
    return get_weekday() < 5


def days_until_workday() -> int:
    """计算距离下一个工作日还有几天（如果是工作日，返回0）"""
    today = get_weekday()
    if today < 5:
        return 0
    # 周六：2 天后是周一；周日：1 天后是周一
    return 7 - today

def get_week_range(date_str: str = None) -> tuple:
    """返回某日期所在周的起止日期（周一、周日），默认今天"""
    from datetime import date, timedelta
    if date_str is None:
        d = date.today()
    else:
        d = date.fromisoformat(date_str)

    # 找到本周一
    monday = d - timedelta(days=d.weekday())
    sunday = monday + timedelta(days=6)

    return monday.isoformat(), sunday.isoformat()

def next_workday() -> str:
    """计算下一个工作日是哪天，返回 YYYY-MM-DD 格式"""
    from datetime import date, timedelta
    today = date.today()
    days = days_until_workday()
    if days == 0:
        # 今天就是工作日，返回今天
        return today.isoformat()
    next_day = today + timedelta(days=days)
    return next_day.isoformat()


def days_until_specific_weekday(weekday: int) -> int:
    """计算距离指定星期几还有几天（0=周一，6=周日）"""
    if weekday < 0 or weekday > 6:
        raise ValueError("星期几必须是 0~6（0=周一，6=周日）")
    today = get_weekday()
    diff = (weekday - today) % 7
    return diff

def days_until_month_end() -> int:
    """计算距离本月最后一天还有几天（0 表示今天就是本月最后一天）"""
    today = datetime.date.today()
    if today.month == 12:
        next_month = datetime.date(today.year + 1, 1, 1)
    else:
        next_month = datetime.date(today.year, today.month + 1, 1)
    return (next_month - today).days - 1

def days_until_year_end() -> int:
    """计算距离本年最后一天还有几天（0 表示今天就是本年最后一天）"""
    today = datetime.date.today()
    return (datetime.date(today.year, 12, 31) - today).days

def days_until_next_festival() -> int:
    """距离下一个传统节日还有几天（O(1)：只算今明两年的节日，带缓存）"""
    from datetime import date

    today = date.today()
    candidates = []

    for year in (today.year, today.year + 1):
        for (m, d) in _get_festival_dates(year):
            candidates.append(date(year, m, d))

    future = [c for c in candidates if c >= today]
    if not future:
        return 365

    return (min(future) - today).days

def secret_message():
    """运行后，打印出作者留下的一句话（彩蛋）"""
    print("【ticktock 作者留言】")
    if is_weekend():
        print("今天是周末，记得好好休息，别写代码啦！")
    else:
        print("今天是工作日，加油写代码，争取早日实现财务自由！")
    print("—— 来自一位四年级的小程序员")