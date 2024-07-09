# pySecurityUpdates
An python example to query updates exporting an excel file

Modules required
- Data frames: [pandas](https://pandas.pydata.org)
- http requests: [requests](https://docs.python.org/3/library/urllib.html) 

### Modules Installation
To install modules, use pip install [module name]

### To compile scripts into an exe 
The following demonstrates how to make a compiled windows executable:
```
python -m PyInstaller --onefile scrape.py # single file
pyinstaller --onefile --add-data "path/to/yourdata.yaml;." yourscript.py
```