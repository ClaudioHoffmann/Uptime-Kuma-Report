# Uptime-Kuma-Report

## Install
Simply clone and install requirements:
```bash
pip install -r requirements.txt
```

## Use

For a report of the last 30 days:

```bash
# Spins up a web server to show the results in a new browser window
python -m kumareport --db kuma.db -d 30

# Renders the report to a standalone HTML file
python -m kumareport --db kuma.db -d 30 > report.html
```

This is the usage help:
```
Usage: python -m kumareport [OPTIONS]

  Spins up a web server to show an uptime report for the given Uptime-Kuma
  database. Redirect stdout to a file to create a standalone HTML file
  instead.

Options:
  -c, --caption TEXT     Optional chart title
  -t, --tag TEXT         Tagname of the monitors to include in the report
  --db FILENAME          Uptime Kuma database path.  [required]
  -d, --days INTEGER     Number of days to report.  [required]
  -a, --aim FLOAT RANGE  Indicate target availability percentage with a red
                         line  [0<=x<=100]
  --help                 Show this message and exit.
```
