#Funciones específicas sobre las emociones detectadas
from textblob import TextBlob


def franjas(t): #Hace falta que se cambie para que lo ponga el usuario
    t = TextBlob("").translate(from_lang='es', to='en')
    polarity = t.sentiment.polarity
    
    if (polarity > -1 and polarity < -0.66):
        return "muy malo" #aquí va la lista de libros correspondiente
    
    elif (polarity > -0.65 and polarity < -0.25):
        return "malo" #aquí va la lista de libros correspondiente
    
    elif (polarity > -0.24 and polarity < 0.25):
        return "neutral" #aquí va la lista de libros correspondiente
    
    elif (polarity > 0.26 and polarity < 0.66):
        return "bueno" #aquí va la lista de libros correspondiente
    
    elif (polarity > 0.67 and polarity < 1):
        return "muy_bueno" #aquí va la lista de libros correspondiente
    
    else:
        return "nada"

#-1/-0.66 muy malo
#-0.65/-0.25 malo
#-0.24/0.25 neutral
#0.26/0.66 bueno
#0.67/1 muy bueno