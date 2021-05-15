import keys
import tweepy

# La informacion de las llaves no estan disponibles :)
auth = tweepy.OAuthHandler(keys.API_KEY, keys.API_SECRET_KEY)
auth.set_access_token(keys.ACCESS_TOKEN, keys.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def imprimir_home():
    public_tweets = api.home_timeline() ## Esto almacena tweets del home

    for tweet in public_tweets:
        print(f'{tweet.user.screen_name}: \n{tweet.text}\n{"*"*60}')

def buscar_tweets():
    id = None
    # id = None y al final del ciclo asignarle el id del último ciclo para que en cada ciclo 
    # se consulten solo los tweets más antiguos que los ya consultados en el último ciclo.
    count = 0
    while count <= 500:
        # El tweet mode extended permite que se obtengan los tweets con 280 caracteres
        tweets = api.search(q='ParoNacional14M',lang='es',tweet_mode = 'extended', max_id = id)
        for tweet in tweets:
            # Si el tweet inicia con RT solo lo cuenta, 
            # No lo guarda, continua con el ciclo
            if tweet.full_text.startswith('RT'):
                count += 1
                continue
            with open('./paro14m.txt', 'a', encoding='utf-8') as f:
                f.write(tweet.full_text + '\n')
                f.close
                count += 1
        id = tweet.id
        print(count)


if __name__ == '__main__':
    buscar_tweets()