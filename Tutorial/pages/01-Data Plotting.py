'''

Streamlit Demo Application - Word Embeddings

Shivani Srivastava

'''

import streamlit as st
import gensim.downloader as api
from gensim.test.utils import datapath
from gensim import utils
import gensim.models
import gensim.models.word2vec
import time
import numpy as np
import pandas as pd
from sklearn.decomposition import IncrementalPCA    
from sklearn.manifold import TSNE                   
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


from gensim.models import doc2vec
from scipy import spatial

#wv = api.load('word2vec-google-news-300')

def load_data(nrows):
    data = pd.read_csv(FILE_ADDRESS, nrows=nrows)
    
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    
    return data


st.sidebar.title('Sidebar Title: Static')

st.sidebar.write(f"hello {st.session_state['user']} !")

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




	









