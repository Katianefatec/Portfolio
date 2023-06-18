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
    return render_template('sobremim.html', experiencias=experiencias) 

experiencias = [
    {
        'imagem': '../static/img/fisio.jpg',
        'cargo': 'Formada em fisioterapia pela FCT - UNESP (2001-2004)'
    },
    {
        'imagem': '../static/img/faculeste.jpeg',
        'cargo': 'Pós-graduada em Intervenção psicológica na mediação e resolução de conflitos (2022-2023)'
    },
    {
        'imagem': '../static/img/fatec.jpeg',
        'cargo': 'Cursando Desenvolvimento de Software Multiplataforma'
    },
    {
        'imagem': '../static/img/nossacaixa.png',
        'cargo': 'Auxiliar administrativo do Banco Nossa Caixa (2006-2007)'
    },
    {
        'imagem': '../static/img/tjsp.jpg',
        'cargo': 'Escrevente técnica do Tribunal de Justiça do Estado de São Paulo (2007-2009)'
    },
    {
        'imagem': '../static/img/jfsp.jpg',
        'cargo': 'Técnica judiciária da Justiça Federal de São Paulo (2009 até o momento)'
    }
]


if __name__ == '__main__':  
    app.run('0.0.0.0')        
         