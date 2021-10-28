import pandas as pd

#visits lists all of the users who have visited the website
visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
#cart lists all of the users who have added a t-shirt to their cart
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
#checkout lists all of the users who have started the checkout
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
#purchase lists all of the users who have purchased a t-shirt 
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

#inspecting all the df
#print(visits.head(), cart.head(), checkout.head(), purchase.head())

# TYPES OF DATA AVAILABLE IN RESPECTIVE DF
#visits consists of user_id and visit_time
#cart contains the user_id and cart_time
#checkout contains user_id and checkout_time
#purchase contains user_id and purchase_time

#combining visits and cart using left merge
visits_carts_left_merge = pd.merge(visits, cart, how='left')

#checking on that data
#print(visits_carts_left_merge.head())

#how many rows does that dataframe have
#print(len(visits_carts_left_merge))

#how many rows are left null in the cart_time
cart_time_null = visits_carts_left_merge[visits_carts_left_merge.cart_time.isnull()]
#print(cart_time_null)
#inspecting
#print(cart_time_null.count())

#The number of cart_time left empty shows that the item has not been added.

#percent of users not placing a t shirt in their cart
#trying another method to get the percentage using len()
percentage = len(cart_time_null) *100 / len(visits_carts_left_merge)

#checking the percent
#print(str(percentage) + '%')

#left merge for cart and checkout
cart_checkout_left_merge = pd.merge(cart, checkout, how='left')

#checking
#print(cart_checkout_left_merge.head())

#making a new table where the values are null
cart_checkout_null = cart_checkout_left_merge[cart_checkout_left_merge.checkout_time.isnull()]

#checking on the df
#print(cart_checkout_null.head())

#making a formula to check the percentage of users who put items in cart but did not procceed to checkout
percent1 = len(cart_checkout_null) *100 / len(cart_checkout_left_merge)

#checking on the percent
#print(str(percent1) + '%')

#merging all four funnels
all_data = pd.concat([visits, cart, checkout, purchase])

#checking out all_data
#print(all_data.head())

#number of rows the purchase_time was left null
all_data_null_pt = all_data[all_data.purchase_time.isnull()]

#checking
#print(all_data_null_pt.head())

#percentage
percent2 = len(all_data_null_pt) * 100 / len(all_data)

#checking on percent2
#print(str(percent2) + '%')

#comparing the percentage
#print('On comparison of the percentages for various cases, we can see the highest percentage belongs to the process where purchase has not be made. It has the highest percentage of ' + str(percent2) + '%')

#average time from visit to checkout
all_data['time_to_purchase'] = all_data.purchase_time - all_data.visit_time

#examining the results
print(all_data.time_to_purchase.mean())
