import os
from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_mail import Mail, Message
from datetime import datetime

app = Flask(__name__)

# Configuração do Flask-Mail
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.environ.get("EMAIL_USER", "seu_email@gmail.com")
app.config["MAIL_PASSWORD"] = os.environ.get("EMAIL_PASSWORD", "sua_senha_app")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("EMAIL_USER", "seu_email@gmail.com")
mail = Mail(app)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/enviar-mensagem", methods=["POST"])
def enviar_mensagem():
    if request.method == "POST":
        try:
            nome = request.form["nome"]
            email = request.form["email"]
            assunto = request.form["assunto"]
            mensagem = request.form["mensagem"]

            # Criar a mensagem
            msg = Message(
                subject=f"Contato do Portfolio: {assunto}",
                recipients=["katy_ane@yahoo.com.br"],  # Email onde você receberá as mensagens
                body=f"Nome: {nome}\nEmail: {email}\n\nMensagem:\n{mensagem}",
                reply_to=email  # Para poder responder diretamente ao remetente
            )

            # Enviar o email
            mail.send(msg)

            return jsonify({"status": "success", "message": "Mensagem enviada com sucesso!"})
        except Exception as e:
            print(f"Erro ao enviar email: {str(e)}")
            return jsonify({"status": "error", "message": f"Ocorreu um erro ao enviar a mensagem: {str(e)}"})

# Definindo as datas de nascimento
data_nascimento_usuario = datetime(1981, 12, 3)
data_nascimento_filha = datetime(2018, 5, 31)


@app.route("/")
def home():
    idade_usuario = (
        datetime.now().year
        - data_nascimento_usuario.year
        - (
            (datetime.now().month, datetime.now().day)
            < (data_nascimento_usuario.month, data_nascimento_usuario.day)
        )
    )
    idade_filha = (
        datetime.now().year
        - data_nascimento_filha.year
        - (
            (datetime.now().month, datetime.now().day)
            < (data_nascimento_filha.month, data_nascimento_filha.day)
        )
    )
    return render_template(
        "index.html", idade_usuario=idade_usuario, idade_filha=idade_filha
    )


@app.route("/experiencia")
def experiencia():
    experiencias = [
        {
            "imagem": "../static/img/fatec.jpeg",
            "alt": "cargo5",
            "titulo": "Cursando Desenvolvimento de Software Multiplataforma na FATEC São José dos Campos (2023-2025)",
        },
        {
            "imagem": "../static/img/faculeste.jpeg",
            "alt": "cargo2",
            "titulo": "Pós-graduada em Intervenção psicológica na mediação e resolução de conflitos (2022-2023)",
        },
        {
            "imagem": "../static/img/fisio.jpg",
            "alt": "formacao",
            "titulo": "Formada em fisioterapia pela FCT - UNESP (2001-2004)",
        },
    ]

    experiencias2 = [
        {
            "imagem": "../static/img/jfsp.jpg",
            "alt": "cargo4",
            "titulo": "Técnica judiciária da Justiça Federal de São Paulo (2009 até o momento)",
        },
        {
            "imagem": "../static/img/tjsp.jpg",
            "alt": "cargo1",
            "titulo": "Escrevente técnica do Tribunal de Justiça do Estado de São Paulo (2007-2009)",
        },
        {
            "imagem": "../static/img/nossacaixa.png",
            "alt": "cargo3",
            "titulo": "Auxiliar administrativo do Banco Nossa Caixa (2006-2007)",
        },
    ]
    return render_template(
        "experiencia.html", experiencias=experiencias, experiencias2=experiencias2
    )



@app.route("/projetos")
def projetos():
    return render_template("projetos.html")


if __name__ == "__main__":
    app.run("0.0.0.0", debug=True)
