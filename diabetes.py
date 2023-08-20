import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
#print(diabetes.keys())    dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])
diabetes_X_train= diabetes.data[-30:]
diabetes_X_test= diabetes.data[:-30]

diabetes_Y_train= diabetes.target[-30:]
diabetes_Y_test= diabetes.target[:-30]

model=linear_model.LinearRegression()
model.fit(diabetes_X_train, diabetes_Y_train)#the training data are fed to the model
diabetes_Y_predict= model.predict(diabetes_X_test)#prdiction done on the testing data

print("Mean squared error: ", mean_squared_error(diabetes_Y_test, diabetes_Y_predict))
print("Weights: ", model.coef_)
print("intercept", model.intercept_)
# plt.scatter(diabetes_X_test, diabetes_Y_test)
# plt.scatter(diabetes_X_test, diabetes_Y_predict)
# plt.show()