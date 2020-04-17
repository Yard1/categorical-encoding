from sklearn.base import BaseEstimator, ClassifierMixin
class EncoderWrapper(BaseEstimator, ClassifierMixin):
    def __init__(self, encoder, classifier):
        self.encoder = encoder
        self.classifier = classifier
    
    def fit(self, X, y, **kwargs):
        self.encoder.fit(X, y)
        X_transformed = self.encoder.transform(X)
        y_transformed = self.encoder.expand_y(y)
        self.classifier.fit(X_transformed, y_transformed)
    
    def predict_proba(self, X):
        X_transformed = self.encoder.transform(X)
        preds = self.classifier.predict_proba(X_transformed)[:,1]
        return self.encoder.average_y(preds)
    
    def predict(self, X):
        return self.predict_proba(X).round()
