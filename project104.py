import pandas as pd
import statistics as st

df = pd.read_csv("SOCR-HeightWeight.csv")

weight_list = df["Weight(Pounds)"].tolist()

median = st.median(weight_list)
mode = st.mode(weight_list)
mean = st.mean(weight_list)

print(f"Mean is {mean}, mode is {mode}, and median is {median}")