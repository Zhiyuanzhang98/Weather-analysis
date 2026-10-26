# 本地开发与检查

本仓库是空气质量分析项目，选择它是因为已经包含数据和可执行笔记本。

## Windows 首次安装
```powershell
py -3.12 -m venv .venv
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

## 日常操作
```powershell
.venv\Scripts\python.exe scripts/check_project.py
.venv\Scripts\python.exe scripts/run_analysis.py
.venv\Scripts\python.exe -m jupyterlab
```

原始 CSV、Excel 和笔记本保留；完整执行结果写入被 Git 忽略的 output/。
离线检查验证数据可读、关键字段、日期和笔记本结构。它不运行网络爬虫，也不代表模型结论已得到验证。
requirements.in 是直接依赖清单；requirements.txt 是配置成功后锁定的环境。
GitHub Actions 配置已准备，推送后才会实际触发远端检查。

## 当前分析的后续改进
- 原笔记本在训练/测试拆分前拟合 StandardScaler，存在数据泄漏风险。
- 模型比较图采用硬编码指标，后续应直接读取当次计算结果。
- 字体配置含 Arial Unicode MS，是否可用取决于运行系统。
这些属于分析方法和呈现改进，不以环境配置通过代替修复。
