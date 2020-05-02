#NAME: Meteumba Lucien 
#September 30
#CPSC-51100, Fall 2018
#PROGRAMMING ASSIGNMENT #4
import pandas as pd

print("CPSC-51100, Fall 1, 2018")
print("NAME: LUCIEN METEUMBA")
print("PROGRAMMING ASSIGNMENT #4")
print ""

a=b=c=d=f=0;          #the number of rating for respectively A, B,C,D,F
coup_a=sed_a=suv_a=0; # number of coupe,sedan and suv for the rating A
coup_b=sed_b=suv_b=0; # number of coupe, sedan and suv for the raing B
coup_c=sed_c=suv_c=0; # number of coupe, sedan and suv for the raing C
coup_d=sed_d=suv_d=0; # number of coupe, sedan and suv for the raing D
coup_f=sed_f=suv_f=0; # number of coupe, sedan and suv for the raing F
feature= ['make','model','type','rating']
df=pd.DataFrame([]) #we initialize our data frame
df=df.T #We transpose the data frame 
df2=pd.DataFrame([]) 
k = int(raw_input("Enter the number of car instances : "))

#asks the user to enter the following fields: make, model, type, rating. Save the feature values for each car in a DataFrame object.
for i in range (k):
    p=map(str,raw_input("Enter the make,model,type,rating: ").split(','))
    s=pd.Series(p, index=feature)
    df2 = pd.DataFrame(s)
    df2=df2.T
    df=df.append(df2, ignore_index=True)    
    
    
#Displays the resulting DataFrame
print(df)
print("\n")

'''compute the number of rating and compute the number of instance
with one of these feature: coupe, sedan, suv and one of these feature: A, B, C, D, F''' 
for i in range (k):
    if p[3]=='A':
        a=a+1  
        if p[2]=='coupe':
            coup_a=coup_a + 1
        if p[2]=='sedan':
            sed_a=sed_a+1   
        if p[2]=='suv':
            suv_a=suv_a+1 
                          
    if p[3]=='B':
        b=b+1
        if p[2]=='coupe':
            coup_b=coup_b + 1
        if p[2]=='sedan':
            sed_b=sed_b+1   
        if p[2]=='suv':
            suv_b=suv_b+1
            
    if p[3]=='C':
        c=c+1
        if p[2]=='coupe':
            coup_c=coup_c + 1
        if p[2]=='sedan':
            sed_c=sed_c+1   
        if p[2]=='suv':
            suv_c=suv_c+1   
            
    if p[3]=='D':
        d=d+1
        if p[2]=='coupe':
            coup_d=coup_d + 1
        if p[2]=='sedan':
            sed_d=sed_d+1   
        if p[2]=='suv':
            suv_d=suv_d+1
            
    if p[3]=='F':
        f=f+1
        if p[2]=='coupe':
            coup_f=coup_f + 1
        if p[2]=='sedan':
            sed_f=sed_f+1   
        if p[2]=='suv':
            suv_f=suv_f+1       
    
         
# Computes the probability of each rating and outputs to the screen.              
if a>0:
    print "Prob(rating=A) =", "%.6f" %  float(a/float(k))
    
if b>0:
    print "Prob(rating=B) =", "%.6f" %  float(b/float(k))
        
if c>=1:
    print "Prob(rating=C) =", "%.6f" %  float(c/float(k))
    
if d>0:
    print "Prob(rating=D) =", "%.6f" %  float(d/float(k))
    
if f>0:
    print "Prob(rating=F) =", "%.6f" %  float(f/float(k))
    
print("\n")

#For each type, computes the conditional probability of that type, given each of the ratings
#Displays the conditional probabilities to the screen.
if (a>0):
    if coup_a>0:
        print "Prob(type=coupe|rating=A) =", "%.6f" %  float(coup_a/float(a))
    if sed_a>0:
        print "Prob(type=sedan|rating=A) =", "%.6f" %  float(sed_a/float(a))
    if suv_a>0:
        print "Prob(type=suv|rating=A) =", "%.6f" %  float(suv_a/float(a))
    
if b>0:
    if coup_b>0:
        print "Prob(type=coupe|rating=B) =", "%.6f" %  float(coup_b/float(b))
    if sed_b>0:
        print "Prob(type=sedan|rating=B) =", "%.6f" %  float(sed_b/float(b))
    if suv_b>0:
        print "Prob(type=suv|rating=B) =", "%.6f" %  float(suv_b/float(b))
    
if c>0:
    if coup_c>0:
        print "Prob(type=coupe|rating=C) =", "%.6f" %  float(coup_a/float(c))
    if sed_c>0:
        print "Prob(type=sedan|rating=C) =", "%.6f" %  float(sed_a/float(c))
    if suv_c>0:
        print "Prob(type=suv|rating=C) =", "%.6f" %  float(suv_a/float(c))
    
if d>0:
    if coup_d>0:
        print "Prob(type=coupe|rating=D) =", "%.6f" %  float(coup_d/float(d))
    if sed_d>0:
        print "Prob(type=sedan|rating=D) =", "%.6f" %  float(sed_d/float(d))
    if suv_d>0:
        print "Prob(type=suv|rating=D) =", "%.6f" %  float(suv_d/float(d))
    
if f>0:
    if coup_f>0:
        print "Prob(type=coupe|rating=F) =", "%.6f" %  float(coup_f/float(f))
    if sed_f>0:
        print "Prob(type=sedan|rating=F) =", "%.6f" %  float(sed_f/float(f))
    if suv_f>0:
        print "Prob(type=suv|rating=F) =", "%.6f" %  float(suv_f/float(f))
