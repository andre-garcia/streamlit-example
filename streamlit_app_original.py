# import altair as alt
# import numpy as np
# import pandas as pd
import streamlit as st
from gradio_client import Client


"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""
#
# num_points = st.slider("Number of points in spiral", 1, 10000, 1100)
# num_turns = st.slider("Number of turns in spiral", 1, 300, 31)
#
# indices = np.linspace(0, 1, num_points)
# theta = 2 * np.pi * num_turns * indices
# radius = indices
#
# x = radius * np.cos(theta)
# y = radius * np.sin(theta)
#
# ## example from internet
# import requests
# import streamlit as st
#
# data = requests.get("'https://jsonplaceholder.typicode.com/todos/1'").json()
#
# st.write(data)
# ## end
#



client = Client("https://andre-garcia-rest-api-alpha.hf.space/--replicas/chhgt/")
result = client.predict(
		"WUSUUUUUUUUUUUUUUUP!!",	# str  in 'name' Textbox component
							api_name="/predict"
)
print(result)
st.write(result)







#
#
# df = pd.DataFrame({
#     "x": x,
#     "y": y,
#     "idx": indices,
#     "rand": np.random.randn(num_points),
# })
#

#
#
# st.altair_chart(alt.Chart(df, height=700, width=700)
#     .mark_point(filled=True)
#     .encode(
#         x=alt.X("x", axis=None),
#         y=alt.Y("y", axis=None),
#         color=alt.Color("idx", legend=None, scale=alt.Scale()),
#         size=alt.Size("rand", legend=None, scale=alt.Scale(range=[1, 150])),
#     ))
