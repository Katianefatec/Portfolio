from flask import app, Flask, render_template, request, url_for
from datetime import datetime

app = Flask(__name__)

data_nascimento_usuario = datetime(1981, 12, 3) 
data_nascimento_filha = datetime(2018, 5, 31)

@app.route('/')
def home():
    idade_usuario = datetime.now().year - data_nascimento_usuario.year - ((datetime.now().month, datetime.now().day) < (data_nascimento_usuario.month, data_nascimento_usuario.day))
    idade_filha = datetime.now().year - data_nascimento_filha.year - ((datetime.now().month, datetime.now().day) < (data_nascimento_filha.month, data_nascimento_filha.day))
    return render_template('index.html', idade_usuario=idade_usuario, idade_filha=idade_filha)

@app.route('/experiencia')
def experiencia():
    experiencias = [
        {"imagem": "../static/img/fatec.jpeg", "alt": "cargo5", "titulo": "Cursando Desenvolvimento de Software Multiplataforma"},
        {"imagem": "../static/img/faculeste.jpeg", "alt": "cargo2", "titulo": "Pós-graduada em Intervenção psicológica na mediação e resolução de conflitos (2022-2023)"},
        {"imagem": "../static/img/fisio.jpg", "alt": "formacao", "titulo": "Formada em fisioterapia pela FCT - UNESP (2001-2004)"}
    ]   
   
    experiencias2 = [
        {"imagem": "../static/img/jfsp.jpg", "alt": "cargo4", "titulo": "Técnica judiciária da Justiça Federal de São Paulo (2009 até o momento)"},
        {"imagem": "../static/img/tjsp.jpg", "alt": "cargo1", "titulo": "Escrevente técnica do Tribunal de Justiça do Estado de São Paulo (2007-2009)"},
        {"imagem": "../static/img/nossacaixa.png", "alt": "cargo3", "titulo": "Auxiliar administrativo do Banco Nossa Caixa (2006-2007)"}
        
    ]
    return render_template('experiencia.html', experiencias=experiencias, experiencias2=experiencias2)

@app.route('/sobremim')
def sobremim():    
    idade_usuario = datetime.now().year - data_nascimento_usuario.year - ((datetime.now().month, datetime.now().day) < (data_nascimento_usuario.month, data_nascimento_usuario.day))
    idade_filha = datetime.now().year - data_nascimento_filha.year - ((datetime.now().month, datetime.now().day) < (data_nascimento_filha.month, data_nascimento_filha.day))
    
    return render_template('sobremim.html', idade_usuario=idade_usuario, idade_filha=idade_filha)

@app.route('/projetos')
def projetos():
    return render_template('projetos.html')

if __name__ == '__main__':  
    app.run('0.0.0.0', debug=True)