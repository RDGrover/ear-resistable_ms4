# Ear-resistable_ms4

[Live website link here](https://ear-resistable.herokuapp.com/)

## UX 

### 1.1 Overview

* When beginning the project I knew I wanted to create an e-commerce website to showcase the earrings my partner has been making over lockdown. I like the idea of showcasing her products, but since she does not want to make her own website I wanted to use this project to display her work. I wanted to create a simple e-commerce website inspired by small businesses with a simple but bright colour scheme and minimalistic style. I wanted the website not to overshadow the products. The store is divided into several categories which each contain multiple products, they are:
    * Single-Piece Earrings
    * Multi-Piece Earrings
    * Deals 
    * Clearance 
    * Summer Collection
* Each product has seven fields which help to make each product unique, they are:
    * Category
    * Name 
    * Sku
    * Description
    * Price
    * Rating 
    * Image

### 1.2 Project Goals

* The website is designed to look inviting but not overwhelming to allow the products to be the main draw. It has all the functionality you would expect from any e-commerce website, big or small. It also has the aesthetic of the website of a smaller business to appeal to people looking to shop smaller and more locally instead of supporting larger companies.

### 1.3 User Goals

* A user would want a simple homepage which is clear and easy to navigate.
* A user would want to be able to search for specific products.
* A user would want to be able to search in specific categories for desired products.
* A user would want to be aware of any new products or special deals.
* A user would want to be able to register an account to keep track of products in their basket and purchases. 
* A user would want to be able to login to their account and logout when they are finished.
* A user would want their cart to be updated as they add products so what they are purchasing is visible and the price is updated.

## User Stories
* As a user I would like to be able to view all products without needing to sign up for an account.
* As a user I would like to be able to access all products from the home page.
* As a user I would like to be able to access all products from any other page on the website.
* As a user I would like to be able to search for specific products if there is a particular product I am looking for.
* As a user I would like to be able to navigate back to the home page from anywhere on the sight by clicking the logo.
* As a user I would like to be able to access individual categories.
* As a user I would like to be able to access multiple categories at once.
* As a user I would like to be able to access all categories at once.
* As a user I would like to be able to select a product and view additional details and be able to purchase that product.
* As a user I would like to see what products are currently in my shopping bag after adding a new one.
* As a user I would like to be able to change the quantity of items within the bag, including removing the objects from the bag.
* As a user I would like to be able to create an account.
* As a user I would like to be able to sign-in to an existing account.
* As a user I would like to be able to view my order history if I have already placed an order.
* As a user I would like to have my personal information regarding shipping and billing saved if logged in.
* As a user I would like to receive a confirmation email after placing an order.
* As a user I would like to see an order summary form after completing my order.
* As a user I would like to see a blog featuring news from the site owners and reviews from other users.
* As a user I would like to see other user's comments on those blog posts.
* As a user I would like to be able to make comments on existing blog posts.

* As a website owner I would like to be able to add new products.
* As a website owner I would like to be able to edit existing products.
* As a website owner I would like to be able to delete existing products.

## Features

### 2.1 Navigation Bar

* The Navbar is consistent across ever page of the site with the same colour scheme and the same functionality. 
* The logo in the top corner will always link back to the home page, allowing the user easily navigate back to the home page.
* The Navbar contains a search bar which will allow the user to search for keywords which appear in product name or description. 
* Underneath the search bar there are dropdown boxes which act as category selectors and will filter products based on the selected attributes.
* The My Profile button allows the to access their own profile and view their previous orders as well as set a default address for the user.
* The cart symbol in the corner has an adaptive number underneath it which updates to show an accurate value to the users selected products, including product price and delivery cost. The cart will also change from a muted grey to black when any products have been added increasing the base value above 0.00. 

### 2.2 Search Bar

* The search bar is a simple search function which is easy to navigate for the user.
* Entering a search term will display the products whose description or name contain the search term.
* This will filter all products regardless of category, so long as they contain the search term within their description or name.

### 2.3 Category Selection

* The user will also be able to use the category selection beneath the search bar.
* These categories will narrow down the products into one or multiple categories which are grouped together. In 'Classic Earrings' there are two subcategories of 'Single-Piece Earrings' and 'Multi-Piece Earrings' which can be displayed individually or together by selecting 'All Earrings'. In 'Offers' there are three subcategories of 'Summer Collection', 'Deals' and 'Clearance' which can be displayed individually or together by selecting 'All Offers'. Within 'All Items' all products will be displayed within a secondary filter which can be applied from the dropdown box including: 'By Price High-Low', 'By Price Low-High' and 'By Rating'. All of these filters can be applied to any products pages using another dropdown box present at the top of each product page.

### 2.4 Product Details

* Each product will link to its own product details page. The user is able to arrive at the product details page in one of three ways, by either selecting the product image, the product name or by clicking the more info button.
* The user will be able to see the product image as well as more information about each product. The user is also given the option to add the product to their bag and select the quantity they would like to add. 

### 2.5 Adding Products to Shopping Bag

* The user can access product details by selecting either, the product image, the product name or the more info button. From the product details page each item can be added to the user's bag.
* The user has the option to select the desired quantity using the provided + and - buttons, or by typing in their own number provided it falls between 1 and 99. 
* The user can then add the product to their bag to be checked out.

### 2.6 Shopping Bag

* The bag has responsive pricing so that when a new item is added to the bag the amount displayed underneath it is changed to the grand total, which is the delivery and order total added together. 
* When a new item is added to the bag a small window is displayed showing the user the current contents of the bag. 
* Selecting the bag button will show the user all the items with the bag and their quantities as well as displaying each products individual prices and their total at the bottom of the page, including the delivery cost if one applies. The user will also be shown the button which will take them to the secure checkoutpage to allow them to purchase the products.

### 2.7 Profile Page

* The user will be able to see the My Account button from all pages in the navbar. Selecting the button will give an unauthenticated user the option to either login or signup for an account. Clicking on either will bring the user to one of the forms which will prompt them for username and password if logging in, or username, email and password for signing up.
* For an authenticated user the my account page will display a profile which contains the users default fields including phone number and address. The profile page will also show the user's order history if they have already ordered products.
* If the user is a superuser then an additional option of product management will appear, allowing the user admin capabilites to manage products. This allows them to add, update or delete products from the store.

## Wireframes

## Technology Used
* HTML5 - The project uses HTML templates throughout.
* CSS3 - The project uses CSS for styling HTML elements.
* JavaScript - The project uses JavaScript for responsive elements mostly in the navbar.
* jQuery - The project uses jQuery to configure interactive JavaScript features.
* Python - The project uses Python to run the application.
* Django - The project uses Django as a framework to build apps for project.
* Google Fonts - The project uses Google Fonts to improve the text of the project.
* Font Awesome - The project uses Font Awesome to illustrate particular functions througout the project.
* Bootstrap - The project uses Bootstrap as a framework for layout, styling and responsive elements.
* Stripe - The project uses Stripe as a payment management system. 
* GitHub - The project uses a GitHub reposistory to store the project and for version control.
* GitPod - The project uses GitPod as a terminal to build the website.
* Git - The project uses Git to save the project and push the project into the GitHub repository.
* Heroku - The project was deployed using Heroku.
* AWS - The project's static and media files were loaded onto the Heroku app using Amazon Web Services.


## Apps
* ear-resistable: the project level app.
* bag: for users to place products.
* checkout: to purchase the products (Stripe integrated).
* home: acts as a landing page and anchor point for easy site navigation.
* products: for users to see the products and see a more detailed view of those products, for developers to add, edit or delete products.
* profiles: stores user information and allows them to access order history.

## Testing 

Testing is documented in a seperate file - [testing.md](/testing.md)

## Testing Device Screens

I have tested the website on all the device screens available within the google chrome inspector. The website looks and functions well across all devices.


## Known Bugs 
* Toasts displaying bag contents is cut off on screens with a width of 320px.
* If you enter a comment and leave the fields filled and reload the page the comment will be submitted again. 

## Deployment 

This project was coded using Git and GitPod, the following steps were made to save code and add it to GitHub repository:
 1. Use git add to move code from the workspace to staging area.
 1. Use git commit to save files to a local repository with a message to say what has been changed since previous commit.
 1. Use git push to move the files from a local repository to a remote repository like GitHub.

To deploy this page to Heroku from its [GitHub repository](https://github.com/RDGrover/ear-resistable_ms4), the following steps were taken:
 1. Go to the **Heroku Dashboard** and create a **New App** with the region set to **Europe**.
 1. In the **Settings** tab of your app click **Reveal Config Vars**.
 1. Enter the required environment variables, **IP**, **PORT** and **MONGO_URI**.
 1. In your IDE of choice create a **env.py** containing the **MONGO_URI** and add it to the **.gitignore**.
 1. In your IDE of choice create a **requirements.txt** by using the command **pip freeze -local > requirements.txt**.
 1. In your IDE of choice create a **Profile** by using the command **echo web: python app.py > Procfile**.
 1. Go to the **Deploy** tab and select **Heroku Git**.
 1. In your IDE of choice use the command **git push heroku main**.

Note: The [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) will need to have been downloaded and installed to push from command line.

To deploy locally use the following steps:
 1. Go to [GitHub repository](https://github.com/RDGrover/ear-resistable_ms4)
 1. Click the **Clone** or **Download** button and copy the URL into the address box https://github.com/RDGrover/ear-resistable_ms4.git
 1. Open your terminal and cd to the path where you want to run the clone of the repository.
 1. Type into the terminal git clone https://github.com/RDGrover/ear-resistable_ms4.git.
 1. Once the repository has been downloaded to the designated folder, you can run the files through the browser to check if it is working.

## Code

* Code for the blog and comments apps were based on the apps posted on [django central](https://djangocentral.com)

## Media

* Background image on the home page sourced from [Pexels](https://www.pexels.com/photo/woman-in-pink-dress-holding-brown-bag-standing-1416377/)

