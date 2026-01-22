# Applicant Filter - 候选人筛选系统

一个可扩展的候选人筛选系统，支持 LinkedIn Business API 集成（预留接口），用于筛选 Operation Manager、Compliance Advisor、Business Development Manager 等职位的候选人。

## 功能特性

- **可扩展筛选器系统**: 基于抽象基类设计，轻松添加新的筛选条件
- **多维度筛选**: 年龄、工作经验、地点、教育/工作背景
- **Excel 导出**: 支持基础报告和详细报告导出
- **LinkedIn API 预留接口**: 可无缝对接 LinkedIn Business API
- **Shell 脚本展示**: 命令行友好的候选人信息展示

## 筛选条件

| 筛选器 | 条件 |
|--------|------|
| AgeFilter | 20 ≤ 年龄 ≤ 40 |
| ExperienceFilter | 1 ≤ 工作年限 ≤ 3 |
| LocationFilter | 排除 Sydney |
| BackgroundFilter | 有中文或英文背景，排除印度/中东地区 |

## 安装

### 环境要求

- Python 3.8+
- pip

### 安装步骤

```bash
# 克隆仓库
git clone https://github.com/B1ueky/applicant-filter-candidate.git
cd applicant-filter-candidate

# 安装依赖
pip install -r requirements.txt
```

## 使用方法

### 基本运行

```bash
python main.py
```

### 详细模式（显示筛选统计）

```bash
python main.py --verbose
```

### 导出详细报告

```bash
python main.py --detailed
```

### Shell 脚本展示

```bash
./scripts/display_candidates.sh
```

## 项目结构

```
applicant_filter_candidate/
├── config/
│   ├── __init__.py
│   └── settings.py          # 筛选条件和 API 配置
├── src/
│   ├── __init__.py
│   ├── candidate.py         # 候选人数据模型
│   ├── filter_manager.py    # 筛选器管理器
│   ├── linkedin_client.py   # LinkedIn API 客户端（预留接口）
│   ├── mock_data.py         # 模拟测试数据
│   ├── exporter.py          # Excel 导出器
│   └── filters/
│       ├── __init__.py
│       ├── base_filter.py       # 筛选器抽象基类
│       ├── age_filter.py        # 年龄筛选器
│       ├── experience_filter.py # 经验筛选器
│       ├── location_filter.py   # 地点筛选器
│       └── background_filter.py # 背景筛选器
├── scripts/
│   └── display_candidates.sh    # Shell 展示脚本
├── output/                      # 输出目录
├── main.py                      # 主程序入口
└── requirements.txt             # 项目依赖
```

## 自定义筛选器

继承 `BaseFilter` 类即可创建新的筛选器：

```python
from src.filters.base_filter import BaseFilter
from src.candidate import Candidate

class CustomFilter(BaseFilter):
    def apply(self, candidate: Candidate) -> bool:
        # 返回 True 表示候选人通过筛选
        return candidate.some_field == some_value
```

然后在 `main.py` 中注册：

```python
filter_manager.add_filter(CustomFilter())
```

## 配置说明

编辑 `config/settings.py` 修改筛选条件：

```python
@dataclass
class FilterSettings:
    min_age: int = 20
    max_age: int = 40
    min_experience_years: float = 1.0
    max_experience_years: float = 3.0
    excluded_locations: List[str] = field(default_factory=lambda: ["Sydney"])
    # ...
```

## LinkedIn API 集成

项目预留了 LinkedIn API 接口，集成步骤：

1. 在 [LinkedIn Developers](https://www.linkedin.com/developers/) 注册应用
2. 获取 API 凭证（client_id, client_secret）
3. 在 `config/settings.py` 配置凭证
4. 实现 `src/linkedin_client.py` 中的 API 调用方法

## 输出示例

### 命令行输出

```
=========================================
姓名: 张伟 (Wei Zhang)
职位: Operation Manager
经验: 2.0年
地点: Melbourne
LinkedIn: https://linkedin.com/in/weizhang
=========================================
```

### Excel 输出

| Name | Position | Experience (Years) | Location | LinkedIn URL |
|------|----------|-------------------|----------|--------------|
| 张伟 (Wei Zhang) | Operation Manager | 2.0 | Melbourne | https://linkedin.com/in/weizhang |

## 许可证

MIT License
