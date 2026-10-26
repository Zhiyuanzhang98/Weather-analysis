# 项目工作约定

- 用中文说明结果，区分已验证、推测和待处理内容。
- 开始前查看仓库状态、README 和依赖文件；保留已有未提交改动。
- 在任务分支修改，每次只处理明确的目标；完成后说明改动和验证结果。
- 不把账号凭据、环境目录或生成的大文件提交到 Git。
- 图片或页面局部修改应保持未修改区域和原始尺寸；精确字体要求不能用近似结果冒充。
- 透明素材需要检查真实背景、边缘和字母封闭区域；网页需要检查相关桌面和手机布局。
- 优先使用当前可用的 GitHub 插件；命令行需要时单独验证 gh 登录。

## Weather-analysis
- Python 3.12 数据分析项目；主入口是 Weather Data Analysis Beijing Ningbo.ipynb。
- Windows 安装：py -3.12 -m venv .venv，然后 .venv\Scripts\python.exe -m pip install -r requirements.txt。
- 启动：.venv\Scripts\python.exe -m jupyterlab。
- 离线检查：.venv\Scripts\python.exe scripts/check_project.py。
- 完整执行：.venv\Scripts\python.exe scripts/run_analysis.py。结果写入 output/，不覆盖原笔记本。
- CSV/XLSX 为原始输入，不在环境配置或验证过程中改写。
- Weather Crawler.ipynb 会请求外部网站并追加 CSV，不作为默认检查步骤。
- 当前模型结果属于历史分析；环境检查通过不代表模型方法或预测结论已经审查。
