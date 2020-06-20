import polyglot 
from polyglot.text import Text ,Word
from polyglot.detect import Detector
import spacy
import logging
import warnings
warnings.filterwarnings("ignore")
import os
import logging
def login_function(message,file_name):
    logger=logging.getLogger()
    file_hander=logging.FileHandler(filename=file_name,mode='a')
    formatter =logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_hander.setFormatter(formatter)
    logger.addHandler(file_hander)
    logger.setLevel(logging.DEBUG)
    logger.debug(message)
def keyword_lemmatization(input_keyword):
    nlp = spacy.load("en_core_web_sm")
    doc=nlp(input_keyword)
    for token in doc:
        lema=token.lemma_
        pos=token.pos_
        message="token is :"+str(token)+", lema is :"+str(lema)+", pos is :"+str(pos)
        login_function(message,"lema.log")
    return lema
def language_detection(input_keyword):
    language_list=["English"]
    
    #text=Text(input_keyword)
    input_keyword=input_keyword.lower()
    detector=Detector(input_keyword,quiet=True)
    detected_lang=detector.language.name
    confidence=detector.language.confidence
    keyword=keyword_lemmatization(input_keyword)
    
    try:
        if detected_lang in language_list:
                keyword=keyword_lemmatization(input_keyword)
                print("Root of Input keyword is {}".format(keyword))
        elif detected_lang=="un":
             raise Exception("Sorry !! can not detected Language for {} BNG Model Can only work for English Keyword".format(input_keyword))
        elif detected_lang not in language_list:
            raise Exception("Detected Language is {} BNG Model Can only work for English Keyword".format(detected_lang))
    except Exception as e:
        #logging.error(e)
        print(e)
        login_function(e,"warning.log")
    return detected_lang,confidence,keyword

#print(language_detection("おはようございます"))
        