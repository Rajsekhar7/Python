#importing essentialmodules
import numpy as np
import ast
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.porter import PorterStemmer #used for stemming
from sklearn.metrics.pairwise import cosine_similarity #used for cosine distance calculation

#Getting the database
movies=pd.read_csv('movies.csv')
credits= pd.read_csv('credits.csv')
movies=movies.merge(credits,on='title')   #merging two database

movies= movies[['movie_id','title','overview','genres','keywords','cast','crew']]  #cutting all unnecessary columns

movies.dropna(inplace=True)  #cutting all place with null value

#creating a function to convert the string of list to list using literal_eval() function from ast library
def conv(obj):
    l=[]
    for i in ast.literal_eval(obj):
        l.append(i['name'])
    return l

#apllying the  function to all list
movies['genres']=movies['genres'].apply(conv)
movies['keywords']= movies['keywords'].apply(conv)

#function to fetch the top 3 cast of the movie
def conv3(obj):
    l=[]
    c=0
    for i in ast.literal_eval(obj):
        if c!=3:
            l.append(i['name'])
            c+=1
        else:
            break
    return l

movies['cast']=movies['cast'].apply(conv3)

#function to fetch the movie director and cinematographer
def dire(obj):
    l=[]
    for i in ast.literal_eval(obj):
        if i['job']=='Director' or i['job']=='Screenplay':
            l.append(i['name'])
    return l

movies['crew']=movies['crew'].apply(dire)

movies['overview']= movies['overview'].apply(lambda x:x.split())    #spliting the sentences into words to define them into tags

#removing the spaces from names to create unique tags and adding all of them to a single column
movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])

#Joining all the keywords to a single column tags and transfwring them to a new dataset called "data"
movies['tags']= movies['cast']+ movies['crew']+ movies['overview']+ movies['genres']+movies['keywords']

data= movies[['movie_id','title','tags']]
data['tags']=data['tags'].apply(lambda x:" ".join(x)) #Converting sll of them to a single string
data['tags']=data['tags'].apply(lambda x:x.lower()) #Converting to lowercase

cv=CountVectorizer(max_features=5000, stop_words='english')  #Vectorizaton of the string tags "max_features=5000" indicates 5000 features were considered while making the vector and "stop_words='english'" denotes the words such as to, from, and are avoided 
vectors =cv.fit_transform(data['tags']).toarray() #fitting the object into tags and converting into a numpy array

#Stemming
ps=PorterStemmer()
def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)

data['tags']=data['tags'].apply(stem)

#print(cv.get_feature_names_out) #to fetch the feature names

#to get the similarity between movies we need to calculate the distance between all movies. As the euclidian distance becomes less reliable with more diensions i am using cosine distance

similarity= cosine_similarity(vectors)

def recommend(movie):
    movie_index= data[data['title']==movie].index[0]
    distances = similarity[movie_index]
    movie_list= sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:11] #enumerate() is used to cinvert lists into tuples. Here it is done to get the real position of movies after 
    for i in movie_list:
        print(data.iloc[i[0]].title)

print(recommend('Batman Begins'))