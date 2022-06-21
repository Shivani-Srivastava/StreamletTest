'''

Streamlit Demo Application - Word Embeddings

Shivani Srivastava

'''

import streamlit as st
import pandas as pd
import plotly.express as px

def load_data(nrows):
    data = pd.read_csv(FILE_ADDRESS, nrows=nrows)
    
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    
    return data


st.sidebar.title('Sidebar Title: Static')

FILE_ADDRESS = st.sidebar.file_uploader('Upload file')

if FILE_ADDRESS is None:

	st.write('Hello, this is a test Streamlit application.')


	st.header('Please upload a dataset using the sidebar on the left. It is preferable for the file to be CSV.')

else:
	dataset = load_data(200)

	VARS = st.sidebar.multiselect("Choose variables to plot histogram: ", dataset.columns)

	st.sidebar.write('Scroll down for exploratory visualizations and generating new variables')

	
	st.title('Main Column: Dynamic')
	
	st.write('Hello, this is a test Streamlit application.')

	st.write('It selects multiple variable from a given dataset,  and plots the histograms.')

	st.write('Checking the below checkbox will allow you to view the raw dataset.')	



	if st.checkbox('Show raw data'):

		st.subheader('Raw data')
		st.write(dataset)


	st.header('Scroll down for visualizations after selecting variables from the sidebar.')
	
	
	#fig = make_subplots(rows=1, cols=len(VARS))
	for i in VARS:

		x_label = i
		fig=px.histogram(dataset, x = i, labels = {'x' : x_label, 'y' : 'Count'})
		st.plotly_chart(fig)




	









