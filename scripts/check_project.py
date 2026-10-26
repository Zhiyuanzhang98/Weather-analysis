from pathlib import Path
import json
import pandas as pd
import nbformat

root = Path(__file__).resolve().parents[1]
report = {}
for name in ("1air_beijing_data.csv", "1air_ningbo_data.csv", "all_data.csv"):
    frame = pd.read_csv(root / name)
    required = {"日期", "AQI指数", "PM2.5", "PM10"}
    missing = required.difference(frame.columns)
    if frame.empty or missing:
        raise ValueError(f"{name}: empty data or missing columns {missing}")
    pd.to_datetime(frame["日期"], errors="raise")
    report[name] = {"rows": len(frame), "columns": len(frame.columns)}
frame = pd.read_excel(root / "air1824_beijing_data.xlsx")
if frame.empty or "AQI指数" not in frame:
    raise ValueError("Excel input has no usable AQI data")
report["air1824_beijing_data.xlsx"] = {"rows": len(frame)}
for path in root.glob("*.ipynb"):
    notebook = nbformat.read(path, as_version=4)
    nbformat.validate(notebook)
    report[path.name] = {"cells": len(notebook.cells), "structure": "valid"}
print(json.dumps(report, ensure_ascii=False, indent=2))
print("PASS: offline input and notebook structure checks")
