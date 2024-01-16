import pandas as pd
import os
import joblib
import keras


def secteurs():
    path=os.path.abspath('C:/Users/MAFO Aurelie/Desktop/karlos/secteur.pkl')
    return joblib.load(path)


def models():
    path=os.path.abspath('C:/Users/MAFO Aurelie/Desktop/karlos/prediction.pkl')
    return joblib.load(path)    


sectors=secteurs()
modele=models()
