import numpy as np
import fetchmaker
# importing the binomial method, and f_oneway, chi2_contingency
from scipy.stats import binom_test, f_oneway, chi2_contingency
# importing the pairwise_tukeyhsd from the statmodels.stats.multicomp
from statsmodels.stats.multicomp import pairwise_tukeyhsd
# different methods
# get_weight, get_tail_length, get_color, get_age, and get_is_rescue

# return the length of the tails of rottweilers
rottweiler_tl = fetchmaker.get_tail_length('rottweiler')
# checking if the values are returned
#print(rottweiler_tl)

# expected rescues = 8%
# finding the number of whippets that are rescued
whippet_rescue = fetchmaker.get_is_rescue('whippet')
#print(whippet_rescue)

# counting the number of non zero values
num_whippet_rescues = np.count_nonzero(whippet_rescue)
# checking the variable
#print(num_whippet_rescues)

# getting the size of the set
num_whippets = np.size(whippet_rescue)
# checking the above term
#print(num_whippets)

# running the binom test
pval = binom_test(num_whippet_rescues, num_whippets, p=0.08)
#print(pval)
# the number of whippets recused does not fall in the significant range, so we reject the null hypothesis

# we will have to run a ANOVA and a Tukey Range test
# first we will run the ANOVA on the weight of the dogs
# weight of whippets
weight_whippets = fetchmaker.get_weight('whippet')
#print(weight_whippets)

# weight of terriers
weight_terriers = fetchmaker.get_weight('terrier')
#print(weight_terriers)

# weight of pitbulls
weight_pitbulls = fetchmaker.get_weight('pitbull')
#print(weight_pitbulls)

# running the ANOVA test
fstats, pval = f_oneway(weight_whippets, weight_terriers, weight_pitbulls)
#print(pval)
# there is a significant difference in the pval, but we do not know which pair is causing it.

# we will run the tukey range test to find out
weights = np.concatenate([weight_whippets, weight_terriers, weight_pitbulls])
# checking the weight
#print(weights)

# now creating the labels for the weights
labels = ['whippet'] * len(weight_whippets) + ['terrier'] * len(weight_terriers) + ['pitbull'] * len(weight_pitbulls)
# checking the output of labels
#print(labels) 
tukey_results = pairwise_tukeyhsd(weights, labels, 0.05)
#print(tukey_results)
# we reject the hypotesis of pitbull and terrier pair
# we reject the hypotesis of terrier and whippet pair

# getting the color of poodle and shihtzu
poodle_colors = fetchmaker.get_color('poodle')
shihtzu_colors = fetchmaker.get_color('shihtzu')

# checking the output for the colors of the respective doggos
#print(poodle_colors)
#print(shihtzu_colors)

color_table = [[np.count_nonzero(poodle_colors == "black"), np.count_nonzero(shihtzu_colors == "black")], [np.count_nonzero(poodle_colors == "brown"), np.count_nonzero(shihtzu_colors == "brown")], [np.count_nonzero(poodle_colors == "gold"), np.count_nonzero(shihtzu_colors == "gold")], [np.count_nonzero(poodle_colors == "grey"), np.count_nonzero(shihtzu_colors == "grey")], [np.count_nonzero(poodle_colors == "white"), np.count_nonzero(shihtzu_colors == "white")]]

# checking out the contingency table newly created
#print(color_table)

# applying chi2_contingency to this table
chi2, pval, dof, expected = chi2_contingency(color_table)
if pval < 0.05 :
  return 'There is a significance in color breakdowns'
else:
  return 'There is no significance in color breakdowns'
