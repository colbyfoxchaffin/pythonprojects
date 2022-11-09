import pandas as pd

#Read Salaries.csv as a dataframe called 'sal'
sal = pd.read_csv('pythonprojects\pandas_exercises\Salaries.csv')

#Check the head of the dataframe
print(sal.head(2))

#Find out how many entries there are using the .info() method
print(sal.info())

#Calculate the average base pay
avgBase = sal['BasePay'].mean()
print(avgBase)

#Find the highest amount of overtime pay in the dataset
print(sal['OvertimePay'].max())

#Find the job title of Joseph Driscoll
JDjob = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']
print("Joseph Driscoll's job title is " + JDjob)

#how much does Joseph Driscoll make?
JDcomp = sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']
print(JDcomp)

#What is the name of the highest paid person (including benefits)?
highestComp = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']

print(highestComp)

#What is the name of the lowest paid person (including benefits)?
lowestComp = sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]['EmployeeName']

print(lowestComp)

#What was the average (mean) BasePay of all employees per year? (2011-2014)?

avgBasePay = sal.groupby('Year').mean()['BasePay']

print(avgBasePay)

#How many unique job titles are there?
print("The number of unique job titles is " + str(sal['JobTitle'].nunique()))

#What are the top 5 most common jobs?
mostCommonJobs = sal['JobTitle'].value_counts().head(5)
print(mostCommonJobs)

#How many Job titles were represented by only one person in 2013?
specialJobs = sum(sal[sal['Year'] == 2013]['JobTitle'].value_counts() == 1)

print("The number of jobs that were held by only one person in 2013 was " + str(specialJobs))

#How many people have the word 'Chief" in their job title?
def chief_string(title):
    if 'chief' in title.lower():
        return True
    else:
        return False

print(sum(sal['JobTitle'].apply(lambda x: chief_string(x))))

#Is there a correlation between Length of the Job Title string and the Salary?

sal['title_len'] = sal['JobTitle'].apply(len)
print(sal[['TotalPayBenefits','title_len']].corr())