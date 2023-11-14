#!/usr/bin/env python
# coding: utf-8

# # Introduction
# 
# Welcome! This analysis explores the statistics of the 2018 Major League Baseball (MLB) season, examining both individual player and team performance. The goal of this project is to ascertain whether there was any correlation between the top players and the most successful teams.

# # Import Libraries
# 

# In[98]:


import requests
import json
import pandas as pd
import numpy as np
from os import path
import matplotlib.pyplot as plt
import seaborn as sns


# # Load Datasets

# There are two datasets used in this project. 
# 
#     1) atbats.csv
# 
#     2) teams.csv

# In[2]:


# Define the file path for the atbats.csv
file_path = r'D:\Code LOU\data_analysis_capstone\Data\atbats.csv'


# In[3]:


# Read the atbats.csv file
data_atbats = pd.read_csv(file_path)


# In[4]:


# The variable data_atbats contains the data from the atbats.csv file
# This will print the first 10 rows of the DataFrame
print(data_atbats.head(11)) 


# In[5]:


# Check the name of each coloumns of dataset 1
print(data_atbats.columns)


# In[6]:


# View the data dimensions: 528 rolls and 23 coloumns 
print(data_atbats.shape)


# I applied the same methodology to load and conduct an initial exploration of the second dataset. This included importing the data, performing preliminary assessments for data quality and structure, and identifying key variables relevant to the analysis objectives.

# In[7]:


# Define the file path for the teams.csv
file_path = r'D:\Code LOU\data_analysis_capstone\Data\teams.csv'


# In[8]:


# Read the atbats.csv file
data_teams = pd.read_csv(file_path)


# In[9]:


# The variable data_players contains the data from the players.csv file
# This will print the first 10 rows of the DataFrame
print(data_teams.head(11)) 


# In[10]:


# View the data dimensions: 30 rolls and 43 coloumns
print(data_teams.shape)


# In[11]:


## Check the name of each coloumns of dataset 2
print(data_teams.columns)


# These two files contain the essential player performance data and team statistics necessary to address our research question. However, they require cleaning and the calculation of key baseball hitter metrics, such as Batting Average (AVG), On-Base percentage (OPS), Runs Batted in (RBI) and more complex calculations like Wins Above Replacement (WAR), among others.

# # Clean and merge the data and calucuate new values

# This initial phase of cleaning we will lay the groundwork for our analysis, enabling us to understand the range, and trends,  within the dataset. By examining the at-bat data, we'll be able to identify any anomalies, patterns, or insights that could influence player evaluations. 

# In[12]:


# initialize empty list to store the atbat data
data_list = []

data = {
    'atbat': r'D:\Code LOU\data_analysis_capstone\Data\atbats.csv'
    }

data_list = []

# loop through each key-value pair in the data dictionary
for key, file_path in data.items():
    # read the CSV file into a dataframe
    atbat_df = pd.read_csv(file_path)
    
    # append the dataframe to data_list
    data_list.append(atbat_df)
    
# concatenate all dataframes in the list into a single atbats dataframe
atbats_df = pd.concat(data_list, ignore_index=True)


# In[13]:


# display first 10 rows the data to examine
atbats_df.head(11)

To enhance clarity and ensure that our dataset is easily understood, it's essential that we update the headers by replacing the current abbreviations with their fully spelled-out terms. Abbreviations, while convenient, can often lead to confusion, especially for those who are not intimately familiar with the context or specifics of baseball statistics. 
# In[14]:


# Dictionary of abbreviations to full terms
abbreviations = {
    'name': 'Player Name',
    'year': 'Year',
    'stint': 'Stint',
    'team': 'Team',
    'lg': 'League',
    'G': 'Games',
    'AB': 'At Bats',
    'R': 'Runs',
    'H': 'Hits',
    '2B': 'Doubles',
    '3B': 'Triples',
    'HR': 'Home Runs',
    'RBI': 'Runs Batted In',
    'SB': 'Stolen Bases',
    'CS': 'Caught Stealing',
    'BB': 'Bases on Balls',
    'SO': 'Strike Outs',
    'IBB': 'Intentional Walks',
    'HBP': 'Hits by Pitch',
    'SH': 'Sacrifice Hits',
    'SF': 'Sacrifice Flies',
    'GIDP': 'Ground Into Double Plays',
    'playerID': 'Player ID'
}

