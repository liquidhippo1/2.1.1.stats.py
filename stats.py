import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# First, split the string on the (hidden characters that indicate) newlines
data = data.splitlines() # we could also do data.split('\n')

# Then, split each item in this list on the commas
# the bracketed expression is a list comprehension
data = [i.split(', ') for i in data] 

# Now, convert create a pandas dataframe
column_names = data[0] # this is the first row
data_rows = data[1::] # these are all the following rows of data
df = pd.DataFrame(data_rows, columns=column_names)

# There's no built-in mode method in Python, so we need scipy.stats


# Convert Alcohol and Tobacco columns to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

#calculate mean
alc_mean = df['Alcohol'].mean() 
tob_mean = df['Tobacco'].mean() 
print "The mean of the alcohol and tobacco is %.2f %.2f" %(alc_mean, tob_mean)

#calculate median
alc_median = df['Alcohol'].median() 
tob_median = df['Tobacco'].median() 
print "The median of the alcohol and tobacco is %.2f %.2f" %(alc_median, tob_median)

#calculate mode
tob_mode = stats.mode(df['Tobacco']) 
alc_mode = stats.mode(df['Alcohol']) 
print "The mode of the alcohol and tobacco is %.2f %.2f" %(float(alc_mode[0]), float(tob_mode[0]))

#calculate the range
alc_range = max(df['Alcohol']) - min(df['Alcohol'])
tob_range = max(df['Tobacco']) - min(df['Tobacco'])
print "The range of the alcohol and tobacco is %.2f %.2f" %(alc_range, tob_range)

#calculate the standard deviation
alc_deviation = df['Alcohol'].std() 
tob_deviation = df['Tobacco'].std() 
print "The deviation of the alcohol and tobacco is %.2f %.2f" %(alc_deviation, tob_deviation)


#calculate the variance
alc_variance = df['Alcohol'].var() 
tob_variance = df['Tobacco'].var() 
print "The variance of the alcohol and tobacco is %.2f %.2f" %(alc_variance, tob_variance)
