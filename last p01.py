#!/usr/bin/env python
# coding: utf-8

# In[1]:


data=['id','name','track','giographic','history','computer','arabic','islamic','english','physics','chemistry','biology','math','total','average','result','grade']
import csv 
f=open ('desktop/student.csv','w')
row=data
writef=csv.writer(f)
writef.writerow(row)
f.close()


# In[2]:


def readfile ():
    import csv 
    f=open ('desktop/student.csv','r')
    readf=csv.reader(f,delimiter =',')
    data=list(readf)
    list1=[]
    student={}
    for i,j in enumerate (data):
        list1=j
        for x in list1:
            student[list1[0]]=list1[1:]
    return(student)
        
    


# In[3]:


def openfile ():
    import os
    os.open('desktop/student.csv')


# In[4]:


#append
def append ():
    import csv 
    f=open ('desktop/student.csv','a',newline='')
    readf=csv.reader(f,delimiter =',')
    row = std_details
    writef=csv.writer(f)
    writef.writerow(row)
    f.close()


# In[5]:


# طباعة صف فارغ
def freerow ():
    import csv 
    f=open ('desktop/student.csv','a',newline='')
    readf=csv.reader(f,delimiter =',')
    row = ['',[]]
    writef=csv.writer(f)
    writef.writerow(row)
    f.close()


# In[6]:


std_details=['','','',0,0,0,0,0,0,0,0,0,0,0,0,'','']
subjects =data[3:13]


# In[7]:


def search ():
    stdid = input ('enter student id :')
    while (stdid in readfile() ):
        if stdid not in readfile():
            print ('student id does not exist')
            break
        else :
            print ('student id already exist ')
            stdid = input ('enter student id :')
    return (stdid)
        
    


# In[8]:


def mainMenu():
    print ('please choose from one of the below options :')
    print ('-----------------------------------------------')
    print ('[1]-add new student :')
    print ('[2]- delete student :')
    print ('[3]- update :')
    print ('[4]- display :')
    print ('[5]- exit')
    


# In[9]:


def addMenu():
    print ('please choose from one of the below options :')
    print ('-----------------------------------------------')
    print ('[1]- foundation :')
    print ('[2]- medical :')
    print ('[3]- engineer :')
    print ('[4]- exit')


# In[10]:


def delete():
    print ('delete')
    #search()
   


# In[11]:


def update ():
    print ('update')
    #search()
    


# In[12]:


def display():
    print ('display')
   


# In[13]:


def updateMenu ():
    print ('please choose from one of the below options :')
    print ('-----------------------------------------------')
    print ('[1]-update name :')
    print ('[2]- update track :')
    print ('[3]- uddate subjects :')
    print ('[5]- exit')
    


# In[14]:


std_details=['','','',0,0,0,0,0,0,0,0,0,0,0,0,'','']
subjects =data[3:13]
marks =[0,0,0,0,0,0,0,0,0,0]
std_details[3:13]=marks


# In[15]:


def std_data():
    std_id=search()
    stdname = input ('enter student name  :')
    std_details[0]=std_id
    std_details[1]=stdname


# In[16]:


def grades ():
    
    std_details[13]=sum(std_details[3:13])
    std_details[14]=(std_details[13]/6)
    average =std_details[14]
    if average >=50:
        result ='pass'
        if average >=90:
            std_details[16] ='A'
        elif average >=80:
            std_details[16] ='B'
        elif average >=70:
            std_details[16] = 'C'
        elif average >=60 :
            std_details[16] ='D'
    else :
        result ='fail'
        grade = 'F'
    std_details[15]=result
    #std_details[16]=grade


# In[17]:


def addNew():
    freerow ()
    choice=0
    while (choice !=4):
        addMenu()
        choice =int(input ('enter option from the above options :'))
        if choice ==1:
            std_data()
            std_details[2]='foundation'
            for i,j in enumerate (subjects) :
                if i==6 :
                    break
                    print (marks)
                print ('enter marks of :',j)
                mark=int(input ())
                marks [i]=mark
            std_details[3:13]=marks
            grades()
            append()
            print (std_details)
        elif choice ==2:
            std_data()
            std_details[2]='medical'
            for i,j in enumerate (subjects) :
                if i<3:
                    continue
                if i ==9 :
                    break
                print ('enter marks of :',j)
                mark=int(input ())
                marks [i]=mark
            std_details[3:13]=marks
            grades()
            append()
        elif choice ==3:
            std_data()
            std_details[2]='engineer'
            for i,j in enumerate (subjects) :
                if i<3:
                    continue
                if i ==8 :
                    continue
                print ('enter marks of :',j)
                mark=int(input ())
                marks [i]=mark
            std_details[3:13]=marks
            grades()
            append()
        elif choice==4:
            break
            
        else :
            print ('invalid option')
            addMenu()
            choice =input ('enter option from the above options :')
            
            
    print ('goodby')
        
    


# In[18]:


mainMenu()
option =input ('enter option from the below options :')
while (option !='5'):
    if option =='1':
        addNew()
        option ='7'
    elif option =='2':
        delete()
    elif option =='3':
        update ()
    elif option =='4':
        display ()
    else :
        print ('invalid option')
        mainMenu()
        option =input ('enter option from the below options :')
print ('goodby')
    


# In[ ]:




