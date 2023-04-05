from sklearn.base import BaseEstimator,TransformerMixin
import pandas as pd
import datetime
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.decomposition import  PCA


class TransformationVoiture(BaseEstimator,TransformerMixin):

    def __init__(self) :
        return None
    

    def fit(self, X, y=None):
        X_=X.copy()
        return self
    
    def transform(self, X, y=None):

        X_=X.copy()

        # suppression de colonne matricule
        X_ = X_.drop(columns=['matricule'], axis=1)

        # transformation de la colonne date_circulation en age
        X_['date_circulation'] = pd.to_datetime(X_['date_circulation'])
        X_['age'] = datetime.datetime.now().year - X_['date_circulation'].dt.year

        # suppression de la colonne date_circulation
        X_ = X_.drop(columns=['date_circulation'], axis=1)

        # transformation de la colonne marque en one hot encoding
        OHE = OneHotEncoder()
        transformed = OHE.fit_transform(X_[['marque']])
        X_.drop(columns = ['marque'],inplace=True)
        X_[OHE.categories_[0]] = transformed.toarray()

        # transformation de la colonne couleur en one hot encoding
        transformed = OHE.fit_transform(X_[['couleur']])
        X_.drop(columns = ['couleur'],inplace=True)
        X_[OHE.categories_[0]] = transformed.toarray()
        
        #Normalisation des données
        ss=StandardScaler()
        ss.fit(X_)
        X_=ss.transform(X_)

        #Reduction des dimensions 
        pca=PCA(n_components=2)
        pca.fit(X_)
        X_=pca.transform(X_)
        
        return X_
    