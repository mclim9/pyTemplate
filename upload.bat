python setup.py sdist
python -m unittest -v test.test_LoadModules.py
twine upload .\dist\covid.tar.gz
