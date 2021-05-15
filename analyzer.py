exclude_words = ['el', 'la', 'los', 'las', 'un',
                'una', 'unos', 'unas', 'al', 'del', 
                'lo', 'le', 'y', 'e', 'o', 'u', 'de',
                'a', 'en', 'que', 'es', 'por', 'para',
                'con', 'se', 'su', 'les', 'me', 'q',
                'te', 'pero', 'mi', 'ya', 'cuando',
                'como', 'estoy', 'voy', 'porque', 'he',
                'son', 'solo', 'tengo', 'muy']


top_words = {}
tweets_topic = open('./paro14m.txt',encoding='utf-8')
for line in tweets_topic:
    # Eliminamos espacios
    # Convertimos a minusculas
    # separamos caracteres.
    words = line.strip().lower().split()

    for word in words:
        if word not in exclude_words:
            # La función get obtiene el valor de la llave
            # que se le pase como primer parametro, si no
            # existe retorna el segundo parametro, si existe
            # retorna el valor actual
            top_words[word] = top_words.get(word,0) + 1
# Se ordena pasando como primer parametro el dict. luego 
# se le pasa el segundo parametro la llave con la que se ordena,
# es decir los valores del dict.
most_used_words = sorted(top_words, key=top_words.get, reverse=True)

# Encontrar los usuarios que son mas nombrados
count_u = 0
for word in most_used_words:
    if count_u < 10 and word.startswith('@'):
        print(top_words[word], word)
        count_u += 1
 
print('*'*40)

# Tambien se puede hacer por palabras
count = 0
for word in most_used_words:
    if count < 20:
        print(top_words[word], word)
        count += 1