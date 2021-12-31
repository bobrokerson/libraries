# option 1
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

---------------------------------------------
#Option 2

from faker import Faker
import pandas as pd

fake = Faker()
fake = Faker('pl_PL')

def generate_ssns(x):
    output = [{"name":fake.pesel(),
                   "year":fake.year(),
                   "email":fake.email()} for x in range(x)]
    return output


faker = pd.DataFrame(generate_ssns(20))
display(faker)
