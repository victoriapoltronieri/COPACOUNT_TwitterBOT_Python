import os
import tweepy
import time
import random
import dotenv
import datetime
from datetime import datetime
from datetime import date

# --------------------------------------------------------------
# ADICIONANDO DOTENV
# --------------------------------------------------------------
dotenv.load_dotenv(dotenv.find_dotenv())

# --------------------------------------------------------------
# LEITURA DAS CHAVES DE ACESSO DOTENV

api_key = os.getenv("api_key")
api_key_secret = os.getenv("api_key_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")
bearer_token = os.getenv('bearer_token')

# --------------------------------------------------------------
# CRIAÇÃO DA API

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True) 

# --------------------------------------------------------------
# DEFINIÇÃO DAS FUNÇÕES DOS TIPOS DE TWEETS

def random_tweet():
    tweets = ["Já comprou a camisa pra assistir os jogos do BR combinando com o mozão?", 
            "2022\n2 0 2 2\n2 + 0 + 2 + 2 = 6\nHexa confirmado!", 
            "Ainda dá tempo de marcar o churrasco na casa da sogra pra assistir a seleção.",
            "#Hexa2022",
            "A skin de Maria Chuteira já tá atualizada.",
            "Vamo assistir Casimiro reagindo aos jogos da copa juntos?",
            "Sou Neymarzete desde criancinha.",
            "*Vendo que os jogos da seleção são em dia de semana*\n\n*Eu pro meu patrão*: Não posso ir trabalhar pois gripá-lo-ei",
            "Dia dos jogos do Brasil:\n- 24/11\n- 28/11\n- 02/12",
            "waka waka ê ê"
            "alexa toca waka_waka-shakira-2010.mp3",
            "Bola na trave não altera o placar, bola na área sem ninguém pra cabecear",
            "Ainda dá tempo de juntar os vizinhos e pintar a rua",
            "Tô sonhando com ela          a Copa do Mundo",
            "Eu: acho que já vou dormir boa noite bjs\nEu também: *buzzfeed ponto com* descubra qual cabelo do neymar você é",
            "Já combinou o bolão com os amigos?",
            "Minha linguagem de amor é presentes, pra me consquistar é só comprar o album da Copa com vários pacotes de figurinha",
            "Agora a inflação foi longe demais... 4 conto o pacote de figurinha é um absurdo. Quem vai aparecer no protesto?",
            "Thomas Muller mandou dizer oi",
            "Última Copa do CR7 e do Messi. Nada mais justo do que a final ser Brasil e Tunísia pra eles aproveitarem bastante a cerimônia de encerramento."]
    
    random_tweet = random.choice(tweets)
    return random_tweet

def calcula_dias_restantes():
    start = date(2022, 11, 20)
    current = date.today()
    #print((start-current).days, "days")
    return (start-current).days

def mais_de_um_dia(dias):
    t = "Faltam " + str(dias) + " dias para a Copa do Mundo FIFA 2022 no Qatar.\n\n"
    return t

def um_dia(dias):
    t = "Falta 1 dia para a Copa do Mundo FIFA 2022 no Qatar!\n\n"
    return t

def dia_zero(dias):
    t = "Alô, amigos da Rede Globo! Copa do Mundo FIFA 2022 começa HOJE"
    return t


def _main_():
    if((datetime.now().time().hour==11)and(datetime.now().time().minute==35)):
       # api.update_status("Entrou aqui povo")
        dias = calcula_dias_restantes()
        frase_extra = random_tweet()

        if(dias > 1):
            tweet = mais_de_um_dia(dias) + frase_extra
            api.update_status(tweet)

        elif(dias == 1):
            tweet = um_dia(dias) + frase_extra
            api.update_status(tweet)
        
        elif(dias == 0):
            tweet = dia_zero(dias)
            api.update_status(tweet)
        
        else:
            tweet = "A Copa do Mundo FIFA 2022 já tá rolando!"

if __name__ == "__main__":
    while True:
        if((datetime.now().time().hour==10) or (datetime.now().time().hour==11)):
            _main_()
            time.sleep(60)

        elif((datetime.now().time().hour==12)):
            time.sleep(79200)
        else:
            time.sleep(3600)
