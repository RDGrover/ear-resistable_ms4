# Testing

## User Story Testing 

### As a user I would like to be able to view all products without needing to sign up for an account.

1. From the home page there are categories available for user selection.
1. Once one of those categories has been selected the user may view all the products in that category.
1. The user does not need to have an account to view the products

Steps Taken:

* Go to Ear-resistable website- https://ear-resistable.herokuapp.com/
* Wait for page to load.
* Observe the categories along the bottom of the header in desktop view and on mobile view in the navbar toggler menu.
* After selecting a category a dropdown will appear where you can see all the products within that category.

### As a user I would like to be able to access all products from the home page.

1. From the home page all categories are accessible on both mobile and desktop view.
1. Each category can be selected, including multiple categories at once, and all the products in the selected category will be displayed.

Steps Taken: 

* Select the 'All Items' category in the header. 
* The dropdown box will display 'By Price Low-High', 'By Price High-Low', 'By Rating' and 'All Items'.
* Select 'All Items'.
* Once page has loaded all products will be displayed.

### As a user I would like to be able to access all products from any other page on the website.

1. The header of the site is consistent across all pages of the site whether in mobile view or desktop view.
1. The header contains the links to all product categories and their pages.

Steps Taken:

* From any page on the website select the 'All Items' category in the header. 
* The dropdown box will display 'By Price Low-High', 'By Price High-Low', 'By Rating' and 'All Items'.
* Select 'All Items'.
* Once page has loaded all products will be displayed.

### As a user I would like to be able to search for specific products if there is a particular product I am looking for.

1. Within the header there is a search bar, which is compressed into an icon in the mobile view.
1. Searching within this will allow the user to search for specific key words within either the name or the description of the product.

Steps Taken:

* Click on the search bar, or the logo in mobile view, the bar can now be typed in.
* Type the word 'blue' to search for any blue earrings. 
* All earrings with blue are displayed. 

### As a user I would like to be able to navigate back to the home page from anywhere on the sight by clicking the logo.

1. The logo is present in the top left corner of the website on every page in the desktop view.
1. Clicking this logo will bring the user back to the home page.
1. On mobile devices the logo is replaced by a simple link which links to the home page.

Steps Taken:

* From any page on the website click the logo, or on mobile devices select the home button from the dropdown box.
* Wait for the page to load.
* The home page will be displayed.

### As a user I would like to be able to access individual categories.

1. Selecting the categories from the header allows you to access the categories and display multiple categories at once.
1. Within that menu the user can also display individual categories.

Steps Taken:

* From any page on the website observe that there are categories in the page header.
* Select 'Classic Earrings' and see the three dropdown option 'Single-Piece Earrings', 'Multi-Piece Earrings' and 'All Earrings'. 
* Select 'Single-Piece Earrings' and all products in that category are displayed. 

### As a user I would like to be able to access multiple categories at once.

1. Selecting the categories from the header allows you to access the categories and display multiple categories at once.
1. Within that menu the user can also display individual categories.

Step Taken:

* From any page on the website observe that there are categories in the page header.
* Select 'Classic Earrings' and see the three dropdown option 'Single-Piece Earrings', 'Multi-Piece Earrings' and 'All Earrings'. 
* Select 'All Earrings' and all products in 'Single-Piece Earrings' and 'Multi-Piece Earrings' are displayed.
* Observe at the top of the page that both categories are printed out to show they are both being displayed.

### As a user I would like to be able to access all categories at once.

1. Selecting the categories from the header allows you to access the categories and display multiple categories at once.
1. Within that menu the user can also display individual categories.
1. The All Items category will display everything in all the other categories

Steps Taken: 

* From any page on the website observe that there are categories in the page header.
* Select 'All Items' and see the four dropdown option 'By Price Low-High', 'By Price High-Low', 'By Rating' and 'All Items'. 
* Select 'All Items' and all products in 'Single-Piece Earrings', 'Multi-Piece Earrings', 'Summer Collection', 'Clearance' and 'Deals' are displayed.
* Observe at the top of the page that all categories are printed out to show they are all being displayed.

### As a user I would like to be able to select a product and view additional details and be able to purchase that product.

1. From any product page all products have three link which will take the user to the product detail page.
1. This allows users to effectively click any part of the product to be able to access that products detail page.

Steps Taken:

* From the product page navigate to any product.
* Observe that each product has an image, a name and a more info button.
* Select any of these.
* Observe you are now on the details page.

### As a user I would like to see what products are currently in my shopping bag after adding a new one.

1. A toast is in place to notify the user whenever a new item is added to their bag which displays the contents of the bag including the new item.
1. This provides the user with updated information about their bag without them having to open it.

Steps Taken: 

* Select any product from any of the pages.
* Select the product's name, image or more info button to access the details page.
* From the details page add the product to your bag by selecting the secure checkout button.
* Observe a notification appear beneath the shopping bag displaying the product just added and any others already in the bag.

### As a user I would like to be able to change the quantity of items within the bag, including removing the objects from the bag.

1. There are several options for editing the amount of the product in the bag, or remove them entirely.
1. The quantity button can be changed to any number including 0 which can then be updated and if it is on 0 the product will be removed.
1. There is also a remove button which will completely remove the product regardless of the quantity.

Step Taken:

* From any page select the bag logo in the top right of the page, that already has products in it.
* Select the secure checkout button and wait for the bag to load.
* Notice the product has a quantity already assigned to it.
* Notice there is a - button to lower the quantity and a + button to increase the quantity. 
* Observe that changing the assigned quantity and clicking update will change the amount and total at the bottom of the page will change to reflect the new price.
* Observe that clicking the remove button will completely remove the product from the bag.

