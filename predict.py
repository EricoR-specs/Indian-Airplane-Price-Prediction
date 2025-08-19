import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json

def run():
    st.title('Flight Data Prediction')

    # Project Summary Section
    st.write('### Summary of Flight Analysis')
    st.write(
        """
        This flight data analysis covers flight volume, popular routes, and the factors that influence ticket prices.

        **Flight Volume and Popular Routes:**
        * **Vistara** is the airline with the highest number of flights, followed by **Air India** and **Indigo**.
        * **Delhi** and **Mumbai** are the main flight hubs, with the highest volume of flights to and from other major cities like **Bangalore**.
        * The highest number of departures occurs in the morning.
        """
    )
    st.markdown('---')

    st.write('### Factors Influencing Ticket Prices')
    st.write(
        """
        Flight ticket prices are not static and are influenced by several key factors:
        * **Airline Type:** Airlines can be grouped into two pricing categories:
            * **Low-Cost Carriers:** Such as **AirAsia**, **Indigo**, and **GO_FIRST**, have relatively stable and affordable prices.
            * **Full-Service Carriers:** Such as **Vistara** and **Air India**, have significantly higher prices and a more varied price range.
        * **Departure and Arrival Times:** Ticket prices vary depending on the combination of departure and arrival times.
        * **Distance Traveled:** Routes with longer distances, which require more fuel, tend to have higher ticket prices.
        * **Time of Booking:** The closer the purchase date is to the departure date, the more ticket prices tend to increase.
        """
    )
    st.markdown('---')

    st.write('### Model Selection and Performance')
    st.write(
        """
        To predict ticket prices, a variety of regression models were evaluated. Simple linear models like Linear Regression and Ridge Regression performed poorly due to the data's complex, non-linear nature. Advanced tree-based models, particularly **boosting models** like **XGBoost** and **LightGBM**, were far more effective at capturing these complex patterns.

        After comparing the models, **XGBoost** was selected as the best choice. Hyperparameter tuning was performed on the model to optimize its performance, resulting in the following final metrics:
        * **Mean R² Score: 0.9787**
          This indicates that the model can explain approximately **98%** of the variance in ticket prices, signifying a very high level of accuracy.
        * **Mean Negative MSE: -10,948,750**
          This score shows that the model has a very low average prediction error, making it a reliable tool for forecasting airline ticket prices.
        """
    )
    st.markdown('---')
    
    # Load model
    try:
        with open('best_xgb_model.pkl', 'rb') as file_1:
            model = pickle.load(file_1)
        st.success("Model loaded successfully!")
    except FileNotFoundError:
        st.error("Error: Model file 'best_xgb_model.pkl' not found. Please ensure it is in the correct directory.")
        return # Exit the function if model is not found

    st.write('## Input Data')
    with st.form(key='data'):
        airlines = ['SpiceJet', 'AirAsia', 'Vistara', 'IndiGo', 'Akasa Air']
        flight_numbers = [f'SG-{np.random.randint(1000, 9999)}' for _ in range(5)] + \
                         [f'I5-{np.random.randint(100, 999)}' for _ in range(5)] + \
                         [f'UK-{np.random.randint(900, 999)}' for _ in range(5)] + \
                         [f'6E-{np.random.randint(100, 999)}' for _ in range(5)] + \
                         [f'QP-{np.random.randint(100, 999)}' for _ in range(5)]
        source_cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata', 'Chennai']
        destination_cities = ['Mumbai', 'Delhi', 'Bangalore', 'Kolkata', 'Chennai']
        departure_times = ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night']
        arrival_times = ['Early_Morning', 'Morning', 'Afternoon', 'Evening', 'Night']
        stops = ['zero', 'one', 'two_or_more']
        classes = ['Economy', 'Business']
        
        airline = st.selectbox('Airline', airlines)
        flight_number = st.selectbox('Flight Number', flight_numbers)
        source_city = st.selectbox('Source City', source_cities)
        destination_city = st.selectbox('Destination City', destination_cities)
        departure_time = st.selectbox('Departure Time', departure_times)
        arrival_time = st.selectbox('Arrival Time', arrival_times)
        stops = st.selectbox('Stops', stops)
        flight_class = st.selectbox('Class', classes)
        duration = st.number_input('Duration (hours)', min_value=1.5, max_value=4.0, step=0.1)
        days_left = st.number_input('Days Left for Departure', min_value=1, max_value=60)

        # Submit button
        submit = st.form_submit_button('Predict')

    if submit:
        data = {
            'airline': airline,
            'flight': flight_number,
            'source_city': source_city,
            'destination_city': destination_city,
            'departure_time': departure_time,
            'arrival_time': arrival_time,
            'stops': stops,
            'class': flight_class,
            'duration': duration,
            'days_left': days_left,
        }
        data = pd.DataFrame([data])
        st.dataframe(data)

        # Make prediction
        prediction = model.predict(data)
        st.write(f'Prediction: {prediction[0]}')

# Call the run function to execute the Streamlit app
if __name__ == "__main__":
    run()