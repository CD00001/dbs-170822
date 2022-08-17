#!/usr/bin/env python
# coding: utf-8

# In[9]:


from flask import Flask,request,render_template


# In[10]:


import joblib


# In[11]:


app= Flask(__name__)

# this __name__ tells the thing that this is my program


# In[12]:


@app.route("/",methods=["GET", "POST"])
def index():
    if request.method == "POST":
        rates = float(request.form.get("rates"))
        model1= joblib.load("regression")
        r1 = model1.predict([[rates]])
        model2= joblib.load("tree")
        r2 = model2.predict([[rates]])
        print(rates)
        return(render_template("index.html", result1=r1, result2=r2))
    else:
        return(render_template("index.html", result1= "waiting", result2="waiting"))


# In[ ]:


if(__name__) == "__main__":
    app.run()


# In[ ]:





# In[ ]:




