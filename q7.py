from copyreg import pickle
from flask import Flask, request
import streamlit as st
import pickle
from sklearn.linear_model import LogisticRegression

pickled_model = open("pickle_wine_model.pkl", "rb")
classifier = pickle.load(pickled_model)

def predict_wine():

    try :
        st.title("Predicting Wine")
        one = st.text_input("Alcohol")
        two = st.text_input("malic_acid")
        three = st.text_input("ash")
        four = st.text_input("alcalinity_of_ash")
        five = st.text_input("magnesium")
        six = st.text_input("total_phenols")
        seven = st.text_input("flavanoids")
        eight = st.text_input("nonflavanoid_phenols")
        nine = st.text_input("proanthocyanins")
        ten = st.text_input("color_intensity")
        eleven = st.text_input("hue")
        twelve = st.text_input("od280/od315_of_diluted_wines")
        thirteen = st.text_input("proline")
        


        result = classifier.predict([[one,two,three,four,five,six ,seven,eight,nine,ten,eleven,twelve,thirteen ]])
        
        if st.button("Print output"):
            st.success(result)
    except Exception as e :
        return f" Error occuredd with message : {e}"

if __name__=="__main__":
    predict_wine()