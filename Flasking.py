from flask import Flask, render_template
import Flask_Model as Model

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <img src="/static/blockM.png"/>
        <h1>McCoy's SI 206 Final Project</h1>
        <ul>
            <li><a href="/Vis-1"> Visualization I: Famous Criminals - Data Table </a></li>
            <li><a href="/Vis-2"> Visualization II: FBI - Michigan Crime Pie Charts </a></li>
            <li><a href="/Vis-3"> Visualization III: DPSS Dorm Incidents </a></li>
            <li><a href="/Vis-4"> Visualization IV: DPSS Incidents by Type </a></li>
        </ul>
    '''

# This could be done in less lineswith GET/POST division
# would be harder for me to navigate and I'm just not
# comfortable enough working with GET/POST division yet.
@app.route('/Vis-1/')
def V1_Menu():
	return(render_template("Vis-1-Menu.html"))

@app.route('/Vis-1/Name')
def V1_Name():
	crims = Model.get_criminals(sort_by="Name")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/Nationality')
def V1_Nationality():
	crims = Model.get_criminals(sort_by="Nationality")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/Title')
def V1_Title():
	crims = Model.get_criminals(sort_by="Title")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/Astro')
def V1_Astro():
	crims = Model.get_criminals(sort_by="Astro", order="asc")
	return(render_template("fame_crims.html",fame_ppl=crims))

@app.route('/Vis-1/BirthYear')
def V1_BirthYear():
	crims = Model.get_criminals(sort_by="BirthYear", order="desc")
	return(render_template("fame_crims.html",fame_ppl=crims))

######################################################################

@app.route('/Vis-2/')
def V2_Menu():
	return(render_template("Vis-2-Menu.html"))

@app.route('/Vis-2/yr=2012')
def V2_2012():
	print("V2 triggered (year=2012)")
	pie = Model.gen_FBI_graph(year_in="2012")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2012"))

@app.route('/Vis-2/yr=2013')
def V2_2013():
	print("V2 triggered (year=2013)")
	pie = Model.gen_FBI_graph(year_in="2013")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2013"))

@app.route('/Vis-2/yr=2014')
def V2_2014():
	print("V2 triggered (year=2014)")
	pie = Model.gen_FBI_graph(year_in="2014")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2014"))

@app.route('/Vis-2/yr=2015')
def V2_2015():
	print("V2 triggered (year=2015)")
	pie = Model.gen_FBI_graph(year_in="2015")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2015"))

@app.route('/Vis-2/yr=2016')
def V2_2016():
	print("V2 triggered (year=2016)")
	pie = Model.gen_FBI_graph(year_in="2016")
	return(render_template("FBI_Crime_Pies.html", pie_in=pie, yy="2016"))

######################################################################

@app.route('/Vis-3')
def V3_Menu():
	return(render_template("Vis-3-Menu.html"))

@app.route('/Vis-3/ByDorm')
def V3_ByDorm():
	incident_data = Model.gen_DPSS_dorm_table(sort_by="Name")
	return(render_template("DPSS-by-Dorm.html",
		dorm_incidents=incident_data))

@app.route('/Vis-3/ByFreq')
def V3_ByFreq():
	incident_data = Model.gen_DPSS_dorm_table(sort_by="Freq")
	return(render_template("DPSS-by-Dorm.html",
		dorm_incidents=incident_data))

######################################################################

@app.route('/Vis-4')
def V4():
	return(render_template("Vis-4-Menu.html"))

@app.route('/Vis-4/ByType_raw')
def V4_ByType_raw():
	freq_data = Model.gen_DPSS_type_table_unrefined(sort_by="Descrip")
	return(render_template("DPSS-by-Type.html", incident_freqs=freq_data))
	#campus_incidents = 5678

@app.route('/Vis-4/ByFreq_raw')
def V4_ByFreq_raw():
	freq_data = Model.gen_DPSS_type_table_unrefined(sort_by="Freq")
	return(render_template("DPSS-by-Type.html", incident_freqs=freq_data))

@app.route('/Vis-4/ByType_refined')
def V4_ByType_refined():
	freq_data = Model.gen_DPSS_type_table_refined(sort_by="Descrip")
	return(render_template("DPSS-by-Type.html", incident_freqs=freq_data))
	#campus_incidents = 5678

@app.route('/Vis-4/ByFreq_refined')
def V4_ByFreq_refined():
	freq_data = Model.gen_DPSS_type_table_refined(sort_by="Freq")
	return(render_template("DPSS-by-Type.html", incident_freqs=freq_data))


######################################################################

def run_it():
	app.run()