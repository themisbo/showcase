import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.impute import KNNImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

penguins = pd.read_csv('PalmerPenguins.csv')
penguins = penguins.dropna()
penguins = penguins.drop("year", axis = 1)
penguins = penguins.drop("island", axis = 1)
penguins = penguins.drop("sex", axis = 1)

# Dictionary containing the mapping
variety_mappings = {0: 'Adelie', 1: 'Gentoo', 2: 'Chinstrap'}

# Encoding the target variables to integers
penguins = penguins.replace(['Adelie', 'Gentoo' , 'Chinstrap'],[0, 1, 2])

species = penguins.pop('species')

pipe_svc = Pipeline([ ('onehot', OneHotEncoder(handle_unknown='ignore', sparse=False)), ('imputer', KNNImputer(n_neighbors=2, weights="uniform")), ('scaler', StandardScaler(with_mean=False)), ('svc', svm.SVC())])

pipe_svc.fit(penguins, species)

def classify(bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g):
    arr = np.array([bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g]) # Convert to numpy array
    arr = arr.astype(np.float64)
    query = arr.reshape(1, -1)

    prediction = variety_mappings[pipe_svc.predict(query)[0]]

    return prediction

# def classify(island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex):
#     arr = pd.DataFrame([island, bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g, sex])
#     query = arr.to_numpy().reshape(1, -1)
#     prediction = pipe_svc.predict(query) 

#     prediction = variety_mappings[pipe_svc.predict(query)[0]]

#     return prediction

# island ="Biscoe"
# bill_length_mm = 48
# bill_depth_mm = 16
# flipper_length_mm = 220
# body_mass_g = 5400
# sex = "male"