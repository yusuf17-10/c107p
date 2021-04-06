import pandas as pd
import plotly.express as px
import csv 


df=pd.read_csv("data.csv")

print("for_all_the_students")

print(df.groupby("level")["attempt"].mean())
print("for_student :TRL_imb")

student_df=df.loc[df["student_id"]=="TRL_imb"]

print(student_df.groupby("level")["attempt"].mean())

fig=px.scatter(df,x="student_id",y="level",color="attempt")
fig.show()

