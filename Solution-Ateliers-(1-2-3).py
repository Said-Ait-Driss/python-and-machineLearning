#!/usr/bin/env python
# coding: utf-8

# <Center><h1>Nassiri Ilyas</h1></center>

# <Center><h1>Atelier 1 :</h1></center>

# ## Exercice 1 :

# In[13]:


temps,Distances=2.75,125.5
Vitesse=Distances/temps
print("la vitesse est :{}".format(Vitesse))
print("la vitesse est :{:.2f}".format(Vitesse))


# ## Exercice 2 :

# In[22]:


premierNumero=int(input("donner le premier nombre entier :"))
print(premierNumero)
deuxiemeNumero=int(input("donner le premier nombre entier :")) 
print(deuxiemeNumero)
helper=premierNumero
premierNumero=deuxiemeNumero
deuxiemeNumero=helper
print("le premier numero est : {} - le deuxieme numero est : {}".format(premierNumero,deuxiemeNumero))


# ## Exercice 3 :

# In[28]:


premiereNote=int(input("donner la premiere note :"))
premierCoef=int(input("donner le Queffition de la note saisi :"))
deuxiemeNote=int(input("donner la deuxieme note :"))
deuxsimeCoef=int(input("donner le deuxieme Queffition :"))
troisiemeNote=int(input("donner la troisieme note :"))
troisiemeCoef=int(input("donner le troisieme Queffition :"))
moyenne =float(((premiereNote * premierCoef)+(deuxiemeNote * deuxsimeCoef) + (troisiemeNote * troisiemeCoef))/(premierCoef+deuxsimeCoef+troisiemeCoef)) 
print("la moyeene est : {:.2f}".format(moyenne))


# <Center><h1>Atelier 2 :</h1></center>

# ## Exercice 1 :

# In[41]:


from math import sqrt
number=float(input("donner un nombre :"))
if number>=0:
    racine=sqrt(number)
    print("la racine carré de {} est : {}".format(number,racine))
else:
    print("le nombre doit etre positif ou null")
    


# ## Exercice 2 (premiere Cas):

# In[47]:


premierMot=input("donner le premier Mot :")
deuxiemeMot=input("donner le deuxieme Mot :")
if premierMot<deuxiemeMot :
    print("1-{}\n2-{}".format(premierMot,deuxiemeMot))
else:
    print("1-{}\n2-{}".format(deuxiemeMot,premierMot))


# ## Exercice 2 (2eme Cas):

# In[57]:


premierMot=input("donner le premier Mot :")
deuxiemeMot=input("donner le deuxieme Mot :")
res=print("1-{}\n2-{}".format(premierMot,deuxiemeMot)) if premierMot<deuxiemeMot else print("1-{}\n2-{}".format(deuxiemeMot,premierMot))


# ## Exercice 3 (Solution dans R):

# In[82]:


from math import sqrt
a=float(input("donner a :"))
b=float(input("donner b :"))
c=float(input("donner c :"))
if a==0 :
    print("a doit etre nombre réel non null")
else :
    delta=(b**2)-(4*a*c)
    if delta==0 :
        print("l'equation a une seul solution dans R : {}".format(-b/(2*a)))
    elif delta>0 :
        print("l'equation a duex solutions dans R : {:.2f} et {:.2f}".format(((-b)-sqrt(delta))/(2*a),((-b)+sqrt(delta))/(2*a)))
    else :
        print("l'equation n'a pas des solution sur R")


# ## Excercice 3 (Solution dans C) :

# In[94]:


from math import sqrt
from cmath import *
a=float(input("donner a :"))
b=float(input("donner b :"))
c=float(input("donner c :"))
if a==0 :
    print("a doit etre nombre réel non null")
else :
    delta=(b**2)-(4*a*c)
    if delta==0 :
        print("l'equation a une seul solution dans C : {}".format(-b/(2*a)))
    elif delta>0 :
        print("l'equation a duex solutions dans C : {:.2f} et {:.2f}".format(((-b)-sqrt(delta))/(2*a),((-b)+sqrt(delta))/(2*a)))
    else :
         print("l'equation a duex solutions dans C : {:.2f} et {:.2f}".format(complex(-b,sqrt(-delta))/(2*a),complex(-b,-sqrt(-delta))/(2*a)))


# ## Exercice 4 :

# In[109]:


pSeuil,vSeuil=2.3,7.41
pression=float(input("donner la pression :"))
volume=float(input("donner le volume :"))
if pression>pSeuil and volume>vSeuil:
    print("arret immediat")
