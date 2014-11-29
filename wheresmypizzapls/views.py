from flask import render_template, request

from wheresmypizzapls import app

@app.route('/')
def view_index():
    return render_template('page-creator.html')

@app.route('/template')
def view_template():
    title = request.args.get('title')
    description = request.args.get('description')
    return render_template('template.html', title=title, description=description)
