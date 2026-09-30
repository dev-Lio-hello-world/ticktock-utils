# ticktock_utils

一个超级简单、轻量级的 Python 时间工具库。支持拿到当前时间、判断闰年、验证日期，还带贴心报错！

## 🚀 快速开始（Quick Start）

安装很简单：

```bash
pip install ticktock_utils
```

然后你就可以用了：

```python
import ticktock_utils

# 拿到今天
year, month, day = ticktock_utils.get_ymd()
print(f"今天是 {year} 年 {month} 月 {day} 日")

# 拿到现在
hour, minute, second = ticktock_utils.get_hms()
print(f"现在是 {hour}:{minute}:{second}")
```

## 🧠 功能列表

| 函数名 | 说明 |
|--------|------|
| `get_ymd()` | 获取当前的年月日，返回 `(年, 月, 日)` |
| `get_hms()` | 获取当前的时分秒，返回 `(时, 分, 秒)` |
| `get_now()` | 获取完整的日期时间对象 |
| `is_leap_year(year)` | 判断某年是否为闰年 |
| `get_days_in_month(year, month)` | 判断某年某月有多少天 |
| `format_date(fmt)` | 任意格式输出当前日期 |
| `validate_date(year, month, day)` | 检查一个日期是否合法 |
| `get_weekday()` | 返回今天是星期几（0=周一，6=周日） |
| `is_weekend()` | 判断今天是否为周末（周六或周日） |
| `days_until_weekend()` | 计算距离下一个周末还有几天 |
| `get_period_of_day()` | 返回当前时间段（早晨、上午、中午、下午、傍晚、深夜） |
| `secret_message()` | 打印作者的一句话（彩蛋） |
| `date_to_timestamp()` | 将日期转换为 Unix 时间戳 |
| `is_past_date()` | 判断目标日期是否已经过去 |
| `time_difference()` | 计算两个时间之间的差 |

## ⚠️ 报错处理

如果你输入了错误的月份或日期，**报错也不会让你头大**：

```python
import ticktock_utils

try:
    ticktock_utils.validate_date(2026, 2, 29)  # 2026年是平年，28天
except ticktock_utils.MonthError:
    print("月份输入有误！")
except ticktock_utils.DayError:
    print("日期超出当月天数了！")
```

## 更新日志🗓
修复了is_same_week / get_week_range 没导出、import datetime + from datetime import datetime 在开头重复（这些在0.14.1修复）将days_until_next_festival提速

## 📜 License

MIT

