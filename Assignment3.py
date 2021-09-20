#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import streamlit as st
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import plotly.express as px

st.title('Plotly Visulaization')
st.text('This is an implemetation of Plotly visualization')

st.header('1. Plotting Inline')

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/school_earnings.csv")
if st.checkbox('Show data'):
    data_load = st.text('Loading data...')
    st.write(df)
    data_load.text('Done!')
    
data = [go.Bar(x=df.School,y=df.Gap)]
st.plotly_chart(data)

st.header('2. Internactive Map')

mapbox_access_token = 'pk.eyJ1Ijoic2FyYWhhcmJhIiwiYSI6ImNrdGN2bW00dDBnc2oycG81M3V0NWptemIifQ.WtS4evyWJ5Tl-3V1T-wewQ'

st.write('Here is a map of Nuclear Waste Sites on American Campuses')
         
df1 = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/Nuclear%20Waste%20Sites%20on%20American%20Campuses.csv')

if st.checkbox('Show data?'):
    st.write(df1)
         
site_lat = df1.lat
site_lon = df1.lon
locations_name = df1.text

data1 = [go.Scattermapbox(lat=site_lat,lon=site_lon,mode='markers',marker=dict(size=17,color='rgb(255, 0, 0)',opacity=0.7),
        text=locations_name,hoverinfo='text'),go.Scattermapbox(lat=site_lat,lon=site_lon,mode='markers',marker=dict(size=8,
        color='rgb(242, 177, 172)',opacity=0.7),hoverinfo='none')]

layout = go.Layout(title='Nuclear Waste Sites on Campus',autosize=True,hovermode='closest',showlegend=False,mapbox=dict(
         accesstoken=mapbox_access_token,bearing=0,center=dict(lat=38,lon=-94),pitch=0,zoom=3,style='light'))

fig = dict(data=data1, layout=layout)

st.plotly_chart(fig)

st.header('3. 3D Plotting')
st.write('This is a 3D visulaization')

s = np.linspace(0, 2 * np.pi, 240)
t = np.linspace(0, np.pi, 240)
tGrid, sGrid = np.meshgrid(s, t)

r = 2 + np.sin(7 * sGrid + 5 * tGrid)  
x = r * np.cos(sGrid) * np.sin(tGrid)   
y = r * np.sin(sGrid) * np.sin(tGrid)  
z = r * np.cos(tGrid)               

surface = go.Surface(x=x, y=y, z=z)
data = [surface]

layout = go.Layout(title='Parametric Plot',scene=dict(xaxis=dict(gridcolor='rgb(255, 255, 255)',zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,backgroundcolor='rgb(230, 230,230)'),yaxis=dict(gridcolor='rgb(255, 255, 255)',zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,backgroundcolor='rgb(230, 230,230)'),zaxis=dict(gridcolor='rgb(255, 255, 255)',zerolinecolor='rgb(255, 255, 255)',
            showbackground=True,backgroundcolor='rgb(230, 230,230)')))

fig1 = go.Figure(data=data, layout=layout)
st.plotly_chart(fig1)

st.header('4. Animated graphs')
st.write('This is an animated visulaization')

df2 = px.data.gapminder()
fig2 = px.scatter(df2, x="gdpPercap", y="lifeExp", animation_frame="year", animation_group="country",size="pop", color="continent",
           hover_name="country",log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90])
st.plotly_chart(fig2)


df3 = px.data.gapminder()
fig3 = px.bar(df3, x="continent", y="pop", color="continent",animation_frame="year", animation_group="country", 
             range_y=[0,4000000000])
st.plotly_chart(fig3)

fig4 = go.Figure(data=[go.Scatter(x=[0, 1], y=[0, 1])],layout=go.Layout(xaxis=dict(range=[0, 5], autorange=False),
        yaxis=dict(range=[0, 5], autorange=False),title="Start Title",
        updatemenus=[dict(type="buttons",buttons=[dict(label="Play",method="animate",args=[None])])]),
        frames=[go.Frame(data=[go.Scatter(x=[1, 2], y=[1, 2])]),go.Frame(data=[go.Scatter(x=[1, 4], y=[1, 4])]),
                go.Frame(data=[go.Scatter(x=[3, 4], y=[3, 4])],layout=go.Layout(title_text="End Title"))])

st.plotly_chart(fig4)

st.header('5. Student Performance')
st.write('This is a visulaization of the student performance data')

Students_data = pd.read_csv('StudentsPerformance.csv')
if st.checkbox('Show Student data'):
    data_load = st.text('Loading data...')
    st.write(Students_data)
    data_load.text('Done!')

