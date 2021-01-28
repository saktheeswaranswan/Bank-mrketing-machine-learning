"""
Alonso Vega
January 23, 2021
ClassifierModel: Used to train a ensemble classifier.
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

class ClassifierModel():
    __slots__ = '_X_mat', '_y_vect', '_freq_table', '_D_test'

    def __init__(self):
        try:
            self._X_mat  = pd.read_csv("X_matrix.csv")
            self._y_vect = pd.read_csv("y_vect.csv")
        except FileNotFoundError:
            print("File was not Found.")
            return None
        print("Data was read-in correctly.")

        self._D_test = []

        # Discretize
        self._X_mat["employees"] = pd.cut(self._X_mat["employees"], 25, labels=False)
        self._X_mat["euribor3Mon"] = pd.cut(self._X_mat["euribor3Mon"], 25, labels=False)
        self._X_mat["consConfidenceIdx"] = pd.cut(self._X_mat["consConfidenceIdx"], 25, labels=False)
        self._X_mat["consPriceIdx"] = pd.cut(self._X_mat["consPriceIdx"], 25, labels=False)
        self._X_mat["empVariation"] = pd.cut(self._X_mat["empVariation"], 25, labels=False)

        attr_list        = list(self._X_mat.columns)
        unqClasses_set   = list(np.unique(self._y_vect))
        self._freq_table = {unqClasses_set[i]: {} for i in range(len(unqClasses_set))}

        # Init. Table
        for i_class in range(len(unqClasses_set)):
            for attr in attr_list:
                self._freq_table[i_class][attr] = {}
                for val in self._X_mat[attr].unique():
                    self._freq_table[i_class][attr][val] = 0

    def train_selectiveNB(self):
        return None

    def split_data(self):
        current_data = pd.concat([self._X_mat, self._y_vect], axis=1)

        list_tt = train_test_split(current_data)
        D_train = list_tt[0]
        D_test  = list_tt[1]

        self._D_test = D_test
        return D_train

    def train_NB(self):
        # Training
        D_train = self.split_data()
        print("Training Matrix Size", D_train.shape[0], " x ", D_train.shape[1])
        print(D_train.head(5))

        for i in range(D_train.shape[0]):
            inst       = D_train.iloc[i, :-1]
            this_class = D_train.iloc[i, -1]

            print("\nInstance: ", i)
            for feat in inst.index:
                this_val = inst.loc[feat]
                self._freq_table[this_class][feat][this_val] += 1

                print("Count of ({}, {}, {}) : ".format(this_class, feat, this_val),
                      self._freq_table[this_class][feat][this_val])
        return None

    def cond_prob(self, attribute_name, class_name, attribute_value):
        # m-estimate
        m = 1

        # |X_i|
        attr_space = self._X_mat[attribute_name].unique()

        p_hat = self._freq_table[class_name][attribute_name][attribute_value]
        p_hat = p_hat + m*(1/attr_space.size)

        attr_expand = 0
        for val in attr_space:
            attr_expand = attr_expand + self._freq_table[class_name][attribute_name][val]



        return None


    def test_NB(self):


        return None

    def train_SVM(self):
        return None

    def train_logistic_regression(self):
        return None

