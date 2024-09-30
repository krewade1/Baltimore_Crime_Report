#!/usr/bin/env python
# coding: utf-8

# In[3]:


pip install skimpy


# In[4]:


pip install skimpy


# In[5]:


import skimpy


# In[7]:


import pandas as pd

# Load the dataset
data = pd.read_csv('/Users/kunalrewade/Desktop/Baltimore911.csv')


# In[8]:


from skimpy import skim

# Generate the summary profile
profile = skim(data)

# Display the profile
print(profile)


# In[11]:


# droping 3 columns since they had many missing values 
data = data.drop(['Location 1', 'vri_name1', 'Weapon'], axis=1)


# In[13]:


# checking the dropped columns
data.head()


# In[15]:


# Removing missing values from all the columns where the % of missing value is less than 5.

data = data.dropna(subset=['Longitude', 'Latitude', 'CrimeTime','Location','Neighborhood'])


# In[16]:


#Checking weather the missing values are dropped or not
profile = skim(data)

# Display the profile
print(profile)


# In[38]:


#Adding mode values to Inside/Outside and Premise
# Find the mode of the column 'Inside/Outside'
mode_value1= data['Inside/Outside'].mode()[0]

# Print the mode value
print("Inside/Outside' mode value:", mode_value1)


# In[41]:


# Find the mode of the column 'Premise'
mode_value2 = data['Premise'].mode()[0]

# Print the mode value
print("Mode of Premise:", mode_value2)


# In[42]:


#Adding mode values to both columns
data['Inside/Outside'] = data['Inside/Outside'].fillna(mode_value1)
data['Premise'] = data['Premise'].fillna(mode_value2)



# In[43]:


#Checking weather the missing values are filled
profile = skim(data)

#here we get all the columns with 0% missing values


# In[44]:


#Extracting the cleaned file
data.to_csv('/Users/kunalrewade/Desktop/Cleaned_Baltimore911.csv', index=False)


# In[ ]:




