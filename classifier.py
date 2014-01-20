from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import ExtraTreesClassifier

class Classifier:

    @classmethod
    def predict(cls, data, targets, cv_data):
        model = KNeighborsClassifier()
        model = ExtraTreesClassifier()
        model = LogisticRegression(C=1, penalty='l2', tol=1.0)
        model.fit(data, targets)
        for d in cv_data:
            model.predict(d)
        return model.predict(cv_data)