elif  volume<vSeuil and pression>pSeuil:
    print("plaise augmente le volume de l'enciente")
elif volume>vSeuil:
    print("plaise diminue le volume de l'enciente")
else :
    print("tous va bien")


# <Center><h1>Atelier 3 :</h1></center>

# ## Exercice 1:

# In[113]:


n=int(input("donner n :"))
s=0
for i in range(0,n+1) :
    s+=i
print("la somme de {} jusqu'à {} est : {}".format(0,n,s))


# ## Exercice 2 :

# In[115]:


n=int(input("donner n :"))
m=int(input("donner m :"))
s=0
for i in range(n,m+1) :
    s+=i
print("la somme de {} jusqu'à {} est : {}".format(n,m,s))


# ## Exercice 3:

# In[124]:


n=int(input("donner n :"))
f=1
for i in range (n,1,-1) :
    f*=i;
print("le factoriel de {} est : {}".format(n,f))


# ## Exercice 4:

# In[122]:


n=int(input("donner n :"))
m=int(input("donner m :"))
s=0
for i in range(n,m+1):
    if i%2!=0 :
        s+=i
print("la somme des nombres impaire entre {} et {} est : {}".format(n,m,s))


# ## Exercice 5:

# In[123]:


n=int(input("donner n :"))
s=0
for i in range(1,n+1) :
    s+=i**2
print("la somme est : {}".format(s))


# ## Exercice 6:

# In[125]:


n=int(input("donner n :"))
s=0
for i in range(1,n+1) :
    s+=((-1)**i)*(i**2+i)
print("la somme est : {}".format(s))


# ## Exercice 7

# In[161]:


x=float(input("donner un nombre de x entre 0 et 1 :"))
while x<=0 or x>=1:
    print("donner un nombre de x entre 0 et 1 :")
n=int(input("donner un nombre de n :"))
somme=0
for i in range(n+1) :
    somme+=x**i
resultat=1/(1-x)
print("la somme de est :{:.2f} = {}".format(somme,resultat))

    


# ## Exercice 8 :

# In[357]:


from math import*
n=int(input("donner un nombre de n:"))
somme=0
produit=1
for i in range(1,n+1):
    somme+=1/(i**2)
for i in range(1,n+1):
    produit*=(4*(i**2))/((4*(i**2)-1))
pi=sqrt(somme*6)
Pi=produit*2
print("la résultat de π est : {}".format(pi))
print("la résultat de π est : {}".format(Pi))


# ## Exercice 9 (la méthode des réctangles) :

# In[336]:


def Somme( a , b , n ) :
    h= (b-a )/n
    somme=0
    for i in range (n):
        xi=a+((i*h)/2)
        xj=a+(((i+1)*h)/2)
        x=(xi+xj)/2
        somme+=(xj-xi) * f (x)
    return somme
def f(x):
    return x**2 #proposons que f(x)=x**2
n=int(input("donner un nombre de n:"))
a=float(input("donner un nombre de a:"))
b=float(input("donner un nombre de b:"))
print(" d'aprés la méthode de réctangle I={}".format(Somme(a,b,n)))


# ## ## Exercice 9 (la méthode de trapèzes) :

# In[337]:


def Somme( a , b , n ) :
    somme=0
    h=(b-a)/n
    for i in range(1,n,2) :
        xi=a+((i*h)/2)
        somme+=f(xi)
    x=((f(a)+f(b))/2)
    return (h*x)+(h*somme)
def f(x):
    return x**2  #proposons que f(x)=x**2
n=int(input("donner un nombre de n:"))
a=float(input("donner un nombre de a:"))
b=float(input("donner un nombre de b:"))
print("d'aprés la méthode de trapèzes I={}".format(Somme(a,b,n)))


# ## Exercice 9 (la méthode de simpson) :

# In[338]:


def Somme( a , b , n ) :
    somme=0
    somme1=0
    h=(b-a)/n
    for i in range(1,n,2) :
        xi=a+((i*h)/2)
        xj=a+(((i+1)*h)/2)
        somme+=f(xi)
    for i in range(0,n,2) :
        xi=(a+((b-a)*i)/(2*n))
        xj=(a+((b-a)*(i+1))/(2*n))
        somme1+=f(xi)
    return (h/6)*(f(a)+f(b)+(4*somme)+(2*somme1))
def f(x):
    return x**2  #suposons que f(x)=x**2
n=int(input("donner un nombre de n:"))
a=float(input("donner un nombre de a:"))
b=float(input("donner un nombre de b:"))
print("d'aprés la méthode de simpson I={}".format(Somme(a,b,n)))

