import streamlit as st
import numpy as np
import pandas as pd

st.title('ちんぽんアプリ')

df = pd.DataFrame(
    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
    )