st.subheader('Male vs Females')
st.write('Here is a visualizing the percentage of male vs female in the data')
figure1 = px.pie(Students_data, names='gender',title='Distribution of gender')
st.plotly_chart(figure1)
    
st.subheader('Level of education vs Scores')
st.write('Here is a visualizing the relationship between the level of education and the scores')
data1 = Students_data.groupby('parental level of education').mean().reset_index() 

figure2 = px.bar(data1, x='parental level of education',y=["math score", "reading score", "writing score"],
                 barmode='group',title='Level of Education and Scores')

st.plotly_chart(figure2)

st.subheader('Race vs Test preparation course')
st.write('Here is a visualizing of the distribution of race for those who completed the test preparation sccore against those who did not')
data2 = Students_data.groupby(['race/ethnicity','test preparation course']).count().reset_index() 
data2.rename(columns={'gender':'count'},inplace=True)

figure3 = px.bar(data2, x='race/ethnicity', y='count',color='test preparation course', barmode='group',title='Race and Test Preparation')
st.plotly_chart(figure3)   

st.subheader('Scores in 3D')
st.write('Click on the button if you would like to view a 3D graph of the scores and completed/none test preparation course')
left_column, right_column = st.columns(2)
pressed = left_column.button('Want to see the scores in 3D?')
if pressed:
    st.write('Here is a visualizing the scores with test preperation course')
    figure4= px.scatter_3d(Students_data, x='math score', y='reading score', z='writing score', color = 'test preparation course')
    st.plotly_chart(figure4)
    
st.header('6. Stock Prices')
st.write('This is a visulaization of 4 different stock prices')

AAPL_data = pd.read_csv('AAPL_2006-01-01_to_2018-01-01.csv')
AABA_data = pd.read_csv('AABA_2006-01-01_to_2018-01-01.csv')
AMZN_data = pd.read_csv('AMZN_2006-01-01_to_2018-01-01.csv')
AXP_data =  pd.read_csv('AXP_2006-01-01_to_2018-01-01.csv')

data3 = pd.concat([AAPL_data,AABA_data,AMZN_data,AXP_data])
data3
st.subheader('All Stock prices')
st.write('This is a visulaization of the stock prices over time')
figure5 = px.line(data3, x=data3["Date"], y=data3['Close'],hover_data={"Date": "|%B %d, %Y"}, color = data3['Name'],title='Stock prices')
st.plotly_chart(figure5)

st.subheader('Stock prices by name')
st.write('This is a visulaization of the chosen stock prices over time')
option = st.sidebar.selectbox('Which stock would you like to view?',set(data3['Name']))
data4 = data3[data3['Name'] == option]
figure6 = px.line(data4, x=data4["Date"], y=data4['Close'],hover_data={"Date": "|%B %d, %Y"},color = data4['Name'],title=option)
st.plotly_chart(figure6)


st.subheader('Animated change in stock prices')
st.write('This is a visualization of the changes in stock prices per year')
year = []
for i in data3['Date'].str.split('-'):
    year.append(i[0])
data3['year'] = year
figure7 = px.bar(data3, x="Open", y="Name", orientation='h', color='Name',animation_frame='year',hover_name='Name',title='The change in stock prices over the years')
st.plotly_chart(figure7)

st.header('7. Super Store Data')
st.write('This is a visulaization of data collected from Super Store')

data4 = pd.read_csv('superstore_train.csv')
data4

st.subheader('Animated change in sales per category')
st.write('This is a visualiztion of sales per sub-category over the years')
year_month = []
splt_char = '-'
for i in data4['Order Date'].str.split(splt_char):
    res = splt_char.join(i[0:2])
    year_month.append(res)
    
data4['year_month'] = year_month 

figure8 = px.bar(data4, x="Sub-Category", y="Sales", animation_frame="year_month", animation_group="Sub-Category", color="Sub-Category",
           hover_name="Category",title='Sales per Category')

st.plotly_chart(figure8)


st.subheader('Ship Mode vs Quantity')
st.write('This is a visualiztion of the ship mode and quantity')
year = []
splt_char = '-'
for l in data4['year_month'].str.split(splt_char):
    year.append(l[0])    
data4['year'] = year
options = st.multiselect('Which ship model would you like to view?',set(data4['Ship Mode']))
data5 = data4[data4['Ship Mode'].isin(options)]
quantity = data5.groupby(['Ship Mode','year'])['Quantity'].sum().reset_index()
figure9 = px.funnel(quantity, x='Ship Mode', y='Quantity', color='year')
st.plotly_chart(figure9)
