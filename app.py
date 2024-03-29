import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load("best_model.joblib")

# Function to preprocess input data
def preprocess_input(date, price, commodity):
    # Convert inputs to DataFrame
    input_data = pd.DataFrame({
        "date": [date],
        "price": [price],
        "commodity": [commodity]
    })
    # Perform any necessary preprocessing steps, such as converting data types, encoding categorical variables, etc.
    # Return the preprocessed input data
    return input_data

# Function to make predictions
def predict_price(input_data):
    # Make predictions using the loaded model
    prediction = model.predict(input_data)
    return prediction

# Main function for Streamlit app
def main():
    st.title('Predicting Food Price Trends in Nigeria Model')

    # Get user input
    date = st.text_input('Date (YYYY-MM-DD):')
    price = st.number_input('Price:')
    commodity = st.text_input('Commodity:')
    
    # Preprocess input data
    input_data = preprocess_input(date, price, commodity)
    
    # Make predictions
    if st.button('Predict'):
        prediction = predict_price(input_data)
        st.success(f'Predicted price: {prediction[0]:.2f}')

if __name__ == '__main__':
    main()

    
    
    