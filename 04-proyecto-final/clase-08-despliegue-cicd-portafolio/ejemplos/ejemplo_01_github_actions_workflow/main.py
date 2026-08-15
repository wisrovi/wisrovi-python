"""Pipeline de CI en GitHub Actions."""
ci = 'name: CI\non: [push]\njobs:\n  test:\n    runs-on: ubuntu-latest'
print(ci)
