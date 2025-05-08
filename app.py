from flask import Flask,render_template

app=Flask(__name__)

#routes
@app.route('/')
def index():
    return('index.html')
@app.route('/spell',methods=['POST','GET'])
def spell():
    pass
@app.route('/grammar',methods=['POST','GET'])

def grammar():
    pass

#main
if __name__ == "__main__":
    app.run(debug=True)