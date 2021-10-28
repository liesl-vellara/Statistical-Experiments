import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')

#examining the first few rows of the df
#print(ad_clicks.head())

#which ad platform is getting the most views
most_views = ad_clicks.groupby('utm_source').user_id.count().reset_index()

#inspecting the data frame most_views
#print(most_views)

#create a new column called is_click which is true if ad_click_timestamp is true
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()

#checking on the ad_clicks
#print(ad_clicks)

#calculating the percentile of people that clicked on the ad
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()

#inspecting
#print(clicks_by_source)

#we want to pivot the table
clicks_pivot = clicks_by_source.pivot(columns = 'is_click', index = 'utm_source', values = 'user_id').reset_index()

#inspecting
#print(clicks_pivot)

#create a new column in clicks_pivot called percent_clicked
clicks_pivot['percent_clicked'] = clicks_pivot[True]*100/ (clicks_pivot[True] + clicks_pivot[False])

#inspecting
#print(clicks_pivot)

#check on ad_clicks if the number of experimental_group is the same
df = ad_clicks.groupby('experimental_group').user_id.count().reset_index()

#checking
#print(df)

#group is_clicked and experimental_group then count the user_id
df2 = ad_clicks.groupby(['experimental_group', 'is_click']).user_id.count().reset_index()

#checking
#print(df2)

#pivoting
df2_pivot = df2.pivot(columns= 'is_click', index ='experimental_group', values ='user_id').reset_index()

#inspecting
#print(df2_pivot)

#percentage for True
df2_pivot['percentage_for_true'] = df2_pivot[True] * 100/ (df2_pivot[True] + df2_pivot[False])

#percentage for False
df2_pivot['percentage_for_false'] = df2_pivot[False] * 100/ (df2_pivot[True] + df2_pivot[False])

#difference in percentage
df2_pivot['difference'] = df2_pivot['percentage_for_true'] - df2_pivot['percentage_for_false']

#inspecting
#print(df2_pivot)

#create two dataframe called a_clicks and b_clicks
#print(ad_clicks.head())

#user_id, utm_source, day, ad_click_timestamp, experimental_group, is_click
a_group = ad_clicks[ad_clicks.experimental_group == 'A']
b_group = ad_clicks[ad_clicks.experimental_group == 'B']

#inspecting those df
#print(a_group.head())
#print(b_group.head())

#Grouping a group based on days and if they clicked
a_group_days = a_group.groupby(['day', 'is_click']).user_id.count().reset_index()

#checking on the table
#print(a_group_days.head())

#pivoting the table
a_group_pivot = a_group_days.pivot(columns='is_click', index='day', values='user_id')

#a_group_pivot percentile
a_group_pivot['percent_clicked'] = a_group_pivot[True] *100/ (a_group_pivot[True] + a_group_pivot[False])

#Checking on the group
print(a_group_pivot)

#repeat the process for b_group
#Grouping a group based on days and if they clicked
b_group_days = a_group.groupby(['day', 'is_click']).user_id.count().reset_index()

#checking on the table
#print(b_group_days.head())

#pivoting the table
b_group_pivot = b_group_days.pivot(columns='is_click', index='day', values='user_id')

#a_group_pivot percentile
b_group_pivot['percent_clicked'] = b_group_pivot[True] *100/ (b_group_pivot[True] + b_group_pivot[False])

#Checking on the group
print(b_group_pivot)

#comparing and choosing the better one
difference_df = pd.DataFrame(a_group_pivot['percent_clicked'] - b_group_pivot['percent_clicked'])

#print the difference
print(difference_df)
