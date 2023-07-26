import pandas as pd


people = {
    "first": ["Corey", 'Jane', 'John'], 
    "last": ["Schafer", 'Doe', 'Doe'], 
    "email": ["CoreyMSchafer@gmail.com", 'JaneDoe@email.com', 'JohnDoe@email.com']
}

df = pd.DataFrame(people)



print(df)
print( df['email'])
print(people["email"])
print( df.count() )

print(df[['last', 'email']])

print("df.columns =",df.columns)
print("df.iloc[[0, 1], 2] =",df.iloc[[0, 1], 2])
print("111 =",111)
print("111 =",111)
print("111 =",111)
print("111 =",111)
print("111 =",111)
print("111 =",111)
print("111 =",111)
print("111 =",111)
