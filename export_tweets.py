import keys
import tweepy
import json

# La informacion de las llaves no estan disponibles :)
auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)

# Si alcanza el limite de request del API, el app espera a que pueda
# volver a hacer requests.
api = tweepy.API(auth, wait_on_rate_limit=True,
wait_on_rate_limit_notify=True)

def imprimir_home():
    public_tweets = api.home_timeline() ## Esto almacena tweets del home

    for tweet in public_tweets:
        print(f'{tweet.user.screen_name}: \n{tweet.text}\n{"*"*60}')

# Se obtiene información de mi usuario
def inf_user():
    data = api.me()
    inf = json.dumps(data._json,indent=2)
    print(json.dumps(data._json,indent=2))
    return inf

def inf_otro_usuario(screen_name):
    '''
    El screen_name es el nombre de la cuenta con la
    que se realiza menciones, en conjunto con el @
    @frluenga = frluenga
    screen_name = frluenga
    '''
    data = api.get_user(screen_name)
    inf = json.dumps(data._json,indent=2)
    print(json.dumps(data._json,indent=2))

def inf_followers(screenName):
    '''
    Retorna de a 20 resultados, es decir entrega de a 
    20 usuarios, para que ampliemos esto se puede hacer 
    con un ciclo for tweepy.Cursor(api.followers,screen_name).items(100)
    '''
    data = api.followers(screen_name = screenName)
    for user in data:
        print(json.dumps(data._json,indent=2))

def timeline(sname):
    '''
        Retorna un objeto tweet, en este caso el ultimo tweet hecho
        por una cuenta especifica.
    '''
    for tweet in tweepy.Cursor(api.user_timeline,screen_name=sname,tweet_mode = 'extended').items(1):
        print(json.dumps(tweet._json,indent=2))

def buscar_tweets(text,n):
    id = None
    count = 0
    while count < n:
        tweets = tweepy.Cursor(api.search,q=text,lang='es',tweet_mode = 'extended',max_id = id).items(10)
        for tweet in tweets:
            print(tweet._json['full_text'])
            print('-'*60)
        count += 1

def guardar_tweets():
    id = None
    # id = None y al final del ciclo asignarle el id del último ciclo para que en cada ciclo 
    # se consulten solo los tweets más antiguos que los ya consultados en el último ciclo.
    count = 0
    while count <= 500:
        # El tweet mode extended permite que se obtengan los tweets con 280 caracteres
        tweets = api.search(q='@Davivienda',lang='es',tweet_mode = 'extended', max_id = id)
        for tweet in tweets:
            # Si el tweet inicia con RT solo lo cuenta, 
            # No lo guarda, continua con el ciclo
            if tweet.full_text.startswith('RT'):
                count += 1
                continue
            with open('./dav.txt', 'a', encoding='utf-8') as f:
                f.write(tweet.full_text + '\n')
                f.close
                count += 1
        id = tweet.id
        print(count)


if __name__ == '__main__':
    buscar_tweets('Davivienda',2)