from flask import app, Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/experiencia')
def experiencia():
    experiencias = [
        {"imagem": "../static/img/fisio.jpg", "alt": "formacao", "titulo": "Formada em fisioterapia pela FCT - UNESP (2001-2004)"},
        {"imagem": "../static/img/faculeste.jpeg", "alt": "cargo2", "titulo": "Pós-graduada em Intervenção psicológica na mediação e resolução de conflitos (2022-2023)"},
        {"imagem": "../static/img/fatec.jpeg", "alt": "cargo5", "titulo": "Cursando Desenvolvimento de Software Multiplataforma"}
    ]
    
    experiencias2 = [
        {"imagem": "../static/img/nossacaixa.png", "alt": "cargo3", "titulo": "Auxiliar administrativo do Banco Nossa Caixa (2006-2007)"},
        {"imagem": "../static/img/tjsp.jpg", "alt": "cargo1", "titulo": "Escrevente técnica do Tribunal de Justiça do Estado de São Paulo (2007-2009)"},
        {"imagem": "../static/img/jfsp.jpg", "alt": "cargo4", "titulo": "Técnica judiciária da Justiça Federal de São Paulo (2009 até o momento)"}
    ]
    return render_template('experiencia.html', experiencias=experiencias, experiencias2=experiencias2)

@app.route('/sobremim')
def sobremim():
    return render_template('sobremim.html') 

if __name__ == '__main__':  
    app.run('0.0.0.0')        
         