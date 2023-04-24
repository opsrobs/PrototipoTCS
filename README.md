# PrototipoTCS

#Primeiros passos:
#Criar a virtual env

python -m venv venv

#Entrar na maquina virtual

venv/Scripts/activate

(caso tenha problemas de permissão ao executar esse comando leia: https://pt.stackoverflow.com/questions/220078/o-que-significa-o-erro-execu%C3%A7%C3%A3o-de-scripts-foi-desabilitada-neste-sistema)

#instalar as bibliotecas necessarias
pip install -r requirements.txt

#criar um arquivo chamado .env em que voce vai colocar o seguinte código:
(gerar a chave API: https://openai.com/blog/openai-api)
OPENAI_API_KEY= #Sua chave da API

#Após isso, pode executar no terminal
flask run 
(caso não tenha flask instalado execute este comando primeiro: pip install Flask)

#com isso, deve iniciar normalmente.
(em caso de erro tente instalar openai com o comando:  pip install openai)