### As a user I would like to be able to create an account.

1. Creating an account will allow the user to keep track of their orders and have their shipping details saved in the checkout.

Steps Taken:

* From any page on the website select the My Account link in the header.
* Two options with appear in the dropdown box if you are not logged in to an account, 'Sign Up' and 'Login'.
* Clicking 'Sign Up' will take you to a form.
* Observe that there is a field that requires an email address, then confirmation of that email address, a username, a password and confirmation of that password.
* Enter the required fields correctly and observe you are redirected to the Login page.
* Enter the username and password that was just created into the login fields.
* Observe being signed in to the account just created.

### As a user I would like to be able to sign-in to an existing account.

1. If the session expires or you have multiple people using the same device on the website then it is essential to be able to login to different accounts.
1. Logging in to an account is located in the same place as creating a new accont.

Steps Taken:

* From any page on the website select the My Account link in the header.
* Two options with appear in the dropdown box if you are not logged in to an account, 'Sign Up' and 'Login'.
* Clicking 'Login' will take you to a form.
* Observe a form with two fields for username or email and password.
* Enter the fields as they correspond to an existing user's details.
* Observe being signed in to an existing account.

### As a user I would like to be able to view my order history if I have already placed an order.

1. After creating an account the user will be able to view their order history and access the order information.
1. This is for the user's benefit to be able to see their history and retrieve order numbers and check the order's contents.

Steps Taken:

* Login to an existing account or create a new one.
* Navigate to the the My Account in the header.
* Two options with appear in the dropdown box if you are not logged in to an account, 'Profile' and 'Logout'.
* Clicking 'Profile' will take you to a new page.
* Observe that on the right hand side of the page their will be displayed an order history if the account has already placed an order.

### As a user I would like to have my personal information regarding shipping saved if logged in.

1. Saving previously entered information will make the user experience much easier as it prevents needless repitition.
1. This will make purchasing easier for the user and make them more likely to buy additional products.

Step Taken:

* Login to an account.
* Navigate to the products page and place an item in your bag.
* Go through to the checkout and purchase the item.
* Enter your shipping details and complete purchase.
* Navigate to another product and add it to your bag.
* Navigate to the bag and go to secure checkout.
* Observe that the order details previously entered have been saved.

### As a user I would like to receive a confirmation email after placing an order.

1. Confirmation emails allow for users to be given all their order information in a way that is more accessible to them than the website's profile page. 

Steps Taken:
* Login to an account.
* Navigate to the products page and place an item in your bag.
* Go through to the checkout and purchase the item.
* Enter your shipping details and complete purchase.
* Navigate to the email account that you used to create your website account.
* Observe a confirmation email sent by the website with your order number included.  

### As a user I would like to see an order summary form after completing my order.

1. This ensures the user knows all the products they have purchased and the amount.
1. This is essential for users if there is an issue with their order so they can show the issue they are having.

Steps Taken: 
* Login to an account.
* Navigate to the products page and place an item in your bag.
* Go through to the checkout and purchase the item.
* Enter your shipping details and complete purchase.
* Observe that there is a summary of the order displayed on the page.

### As a user I would like to see a blog featuring news from the site owners and reviews from other users.

1. The blog acts as a way of store owners communicating with their users.

Steps Taken: 
* Navigate to the footer and observe the blog button.
* Select the blog button.
* Observe the blog load up with all available posts.

### As a user I would like to see other user's comments on those blog posts.

1. Comments are a way of the user then communicating back to the store owners in regards to their blog posts. 

Steps Taken:
* Navigate to the footer and observe the blog button.
* Select the blog button.
* Observe the blog load up with all available posts.
* Select the Read More button.
* Scroll down the screen and observe all comments associated with that blog post.

### As a user I would like to be able to make comments on existing blog posts.

1. The ability to comment allows the user to feel more involved with news from the website.

Steps Taken:
* Navigate to the footer and observe the blog button.
* Select the blog button.
* Observe the blog load up with all available posts.
* Select the Read More button.
* Scroll down the screen and observe a form which will allow you to make a comment on that blog post.

### As a website owner I would like to be able to add new products.

1. Adding products is an essential part of managing the website. 
1. The functionality of adding it outside the django admin.

Steps Taken: 
* Login as a superuser.
* Navigate to My Account in the header.
* See a dropdown menu with three items appear 'Product Management', 'Profile' and 'Logout'.
* Select 'Product Management'.
* Observe the form to add a new product to the database.
* Fill out the required fields and observe the new product which has been added to the database.

### As a website owner I would like to be able to edit existing products.

1. Editing products is an essential part of managing the website. 
1. The functionality of adding it outside the django admin.

Steps Taken: 
* Login as a superuser.
* Select a product and navigate to its product detail page.
* Observe that there is an edit button on the right of the product image.
* Select the edit button.
* Observe a form appearing with the fields already filled out with the details of the project which can be changed. 
* Change one of the fields and select Save Changes.
* Observe the changed field saved into the product on the website.

### As a website owner I would like to be able to delete existing products.

1. Deleting products is an essential part of managing the website. 
1. The functionality of adding it outside the django admin.

Steps Taken: 
* Login as a superuser.
* Select a product and navigate to its product detail page.
* Observe that there is a delete button on the right of the product image.
* Select the delete button.
* Observe the product being removed from the database.