# Rename the columns using the dictionary
atbats_df.rename(columns=abbreviations, inplace=True)

# Display the new column names to verify they've been updated
print(atbats_df.columns)


# Next, We will organizate the dataframe by league, starting with the Ameriacn leagne first.  

# In[15]:


# display the last 15 rows the data to ensure accuracy 
atbats_df.tail(15)


# In[16]:


# Now sort by 'League' with 'AL' first
atbats_df_sorted = atbats_df.sort_values(by='League').reset_index(drop=True)

# Display the sorted DataFrame to verify 'AL' is first
print(atbats_df_sorted[['League', 'Player Name']].head(11))


# In[17]:


# Display the sorted DataFrame to verify 'NL' is last
print(atbats_df_sorted[['League', 'Player Name']].tail(11))


# In[18]:


print(atbats_df.columns)


# In[19]:


# Calculate Batting Average (BA) - Number of Hits divided by the number of At Bats
# We need to ensure we are not dividing by zero, so we use the .replace() method to avoid division by zero errors.
atbats_df['Batting Avg'] = atbats_df['Hits'] / atbats_df['At Bats'].replace(0, np.nan)

# Calculate On-Base Percentage (OBP)
atbats_df['OnBase Percentage'] = (atbats_df['Hits'] + atbats_df['Bases on Balls'] + atbats_df['Hits by Pitch']) / \
                   (atbats_df['At Bats'] + atbats_df['Bases on Balls'] + atbats_df['Hits by Pitch'] + atbats_df['Sacrifice Flies']).replace(0, np.nan)

# Assuming you have some logic to calculate RBI, here we will sum up a few statistics as an example
atbats_df['Runs Batted In Calculated'] = atbats_df['Home Runs'] + atbats_df['Doubles'] + atbats_df['Triples']


# In[20]:


print("RBI, OBP, and BA for each player:")
print(atbats_df[['Player Name', 'Runs Batted In Calculated', 'OnBase Percentage', 'Batting Avg']].head(11))


# In[21]:


#check to ensure that the calucation are infact in the dataframe. 
print(atbats_df)


# Finally, we will rank the players by highest batting average and by leaguage.  remove NaN (players with no infomration)

# In[24]:


# Drop rows where 'BA' is NaN
atbats_df = atbats_df.dropna(subset=['Batting Avg'])

# Drop rows where 'BA' is 0.0
atbats_df = atbats_df[atbats_df['Batting Avg'] != 0.0]

# Sort the DataFrame first by 'League' and then by 'BA'
atbats_df_sorted = atbats_df.sort_values(by=['League', 'Batting Avg'], ascending=[True, False])

# Separate the sorted dataframe into AL and NL players
al_players = atbats_df_sorted[atbats_df_sorted['League'] == 'AL']
nl_players = atbats_df_sorted[atbats_df_sorted['League'] == 'NL']


# In[25]:


# Now print the top AL players by batting average
print("Top AL players by BA:")
print(al_players[['Player Name', 'League', 'Batting Avg']].head(11))


# In[26]:


# Now print the bottom AL players by batting average
print("Top AL players by BA:")
print(al_players[['Player Name', 'League', 'Batting Avg']].tail(11))


# In[27]:


# Define the path where you want to save the CSV file
file_path = r'D:\Code LOU\data_analysis_capstone\Cleaned_Data\cleaned_atbats.csv'

# Save the sorted DataFrame to the CSV file at the specified path
atbats_df_sorted.to_csv(file_path, index=False)

print(f"The cleaned DataFrame has been saved to {file_path}")


# The next step in the process involves the evaluation of the 'teams.csv' dataset. Similar to the at-bat data, we need to ensure the integrity and relevance of the team data. 
# 
# This will involve the removing certain columns that do not offer critical insights for our specific analytical goals. Columns such as 'Innings Pitched Outs','park names' and 'attendance', while potentially interesting, may not contribute to a focused analysis of team performance metrics or player evaluation.

