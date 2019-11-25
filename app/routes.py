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
                    <div>
                    <button class="mui-btn mui-btn--raised mui-btn--primary"><a href="#">G</a></button>
                    </div>
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


@app.route("/test/indian-batting/stats")
def indian_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/INDIA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route("/test/afg-batting/stats")
def afg_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/AFG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/aus-batting/stats")
def aus_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/AUS.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/bdesh-batting/stats")
def bdesh_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/BDESH.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/eng-batting/stats")
def eng_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/ENG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/ire-batting/stats")
def ire_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/IRE.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/nz-batting/stats")
def nz_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/NZ.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/pak-batting/stats")
def pak_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/PAK.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/sa-batting/stats")
def sa_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/SA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/sl-batting/stats")
def sl_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/SL.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/wi-batting/stats")
def wi_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/WI.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/test/zim-batting/stats")
def zim_test_batsmen():
    df1 = pd.read_excel("app/data/testbatters/ZIM.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')



@app.route('/test/ind-batting/graph')
def indgraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/INDIA.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Indian Batsmen")
    return render_template('graph2.html', chart=chart)


@app.route('/test/afg-batting/graph')
def afggraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/AFG.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Afghanistan Batsmen")
    return render_template('graph2.html', chart=chart)
 
@app.route('/test/aus-batting/graph')
def ausgraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/AUS.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Australia Batsmen")
    return render_template('graph2.html', chart=chart)

@app.route('/test/bdesh-batting/graph')
def bdeshgraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/BDESH.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Bangladesh Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/test/eng-batting/graph')
def enggraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/ENG.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="England Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/test/ire-batting/graph')
def iregraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/IRE.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="IRELAND Batsmen")
    return render_template('graph2.html', chart=chart)
 
 
@app.route('/test/nz-batting/graph')
def nzgraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/NZ.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="New-Zealand Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/test/pak-batting/graph')
def pakgraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/PAK.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Pakistan Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/test/sa-batting/graph')
def sagraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/SA.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="South Africa Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/test/sl-batting/graph')
def slgraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/SL.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Sri Lanka Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/test/wi-batting/graph')
def wigraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/WI.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="West Indies Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/test/zim-batting/graph')
def zimgraph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/testbatters/ZIM.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Zimbawe Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route("/odi/indian-batting/stats")
def indian_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/INDIA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route("/test/afg-batting/stats")
def afg_odi_batsmen():
    df1 = pd.read_excel("app/data/testbatters/AFG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/aus-batting/stats")
def aus_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/AUS.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/bdesh-batting/stats")
def bdesh_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/BDESH.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/eng-batting/stats")
def eng_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/ENG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/ire-batting/stats")
def ire_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/IRE.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/nz-batting/stats")
def nz_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/NZ.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/pak-batting/stats")
def pak_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/PAK.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/sa-batting/stats")
def sa_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/SA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/sl-batting/stats")
def sl_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/SL.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/wi-batting/stats")
def wi_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/WI.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/odi/zim-batting/stats")
def zim_odi_batsmen():
    df1 = pd.read_excel("app/data/odibatters/ZIM.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/odibatsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')



@app.route('/odi/ind-batting/graph')
def indo_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/INDIA.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Indian Batsmen")
    return render_template('graph2.html', chart=chart)


@app.route('/odi/afg-batting/graph')
def afgo_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/AFG.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Afghanistan Batsmen")
    return render_template('graph2.html', chart=chart)
 
@app.route('/odi/aus-batting/graph')
def auso_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/AUS.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Australia Batsmen")
    return render_template('graph2.html', chart=chart)

@app.route('/odi/bdesh-batting/graph')
def bdesho_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/BDESH.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Bangladesh Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/odi/eng-batting/graph')
def engo_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/ENG.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="England Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/odi/ire-batting/graph')
def ireo_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/IRE.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="IRELAND Batsmen")
    return render_template('graph2.html', chart=chart)
 
 
