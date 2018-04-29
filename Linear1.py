#http://scikit-learn.org/stable/auto_examples/linear_model/plot_ols.html#sphx-glr-auto-examples-linear-model-plot-ols-py
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

diabetes= datasets.load_diabetes()

diabetes_X=diabetes.data[:,np.newaxis,2]

diabetes_X_train=diabetes_X[:-20]
diabetes_X_test=diabetes_X[-20:]

diabetes_y_train=diabetes.target[:-20]
diabetes_y_test=diabetes.target[-20:]

regr=linear_model.LinearRegression()

regr.fit(diabetes_X_train,diabetes_y_train)

diabetes_y_pred=regr.predict(diabetes_X_test)

print('Coeffcients:', regr.coef_)
print('Mean squared error:' % mean_squared_error(diabetes_y_test,diabetes_y_pred))

print('Variance score: %.2f' % r2_score(diabetes_y_test, diabetes_y_pred))

plt.scatter(diabetes_X_test,diabetes_y_test, color='red')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=4)

plt.xticks(())
plt.yticks(())

plt.show()