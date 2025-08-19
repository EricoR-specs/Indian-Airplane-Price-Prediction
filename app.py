import streamlit as st
import predict

st.set_page_config(page_title="Churn_checking", layout="wide", initial_sidebar_state="auto")
st.title("Airplane Ticket Price Prediction App")
st.write("This app predicts the price of airplane tickets based on various features.")


predict.run()
