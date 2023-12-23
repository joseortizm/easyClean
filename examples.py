from easyclean import clean, datasets
import pandas as pd
import random as rd

#m = clean.test('jose')
#print(m)

#dataframe for testing
path = 'test.csv'
df = pd.read_csv(path, encoding = 'unicode_escape')
#print(df.head())
#print(df.isnull().sum())
newDf = df.dropna()
#print(newDf.isnull().sum())
comments = newDf['text']
#print(comments.head())
comments_list = list(comments)
#print(len(comments_list))
#print(comments_list)

#5 comments 
randomComments = rd.sample(comments_list, 5)
#print(randomComments)

'''
#examples rex
#one comment
print(randomComments[0])
posRegular = clean.rex(randomComments[0]) #check space when start
print(posRegular)
#manual comment
comentario = '   @handz  a z y Z ~it: ^ } :-* was_] HOLA with  <3 ` A B :D :=D :) :() @{ quiet [.... <> % unfortunatly!!!!! http://www.google.com' # pend with: _ 
print(comentario) 
posRegularText = clean.rex(comentario)
print(posRegularText)
print(clean.cstopwords(posRegularText))
'''


#examples gethashtag
'''
comment = 'hi how are you? #live #paris love you #family'
listHashtag = clean.gethashtags(comment) #Parameter hash: default is False, True: word without #
print(listHashtag)
'''

#examples getnumbers
'''
comment = 'how are 1s24 3 you 16F hi 69$'
numbers = clean.getnumbers(comment)
print(numbers)
'''

#examples geturls
'''
comment = 'hello friend https://www.example.com go to http://exampletwoo.org'
urls = clean.geturls(comment)
print(urls)
'''

#examples emails
'''
comment = 'hello friend jose@hi5.com go to pepe@hi5you.org hello 56'
urls = clean.getemails(comment)
print(urls)
'''

#examples users
'''
comment = 'hello friend @joseortizm_ go to @capacitadero hello 56'
users = clean.getusers(comment)
print(users)
'''
#examples reduce txt
'''
comment = 'hellooooo friendsss hoowww are youuu?'
reducido = clean.reducetext(comment)
print(reducido)
'''

#datasets#


originalDataset = "../datasets/reviews/IMDBDatasetSPANISH.csv"
pandasDF = pd.read_csv(originalDataset)
filas = ['review_es', 'sentiment'] #columnas por mantener
DF = datasets.delete(pandasDF, filas)
#print(DF)


#listDatasets = ["../datasets/reviews/IMDBDatasetSPANISH.csv", "../datasets/reviews/filmaffinity", "../datasets/reviews/muchocine"]
listDatasets = [DF, "../datasets/reviews/filmaffinity", "../datasets/reviews/muchocine", 2]

nPath = datasets.join(listDatasets)
print(nPath)








