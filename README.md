# my test repo
This is the repository developed alongside the course "Scientific Software Development", March 2022, Inga S. Ulusoy, Scientific Software Center.

You can find this on [testPyPI](https://test.pypi.org/project/myteam/).

To upload to testPyPi
```
python -m twine upload --skip-existing --repository testpypi dist/*
```

To install with dependencies from PyPi:
```
python -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple myteam
```
