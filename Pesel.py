import pandas as pd
from faker import Faker 

fake = Faker('pl_PL')

def generate_ssns(x): 
    number ={}
    for i in range(0,x): 
        number[i] = {}
        number[i]=fake.pesel()
     

    return number
    
df = pd.Series(generate_ssns(10))

dff=pd.DataFrame(df, columns=['Pesel'])

display(dff)
