import streamlit as st
import pickle
from random import *

def classify(num):
    if num == 1:
        return 'Skipped'
    else:
        return 'Not-Skipped'

def main ():
    lgbm = pickle.load(open('model.pkl', 'rb'))

    html_temp = """
    <div style="background-color:teal ;padding:10px">
    <h2 style="color:white;text-align:center;"> Spotify Skip Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write("""
This app predicts **whether the song should be skipped or not** !
""")

    sp = st.slider('Select session_position', 0, 20)
    duration = st.slider('Select duration', 30.0, 1800.0)
    yr = st.slider("Select release_year:", 1950, 2019)
    est = st.slider('Select us_popularity_estimate', 90.0, 100.0)
    acous = st.slider('Select acousticness', 0.0, 1.0)
    beat_str = st.slider('Select beat_strength', 0.0, 1.0)
    bounce = st.slider('Select bounciness', 0.0, 1.0)
    dance = st.slider('Select danceability', 0.0, 1.0)
    rangemean = st.slider('Select dyn_range_mean', 0.0, 20.0)
    energy = st.slider('Select energy', 0.0, 1.0)
    flat = st.slider('Select flatness', 0.5, 1.0)
    instrument = st.slider('Select instrumentalness', 0.0, 1.0)
    key = st.slider('Select key' , 0.0 , 11.0 )
    live = st.slider('Select liveness', 0.0, 1.0)
    loud = st.slider('Select loudness', -25.0, 0.0)
    m = st.slider('Select mechanism', 0.0, 1.0)
    mode = st.selectbox('Select mode', (0.0, 1.0))
    o = st.slider('Select organism', 0.0, 1.0)
    s = st.slider('Select speechiness', 0.0, 1.0)
    tempo = st.slider('Select tempo', 50.0, 220.0)
    time_signature = st.selectbox('Select Time-Signature' , (0.0 , 1.0) ) + 3
    v = st.slider('Select valence', 0.0, 1.0)
    a0 = st.slider('Select acoustic_vector_0', -1.0, 1.0)
    a1 = st.slider('Select acoustic_vector_1', -1.0, 1.0)
    a2 = st.slider('Select acoustic_vector_2', -1.0, 1.0)
    a3 = st.slider('Select acoustic_vector_3', -1.0, 1.0)
    a4 = st.slider('Select acoustic_vector_4', -1.0, 1.0)
    a5 = st.slider('Select acoustic_vector_5', -1.0, 1.0)
    a6 = st.slider('Select acoustic_vector_6', -1.0, 1.0)
    a7 = st.slider('Select acoustic_vector_7', -1.0, 1.0)
    skipped = randint(0,1)
    inputs = [[sp,duration,yr,est,acous,beat_str,bounce,dance,rangemean,energy,flat,instrument,key,live,
               loud,m,mode,o,s,tempo,time_signature,v,a0,a1,a2,a3,a4,a5,a6,a7
                ,sp,skipped,duration,yr,est,acous,beat_str,bounce,dance,rangemean,energy,flat,instrument,key,live,
               loud,m,mode,o,s,tempo,time_signature,v,a0,a1,a2,a3,a4,a5,a6,a7]]

    if st.button('Classify'):
        st.success(classify(lgbm.predict(inputs)))

if __name__ == '__main__':
    main()




