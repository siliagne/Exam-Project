
#This is part 3 

from flask import Flask
from flask import render_template
from flask import request
#user = request.form['user']
from progettopart1 import Registry

app = Flask(__name__)

@app.route('/')
def IndexPage():
	reg = Registry().registry()
	link = Registry().links()
	return render_template('1homepage.html', registry = reg, links = link, length = 9)
 
@app.route('/Meta') #metadata info
def FirstPage():
	output = Registry.metadata
	return render_template('2metadata.html', result = output)

@app.route('/Sem') #semantics info
def SecondPage():
	output = Registry().semantics()
	return render_template('3semantics.html', result = output)

@app.route('/Genes') #genes info
def ThirdPage():
	output = Registry().genes()
	return render_template('4genes.html', result = output)
 
@app.route('/SG') #sentenceg info
def FourthPage():
	output = Registry().sentenceg()
	return render_template('5genesentences.html', result = output)
 
@app.route('/Diseases') #diseases info
def FifthPage():
	output = Registry().diseases()
	return render_template('6disease.html', result = output)
 
@app.route('/SD') #sentenced info
def SixthPage():
	output = Registry().sentenced()
	return render_template('7diseasesentences.html', result = output)
 
@app.route('/Top') #top10 info
def SeventhPage():
	output = Registry().top10()
	return render_template('8top10.html', result = output)
 
@app.route('/GetoDis') #gene to disease info
def EighthPage():
	output = Registry().genetod()
	return render_template('9genetodisease.html', result = output)
 
@app.route('/DistoGe') #disease to gene info
def NinthPage():
	output = Registry().diseasetog()
	return render_template('10diseasetogene.html', result = output)
if __name__ == '__main__':
    app.run()
