import pandas as pd
import numpy as np

import tensorflow
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model

# dados de treinamento
train_data = pd.read_csv("./static/data_files/tweet_emotions.csv")    
training_sentences = []

for i in range(len(train_data)):
    sentence = train_data.loc[i, "content"]
    training_sentences.append(sentence)

#carregue o modelo
model = load_model("./static/model_files/Tweet_Emotion.h5")

vocab_size = 40000
max_length = 100
trunc_type = "post"
padding_type = "post"
oov_tok = "<OOV>"

tokenizer = Tokenizer(num_words=vocab_size, oov_token=oov_tok)
tokenizer.fit_on_texts(training_sentences)

#atribuir emoticons para emoções diferentes
emo_code_url = {
    "vazio": [0, "./static/emoticons/Empty.png"],
    "tristeza": [1,"./static/emoticons/Sadness.png" ],
    "entusiasmo": [2, "./static/emoticons/Enthusiasm.png"],
    "neutro": [3, "./static/emoticons/Neutral.png"],
    "preocupação": [4, "./static/emoticons/Worry.png"],
    "surpresa": [5, "./static/emoticons/Surprise.png"],
    "amor": [6, "./static/emoticons/Love.png"],
    "diversão": [7, "./static/emoticons/fun.png"],
    "ódio": [8, "./static/emoticons/hate.png"],
    "felicidade": [9, "./static/emoticons/happiness.png"],
    "tédio": [10, "./static/emoticons/boredom.png"],
    "alívio": [11, "./static/emoticons/relief.png"],
    "raiva": [12, "./static/emoticons/anger.png"]
    
    }
# escreva a função para prever a emoção
def predict(text):
    #variáveis para armazenar emoção e emoji
    predicted_emotion=""
    predicted_emotion_img_url=""
    
    #Teste para verificar conteúdo digitado e fazer previsão
    if  text!="":
        sentence = []
        sentence.append(text)
        #tokenizar
      
        #preencher
        
        #transformar em array
      
        #use argmax
                
        
        #print(predicted_class_label)   
        for key, value in emo_code_url.items():
            #condicional para mostrar etiqueta e emoção

        return #mostre
        
