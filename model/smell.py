import os
import openai
from . import db


class RequirementSmell(db.Model):
    __tablename__ = "smells"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(80))
    detalhe = db.Column(db.String(256))

    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def get_smell(self, text, model, get_smells):
        textvar=text
        prompt_text ='''Histórias de usuários são requisitos que demonstram como um software deve se comportar, os quais são seguidos pelos desenvolvedores de software no momento da construção, 
        por exemplo: Dado que sou um usuário do site de rede social, desejo poder postar mídias. 
        Nesse caso, o dono do produto escreveu uma funcionalidade sobre o sistema de rede social que o usuário deve ter, nesse caso, o usuário pode postar uma mídia no sistema. 
        Um problema que pode ocorrer nas histórias de usuário é a escrita feita de forma que cause má interpretação pelo desenvolvedor do sistema, o qual por sua vez pode acabar criando a funcionalidade de forma errada. 
        A partir de agora, irei chamar esses problemas de "requiriments smells". 
        Considere essa seguinte lista de requiriments smells:  
        {}
        Repare que existem 8 requiriments smells, para cada um, separado por vírgulas, existe "id" "nome" e "detalhe". 
        É importante ressaltar que essa lista nunca deve ser repetida, apenas deve-se retornar o Requiriment Smell encontrado, no caso o "id" "nome" e o motivo dele estar presente. 
        Caso encontre mais que um, separe-os com um ponto. 
        O id 8 é utilizando quando nenhum dos 7 primeiros é encontrado, então, caso não encontre nenhum requiriment smell, retorne: "8, Nenhum requiriment smell encontrado". 
        Para facilitar, considere este exemplo "Dado que sou um usuário do site de rede social, desejo poder postar mídias". 
        Neste caso, percebe-se um Requiriment Smell, o id 2.
        Nesse exemplo, você deveria retornar exatamente a seguinte resposta: 
        2. Incomplete References. A parte "desejo poder postar mídias" está incompleta, pois não está especificado qual tipo de mídia, podendo ser vídeos, audios ou imagens.
        Então como mostrado no exemplo, ao enviar uma história de usuário, a mesma deve ser lida e comparada com a lista para verificar se algum dos requiriments smells é identificado. 
        Agora que você sabe como fazer, verifique a seguinte História de Usuário: {}
        resposta:'''.format(get_smells, textvar)
        
        response = openai.Completion.create(
            model=model,
            temperature=0.08,
            top_p=0.3,
            max_tokens= 256,
            prompt=prompt_text)
        print('PROMPT: ')
        print(prompt_text)
        print('USER STORIE: ')
        print(text)
        print('RESPONSE GPT: ')
        print(response)
        return response

    def __repr__(self) -> str:
        return "id: " + self.id + " nome: " + self.nome + " detalhe: " + self.detalhe
