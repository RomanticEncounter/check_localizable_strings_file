# localizable_strings_checker

> 基于 AI 生成的用于检查`Localizable.strings`的工具

[Qwen对话过程](https://chat.qwen.ai/s/e2a1ec86-244e-42b1-a336-09f6d9ee3440?fev=0.0.107)

![iTerm Screenshot](https://github.com/user-attachments/assets/331126b8-73df-4cf4-95fd-7a8125183a79)


## 一、工具概述

本工具专为解决 `iOS` 开发者在 `Xcode` 开发者工具中，无法精准检查`Localizable.strings`文件内具体报错问题的痛点而开发。基于 `Qwen3-235B-A22B` 大模型技术编写，它能快速且细致地对文件进行全面检查，涵盖分号结尾、单行注释、多行注释等多项关键内容，助力开发者高效提升多语言本地化工作的质量与效率。

#### 项目结构如下：

```text
localizable_strings_checker/
├── setup.py
├── README.md
└── src/
    └── csf/
        ├── __init__.py
        └── cli.py
```

## 二、使用方法

~~打开终端，`cd`到此工具文件路径下，输入以下命令~~
```diff
- python3 check_localizable_strings_file.py xxxxx/en.lproj/Localizable.strings

+ cd path/localizable_strings_checker
```

#### **步骤 1：创建虚拟环境**

```bash
python3 -m venv venv #创建虚拟环境
```
#### **步骤 2：激活虚拟环境**

```bash
source venv/bin/activate #激活虚拟环境
```
激活后，终端提示符会显示 (venv)，表示已进入虚拟环境。

#### **步骤 3：在虚拟环境中安装依赖**

```bash
pip install setuptools #安装工具依赖
pip install -e .  #安装你的工具到虚拟环境中

csf test_localizable.strings #测试工具运行
```

此时安装的包仅对当前虚拟环境生效，不会影响系统环境。

#### **步骤 4：退出虚拟环境（可选）**

```bash
deactivate
```

## 三、检查内容详情

1. 语法错误检查
- 分号结尾检查：验证每个键值对结尾是否正确添加分号，缺少分号将触发报错提示，并标注具体行号。
- 引号成对检查：检查字符串中的引号是否成对出现，单引号或双引号缺失、多余都会被标记，同时提示错误位置。
- 键值对格式检查：确保键值对采用`"key" = "value";`的标准格式，格式错误（如等号缺失、键值未用引号包裹）会被精准定位并提示。
- 值中的未转义双引号检查：扫描值中的双引号，若未使用反斜杠进行转义，工具会指出该问题，避免字符串解析错误。

2. 注释相关检查
- 单行注释检查：识别以`//`开头的单行注释，若注释格式错误（如注释符号后无空格、注释内容包含非法字符），将在报告中列出。
- 多行注释检查：检查以`/*`开头、`*/`结尾的多行注释，检测是否存在未闭合的多行注释情况，一旦发现，立即标注注释起始和可能缺失结尾的位置。

3. 逻辑错误检查
- 键或值为空检查：遍历所有键值对，若键或值为空字符串，工具会记录并提示，避免无效的本地化配置。
- 键重复检查：查找文件中重复的键名，重复的键会导致本地化取值混乱，工具将详细列出重复键及其所在行号。

