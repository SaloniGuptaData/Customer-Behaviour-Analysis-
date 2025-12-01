#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv('customer_shopping_behavior.csv')


# In[2]:


df.head()


# In[3]:


df.info()


# In[4]:


df.describe()


# In[5]:


df.describe(include='all')


# In[6]:


df.isnull().sum()


# In[9]:


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x:x.fillna(x.median()))


# In[10]:


df.isnull().sum()


# In[11]:


df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')


# In[12]:


df.columns


# In[13]:


df = df.rename(columns={'purchase_amount_(usd)':'purchase_amount'})


# In[14]:


df.columns


# In[15]:


# create a new column age_group

labels = ['Young Adult', 'Adult', 'Middle-aged', 'Senior']
df['age_group'] = pd.qcut(df['age'], q=4, labels = labels)


# In[16]:


df[['age', 'age_group']].head(10)


# In[17]:


# create a column purchase_frequency_days

frequency_mapping = {
    'Fortnightly':14,
    'Weekly': 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}

df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)


# In[18]:


df[['purchase_frequency_days', 'frequency_of_purchases']].head(10)


# In[20]:


df[['discount_applied', 'promo_code_used']].head(10)


# In[21]:


(df['discount_applied'] == df['promo_code_used']).all()


# In[22]:


df = df.drop('promo_code_used', axis=1)


# In[23]:


df.columns


# In[24]:


pip install sqlalchemy pymysql mysql-connector-python pandas


# In[29]:


from sqlalchemy import create_engine

# Connection details
username = "root"           # MySQL Workbench username
password = "12345"  # MySQL Workbench password
host = "localhost"   # Typically localhost
port = "3306"        # default mysql workbench port
database = "customer_behavior"  # Name of database you created

# Create engine (connection)
engine = create_engine(f"mysql+pymysql://{username}:{password}@{host}:{port}/{database}")

# load Dataframe into MySQL
table_name = "customer"
df.to_sql('customer', engine, if_exists="replace", index=False)

print(f"Data successfully loaded into table'{table_name}' in database '{database}'.")


# In[ ]:




