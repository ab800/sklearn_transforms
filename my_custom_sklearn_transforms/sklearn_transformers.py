from sklearn.base import BaseEstimator, TransformerMixin
from imblearn.combine import SMOTETomek

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')



class FixUnderfit:
    def __init__(self, columns = None):
        self.data=self

    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        # Primero copiamos el dataframe de datos de entrada 'X'
        df2 = X.copy()
	
#los uno
obj = pd.DataFrame({'OBJETIVO': []})
df6 = pd.concat([df2, obj], axis=1)

            
        #divido dataframes uno con Sospechosos, otro con Aceptados
        df4 = df2.loc[df2['OBJETIVO'] == 'Sospechoso']
        df5= df2.loc[df2['OBJETIVO'] == 'Aceptado']

        #para balancear muestras tomo 8000 del df con sospechosos
        df8 = df4.sample(8000, replace=True)

        #limpio indices, asi al unirlos no da error
        df8.reset_index(inplace=True, drop=True)
        df5.reset_index(inplace=True, drop=True)

        #loa uno en el ultimo df a entregar
        df6= df8.append(df5) 

        #limpio sus indices, por las dudas
        df6.reset_index(inplace=True, drop=True)

        # Devolvemos ultimo dataframe
        return df6
    
    
    
class MySampling:
    def __init__(self, columns = None):
        self.data=self

    def fit(self, X_train, y_train):
	nm = SMOTETomek(ratio='auto')
        X_train, y_train = nm.fit_resample(X_train, y_train)

       return X_train, y_train
    
    def transform(self, X_train, y_train):
       nm = SMOTETomek(ratio='auto')
        X_train, y_train = nm.fit_resample(X_train, y_train)

       return X_train, y_train
  
