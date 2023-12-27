from flask import Flask, render_template, request, redirect, send_file
import pandas as pd
import re

app = Flask(__name__)

columns = ['Utterance', 'Type']
chat_df = pd.DataFrame(columns=columns)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        global name
        name = file.filename
        

        if file:
            global chat_df
            chat_df = pd.read_csv(file)
            chat_df = chat_df.iloc[:-3] 
        
    return render_template('index.html', chat_data=chat_df.to_dict(orient='records'))

@app.route('/save_summary', methods=['POST'])
def save_summary():
    if request.method == 'POST':
        summary_type = request.form.get('summary_type')
        summary = request.form.get('summary')
        global name
        global chat_df
        new_row = {'Utterance': summary_type, 'Type': summary}
        chat_df = chat_df.append(new_row, ignore_index=True)
    return redirect('/')

@app.route('/getCSV')
def save_csv():
    global name
    return send_file(
        name,
        mimetype='text/csv',
        download_name=name,
        as_attachment=True
    )

if __name__ == '__main__':
    app.run("0.0.0.0",8080,debug=True)

