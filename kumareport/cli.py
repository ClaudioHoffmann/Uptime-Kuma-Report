from typing import Optional
import click
import sys

from datetime import datetime, timedelta

from .database import Database
from .chart import chart_plotly


@click.command(help="""
Spins up a web server to show an uptime report for the given Uptime-Kuma database.
Redirect stdout to a file to create a standalone HTML file instead.
""")
@click.option('--caption', '-c', help='Optional chart title', type=str)
@click.option('--tag', '-t', help='Tagname of the monitors to include in the report')
@click.option('--db', help='Uptime Kuma database path.', type=click.File(), required=True)
@click.option('--days', '-d', help='Number of days to report.', type=int, required=True)
@click.option('--aim', '-a', help='Indicate target availability percentage with a red line', type=click.FloatRange(0, 100))
def cli(db, days, tag, caption: Optional[str], aim: Optional[float]):
    Database(db.name)

    end = datetime.now()
    start = (end - timedelta(days=days))

    chart = chart_plotly(start, end, tag, caption, aim)
    if sys.stdout.isatty():
        chart.show()
    else:
        print(chart.to_html(include_plotlyjs='cdn'))