# In[28]:


# Define the file path for the teams.csv
file_path = r'D:\Code LOU\data_analysis_capstone\Data\teams.csv'


# In[29]:


# Read the teams.csv file
data_teams = pd.read_csv(file_path)


# In[30]:


# The variable data_teams contains the data from the teamss.csv file
# This will print the first 10 rows of the DataFrame
print(data_teams.head(11)) 


# In[31]:


# Check the name of each coloumns of dataset 2
print(data_teams.columns)


# In[32]:


# View the data dimensions: 30 rolls and 43 coloumns 
print(data_teams.shape)


# In[33]:


#To enhance the focus and efficiency of our analysis, we will remove unnecessary columns.
# Columns to be removed
columns_to_remove = ['yearID', 'park', 'attendance', 'BPF', 'PPF', 'IPouts', 'SOA']

# Removing the specified columns only if they exist
data_teams = data_teams.drop(columns=[col for col in columns_to_remove if col in data_teams.columns], inplace=False)

# Display the DataFrame columns to verify the changes
print(data_teams.columns)


# In[34]:


# Displaying the first few rows of the modified DataFrame for verification
print(data_teams.head(11))


# In[35]:


# Dictionary of abbreviations to full terms
abbreviations = {
    'lgID': 'League',
    'teamID': 'Team',
    'divID': 'Division',
    'G': 'Games',
    'W': 'Wins',
    'L': 'Losses',
    'AB': 'At Bat',
    'R': 'Runs',
    'H': 'Hits',
    'WCwin': 'Wildcard Win',
    'LgWin': 'League Win',
    'WSwin': 'World Series Win',
    '2B': 'Doubles',
    '3B': 'Triples',
    'HR': 'Home Runs',
    'RBI': 'Runs Batted In',
    'SB': 'Stolen Bases',
    'CS': 'Caught Stealing',
    'BB': 'Bases on Balls',
    'SO': 'Strike Outs',
    'IBB': 'Intentional Walks',
    'HBP': 'Hits by Pitch',
    'SH': 'Sacrifice Hits',
    'SF': 'Sacrifice Flies',
    'RA': 'Runs Allowed',
    'ER': 'Earned Runs',
    'ERA': 'Earned Run Average',
    'CG': 'Complete Games',
    'SHO': 'Shut Outs',
    'SV': 'Saves',
    'HA': 'Hits Allowed',
    'HRA': 'Home Runs Allowed',
    'BBA': 'Bases on Balls Allowed',
    'E': 'Errors',
    'DP': 'Double Plays',
    'FP': 'Fielding Percentage',
    'name': 'Team Name',
}

# Rename the columns in the data_teams DataFrame
data_teams.rename(columns=abbreviations, inplace=True)

# Display the new column names to verify they've been updated
print(data_teams.columns)


# In[36]:


print(data_teams.tail(11))


# In[37]:


#Move the Team Name to the first column on the dataset.
data_teams = data_teams[['Team Name'] + [col for col in data_teams.columns if col != 'Team Name']]

print(data_teams.head())


# In[38]:


data_teams.head(15)


# In[39]:


# Assuming data_teams is the DataFrame you want to save
file_path = r'D:\Code LOU\data_analysis_capstone\Cleaned_Data\cleaned_teams.csv'

# Save the DataFrame to the CSV file at the specified path
data_teams.to_csv(file_path, index=False)

print(f"The cleaned DataFrame has been saved to {file_path}")


# Next, We will merge both of the cleaned datasets. 

# In[40]:


#reinspect the datasets coloumns 
print(data_atbats.columns)
print(data_teams.columns)


# In[41]:


merged_df = pd.merge(data_atbats, data_teams, left_on='team', right_on='Team')

print(merged_df.head())


# # Merge

# In[42]:


# Define the file path where you want to save the merged dataset
file_path = r'D:\Code LOU\data_analysis_capstone\Cleaned_Data\merged_dataset.csv'

# Save the merged DataFrame to a CSV file at the specified path
merged_df.to_csv(file_path, index=False)

# Print a confirmation message
print(f"Merged dataset saved to {file_path}")


# In[43]:


print(list(merged_df.columns))


