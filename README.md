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

| 函数名                                 | 说明                                                 |
|----------------------------------------|------------------------------------------------------|
| `get_ymd()`                            | 获取当前的年月日，返回 `(年, 月, 日)`                |
| `get_hms()`                            | 获取当前的时分秒，返回 `(时, 分, 秒)`                |
| `get_now()`                            | 获取完整的日期时间对象                               |
| `is_leap_year(year)`                   | 判断某年是否为闰年                                   |
| `get_days_in_month(year, month)`       | 判断某年某月有多少天                                 |
| `format_date(fmt)`                     | 任意格式输出当前日期                                 |
| `validate_date(year, month, day)`      | 检查一个日期是否合法                                 |
| `get_weekday()`                        | 返回今天是星期几（0=周一，6=周日）                   |
| `is_weekend()`                         | 判断今天是否为周末（周六或周日）                     |
| `days_until_weekend()`                 | 计算距离下一个周末还有几天                           |
| `get_period_of_day()`                  | 返回当前时间段（早晨、上午、中午、下午、傍晚、深夜） |
| `secret_message()`                     | 打印作者的一句话（彩蛋）                             |
| `date_to_timestamp(date_str)`          | 将日期转换为 Unix 时间戳                             |
| `is_past_date(target_date)`            | 判断目标日期是否已经过去                             |
| `time_difference(start, end)`          | 计算两个时间之间的差                                 |
| `get_week_of_month()`                  | 判断今天是本月第几周（28号后返回提示）               |
| `get_festival()`                       | 判断今天是不是中国传统节日                           |
| `days_until_next_festival()`           | 距离下一个传统节日还有几天                           |
| `rest_reminder(interval, max_times)`   | 每隔 N 分钟弹窗提醒休息                              |
| `days_between(date1, date2)`           | 计算两个日期相差天数                                 |
| `format_duration(seconds)`             | 把秒数转成“1天2小时3分”格式                          |
| `is_same_day(date1, date2)`            | 判断两个日期是不是同一天                             |
| `zhuangge_quote()`                     | 随机返回一条装哥语录（彩蛋）                         |
| `time_ago(dt_str)`                     | 把过去时间点转成“多久之前”                           |
| `countdown_to_date(target_date)`       | 距离某日期还有几天                                   |
| `countdown_to_next_hour()`             | 距离下一个整点还有几分钟                             |
| `get_season(date_str)`                 | 返回季节（春/夏/秋/冬）                              |
| `is_same_week(date1, date2)`           | 判断两个日期是否同一周（ISO 周）                     |
| `is_workday()`                         | 判断今天是不是工作日                                 |
| `days_until_workday()`                 | 距离下一个工作日还有几天                             |
| `next_workday()`                       | 下一个工作日是哪天                                   |
| `days_until_specific_weekday(weekday)` | 距离指定星期几还有几天                               |
| `days_until_month_end()`               | 距离本月最后一天还有几天                             |
| `days_until_year_end()`                | 距离本年最后一天还有几天                             |
| `get_week_range(date_str)`             | 返回某日期所在周的起止日期                           |
| `lunar_to_solar(year, month, day)`     | 农历转公历                                           |
| `solar_to_lunar(year, month, day)`     | 公历转农历                                           |
| `get_zodiac(year)`                     | 返回生肖                                             |
| `get_ganzhi(year)`                     | 返回该年干支，如“甲辰”                               |
| `get_ganzhi_full(year)`                | 返回天干、地支、干支、生肖                           |
| `get_ganzhi_from_date(date)`           | 按日期算干支                                         |
| `get_solar_term(date)`                 | 返回该日期节气名，不是则 None                        |
| `next_solar_term(date)`                | 返回（节气名，还有几天）                             |
| `get_solar_terms(year)`                | 返回该年所有节气                                     |
| `get_zodiac_sign(date)`                | 按日期返回星座                                       |
| `is_same_month(date1, date2)`          | 判断两个日期是否同一个月                             |
| `days_until_next_month()`              | 距离下个月1号还有几天                                |

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


## 📜 License

MIT

## 📝 更新日志 (Changelog)

- 增加了大部分函数的类型提示 比如
- **get_solar_terms**
- **get_ganzhi_full**
- **get_season**

👉 [点击这里查看 CHANGELOG.md](https://github.com/dev-lio-hello-world/ticktock_utils/blob/main/CHANGELOG.md)