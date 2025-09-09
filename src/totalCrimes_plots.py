# Generate barplot and regplot of total crimes per year

import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
df = pd.read_csv("chicago_crime.csv")
# Convert Date column to datetime format
df['DATE'] = pd.to_datetime(df['DATE'])

# Find the earliest date
earliest_date = df['DATE'].min()
# Find the latest date
latest_date = df['DATE'].max()

print(f"Earliest Date: {earliest_date}")
print(f"Latest Date: {latest_date}")

# Earliest Year = 2001
# Latest Year = 2018

# Slice dataframe for each year in timeframe (2001-2018)

# 2001
df_2001 = df[df['DATE'].dt.year == 2001]
list_2001 = df_2001.values.tolist()
crimes_2001 = len(list_2001)

# 2002
df_2002 = df[df['DATE'].dt.year == 2002]
list_2002 = df_2002.values.tolist()
crimes_2002 = len(list_2002)

# 2003
df_2003 = df[df['DATE'].dt.year == 2003]
list_2003 = df_2003.values.tolist()
crimes_2003 = len(list_2003)

# 2004
df_2004 = df[df['DATE'].dt.year == 2004]
list_2004 = df_2004.values.tolist()
crimes_2004 = len(list_2004)

# 2005
df_2005 = df[df['DATE'].dt.year == 2005]
list_2005 = df_2005.values.tolist()
crimes_2005 = len(list_2005)

# 2006
df_2006 = df[df['DATE'].dt.year == 2006]
list_2006 = df_2006.values.tolist()
crimes_2006 = len(list_2006)

# 2007
df_2007 = df[df['DATE'].dt.year == 2007]
list_2007 = df_2007.values.tolist()
crimes_2007 = len(list_2007)

# 2008
df_2008 = df[df['DATE'].dt.year == 2008]
list_2008 = df_2008.values.tolist()
crimes_2008 = len(list_2008)

# 2009
df_2009 = df[df['DATE'].dt.year == 2009]
list_2009 = df_2009.values.tolist()
crimes_2009 = len(list_2009)

# 2010
df_2010 = df[df['DATE'].dt.year == 2010]
list_2010 = df_2010.values.tolist()
crimes_2010 = len(list_2010)

# 2011
df_2011 = df[df['DATE'].dt.year == 2011]
list_2011 = df_2011.values.tolist()
crimes_2011 = len(list_2011)

# 2012
df_2012 = df[df['DATE'].dt.year == 2012]
list_2012 = df_2012.values.tolist()
crimes_2012 = len(list_2012)

# 2013
df_2013 = df[df['DATE'].dt.year == 2013]
list_2013 = df_2013.values.tolist()
crimes_2013 = len(list_2013)

# 2014
df_2014 = df[df['DATE'].dt.year == 2014]
list_2014 = df_2014.values.tolist()
crimes_2014 = len(list_2014)

# 2015
df_2015 = df[df['DATE'].dt.year == 2015]
list_2015 = df_2015.values.tolist()
crimes_2015 = len(list_2015)

# 2016
df_2016 = df[df['DATE'].dt.year == 2016]
list_2016 = df_2016.values.tolist()
crimes_2016 = len(list_2016)

# 2017
df_2017 = df[df['DATE'].dt.year == 2017]
list_2017 = df_2017.values.tolist()
crimes_2017 = len(list_2017)

years = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
             2014, 2015, 2016, 2017]

crimes_by_year = [crimes_2001, crimes_2002, crimes_2003, crimes_2004, crimes_2005, crimes_2006, crimes_2007, 
                     crimes_2008, crimes_2009, crimes_2010, crimes_2011, crimes_2012, crimes_2013, crimes_2014, 
                     crimes_2015, crimes_2016, crimes_2017]

array_crimes_by_year = np.array(crimes_by_year)

mean_crimes = np.mean(array_crimes_by_year)
median_crimes = np.median(array_crimes_by_year)
std_crimes = np.std(array_crimes_by_year)

print(f"Median number of crimes of {median_crimes} from 2001-2017")
print(f"Mean number of crimes of {round(mean_crimes, 2)} with standard deviation of {round(std_crimes, 2)} from 2001-2017")

# Compile all data into Python dictionary for Seaborn plot
total_crime_data = {
    'Year': [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 
             2014, 2015, 2016, 2017],
    'Total Crimes': [crimes_2001, crimes_2002, crimes_2003, crimes_2004, crimes_2005, crimes_2006, crimes_2007, 
                     crimes_2008, crimes_2009, crimes_2010, crimes_2011, crimes_2012, crimes_2013, crimes_2014, 
                     crimes_2015, crimes_2016, crimes_2017]
}

sns.set(rc={'figure.figsize':(10, 6)})

# Seaborn bar plot of total crimes per year, 2001-2017
sns.barplot(x='Year', y='Total Crimes', data=total_crime_data)
plt.title('Total Crimes in Chicago, 2001-2017')
plt.show()

# Seaborn regression plot of total crimes per year, 2001-2017
sns.regplot(x=years, y=crimes_by_year)
plt.title('Total Crimes in Chicago, 2001-2017')
plt.xlabel('Year')
plt.ylabel('Total Crimes')
plt.show()

