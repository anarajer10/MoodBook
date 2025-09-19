#Funciones específicas sobre las emociones detectadas
from textblob import TextBlob
from deep_translator import GoogleTranslator
from langdetect import detect

def franjas(t):  #t --> texto 
    """
    Recibe un texto en español/inglés, lo traduce si hace falta y analiza el tipo de sentimiento
    """
    try:
        detected_lang = detect(t)
        if (detected_lang == 'es' ):
            traduccion = GoogleTranslator(source='es', target='en').translate(t) #Se traduce
            blob = TextBlob(traduccion)
        elif detected_lang == "en":
            blob = TextBlob(t)
        else:
            return "Idioma no compatible, por favor introducir en español o inglés"

        polarity = blob.sentiment.polarity
        
        if (polarity > -1 and polarity < -0.66):
            return "muy malo" #aquí va la lista de libros correspondiente
        
        elif (polarity > -0.65 and polarity < -0.25):
            return "malo" #aquí va la lista de libros correspondiente
        
        elif (polarity > -0.24 and polarity < 0.25):
            return "neutral" #aquí va la lista de libros correspondiente
        
        elif (polarity > 0.26 and polarity < 0.66):
            return "bueno" #aquí va la lista de libros correspondiente
        
        elif (polarity > 0.67 and polarity < 1):
            return "muy bueno" #aquí va la lista de libros correspondiente
        
        else:
            return "nada"
        
    except Exception as e:
        print("Error en análisis: ", e)
    #-1/-0.66 muy malo
    #-0.65/-0.25 malo
    #-0.24/0.25 neutral
    #0.26/0.66 bueno
    #0.67/1 muy bueno
