from audioop import avg
from itertools import count
from logging import PlaceHolder
import numpy as np
from sklearn.model_selection import learning_curve
import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

df=pd.read_csv("E:\streamlit-learning\dashboard/bank.csv")

st.set_page_config(
    page_title='Real-Time Data Science Dashboard',
    page_icon=("✅"),
    layout='wide'
)
st.title("Real-Time/Live Data Science Dashboard")

job_filter=st.selectbox("Select  the Job",pd.unique(df['job']))

#creating a singlr element container
PlaceHolder=st.empty()

#dashboard filter

df=df[df['job']==job_filter]

#near real-time /live feed simulation
for second in range(200):
    df['age_new']=df['age']*np.random.choice(range(1,5))
    df['balance_new']=df['balance']*np.random.choice(range(1,5))
#creating KPTs
    avg_age=np.mean(df['age_new'])
    count_married=int(df[(df["marital"]=='married')]['marital'].count()+np.random.choice(range(1,30)))
    balance=np.mean(df['balance_new'])

    with PlaceHolder.container():
        #creating three columns
        kpi1,kpi2,kpi3=st.columns(3)

        #filling these columns with respective metrics of kpis
        kpi1.metric(label="Age⌛",value=round(avg_age),delta=round(avg_age)-10)
        kpi2.metric(label="Married Count💍",value=int(count_married),delta=- 10 + count_married)
        kpi3.metric(label="A/C Balance $",value=f"$ {round(balance,2)}",delta= - round(balance/count_married)*100)

        # create 2 columns for chart
        fig_col1,fig_col2=st.columns(2)
        with fig_col1:
            st.markdown("### First Chart")
            fig=px.density_heatmap(data_frame=df, x='age_new')
            st.write(fig)
        with fig_col2:
            st.markdown("### Second Chart")
            fig2=px.histogram(data_frame=df,x='age_new')
            st.write(fig2)
        st.markdown("### Detailed Data View")
        st.dataframe(df)
        time.sleep(1)