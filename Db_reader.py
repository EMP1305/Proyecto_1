import sklearn,sklearn.feature_extraction,os,pickle,nltk

f_names = os.listdir(os.path.join(os.path.dirname(__file__),'Db'))
documents = list()
counter = 1
nltk.download('stopwords')

for f_name in f_names:
    f = open (os.path.join(os.path.join(os.path.dirname(__file__),'Db'),f'{f_name}'),'r',encoding='utf-8')
    documents.append(f.read())
    print (f'{counter}/{len(f_names)}')
    counter+=1
    
vectorizer = sklearn.feature_extraction.text.TfidfVectorizer(lowercase=True,stop_words=nltk.corpus.stopwords.words('spanish'))
vector = vectorizer.fit_transform(documents)

p = open('db.pickle','wb')
pickle.dump([vector,vectorizer,f_names],p)