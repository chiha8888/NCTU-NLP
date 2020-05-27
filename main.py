from flask import Flask
from flask import render_template
from flask import request
import pandas as pd

app=Flask(__name__)
app.config['DEBUG']=True

@app.route('/question',methods=['GET'])
def send_question():
    try:
        id=int(request.args.get('id'))
        if id>=0 and id<=376:
            print(f'request tweet id {id}')
            return render_template('index.html', tweet=tweets[id])
        else:
            print(f'id {id} is not between [0,376]')
    except:
        print('sending question fails.')

if __name__=='__main__':
    tweets=pd.read_csv('https://gist.githubusercontent.com/bshmueli/c99fc0abf56460e644bd610bf3024e83/raw/720285d133c85d94e0aa3fe3edcc199f6d99e3f7/lab4-data.csv')
    tweets=tweets['text']
    app.run(host='0.0.0.0',port=3000)

