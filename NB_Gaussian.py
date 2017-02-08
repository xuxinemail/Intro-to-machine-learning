import numpy as np
from sklearn.naive_bayes import GaussianNB

X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])
classifier = GaussianNB()
classifier.fit(X, Y)
print classifier.predict([[-0.8, -1]])
# calculate the accuracy (# of correct prediction/ # of examples)
# method 1
# pred = classifier.predict(X)
# correct = 0
# for i in range(len(Y)):
#     if pred[i] == Y[i]:
#         correct+=1
# accuracy = correct/len(Y)
# print accuracy

#method2
from sklearn.metrics import accuracy_score
pred = classifier.predict(X)
print accuracy_score(Y, pred)