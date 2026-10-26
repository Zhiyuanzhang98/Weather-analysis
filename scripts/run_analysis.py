from pathlib import Path
import sys
import nbformat
from nbclient import NotebookClient
from jupyter_client.kernelspec import KernelSpecManager

root = Path(__file__).resolve().parents[1]
out = root / "output"
out.mkdir(exist_ok=True)
nb = nbformat.read(root / "Weather Data Analysis Beijing Ningbo.ipynb", as_version=4)
# Bind execution to this project's interpreter, not a globally installed kernel.
client = NotebookClient(nb, timeout=300, kernel_name="python3", resources={"metadata": {"path": str(root)}})
client.create_kernel_manager()
client.km.kernel_spec.argv = [sys.executable, "-m", "ipykernel_launcher", "-f", "{connection_file}"]
client.execute()
target = out / "analysis.executed.ipynb"
nbformat.write(nb, target)
print(f"PASS: analysis executed; saved to {target}")
