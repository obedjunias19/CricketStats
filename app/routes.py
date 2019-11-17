from app import app
from flask import render_template
import pandas as pd
from pandas_highcharts.core import serialize

@app.route("/")
@app.route("/index")
def index():
    return(render_template("index.html"))

@app.route("/dashboard")
def dashboard():
    return(render_template("dashboard.html"))

@app.route("/test/rankings")
def test_rankings():
    df1 = pd.read_csv("app\data\TestRanks.xslx",sep="\t")
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testrankings.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/graph')
def graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 500):
    df1 = pd.read_csv("app/data/TestRanks.xslx",sep="\t")
    df1.dropna(inplace=True)
    df2 = df1[[' Points ',' Team ']]
    df2.set_axis(df2[' Team '],axis=0,inplace=True)
    chart = serialize(df2, render_to='my-chart', output_type='json',kind="bar",title=" ICC Test Rankings")
    return render_template('graph1.html', chart=chart)
 


