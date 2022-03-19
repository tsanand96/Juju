
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.title("Hi Ju! DASHBOARD ALERT!")
st.subheader("Few Figures to Show the dynamics of our relationship")

st.markdown("##### The Amount of Love that I have on you has increased a lot over the years <3")
# Love vs Year
dic = {
    "Year" : [2014, 2019, 2019, 2020, 2020, 2021, 2021, 2022],
    "Love" : [10, 10, 100, 100, 200, 200, 300, 300]
}
data = pd.DataFrame(dic)
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Love'])
plt.title("Love vs Year")
st.pyplot(fig)

#

# Respect on you
st.markdown("##### While the respect that I have on you has burst open the rooofff")
list1 = [2019, 2020, 2020.5, 2021, 2021.5, 2022]
list2 = [100, 150, 300, 500, 800, 1200]
dic = {
    "Year" : [2019.5, 2020, 2020.5, 2021, 2021.5, 2022],
    "Respect" : [100, 150, 300, 500, 800, 1200]
}
data = pd.DataFrame(dic)
fig, ax = plt.subplots()
ax.plot(data['Year'], data['Respect'])
plt.title("Respect vs Year")
st.pyplot(fig)

st.markdown("# ")
st.markdown("##### You have a Surprise!")

if st.button("Surprise Me"):
    st.write("I Understand that you need me badly now! And would like to see me!!")
    st.write("So I thought I will provide that virtually :P")

if st.radio("READY FOR THE VIRTUAL PARTY?", ['No', 'Yes']) == 'Yes':
    x = st.selectbox('Choose what you need now', ['Nothing', 'Hug', 'Kiss', 'Cuddle', 'Dine Together'])
    if x == 'Hug':
        st.image("hug.jpg")
    elif x == 'Kiss':
        st.image("kiss.jpg")
    elif x == 'Cuddle':
        st.image("cuddle.jpg")
    elif x == 'Dine Together':
        st.image("eating.jpg")

    y = st.selectbox('Lets Make it interesting :P, What we really should do!!!!', ['Nothing', 'Run Away', 'Take an Aruva', 'Keep Calm and Eat Biriyani'])
    if y == 'Run Away':
        st.image("runningaway.jpg")
    elif y == 'Take an Aruva':
        st.image("aruva.jpg")
    elif y == 'Keep Calm and Eat Biriyani':
        st.write("Enna nadandha namakenna! :P")
        st.image("biriyani.jpg")

    if st.button("Click this at the End"):
        st.write("Everything will fall in place my swweeetttheart! Don't worry")
        st.write("Now Stop Grinning and Start Konjifying me :)")


