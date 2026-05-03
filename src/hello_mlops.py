import sys
import pandas as pd
import numpy as np
import sklearn
import dvc
import mlflow

print("=" * 60)
print("✓ MLOps Environment Ready!")
print("=" * 60)

print(f"Python version: {sys.version}")
print(f"pandas: {pd.__version__}")
print(f"numpy: {np.__version__}")
print(f"sklearn: {sklearn.__version__}")
print(f"dvc: {dvc.__version__}")
print(f"mlflow: {mlflow.__version__}")