# # New Measurements

# Grouped Aggregations:
# Perform group-wise analysis by aggregating data based on certain categories. 
# For instance, you could group by 'Team' or 'League' and calculate average runs, hits, or other statistics to compare team or league performance.
# 
# To perform a grouped aggregation analysis on your DataFrame, you can use the groupby method in pandas along with aggregation functions like mean, sum, count, etc. Assuming you want to group by 'Team' or 'League' and calculate average runs, hits, or other statistics, here's how you can do it:

# Teams Status

# In[90]:


# Assuming 'merged_df' is your merged DataFrame
# Group by 'Team' and calculate average runs, hits, and home runs, then round to nearest integer
team_stats = np.round(merged_df.groupby('Team')['Runs', 'Hits', 'Home Runs', '].mean(), 0)

# Display the team statistics
print("Average stats by Team:")
print(team_stats)

# Similarly, group by 'League' and calculate the same statistics, then round to nearest integer
league_stats = np.round(merged_df.groupby('League')['Runs', 'Hits', 'Home Runs' ].mean(), 0)

# Display the league statistics
print("\nAverage stats by League:")
print(league_stats)


# In[48]:


# Sorting the team_stats DataFrame by 'Runs' in descending order
sorted_team_stats = team_stats.sort_values('Runs', ascending=False)

# Creating the bar chart with sorted data
plt.figure(figsize=(10, 6))
sns.barplot(x=sorted_team_stats.index, y=sorted_team_stats['Runs'])
plt.title('Average Runs by Team (Highest to Lowest)')
plt.xlabel('Team')
plt.ylabel('Average Runs')
plt.xticks(rotation=45)
plt.show()


# In[52]:


# Assuming 'merged_df' is your original DataFrame
# Group by 'Team' and calculate average hits, then sort in descending order
team_stats = merged_df.groupby('Team')['Hits'].mean().sort_values(ascending=False)

# Creating the bar chart for average hits
plt.figure(figsize=(10, 6))
sns.barplot(x=team_stats.index, y=team_stats)
plt.title('Average Hits by Team (Highest to Lowest)')
plt.xlabel('Team')
plt.ylabel('Average Hits')
plt.xticks(rotation=45)
plt.show()


# In[82]:


# Assuming 'merged_df' is your original DataFrame
# Group by 'Team' and calculate average hits, then sort in descending order
team_stats = merged_df.groupby('Team')['Home Runs'].mean().sort_values(ascending=False)

# Creating the bar chart for average hits
plt.figure(figsize=(10, 6))
sns.barplot(x=team_stats.index, y=team_stats)
plt.title('Average HRs by Team (Highest to Lowest)')
plt.xlabel('Team')
plt.ylabel('Average HR')
plt.xticks(rotation=45)
plt.show()


# In[85]:


# Assuming 'merged_df' is your original DataFrame
# Group by 'Team' and calculate average hits, then sort in descending order
team_stats = merged_df.groupby('Team')['Wins'].mean().sort_values(ascending=False)

# Creating the bar chart for average hits
plt.figure(figsize=(10, 6))
sns.barplot(x=team_stats.index, y=team_stats)
plt.title('Average Wins by Team (Highest to Lowest)')
plt.xlabel('Team')
plt.ylabel('Wins')
plt.xticks(rotation=45)
plt.show()


# Player stats 

# In[94]:


# Assuming 'merged_df' is your merged DataFrame with 'name' and 'Team' columns

# Group by 'name' (player) and calculate average home runs, then round to nearest integer
player_avg_hr = np.round(merged_df.groupby('name')['R'].mean(), 0)

# Convert player_avg_hr to a DataFrame and reset index
player_avg_hr_df = player_avg_hr.reset_index()

# Merging with original DataFrame to get team names
# Dropping duplicates in the original DataFrame to get unique name-Team pairs
unique_name_team = merged_df[['name', 'Team']].drop_duplicates()

# Merging the average home runs DataFrame with the unique name-Team DataFrame
merged_with_teams = pd.merge(player_avg_hr_df, unique_name_team, on='name')

# Sort by 'HR' (home runs) to get the top ten players
top_ten_players_with_teams = merged_with_teams.sort_values(by='R', ascending=False).head(10)

# Display the statistics for the top ten players along with their team names
print("Top Ten Players with the Most Runs:")
print(top_ten_players_with_teams[['name', 'R', 'Team']])


# In[99]:


# Sample data for demonstration purposes
data = {
    'name': ['Player 1', 'Player 2', 'Player 3', 'Player 4', 'Player 5'],
    'statistic': [40, 35, 30, 25, 20]  # Replace 'statistic' with the relevant measure, e.g., runs, hits, etc.
}

# Creating a DataFrame from the sample data
top_players = pd.DataFrame(data)

# Sizes for the treemap
sizes = top_players['statistic']

# Creating the treemap
plt.figure(figsize=(10, 8))
squarify.plot(sizes, label=top_players['name'], alpha=0.7)
plt.title('Tree Map of Top 5 Players')
plt.axis('off')  # Re


# In[73]:


# Assuming 'merged_df' is your merged DataFrame with 'name' and 'Team' columns

# Group by 'name' (player) and calculate average home runs, then round to nearest integer
player_avg_hr = np.round(merged_df.groupby('name')['HR'].mean(), 0)

# Convert player_avg_hr to a DataFrame and reset index
player_avg_hr_df = player_avg_hr.reset_index()

# Merging with original DataFrame to get team names
# Dropping duplicates in the original DataFrame to get unique name-Team pairs
unique_name_team = merged_df[['name', 'Team']].drop_duplicates()

# Merging the average home runs DataFrame with the unique name-Team DataFrame
merged_with_teams = pd.merge(player_avg_hr_df, unique_name_team, on='name')

# Sort by 'HR' (home runs) to get the top ten players
top_ten_players_with_teams = merged_with_teams.sort_values(by='HR', ascending=False).head(10)

# Display the statistics for the top ten players along with their team names
print("Top Ten Players with the Most Home Runs:")
print(top_ten_players_with_teams[['name', 'HR', 'Team']])


# In[ ]:





# In[76]:


# Assuming 'merged_df' is your merged DataFrame with 'name' and 'Team' columns

# Group by 'name' (player) and calculate average home runs, then round to nearest integer
player_avg_hr = np.round(merged_df.groupby('name')['RBI'].mean(), 0)

# Convert player_avg_hr to a DataFrame and reset index
player_avg_hr_df = player_avg_hr.reset_index()

# Merging with original DataFrame to get team names
# Dropping duplicates in the original DataFrame to get unique name-Team pairs
unique_name_team = merged_df[['name', 'Team']].drop_duplicates()

# Merging the average home runs DataFrame with the unique name-Team DataFrame
merged_with_teams = pd.merge(player_avg_hr_df, unique_name_team, on='name')

# Sort by 'HR' (home runs) to get the top ten players
top_ten_players_with_teams = merged_with_teams.sort_values(by='RBI', ascending=False).head(10)

# Display the statistics for the top ten players along with their team names
print("Top Ten Players with Most RBIs:")
print(top_ten_players_with_teams[['name', 'RBI', 'Team']])


# In[95]:


# Assuming 'merged_df' is your merged DataFrame with 'name' and 'Team' columns

# Group by 'name' (player) and calculate average home runs, then round to nearest integer
player_avg_hr = np.round(merged_df.groupby('name')['H'].mean(), 0)

# Convert player_avg_hr to a DataFrame and reset index
player_avg_hr_df = player_avg_hr.reset_index()

# Merging with original DataFrame to get team names
# Dropping duplicates in the original DataFrame to get unique name-Team pairs
unique_name_team = merged_df[['name', 'Team']].drop_duplicates()

# Merging the average home runs DataFrame with the unique name-Team DataFrame
merged_with_teams = pd.merge(player_avg_hr_df, unique_name_team, on='name')

# Sort by 'HR' (home runs) to get the top ten players
top_ten_players_with_teams = merged_with_teams.sort_values(by='H', ascending=False).head(10)

# Display the statistics for the top ten players along with their team names
print("Top Ten Players with Most RBIs:")
print(top_ten_players_with_teams[['name', 'H', 'Team']])

