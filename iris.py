from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
iris= datasets.load_iris()
#print(iris.keys())
#print(iris.DESCR)
features= iris.data
lables= iris.target
clf= KNeighborsClassifier()
clf.fit(features,lables)
print(clf.predict([[12,1,1,1]]))