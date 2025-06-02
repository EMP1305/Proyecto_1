import pickle,sklearn.metrics,sklearn,pandas,os,sklearn.feature_extraction,nltk

inp = input('Search:\n\n')

while inp != '':
    p = open(os.path.join(os.path.dirname(__file__),'db.pickle'),'rb')
    vector,vectorizer,f_names = pickle.load(p)
    tfidf = vectorizer.transform([inp])
    cos_sim = sklearn.metrics.pairwise.cosine_similarity(tfidf,vector)
    results = pandas.Series(cos_sim[0],index=f_names)
    print ('Most relevant results:\n')
    print(results.sort_values(ascending=False) [results>0])
    print('\n If you want to end, do not type anything')
    inp = input('Search:\n\n')