#!/usr/bin/env python
# coding: utf-8

# # Working on Real-Time Project on 'Udemy Courses Dataset

# (A Part of Big Data Analysis)

# 
# 
# 
# # UDEMY COURSES DATASET
# 
# 
# This dataset contains all course data for all subjects.
# 
# We will analyse te data using the Pandas Library.
# 
# 

# In[3]:


import pandas as pd


# In[6]:


data = pd.read_csv(r"C:\Users\hp\Downloads\7. Udemy Courses.csv")


# In[9]:


data.head()


# ## 1.What are all different subjects for which Udemy is offering courses?

# In[11]:


data.subject.unique()


# ## 2. Which subject has the maximum number of course?

# In[12]:


data.head(2)


# In[13]:


data.subject.value_counts()


# ## 3. Show all the courses which are free of cost.

# In[14]:


data.head(2)


# In[15]:


data.is_paid == False


# In[38]:


Free = data[data.is_paid == False]
Free


# In[37]:


len(Free)


# ## 4. Show all the courses which are paid.

# In[22]:


data[data.is_paid == True]


# ## 5. Which are Top Selling Courses?

# In[24]:


data.sort_values("num_subscribers" , ascending = False)


# ## 6. Which are Least Selling Courses?

# In[25]:


data.sort_values("num_subscribers")


# ## 7. Show all courses of Graphic Design where the price is below 100.

# In[27]:


data.head(2)


# In[31]:


data[(data.subject == "Graphic Design") & (data.price < '100')]


# In[33]:


data[(data.subject == "Graphic Design") & (data.price == '100')]


# ## 8. List out all the courses that are related with 'Python'.

# In[34]:


data.head(1)


# In[35]:


data[data.course_title.str.contains("Python")]


# In[39]:


len(data[data.course_title.str.contains("Python")])


# ## 9. What are courses that published in year 2015?

# In[40]:


data.head(1)


# In[41]:


data.dtypes


# In[43]:


data["published_timestamp"] = pd.to_datetime(data.published_timestamp)


# In[45]:


data.dtypes


# In[46]:


data.head(1)


# In[47]:


data['Year'] = data['published_timestamp'].dt.year


# In[48]:


data


# In[50]:


data[data.Year == 2015]


# ## 10. What are te Max. Number of Subscribers for Each Level of courses?

# In[51]:


data.head(1)


# In[53]:


data.level.unique()


# In[56]:


data.groupby('level')['num_subscribers'].max()


# In[57]:


data.groupby('level').max()

