# Portifolio_design_digital

##Trabalho semestral

###Olá, sou a Katiane Soares!

Esse projeto tem a finalidade de criar um portifólio profissional para a disciplina de Design Digital

Contém a pasta Doc com o arquivo wireframe.pdf

Contém a pasta Src com o arquivo app.py e a pasta templates, com os seguintes arquivos:
- base.html
- home.html
- experiencia.html
- sobremim.html

Para executar o projeto, siga as instruções abaixo:

1. Instale o Python em seu computador. Recomendamos a versão 3.8 ou superior.

   - Para instalar o Python no Windows, acesse o [site oficial](https://www.python.org/downloads/windows/) e baixe o instalador adequado à sua versão do Windows.


2. Instale o GIT em seu computador. No site oficial do Git (http://git-scm.com/), clique em “Download for Windows” e selecione a versão adequada para seu sistema (32 ou 64 bits). Depois de baixado, clique duas vezes no arquivo para iniciar o assistente de instalação. Basta seguir as instruções na tela, clicando em Next. Ao término, clique em Finish para concluir com êxito a instalação.


3. Clone este repositório em sua máquina. No diretório desejado, abra o CMD (prompt de comando) do Windows (no explorador de arquivos, basta selecionar o caminho da pasta, digitar "cmd" e pressionar Enter) e digite:

```
git clone https://github.com/Katianefatec/Portifolio.git
```


4. Entre na pasta do repositório:

```
cd \portifolioclone\Src
```

5. Crie e ative um ambiente virtual:

```
python -m venv venv
venv\Scripts\activate
```

6. Instale as dependências do projeto:

```
pip install -r ..\requirements.txt

...
7. Executar a aplicação (na pasta src/)
...
python app.py
...

8. Clique no endereço de IP que será gerado para abrir o site no navegador:

```
Ctrl+Clique para seguir o link

Caso ocorram erros durante a execução do projeto, verifique se os passos acima foram seguidos corretamente e se todas as dependências estão instaladas corretamente.

...

## Instruções para a implantação no Vercel

1. Instalar o node e seu gerenciador de pacotes, ou seja, o npm 
2. Instalar o vercel através do comando: 
    ```console 
    npm install -g vercel 
    ```
3. Considerando que você já criou uma conta no Vercel, e que
 está logado, utilize o comando seguinte no mesmo nível do arquivo vercel.json
    ```console 
    vercel
    ```
4. Defina um nome para a sua aplicação e utilize todas as demais opções de acordo com o padrão sugerido. 
5. Verifique se o link disponibilizado ao final do processo de upload/build está acessível, caso não esteja, execute o comando 
    ```console 
    vercel --prod 
    ```