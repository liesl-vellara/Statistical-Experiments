import pandas as pd
from scipy.stats import chi2_contingency, binom_test

# loading the csv file
df = pd.read_csv('clicks.csv')
print(df.head())
# user_id: a unique id for each visitor to the FarmBurg site
# ab_test_group: either A, B, or C depending on which group the visitor was assigned to
# click_day: only filled in if the user clicked on a link to purchase

# cleaning the data
df['is_purchase'] = df['click_day'].apply(lambda x: 'Purchase' if pd.notnull(x) else 'No Purchase')

# grouping the data based on is_purchase
purchase_counts = df.groupby(['group', 'is_purchase']).user_id.count().reset_index()
print(purchase_counts)

# A No purchase = 1350
# A Purchase = 316
# B No purchased = 1483
# B Purchased = 183
# C No purchase = 1583
# C Purchased = 83
contingency = [[316, 1350], [183, 1483], [83, 1583]]
chi2, pvalue, dof, expected = chi2_contingency(contingency)
print(pvalue)

is_significant = (True if pvalue < 0.05 else False)
print(is_significant)
# output is true

# checking the number of visitors to the site
num_visits = len(df)
print(num_visits)
# our target per week is to reach $1000 
# Number of burgers to sell at $0.99
sale_099 = 1000/0.99
# chekcing the sales rate of the $0.99 price point
p_clicks_099 = sale_099 / num_visits

# Number of burgers to sell at $1.99
sale_199 = 1000/1.99
# chekcing the sales rate of the $1.99 price point
p_clicks_199 = sale_199 / num_visits

# Number of burgers to sell at $1.99
sale_499 = 1000/4.99
# chekcing the sales rate of the $4.99 price point
p_clicks_499 = sale_499 / num_visits

print("The different rates for different price points are: " + str(p_clicks_099) + ", "  + str(p_clicks_199) + ", " + str(p_clicks_499) + " repectively for the $0.99, $1.99 and the $4.99")

# We want to see if the percent of Group A that purchased an upgrade package is significantly greater than p_clicks_099 (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our target of $1,000).

#runing the Binom test for each group to see if  the observed purchase rate is significantly greater than what we need in order to generate at least $1,000 per week\
# binom_test(purchase, total number of visitor, purchase rate for each price point)
pvalueA = binom_test(316, 1666, p_clicks_099)
print(pvalueA)

pvalueB = binom_test(183, 1666, p_clicks_199)
print(pvalueB)

pvalueC = binom_test(83, 1666, p_clicks_499)
print(pvalueC)
# after seeing the different p values for the different samples, we conclude that the $4.99 is lesser than the pval
# hence if we want to hit our target, we can charge the $4.99 compared to the $0.99 and the $1.99
