![Mobile and Ipad View](wireframes_mockups/ipadIphone.png?raw=true)
[![Build Status](https://travis-ci.com/Rawa08/FullstackWithDjango.svg?branch=master)](https://travis-ci.com/Rawa08/FullstackWithDjango)

## Live app  [HERE](https://myfragrance.herokuapp.com/)


# My Fragrance
Online Perfume Shop
This project is a solution the last milestone project of the Full Stack Frameworks Diploma course at CodeInstitute.net

## Testing my app
1. Choose products
2. Go to Checkout
3. Register an account
4. Pay with:  
 CreditCard number: 4242 4242 4242 4242  
 CVV: 3 digits   
 Year & Month: Any month in the future   
 Warning: Don't use a real CreditCard   

 # UX
 
The purpose of this website is to provide customers with new and exclusive perfumes. 
Customer can filter out the products depending on gender, see the latest arrivals , write a review and see what others have written about the product.

Site Owner can upload new products through the admin page and find completed orders. 
Site owner have to aprove the reviews in order to be published.

# Features
User are able to search for a perfume, filter out products, add products to cart and change the amount.   
In order to complete the purches the user have to register an account and pay with a creditcard.  
User can choose a product to write a review about.   
User can contact the site owner thru the contact page.

## Features Left to Implement:
I want to give  user the ability to choose between several volume of a product on the product page, 
and the site Owner can add several volume with its associated price for a perfume.

Give Customer ability to order products without a registred account.

# Technologies Used
## Languages : 
HTML5 
CSS 
JavaScript 
Python3 
## Libraries and Frameworks: 
Bootstrap 
jQuery 
Font Awesome 
Django
## APIs
SendGrid - API is used to email users that request a password reset.
Stripe - API to process payments in users subscritions.

## Other Technologies:
Amazon S3 bucket - Static and Media file Storage.
Github - for version control.
GitPod - Online IDE used to develop this project.
Heroku - for deployment.
Postgres - Relational database.


# Testing
The website responsiveness and functionality was tested on:
Safari on apple mobile devices 
(Iphone 8plus, xr, xs, 11 pro Max).
Chrome for android (SM-Galaxy s10+, Huawei p30 pro ).
Chrome for Mac and PC.
Safari for Mac.

All the Links, Buttons, Forms and CRUD functions are manually tested on Desktop and mobile devices.
Travis-CI was used for Continuous Integration. [![Build Status](https://travis-ci.com/Rawa08/FullstackWithDjango.svg?branch=master)](https://travis-ci.com/Rawa08/FullstackWithDjango)

# Credits
I used those codes i learned from codeinstitute.net's Walkthrough projects on the fullstack moduell
https://github.com/Code-Institute-Solutions/AuthenticationAndAuthorisation  
https://github.com/Code-Institute-Solutions/BlogAllAboutIt  

In order to create the review function i  got inspired by https://djangocentral.com/creating-comments-system-with-django/
and used some of their codes.

This website is made with template from https://startbootstrap.com
https://startbootstrap.com/previews/shop-homepage/