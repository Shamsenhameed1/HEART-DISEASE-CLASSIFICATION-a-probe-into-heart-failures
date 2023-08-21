#!/usr/bin/env python
# coding: utf-8

#    
#    <span style="color: blue;font-size: 32px;">HEART DISEASE CLASSIFICATION-a probe into heart failures
#    </span> 
#   
#    
#    As a general guide:The ideal blood pressure is considered to be between 90/60mmHg and 120/80mmHg,
#  high blood pressure is considered to be 140/90mmHg or higher,
#  Low blood pressure is considered to be below 90/60mmHg.
#  
#  Cardiovascular illnesses (CVDs) are the major cause of death worldwide. CVDs include coronary heart disease, cerebrovascular disease, rheumatic heart disease, and other heart and blood vessel problems. According to the World Health Organization, 17.9 million people die each year. Heart attacks and strokes account for more than four out of every five CVD deaths, with one-third of these deaths occurring before the age of 70. A comprehensive database for factors that contribute to a heart attack has been constructed.
# 
# The main purpose here is to collect characteristics of Heart Attack or factors that contribute to it.
# The size of the dataset is 1319 samples, which have nine fields, where eight fields are for input fields and one field for an output field. Age, gender, heart rate (impulse), systolic BP (pressurehight), diastolic BP (pressurelow), blood sugar(glucose), CK-MB (kcm), and Test-Troponin (troponin) are representing the input fields, while the output field pertains to the presence of heart attack (class), which is divided into two categories (negative and positive); negative refers to the absence of a heart attack, while positive refers to the presence of a heart attack.
#  
#  ## PROJECT DELIVERABLES
#  
#  i.   What gender is more prone to heart failure?
#  ii.  proportionality between age and class
#  iii. What Age range is more prone to heart attacks?
#  iv.  What is the corellation between high blood pressure and heart attack?
#  v.   What is the corellation between low blood pressure and heart attack?
#    

# In[8]:


import pandas as pd


# In[9]:


import numpy as np


# In[10]:


Hdd = pd.read_csv("C:/Users/hamee/Desktop/Heart disease dataset.csv")


# In[11]:


Hdd.head(10)


# In[12]:


import matplotlib.pyplot as plt


# In[13]:


Hdd.describe()


# In[14]:


Hdd.info()


# # DATA CLEANING
#                     
# ..... Check for and remove duplicates

# In[15]:


Hdd.drop_duplicates


#  There were no Duplicates

#  Now Check for missing values

# In[17]:


print (Hdd.isnull().sum())


#  There are no Null values in Dataset

# # DATA EXPLORATION
# i. What gender is more prone to heart failure?

# In[23]:


Question1 =Hdd.groupby(["class","gender"]).count()


# In[24]:


print (Question1)


# 1= Female
# 0= Male
# According to my Analysis, it was discovered that Females are more prone to having heart Attacks than males

# 11. proportionality between age and class

# In[29]:


Question2 = Hdd.groupby(["class", "age"]).size().sort_values(ascending=False)

print(Question2)


# It was discovered that Age is not directly proportional to heart attacks

# In[12]:


Hdd.groupby(["class", "age"]).size().sort_values(ascending=False)


# iv. what is the corellation between high blood pressure and heart attack?

# In[29]:


Hdd['class'] = Hdd['class'].replace({'positive': 1, 'negative': 0})


# In[30]:


Hdd.head()


# In[31]:


correlation = Hdd["age"].corr(Hdd["class"])


# In[32]:


print (correlation)


# In[33]:


plt.scatter(Hdd['age'], Hdd['class'])
plt.xlabel('Age')
plt.ylabel('Class')
plt.title('Correlation between Age and Class')
plt.show()


#  A correlation value of -0.238 suggests that there is a weak negative linear relationship between the two variables. This means that as one variable increases, the other variable tends to decrease slightly, but the relationship is not very strong or consistent.

# v.  What is the corellation between low blood pressure and heart attack?

# In[35]:


correlation = Hdd["class"].corr(Hdd["pressurelow"])


# In[36]:


print (correlation)


# In[37]:


plt.scatter(Hdd['class'], Hdd['pressurelow'])
plt.xlabel('class')
plt.ylabel('pressurelow')
plt.title('Correlation between class and pressurelow')
plt.show()


# For a correlation value as small as 0.00966, I concluded that there is no practical or meaningful linear correlation between the variables being studied. 

# In[ ]:




