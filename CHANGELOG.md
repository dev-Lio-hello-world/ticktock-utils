\# 更新日志 (Changelog)



本项目所有的版本更新都会记录在此文件中。

格式基于 \[Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)，并且遵循 \[语义化版本 (Semantic Versioning)](https://semver.org/lang/zh-CN/)。



\## \[Unreleased]

\### 计划中

\- 准备引入更底层的国际化 (i18n) 架构。

\- 规划未来的破坏性更新 (Breaking Changes)。



\## \[1.1.2] - 2026-10-20

\### 新增 (Added)

\- 因为PyPI无法直接托管CHANGELOG.md 因此在这个版本 加了折叠式CHANGELOG.md 



\## \[1.1.1] - 2026-10-20

\### 新增 (Added)

\- 增加了大部分函数的类型提示 比如

\- \*\*get\_solar\_terms\*\*

\- \*\*get\_ganzhi\_full\*\*

\- \*\*get\_season\*\*



\## \[1.1.0] - 2026-10-20

\### 新增 (Added)

\- 优化了函数\*\*get\_solar\_term\*\*

\- \*\*next\_solar\_term\*\*

\- \*\*get\_solar\_terms\*\*

\- 从O(n)改成O(1)



\## \[1.0.0] - 2026-10-20

\### 新增 (Added)

\- \*\*多语言自动适配\*\*：引入了 `locale` 检测机制。在 Linux/macOS 下读取 `LANG` 环境变量，在 Windows 下读取系统默认语言，实现报错语言的自动切换。

\- \*\*强制覆盖机制\*\*：新增环境变量 `TICKTOCK\_LANG`，支持用户强制指定 `en` 或 `zh`，无视系统默认环境。

\- 将 `error\_is\_english` 变量的默认值改为由上述自动检测逻辑动态获取。

\- 增加 `\_detect\_language()` 内部函数，负责解析语言环境。

``

\### 改进 (Changed)

\- 彩蛋函数 `secret\_message()` 现在会根据当前语言环境，自动输出对应的中文或英文留言。



\## \[0.20.0] - 2026-10-18

\### 新增 (Added)

\- 新增 `is\_same\_month(date1, date2)` 函数，用于判断两个 ISO 格式的日期字符串是否在同一个月。

\- 新增 `days\_until\_next\_month()` 函数，计算距离下个月 1 号还有几天。



\### 文档 (Documentation)

\- 补齐了 README 中缺失的 40 多个函数功能对照表，完善了接口文档。



\### 改进 (Changed)

\- 更新了 `\_\_init\_\_.py` 的导入及导出列表，加入新函数 `is\_same\_month` 和 `days\_until\_next\_month`。



\## \[0.19.0] - 2026-10-17

\### 新增 (Added)

\- \*\*星座查询系统\*\*：新增 `get\_zodiac\_sign(date)` 函数。通过将月份和日期转换为整数，并利用 `bisect` 模块进行二分查找，实现 \\(O(\\log n)\\) 复杂度的极速星座匹配。



\### 改进 (Changed)

\- 更新了 `\_\_init\_\_.py`，将 `get\_zodiac\_sign` 补充进导入列表和 `\_\_all\_\_` 导出列表。

\- 优化了文件头部的导入，统一在顶部引入了 `from datetime import date`。



\### 内部 (Internal)

\- 在 `if \_\_name\_\_ == "\_\_main\_\_":` 中加入了极其硬核的星座边界测试用例（24 个测试点），覆盖了 12 星座的「第一天」和「最后一天」，确保二分查找逻辑绝对精准。



\## \[0.18.0] - 2026-10-16

\### 新增 (Added)

\- \*\*二十四节气系统\*\*：新增常量列表 `SOLAR\_TERMS`，硬编码了 24 节气的公历典型日期。

\- 新增 `get\_solar\_term(date)` 函数，判断传入日期是否为节气。

\- 新增 `next\_solar\_term(date)` 函数，通过循环向后遍历最多 370 天，返回下一个节气名称及距今天数。

\- 新增 `get\_solar\_terms(year)` 函数，返回该年所有节气的列表。



\### 改进 (Changed)

\- 在 `\_\_init\_\_.py` 的导入部分新增了上述三个节气函数。



\## \[0.17.1] - 2026-10-15

\### 新增 (Added)

\- \*\*干支纪年体系\*\*：正式加入中国传统的干支历法系统。新增常量列表 `TIANGAN`、`DIZHI` 和 `SHENGXIAO`。

\- 新增 `get\_ganzhi(year)`、`get\_ganzhi\_full(year)` 及 `get\_ganzhi\_from\_date(date)` 函数，支持干支与生肖的精准查询。



\### 内部 (Internal)

\- 补充了 `if \_\_name\_\_ == "\_\_main\_\_":` 测试代码，验证了春节前后干支纪年的切换逻辑。



\## \[0.16.0] - 2026-10-14

\### 新增 (Added)

\- \*\*农历互转\*\*：新增 `lunar\_to\_solar(year, month, day)` 和 `solar\_to\_lunar(year, month, day)` 函数，正式支持公历与农历的双向转换。

\- \*\*生肖查询\*\*：新增 `get\_zodiac(year)` 函数，根据公历年份返回对应生肖。



\### 变更 (Changed)

\- \*\*彩蛋双语化支持\*\*：新增全局变量 `easter\_egg\_is\_english`，用于独立控制彩蛋的显示语言。

\- 重构了 `zhuangge\_quote()` 和 `secret\_message()`，现在它们会根据变量输出完整的中文或英文版本。



\## \[0.14.2] - 2026-10-13

\### 新增 (Added)

\- 新增 `days\_until\_month\_end()` 函数，计算距离本月最后一天还有几天。

\- 新增 `days\_until\_year\_end()` 函数，计算距离本年最后一天还有几天。



\### 性能优化 (Performance)

\- \*\*节日倒计时重构\*\*：彻底重写了 `days\_until\_next\_festival()`，引入了 `functools.lru\_cache` 缓存机制，将循环 366 次的暴力算法优化为 \\(O(1)\\) 查找。



\### 修复 (Fixed)

\- 修复了 `\_\_init\_\_.py` 中 `\_\_all\_\_` 列表里缺失的逗号。



\## \[0.13.0] - 2026-10-12

\### 新增 (Added)

\- 新增 `days\_until\_specific\_weekday(weekday)` 函数，计算距离指定星期几还有多少天。

\- 补齐了 `next\_workday()` 函数的实现，支持计算并返回下一个工作日的 ISO 格式日期。



\## \[0.12.1] - 2026-10-11

\### 新增 (Added)

\- 新增 `is\_same\_week()`、`is\_workday()`、`days\_until\_workday()` 和 `get\_week\_range()` 函数，全面支持周相关计算。

\- 补全了 `next\_weekday` 函数的实现，并正式加入顶层导出列表。



\## \[0.11.1] - 2026-10-09

\### 新增 (Added)

\- 新增 `get\_season(date\_str)` 函数，根据传入的 ISO 日期（不传则默认今天），自动判断并返回当前季节。



\### 改进 (Changed)

\- 更新了 `\_\_init\_\_.py`，将 `get\_season` 加入顶层导出列表。



\## \[0.10.0] - 2026-10-08

\### 新增 (Added)

\- 新增 `time\_ago(dt\_str)` 函数，将过去的时间转换为“X秒前”、“X分钟前”等描述。

\- 新增 `countdown\_to\_date(target\_date)` 函数，计算距离目标日期还有几天。



\### 改进 (Changed)

\- \*\*重构休息提醒\*\*：重写了 `rest\_reminder(interval, max\_times)` 函数，移除了原本危险的 `while True` 死循环，改为限制最大弹窗次数。



\## \[0.9.0] - 2026-10-07

\### 新增 (Added)

\- 新增 `is\_same\_day(date1, date2)` 函数，用于判断两个日期是否为同一天。

\- \*\*彩蛋加入\*\*：新增 `zhuangge\_quote()` 函数，内置 10 条“装哥语录”，每次调用随机返回一条。



\### 内部 (Internal)

\- 引入了 Python 标准库 `random` 模块，用于支持随机彩蛋的抽取。



\## \[0.8.0] - 2026-10-06

\### 新增 (Added)

\- 新增 `days\_between(date1, date2)` 函数，计算两个日期之间相差的天数。

\- 新增 `format\_duration(seconds)` 函数，将纯秒数转换为人类可读的“X天X小时X分X秒”格式。



\### 改进 (Changed)

\- 优化了 `get\_week\_of\_month()` 的返回值提示语，针对 28 号之后增加了更详细的解释文案。



\## \[0.7.0] - 2026-10-05

\### 新增 (Added)

\- 新增 `rest\_reminder(time)` 函数，利用 `tkinter` 实现定时弹窗休息提醒。

\- 新增 `countdown\_to\_next\_hour()` 函数，计算距离下一个整点还有多少分钟。



\## \[0.6.0] - 2026-10-04

\### 新增 (Added)

\- 新增 `get\_week\_of\_month()` 函数，计算今天是本月的第几周（28号之后返回不在计算内）。

\- 新增 `days\_until\_next\_festival()` 函数，计算距离下一个传统节日还有几天。



\## \[0.5.0] - 2026-10-02

\### 新增 (Added)

\- \*\*农历节日查询\*\*：引入第三方库 `lunarcalendar`，新增 `get\_festival()` 函数，支持识别春节、元宵节等传统节日。

\- \*\*除夕特殊判定\*\*：加入了“判断下一天是否为正月初一”的逻辑。



\### 依赖 (Dependencies)

\- 新增项目依赖：`lunarcalendar`。



\## \[0.4.0] - 2026-10-01

\### 新增 (Added)

\- 新增 `get\_period\_of\_day()` 函数，返回早晨、上午、中午等时间段。

\- 新增 `is\_past\_date()` 和 `time\_difference()` 函数，支持时间差计算。

\- 新增 `date\_to\_timestamp()` 函数，支持将日期转换为 Unix 时间戳。



\## \[0.3.1] - 2026-09-25

\### 新增 (Added)

\- 基础框架成型，提供核心的日期时间获取功能。

\- 新增闰年判断、获取某月天数、日期格式化输出等功能。

\- 引入日期验证器，并内置了自定义异常类 `TimeError`、`MonthError` 和 `DayError`。

\- 增加周末判断功能，以及倒计时到周末的功能。

\- 添加作者留言彩蛋 `secret\_message()`。



\## \[0.2.0] - 2026-09-05

\### 新增 (Added)

\- \*\*初次发布 (Initial Release)\*\*。

\- 实现最基本的日期时间获取功能。

\- 支持通过 pip 安装。

