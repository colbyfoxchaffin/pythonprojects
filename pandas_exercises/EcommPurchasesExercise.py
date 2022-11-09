import pandas as pd

#Read in the Ecommerce Purchases csv filea and set it to a dataframe called 'ecom'

ecom = pd.read_csv('pythonprojects\pandas_exercises\Ecommerce Purchases.csv')

print(ecom.head(5))

#How many rows and columns are there?

#Rows
print(len(ecom.index))

#Columns
print(len(ecom.columns))

#Both at once
print(ecom.info()) 

#What is the average purchase price?
avgPurchasePrice = ecom['Purchase Price'].mean()
print("The average purchase price is $" + str(avgPurchasePrice))

#What were the highest and lowest purchase prices?
maxPurchasePrice = ecom['Purchase Price'].max()
minPurchasePrice = ecom['Purchase Price'].min()

print(maxPurchasePrice)
print(minPurchasePrice)

#How many people have English as their language of choice on the website?
englishSpeakers = ecom[ecom['Language'] == 'en']['Language'].count()
print(englishSpeakers)

#How many people have the job title "Lawyer"
lawyers = len(ecom[ecom['Job'] == 'Lawyer'].index)
print(lawyers)

#How many people made the purchase during the morning(AM) and how many people made the purchase during afternoon(PM)?

purchases = ecom['AM or PM'].value_counts()
print(purchases)

#What are the 5 most common Job Titles?
commonJobs = ecom['Job'].value_counts().head(5)
print(commonJobs)

#Someone made a purchase that came from Lot:"90 WT", what was the Purchase Price for this transaction?

purchasePrice = ecom[ecom['Lot'] == '90 WT']['Purchase Price']
print(purchasePrice)

#What is the email of the person with the following credit card number? 4926535242672853

ccPerson = ecom[ecom['Credit Card'] == 4926535242672853]['Email']
print(ccPerson)

#How many people have American Express as their Credit Card Provider and made a purchase above $95?

#Using mulitple condition selection
amexAnd95 = ecom[(ecom['CC Provider'] == 'American Express') & (ecom['Purchase Price']> 95)].count()

print(amexAnd95)

#How many people have  credit card that expires in 2025?
expYear = sum(ecom['CC Exp Date'].apply(lambda exp: exp[3:]=='25'))


#What are the top 5 most popular email providers?
emailProviders = ecom['Email'].apply(lambda email: email.split('@')[1]).value_counts().head(5)

print(emailProviders)