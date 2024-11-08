import plotly.express as px
import pandas as pd

from datetime import datetime
from typing import Optional

from .database import Database


def chart_plotly(
    start: datetime, end: datetime, tagname=None, caption: Optional[str] = None, aim: Optional[float] = None
):
    """Returns a plotly chart for the given timespan."""
    db = Database.db

    excel = {}
    cur = db.cursor()
    if tagname == None or tagname == '':
        cur.execute('SELECT monitor.id, monitor.name from monitor where monitor.active = 1')
    else:
        cur.execute('SELECT monitor.id, monitor.name from monitor JOIN monitor_tag on (monitor.id = monitor_tag.monitor_id) JOIN tag on (tag.id = monitor_tag.tag_id) where tag.name = ? and monitor.active = 1', (tagname, ))
    result = cur.fetchall()

    for i in result:
        mon_id = i[0]
        mon_name = i[1]

        if result == None:
            continue
        else:
            if 'Id' not in excel:
                excel['Id'] = {}
            if 'Name' not in excel:
                excel['Name'] = {}
            if 'Uptime' not in excel:
                excel['Uptime'] = {}
            excel['Id'][i] = mon_id
            excel['Name'][i] = str(mon_name)
            excel['Uptime'][i] = db.percent_by_monitor_id(mon_id, start, end)

    data = pd.DataFrame.from_dict(excel)
    fig = px.bar(data, x='Name', y='Uptime', hover_data=['Name'], title=caption)
    if aim:
        fig.add_hline(aim, line_color='Red')
    return fig
