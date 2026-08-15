"""Dockerfile Ligero (python:3.11-slim)."""
df = 'FROM python:3.11-slim\nWORKDIR /app\nCOPY . .\nCMD ["python", "main.py"]'
print(df)