@app.route('/odi/nz-batting/graph')
def nzo_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/NZ.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="New-Zealand Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/odi/pak-batting/graph')
def pako_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/PAK.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Pakistan Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/odi/sa-batting/graph')
def sao_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/SA.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="South Africa Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/odi/sl-batting/graph')
def slo_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/SL.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Sri Lanka Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/odi/wi-batting/graph')
def wio_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/WI.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="West Indies Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/odi/zim-batting/graph')
def zimo_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/odibatters/ZIM.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Zimbawe Batsmen")
    return render_template('graph2.html', chart=chart)
 
@app.route("/T20/indian-batting/stats")
def indian_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/INDIA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route("/test/afg-batting/stats")
def afg_T20_batsmen():
    df1 = pd.read_excel("app/data/testbatters/AFG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/aus-batting/stats")
def aus_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/AUS.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/bdesh-batting/stats")
def bdesh_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/BDESH.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/eng-batting/stats")
def eng_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/ENG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/ire-batting/stats")
def ire_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/IRE.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/nz-batting/stats")
def nz_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/NZ.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/pak-batting/stats")
def pak_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/PAK.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/sa-batting/stats")
def sa_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/SA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/sl-batting/stats")
def sl_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/SL.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/wi-batting/stats")
def wi_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/WI.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route("/T20/zim-batting/stats")
def zim_T20_batsmen():
    df1 = pd.read_excel("app/data/T20batters/ZIM.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/t20batsmen.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')



@app.route('/T20/ind-batting/graph')
def indt_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/INDIA.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Indian Batsmen")
    return render_template('graph2.html', chart=chart)


@app.route('/T20/afg-batting/graph')
def afgt_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/AFG.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Afghanistan Batsmen")
    return render_template('graph2.html', chart=chart)
 
@app.route('/T20/aus-batting/graph')
def aust_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/AUS.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Australia Batsmen")
    return render_template('graph2.html', chart=chart)

@app.route('/T20/bdesh-batting/graph')
def bdesht_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/BDESH.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Bangladesh Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/T20/eng-batting/graph')
def engt_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/ENG.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="England Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/T20/ire-batting/graph')
def iret_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/IRE.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="IRELAND Batsmen")
    return render_template('graph2.html', chart=chart)
 
 
@app.route('/T20/nz-batting/graph')
def nzt_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/NZ.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="New-Zealand Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/T20/pak-batting/graph')
def pakt_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/PAK.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Pakistan Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/T20/sa-batting/graph')
def sat_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/SA.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="South Africa Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/T20/sl-batting/graph')
def slt_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/SL.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Sri Lanka Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/T20/wi-batting/graph')
def wit_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/WI.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="West Indies Batsmen")
    return render_template('graph2.html', chart=chart)
 

@app.route('/T20/zim-batting/graph')
def zimt_graph(chartID = 'chart_ID', chart_type = 'column', chart_height = 800):
    df1 = pd.read_excel("app/data/T20batters/ZIM.xls",sep="\t",index_col=[1])
    df1.dropna(inplace=True)
    chart = serialize(df1, render_to='my-chart', output_type='json',kind="line",title="Zimbawe Batsmen")
    return render_template('graph2.html', chart=chart)

@app.route('/test/zim-bowling/stats')
def zim_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/ZIM.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/afg-bowling/stats')
def afg_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/AFG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/aus-bowling/stats')
def aus_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/AUS.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/bdesh-bowling/stats')
def bdesh_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/BDESH.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/eng-bowling/stats')
def eng_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/ENG.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')


@app.route('/test/indian-bowling/stats')
def india_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/INDIA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/ire-bowling/stats')
def ire_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/IRE.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/nz-bowling/stats')
def nz_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/NZ.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')
                        

@app.route('/test/pak-bowling/stats')
def pak_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/PAK.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/sa-bowling/stats')
def sa_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/SA.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')

@app.route('/test/sl-bowling/stats')
def sl_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/SL.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')
                    

@app.route('/test/wi-bowling/stats')
def wi_Test_bowlers():
    df1 = pd.read_excel("app/data/testbowlers/WI.xls",sep="\t",index_col=[0])
    df1.dropna(inplace=True)
    table1 = df1.to_html(header=False,index=False,border=0)
    with open("app/templates/testbowlers.html","r") as ht1:
        ht11 = ht1.read()
    return(ht11+table1+
            ''' </div>
                    </section>
                        </body>
                            </html>''')