import streamlit as st
import pandas as pd
import joblib


st.title('Vehicle Insurance Response prediction')

#read the dataset to fill the values in the drop down list
df = pd.read_csv('train.csv')

#"Gender": Gender,
#"Age": Age,
#"Driving_License": Driving_License,
#"Region_Code": Region_Code,
#"Previously_Insured": Previously_Insured,
#"Vehicle_Age": Vehicle_Age,
#"Vehicle_Damage": Vehicle_Damage,
#"Annual_Premium": Annual_Premium,
#"Policy_Sales_Channel": Policy_Sales_Channel,
#"Vintage": Vintage,





#create the input fields
Gender = st.selectbox("Gender", pd.unique(df['Gender']))
Age = st.number_input("Age")
Driving_License = st.number_input("Driving_License")
Region_Code = st.selectbox("Region_Code", pd.unique(df['Region_Code']))
Previously_Insured = st.selectbox("Previously_Insured", pd.unique(df['Previously_Insured']))
Vehicle_Age = st.selectbox("Vehicle_Age", pd.unique(df['Vehicle_Age']))
Vehicle_Damage = st.selectbox("Vehicle_Damage", pd.unique(df['Vehicle_Damage']))
Annual_Premium = st.number_input('Annual_Premium')
Policy_Sales_Channel = st.selectbox("Policy_Sales_Channel", pd.unique(df['Policy_Sales_Channel']))
Vintage = st.selectbox("Vintage", pd.unique(df['Vintage']))





#convert the input values into a dictionary
inputs = {
"Gender": Gender,
"Age": Age,
"Driving_License": Driving_License,
"Region_Code": Region_Code,
"Vehicle_Age": Vehicle_Age,
"Vehicle_Damage": Vehicle_Damage,
"Previously_Insured": Previously_Insured,
"Annual_Premium": Annual_Premium,
"Policy_Sales_Channel": Policy_Sales_Channel,
"Vintage": Vintage


}


#Click for prediction (prediction button)

if st.button("Predict"):
    model = joblib.load("cross_sell_pipeline_model.pkl")
    #input to the fields
    X_input = pd.DataFrame(inputs, index=[0])
    #model prediction
    prediction = model.predict(X_input)
    #display the prediction
    st.write(prediction)
