# importing scipy with ttest_1samp, ttest_ind (two sample t test), chi2_contingency
from scipy.stats import ttest_1samp, ttest_ind, chi2_contingency
import familiar


# loading the packs that are equal to 'vein'
vein_pack_lifespans = familiar.lifespans(package='vein')

#print(vein_pack_lifespans)

# using one sample ttest to check the pval
tstat, vein_pack_test = ttest_1samp(vein_pack_lifespans, 71)

# using a loop to check the outcome
if vein_pack_test < 0.05:
  print('The Vein Pack Is Proven To Make You Live Longer!')
else:
  print('The Vein Pack Is Probably Good for You Somehow!')

# getting the artery pack
artery_pack_lifespans = familiar.lifespans(package='artery')
# checking if the data is loaded
#print(artery_pack_lifespans)

# we will be running a two sample t test
ttest, package_comparison_results = ttest_ind(vein_pack_lifespans, artery_pack_lifespans)
# checking if the test works
#print(package_comparison_results)

# loop to see if the package is greater than 0.05
if package_comparison_results < 0.05:
  print("the Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is also a great product!")

#total sample size = 200
# number of response 145
# importing the contingency table for iron
iron_contingency_table = familiar.iron_counts_for_package()

# checking if the contingency table works out
#print(iron_contingency_table)

# running the chi2_contingency test
chi2, iron_pval, dof, expected = chi2_contingency(iron_contingency_table)

# checking the pval from the contingency table
#print(iron_pval)

if iron_pval < 0.05:
  print('The Artery Package is proven to make you healthier!')
else:
  print('While we cannot say the artery package will help you, I bet it is nice!')
