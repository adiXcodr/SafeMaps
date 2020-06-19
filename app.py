from flask import Flask, request, jsonify, render_template, flash, redirect, url_for
from app_functions import *
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route('/')
def home():
    return render_template('index.html')



@app.route('/connectMap',methods=['POST'])

def connectMap():
    G,adj=createGraph()
    displayGraph(G)
    s = str(request.form.get('source'))
    d = str(request.form.get('destination'))
    if(s==d):
        output='You are in the destination'
    else:
        safest_path_text,criteria=startProg(G,adj,s,d)
        output=str(safest_path_text)+' and Criteria='+criteria
    return render_template('index.html', safest_path='{}'.format(output))
    

if __name__ == "__main__":
    app.run(debug=True)