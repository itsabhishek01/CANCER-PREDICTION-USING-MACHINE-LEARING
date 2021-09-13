#############BREAST CANCER PREDICTION THROUGH MACHINE LEARNING######
######-------MADE BY ABHISHEK------#################################

#################--------START---------#############################

import pandas as pd

df=pd.read_csv('data.csv')
df = df.drop(columns=["id","Unnamed: 32"])

#checking if there is any missing value

#print(df.isnull().sum())

x=df.iloc[0:569,1:31]#independent
y=df["diagnosis"]#dependent


#changing string to numeric form
from sklearn.preprocessing import LabelEncoder
la=LabelEncoder()

y=la.fit_transform(y)

#scaling our independent data
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x=sc.fit_transform(x)

#train test
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

#          -------------------- END OF PRE-PROCESSING-------------------------------

#classifiction
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr.fit(x_train,y_train)

y_pred=lr.predict(x_test)

#checking accuracy
from sklearn.metrics import accuracy_score
print("Accuracy Score is:")
print(accuracy_score(y_test, y_pred))

#saving models
from joblib import dump
dump(la,"diagnosis.joblib")
dump(sc,"scaling.joblib")
dump(lr,"regressor.joblib")

#-----------------#----------#------------#-----------#----------------#---------#
##############################----------END------------###########################
