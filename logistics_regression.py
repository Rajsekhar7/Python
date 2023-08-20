from sklearn import datasets
import numpy as np
from sklearn.linear_model import LogisticRegression
iris= datasets.load_iris()
x= iris.data[:,3:]
y= (iris.target== 2).astype(np.int_)
clf= LogisticRegression()
clf.fit(x,y)
a=float(input("Enter Petal width: "))
print(clf.predict([[a]]))