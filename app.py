import streamlit as st 
import pickle 
from sklearn.feature_extraction.text import TfidfVectorizer 
import spacy 
from spacy.lang.en import STOP_WORDS
import re 
from textblob import TextBlob

nlp = spacy.load('en_core_web_lg')
set_of_stop_words = set(STOP_WORDS)

new_set_stop_words = set_of_stop_words - set(['not', 'no', 'never', 'very', 'extremely', 'barely','of','why','what','is','in','it','was','have','had'])

# Importing sentiment analysis model 
with open('Models/sentiment_analysis','rb') as f:
    model = pickle.load(f) 


# 1. Removing Punctuations
def Punctuation_remover(text2):
    Punct_pattern = re.compile(r'[^\w\s]')
    return Punct_pattern.sub('',text2) 


# 2. Lemmatization 
def lemmatize(text5):
    doc = nlp(text5)
    
    new = []
    
    for tokken in doc:
      new.append(tokken.lemma_)
    
    new_text = ' '.join(new)
    return new_text


# 3. Stop Words 
def stop_word(text6):
    new1 = [word for word in text6.split() if word.lower() not in new_set_stop_words]
    return ' '.join(new1)

# 4. Spelling Correction 
def spelling_correction(text7):
    textblb = TextBlob(text7)
    return textblb.correct().string

# defining a preprocessor function
def text_preprocessor(text_input):
    t1 = stop_word(text_input)
    t2 = Punctuation_remover(t1)
    t3 = lemmatize(t2)
    t4 = spelling_correction(t3)
    return t4

# transformer
with open('Models/vectorizer','rb') as f:
     vectorizer = pickle.load(f)

def main():
    st.title('SENTIMENT ANALYZER') 
    text = st.text_input('ENTER REVIEW OF CUSTOMER: ')
    
    text_preprocessed = text_preprocessor(text)
        
    text_transformed = vectorizer.transform([text_preprocessed])  # Use transform() if the vectorizer is already fitted
            
    if st.button('Analyze'):
        result = model.predict(text_transformed)
        if result==1:
            st.success('Positive Review')
        else:
            st.error('Negative Review')
        
        






 


if __name__ == '__main__':
    main()





