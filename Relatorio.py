from flask import Flask, render_template, request, redirect, session, flash, url_for, send_from_directory
import os, time

app = Flask(__name__)
app.secret_key = 'jhonatan'

app.config['UPLOAD_PATH'] = os.path.dirname(os.path.abspath(__file__)) + '/uploads'


@app.route('/heatmap')
def index():
    return render_template('HeatmapCrimes.html')

@app.route('/PlotTempo')
def novo():
    return render_template('Plot_timeseries.html')

@app.route('/GroupCrimes')
def a():
    return render_template('GroupCrimes.html')

app.run(debug=True)