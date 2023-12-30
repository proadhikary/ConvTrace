import pandas as pd
from flask import Flask, render_template, request, redirect, make_response, flash


app = Flask(__name__)

columns = ['Utterance', 'Type', 'Sub Topic' ]
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
            chat_df = chat_df.iloc[:-2] 
        
    return render_template('index.html', chat_data=chat_df.to_dict(orient='records'))

@app.route('/save_summary', methods=['POST'])
def save_summary():
    if request.method == 'POST':
        summary_rt = request.form.get('summary_rt')
        summary_sh = request.form.get('summary_sh')
        summary_pd = request.form.get('summary_pd')

        global chat_df
        new_rows = [
            
            {'Utterance': 'summary_sh', 'Sub topic': summary_sh},
            {'Utterance': 'summary_pd', 'Sub topic': summary_pd},
            {'Utterance': 'summary_rt', 'Sub topic': summary_rt},
        ]

        chat_df = chat_df.append(new_rows, ignore_index=True)
        resp = make_response(chat_df.to_csv(index=False))
        resp.headers["Content-Disposition"] = "attachment; filename=download.csv"
        resp.headers["Content-Type"] = "text/csv"
        chat_df = chat_df[0:0]
    return  resp

if __name__ == '__main__':
    app.run("0.0.0.0",8520,debug=True)

