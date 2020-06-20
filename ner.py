import spacy
nlp = spacy.load("en_core_web_sm")
def ner_detection(text):
    sentence=text.lower()
    doc = nlp(sentence)
    try:
        for ent in doc.ents:
            ner=ent.label_
            if ner=="GPE":
                ner="Countries, cities, states"
            if ner=="ORG":
                ner="Companies, agencies, institutions,cities,states"
            if ner=="PERSON":
                ner="PERSON"
            if ner=="NORP":
                ner="Nationalities or religious or political groups"
            if ner=="MONEY":
                ner="Monetary values, including unit"
            if ner=="CARDINAL":
                ner="Numerals that do not fall under another type"
            if ner=="FAC":
                ner="Buildings, airports, highways, bridges, etc"
            if ner=="LOC":
                ner="Non-GPE locations, mountain ranges, bodies of water"
            if ner=="PRODUCT":
                ner="Objects, vehicles, foods, etc. (Not services.)"
            if ner=="EVENT":
                ner="Named hurricanes, battles, wars, sports events, etc"
            if ner=="WORK_OF_ART":
                ner="Titles of books, songs, etc"
            if ner=="LAW":
                ner="Named documents made into laws"
            if ner=="DATE":
                ner="Absolute or relative dates or periods"
            if ner=="TIME":
                ner="Times smaller than a day"
            if ner=="PERCENT":
                ner="Percentage, including ”%“"
            if ner=="QUANTITY":
                ner="Measurements, as of weight or distance"
            if ner=="ORDINAL":
                ner="ORDINAL:first, second etc"
        return ner
    except UnboundLocalError:
        return ""
#ner=ner_detection("narendra modi")
#print(ner)
#print(type(ner))