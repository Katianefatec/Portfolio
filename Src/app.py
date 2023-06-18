from flask import app, Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/experiencia')
def experiencia():
    return render_template('experiencia.html')

@app.route('/sobremim')
def sobremim():
    return render_template('sobremim.html') 

if __name__ == '__main__':  
    app.run('0.0.0.0')        
         