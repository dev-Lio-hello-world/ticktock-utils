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

<details>
<summary>点击展开查看完整更新日志</summary>

# 更新日志 (Changelog)

本项目所有的版本更新都会记录在此文件中。
格式基于 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，并且遵循 [语义化版本 (Semantic Versioning)](https://semver.org/lang/zh-CN/)。

## [Unreleased]
### 计划中
- 准备引入更底层的国际化 (i18n) 架构。
- 规划未来的破坏性更新 (Breaking Changes)。

## [1.1.2] - 2026-10-20
### 新增 (Added)
- 因为PyPI无法直接托管CHANGELOG.md 因此在这个版本 加了折叠式CHANGELOG.md 

## [1.1.1] - 2026-10-20
### 新增 (Added)
- 增加了大部分函数的类型提示 比如
- **get_solar_terms**
- **get_ganzhi_full**
- **get_season**

## [1.1.0] - 2026-10-20
### 新增 (Added)
- 优化了函数**get_solar_term**
- **next_solar_term**
- **get_solar_terms**
- 从O(n)改成O(1)

## [1.0.0] - 2026-10-20
### 新增 (Added)
- **多语言自动适配**：引入了 `locale` 检测机制。在 Linux/macOS 下读取 `LANG` 环境变量，在 Windows 下读取系统默认语言，实现报错语言的自动切换。
- **强制覆盖机制**：新增环境变量 `TICKTOCK_LANG`，支持用户强制指定 `en` 或 `zh`，无视系统默认环境。
- 将 `error_is_english` 变量的默认值改为由上述自动检测逻辑动态获取。
- 增加 `_detect_language()` 内部函数，负责解析语言环境。
``
### 改进 (Changed)
- 彩蛋函数 `secret_message()` 现在会根据当前语言环境，自动输出对应的中文或英文留言。

## [0.20.0] - 2026-10-18
### 新增 (Added)
- 新增 `is_same_month(date1, date2)` 函数，用于判断两个 ISO 格式的日期字符串是否在同一个月。
- 新增 `days_until_next_month()` 函数，计算距离下个月 1 号还有几天。

### 文档 (Documentation)
- 补齐了 README 中缺失的 40 多个函数功能对照表，完善了接口文档。

### 改进 (Changed)
- 更新了 `__init__.py` 的导入及导出列表，加入新函数 `is_same_month` 和 `days_until_next_month`。

## [0.19.0] - 2026-10-17
### 新增 (Added)
- **星座查询系统**：新增 `get_zodiac_sign(date)` 函数。通过将月份和日期转换为整数，并利用 `bisect` 模块进行二分查找，实现 \(O(\log n)\) 复杂度的极速星座匹配。

### 改进 (Changed)
- 更新了 `__init__.py`，将 `get_zodiac_sign` 补充进导入列表和 `__all__` 导出列表。
- 优化了文件头部的导入，统一在顶部引入了 `from datetime import date`。

### 内部 (Internal)
- 在 `if __name__ == "__main__":` 中加入了极其硬核的星座边界测试用例（24 个测试点），覆盖了 12 星座的「第一天」和「最后一天」，确保二分查找逻辑绝对精准。

## [0.18.0] - 2026-10-16
### 新增 (Added)
- **二十四节气系统**：新增常量列表 `SOLAR_TERMS`，硬编码了 24 节气的公历典型日期。
- 新增 `get_solar_term(date)` 函数，判断传入日期是否为节气。
- 新增 `next_solar_term(date)` 函数，通过循环向后遍历最多 370 天，返回下一个节气名称及距今天数。
- 新增 `get_solar_terms(year)` 函数，返回该年所有节气的列表。

### 改进 (Changed)
- 在 `__init__.py` 的导入部分新增了上述三个节气函数。

## [0.17.1] - 2026-10-15
### 新增 (Added)
- **干支纪年体系**：正式加入中国传统的干支历法系统。新增常量列表 `TIANGAN`、`DIZHI` 和 `SHENGXIAO`。
- 新增 `get_ganzhi(year)`、`get_ganzhi_full(year)` 及 `get_ganzhi_from_date(date)` 函数，支持干支与生肖的精准查询。

### 内部 (Internal)
- 补充了 `if __name__ == "__main__":` 测试代码，验证了春节前后干支纪年的切换逻辑。

## [0.16.0] - 2026-10-14
### 新增 (Added)
- **农历互转**：新增 `lunar_to_solar(year, month, day)` 和 `solar_to_lunar(year, month, day)` 函数，正式支持公历与农历的双向转换。
- **生肖查询**：新增 `get_zodiac(year)` 函数，根据公历年份返回对应生肖。

### 变更 (Changed)
- **彩蛋双语化支持**：新增全局变量 `easter_egg_is_english`，用于独立控制彩蛋的显示语言。
- 重构了 `zhuangge_quote()` 和 `secret_message()`，现在它们会根据变量输出完整的中文或英文版本。

## [0.14.2] - 2026-10-13
### 新增 (Added)
- 新增 `days_until_month_end()` 函数，计算距离本月最后一天还有几天。
- 新增 `days_until_year_end()` 函数，计算距离本年最后一天还有几天。

### 性能优化 (Performance)
- **节日倒计时重构**：彻底重写了 `days_until_next_festival()`，引入了 `functools.lru_cache` 缓存机制，将循环 366 次的暴力算法优化为 \(O(1)\) 查找。

### 修复 (Fixed)
- 修复了 `__init__.py` 中 `__all__` 列表里缺失的逗号。

## [0.13.0] - 2026-10-12
### 新增 (Added)
- 新增 `days_until_specific_weekday(weekday)` 函数，计算距离指定星期几还有多少天。
- 补齐了 `next_workday()` 函数的实现，支持计算并返回下一个工作日的 ISO 格式日期。

## [0.12.1] - 2026-10-11
### 新增 (Added)
- 新增 `is_same_week()`、`is_workday()`、`days_until_workday()` 和 `get_week_range()` 函数，全面支持周相关计算。
- 补全了 `next_weekday` 函数的实现，并正式加入顶层导出列表。

## [0.11.1] - 2026-10-09
### 新增 (Added)
- 新增 `get_season(date_str)` 函数，根据传入的 ISO 日期（不传则默认今天），自动判断并返回当前季节。

### 改进 (Changed)
- 更新了 `__init__.py`，将 `get_season` 加入顶层导出列表。

## [0.10.0] - 2026-10-08
### 新增 (Added)
- 新增 `time_ago(dt_str)` 函数，将过去的时间转换为“X秒前”、“X分钟前”等描述。
- 新增 `countdown_to_date(target_date)` 函数，计算距离目标日期还有几天。

### 改进 (Changed)
- **重构休息提醒**：重写了 `rest_reminder(interval, max_times)` 函数，移除了原本危险的 `while True` 死循环，改为限制最大弹窗次数。

## [0.9.0] - 2026-10-07
### 新增 (Added)
- 新增 `is_same_day(date1, date2)` 函数，用于判断两个日期是否为同一天。
- **彩蛋加入**：新增 `zhuangge_quote()` 函数，内置 10 条“装哥语录”，每次调用随机返回一条。

### 内部 (Internal)
- 引入了 Python 标准库 `random` 模块，用于支持随机彩蛋的抽取。

## [0.8.0] - 2026-10-06
### 新增 (Added)
- 新增 `days_between(date1, date2)` 函数，计算两个日期之间相差的天数。
- 新增 `format_duration(seconds)` 函数，将纯秒数转换为人类可读的“X天X小时X分X秒”格式。

### 改进 (Changed)
- 优化了 `get_week_of_month()` 的返回值提示语，针对 28 号之后增加了更详细的解释文案。

## [0.7.0] - 2026-10-05
### 新增 (Added)
- 新增 `rest_reminder(time)` 函数，利用 `tkinter` 实现定时弹窗休息提醒。
- 新增 `countdown_to_next_hour()` 函数，计算距离下一个整点还有多少分钟。

## [0.6.0] - 2026-10-04
### 新增 (Added)
- 新增 `get_week_of_month()` 函数，计算今天是本月的第几周（28号之后返回不在计算内）。
- 新增 `days_until_next_festival()` 函数，计算距离下一个传统节日还有几天。

## [0.5.0] - 2026-10-02
### 新增 (Added)
- **农历节日查询**：引入第三方库 `lunarcalendar`，新增 `get_festival()` 函数，支持识别春节、元宵节等传统节日。
- **除夕特殊判定**：加入了“判断下一天是否为正月初一”的逻辑。

### 依赖 (Dependencies)
- 新增项目依赖：`lunarcalendar`。

## [0.4.0] - 2026-10-01
### 新增 (Added)
- 新增 `get_period_of_day()` 函数，返回早晨、上午、中午等时间段。
- 新增 `is_past_date()` 和 `time_difference()` 函数，支持时间差计算。
- 新增 `date_to_timestamp()` 函数，支持将日期转换为 Unix 时间戳。

## [0.3.1] - 2026-09-25
### 新增 (Added)
- 基础框架成型，提供核心的日期时间获取功能。
- 新增闰年判断、获取某月天数、日期格式化输出等功能。
- 引入日期验证器，并内置了自定义异常类 `TimeError`、`MonthError` 和 `DayError`。
- 增加周末判断功能，以及倒计时到周末的功能。
- 添加作者留言彩蛋 `secret_message()`。

## [0.2.0] - 2026-09-05
### 新增 (Added)
- **初次发布 (Initial Release)**。
- 实现最基本的日期时间获取功能。
- 支持通过 pip 安装。

</details>