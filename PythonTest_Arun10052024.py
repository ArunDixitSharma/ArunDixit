#!/usr/bin/env python
# coding: utf-8

# In[15]:


#1.	Store 3 in a variable and convert it into integer, string and float 
#ad= 1
#print(type(ad)) 
#ad1= float(ad) 
#print(ad1) 
#bd= "1" 
#print(type(bd)) 
#bd1= int(bd) 
#print(type(bd1)) 
bd2= str(bd1) 
print(type(bd2))


# In[16]:


#2.	Write python syntax to check type of variable. 
type()


# In[24]:


#3.	Below is list of variables, please mention which is right and which is wrong. 
#myvar=3 
#myVar=4 
#my_var=5 
#_my_var=2 
#my-var=2 # Not 
#MYVAR=2 
#Myvar2=2 
#my var=2 # Not


# In[26]:


#x = “Orange” 
#y = “Banana” 
#z = “Cherry”


# In[29]:


#x = “Orange”
#y = “Orange”
#z = “Orange”
 
#x=y=z="Orange"


# In[31]:


#x="Hello,World!" 
#print(x[6:9])


# In[32]:


#print(len(x))


# In[38]:


#print(x[7:-2])


# In[39]:


#print(x.upper())


# In[40]:


#print(x.lower())


# In[41]:


#print(x.strip())


# In[42]:


print(x.replace("H","J"))


# In[43]:


print(x.split(","))


# In[48]:


a="Hello" 
b="World" 
 
x1= a + b 
print(x1)


# In[49]:


e= "We are the so-called /Vikings/ from the north" 
print(e)


# In[50]:


lis= ["apple", "banana", "cherry", "watermelon", "orange", "plum"]   
print(len(lis)) 


# In[51]:


print(lis[2])


# In[53]:


print(lis[2:-1])


# In[56]:


lis[3]= "grapes" 
print(lis)


# In[57]:


lis[1:2]= [“kiwi”, “mango”]


# In[59]:


lis[4]= "lichi" 
print(lis)


# In[63]:


lis.insert(6,"blueberry") 
print(lis)


# In[61]:


lis.extend["Sunil", "Saket", "Suita", "Raj", "Gopal"]


# In[66]:


new_list = ["Sunil", "Saket", "Suita", "Raj", "Gopal"] 
final= lis + new_list 
print(final)


# In[67]:


lis.remove("apple")
lis.pop("apple")
del lis


# In[ ]:




