[View the live project here](https://salon-wholesale-b203aeb779cf.herokuapp.com/)

# Salon365 Wholesales Website

The Salon365 website is a wholesale website that allows users to buy a range of beauty products at a lower cost. To start purchasing products, user will have to create an account with Salon365. Without a log in or password then all they would be able to do is browse the site. Once registration has been completed, user can then search for products by category, price and alphabetically. Products then can be bought by adding to cart, saved on their own personal wishlist on their profile page and also leave reviews on products they like or dislike. 

![Image of my responsive site](/docs/images/responsive.png)


## User Experience (UX)
### Project Goals
For Salon365, the main goal is to create a fully functional e-commerce website that allows users to create an account, browse products that they can then add to cart, add to wishlist or create a review and receive order confirmation on their orders. 

* The goal of the e-commerce website was to develop additional features to improve user experience and extend the use of the site. These additional features are as follows:
  * Wishlist functionality
  * Review functionality for any products
  * Creating an easy flowing and accessible website with basic black and white colours to allow images and important text to be seen clearly so nothing goes amiss. 


### **User Stories**

#### **Viewing and Navigation**
* View the site on a range of device sizes
* View a list of beauty products 
* View individual product details
* Easily view the total of my purchases at any time

<br/>

#### **Registration and User Accounts**
* Easily register for an account
* Easily log in or log out
* Easily recover my password in case I forget it
* Receive an email confirmation after registering
* Have a personalised user profile
* Have a personalised wishlist

<br/>

#### **Sorting and Setting**
* Sort the list of available products
* Sort a specific category of product
* Search for a product by name or description
* Easily see what I have searched for and the number of results

<br/>

#### **Purchasing and Checkout**
* Easily select the quantity of a product when purchasing it
* View items in my bag to be purchased
* Adjust the number of individual items in my bag
* Easily enter my payment information
* Feel my personal and payment information is safe and secure
* View an order confirmation after checkout

<br/>

#### **Admin and Store Management**
* Add product
* Edit/update a product
* Delete a product
* Create sale items including prices, start dates, and end dates (on the Django admin page)

---
<br/>
## Design
### Colour Scheme

The colour scheme of the site is simply black and white.

* The background is white to ensure the site is clean and readable and that the users' focus is always the products instead of them being distracted
* The site text is black which again ensures readability but also to provide enough contrast with the white background

### Typography

[Google Fonts](https://fonts.google.com/) was used to import the fonts featured in the site, both fonts used are of the type sans-serif to maintain consistency

### Icons and Images

* All icons used throughout the site were provided by [FontAwesome](https://fontawesome.com/)
* All product images were taken from [Qogita Website](https://www.qogita.com)
* The home page image is a simple image taken from Google

### Models
For this website I created 2 new models of a Wishlist and Product Review. This wishlist is linked to the product model allowing users to view a product and save it on their own personal profile. The wishlist model uses the relationship of the product id to work with the users log in data to achieve this. Same with the Review model, the products is linked to the model as well as the user model to allow the logged in user to select the product from the product list and use the text field to input their review which will then be shown on the frontend along with a date and time stamp. 
![Model image]()

### Features
The website is made up of 11 pages:

  * Home Page - Shows the User the main start paghe where they can start to navigate around the site and start to log in or register
  * All Products - This page show the user all the products available. 
  * Product Detail/Review - A more close up of the product page showing the user a description of the product with an option to add to cart, add to wishlist or createa review
  * Product Management - Allows the superuser to modify the site
  * My Profile/Wishlist - Shows the current users profile details along with what product(s) they have saved so far
  * Logout - To log the user out
  * Register - To sign up
  * Sign-in - To allow access to the site
  * Shopping Bag - Shows the user what is in their bag at the present time
  * Checkout - Allow the user to add checkout information so order can be processed
  * Checkout Success - Page that shows the order was successful


### Languages Used
* HTML, CSS, Python, and JavaScript along with the Django framework inlcuding Jinja

### Frameworks, Libraries, and Programs Used
* [Stripe](https://stripe.com)
* [AWS](https://aws.amazon.com/) to hold media files
* [Bootstrap](https://getbootstrap.com/) was utilised to create a core HTML structure similar to Boutique Ado so that my time could be spent on providing functionality
* [CI Python Linter](https://pep8ci.herokuapp.com/#)
* [Django](https://www.djangoproject.com/) was used as a Python framework
* [ElephantSQL](https://www.elephantsql.com/) was used to host the database for this site
* [Font Awesome version 6](https://fontawesome.com/) was used for all icons seen across the site
* [GitHub](https://github.com/) was used to store the repository for this quiz project, with GitHub Pages hosting the site
* [Gitpod](https://www.gitpod.io/) is the environment in which this project was created and worked on
* Google Chrome Developer Tools was used as a debugging tool, and to help visualise the site in different screen sizes to ensure that user experience remained clean and efficient no matter the screen size
* [Google Fonts](https://fonts.google.com/) provided the links for both fonts used on the site, and aided in selecting fonts that are complimentary to one another
* [Heroku](https://www.heroku.com/?) was used in addition to GitHub as the deployment platform for this site due to the use of databases
* [Jigsaw W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to validate CSS used
* [Jinja](https://jinja.palletsprojects.com/en/3.1.x/) was used as a templating language 
* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) to test the quality and responsiveness of each page on the site
* [Tech Sini](https://techsini.com/multi-mockup/index.php) aided in the creation of a multi-device mockup image so that I could test the appearance and functionality of the site on multiple device sizes, and provided the image seen at the beginning of this document
* [WAVE](https://wave.webaim.org/) Web Accessibility Evaluation Tool was used to test my site against accessibility criteria.
* [W3C Markup Validator](https://validator.w3.org/) to validate HTML

### Deployment

deployed using Heroku by the following steps:

Elephant SQL
1. Go to [ElephantSQL](https://www.elephantsql.com/) and either create an account or log in via GitHub
2. Click the 'Create New Instance' button
3. Choose your plan (The Tiny Turtle free plan is acceptable), name your instance and leave the tags blank if you wish then click the 'Select Region' button
4. Select a data centre that is closest to you
5. Click the 'Review' button
6. Double check your details then click the 'Create Instance' button
7. Navigate to the ElephantSQL dashboard and click on the database instance name you provided for this project
8. In the URL section copy the database URL to your clipboard
9. We will shortly return to this tab so leave it open

Heroku
1. Log into Heroku and click the 'New' button, then the 'Create a new app' button
2. Enter a name for your app (this must be unique), choose the region that is closest to you and click the 'Create app' button
3. Click 'Reveal Config Vars'
4. Navigate back to your ElephantSQL tab and ensure the database URL is copied to your clipboard
5. On Heroku add a config var named 'DATABASE_URL' and paste your ElephantSQL database URL as the accompanying value, then click 'Add'
6. Add all other necessary environment variables to this config var section from your project's .env file apart from the DEVELOPMENT variable
7. Find the 'Deploy' tab for your app on Heroku and click it
8. In the Deployment method section click 'Connect to GitHub', type your repo name and click 'Connect'
9. Click 'Enable Automatic Deploys' to ensure that your GitHub repository and Heroku are synced if you make any further code or project changes
10. Click 'Deploy Branch' to let Heroku begin building the site
11. We must now initialise our empty database by clicking 'More' then 'Run console'
12. In the terminal that has appeared type 'from salon_wholesale import db' and click enter
13. Now type 'db.create_all()' and hit enter again
14. Type 'exit()' to exit the Python terminal and close the console, our Heroku database will now contain the tables and columns created from our models.py files
15. Click the 'Open app' button to visit your built site

AWS
1. Navigate to [AWS](https://aws.amazon.com/), log in or create an account if you don't already have one
2. Search for S3 in Services, and click the 'Create bucket' button
3. Enter a bucket name (this should relate to your Heroku app name), and select the region closest to you
4. Uncheck 'Block all public access' and acknowledge that the bucket will be public, click 'ACLs enabled' and 'Bucket owner preferred', click 'Create bucket'
5. Click the bucket instance you just created and navigate to the Properties tab
5. Scroll down to 'static website hosting' and click 'use this bucket to host a website'
6. Enter default values of index.HTML for the Index document, and error.HTML for the Error document then click 'Save'
7. On the Permissions tab paste the following code into the CORS configuration editor: 
[
  {
      "AllowedHeaders": [
          "Authorization"
      ],
      "AllowedMethods": [
          "GET"
      ],
      "AllowedOrigins": [
          "*"
      ],
      "ExposeHeaders": []
  }
]
8. Click 'Save'
9. Navigate to 'Bucket Policy' and select 'policy generator', the type of which is 'S3 Bucket Policy', type * into the Principal field, and select 'get object' for the action
10. Copy your arn from the Bucket Policy tab and paste this into the ARN field on the policy generator page, then click 'Add Statement', then 'Generate Policy'
11. Copy the code displayed to your clipboard and paste this into the Bucket Policy editor. Before saving add a '/*' to the end of the Resource key, then click 'Save'
12. Navigate to the 'Access Control List' tab, click 'edit' and enable List for Everyone (public access) and accept the warning box
13. From the AWS site search for 'IAM', click 'User Groups' and then click 'Create New Group'
14. Name this group something that makes sense for the logic of your project, I named this 'manage-salon-wholesale', then click 'Create Group'
15. From the IAM dashboard click 'Policies' then 'Create Policy'
16. Click the 'JSON' tab and select 'import policy', search for 'S3' and import the 'AmazonS3FullAccess' policy
17. Find your arn from the Bucket Policy page in S3 and copy it, paste this into the 'Resource' key in the JSON tab instead of the '*' value. The format should be
"Resource": [
    'your_arn_here',
    'your_arn_here/*'
]
18. Click 'Review Policy', and give it a name and description
19. Click 'Create Policy'
20. Navigate back to the 'User Groups' page and click on the group you created
21. Click 'Attach Policy', search for the policy you just created and select it, then click 'Attach Policy'
22. Finally navigate to the 'Users' page and click 'Add User'
23. Create a user named 'your-site-name-staticfiles-user', click 'Next' then select the group we created earlier and click 'Next' again and 'Create User' to add your user to this group
24. In the Identity and Access Management tab click on Users, and click on the username of the user you just created
25. Click the 'security credentials' tab, scroll down to 'access keys' and click 'create access key'
26. On the 'Access key best practices & alternatives' page click 'Other' as our use case, follow this process to the end and click the 'download .csv' button
27. Save this .csv file as they are only available to us once and will be used to authenticate our user from our Django app

Back in the Gitpod CLI:
1. Type 'pip3 install boto3' into the terminal
2. Type 'pip3 install django-storages' into the terminal
3. Type 'pip3 freeze > requirements.txt' into the terminal to update this file
4. In settings.py add 'storages', to our installed apps
5. Still in settings.py add the following code:
if 'USE_AWS' in os.environ:
  AWS_STORAGE_BUCKET_NAME = 'your_aws_bucket_name_here'
  AWS_S3_REGION_NAME = 'your_aws_region_name_here'
  AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
  AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

  STATICFILES_STORAGE = 'custom_storages.StaticStorage'
  STATICFILES_LOCATION = 'static'
  DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
  MEDIAFILES_LOCATION = 'media'

  STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
  MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'
6. Navigate to Heroku and add these AWS keys to our config variables, the AWS_ACCESS_KEY_ID, and AWS_SECRET_ACCESS_KEY can be found in the .csv file we downloaded and saved earlier
7. Add the key 'USE_AWS' with the value 'True' (without quotation marks) to our Heroku config vars
8. Back in our workspace create a base-level file called 'custom_storages.py' and add the following code:
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticStorage(S3Boto3Storage):
    location = settings.STATICFILES_LOCATION
class MediaStorage(S3Boto3Storage):
    location = settings.MEDIAFILES_LOCATION
9. Add, commit and push your changes using the syntax 'git add .', 'git commit -m "add a message here", 'git push'

Back on AWS:
1. Navigating to our bucket we can now see a static folder in our bucket containing all of our static files
2. In S3 click 'Create folder' and name this folder 'media', click 'Save'
3. Click the just created 'media' folder, then click 'upload', 'Add files' and select all the product and site images for the website
4. Click 'Next' and under 'manage public permissions' select 'grant public read access to this object(s)', click 'Next' again and click 'Upload'

In Django admin:
1. Login to your superuser account on the Django admin
2. Click 'email addresses' and set your superuser's email address to verified and primary

Stripe:
1. Login to your Stripe account, click 'Developers' and 'API keys' and locate your publishable key and secret key
2. Check these keys and values are added to your Heroku config vars, if not add them now
3. Create a new webhook endpoint by going to Webhooks in the Developers menu, click 'Add endpoint' and paste your deployed url here but add '/checkout/wh/' to the end of the url, click to receive all events then click 'Add endpoint'
4. Click to reveal your Signing secret and add this value to your Heroku config vars
5. Ensure all the variables in Heroku config vars match the names you've provided in your settings.py file

1. Your deployed site should now appear and function the same way as your development site with all static and media files loading and displaying appropriately

How to Fork the Salon_wholesale
1. Login to your GitHub account
2. Navigate to the 'salon_wholesale' repository and click the 'Fork' button in the top right corner

How to Clone
1. Login to your GitHub account
2. Navigate to the 'salon_wholesale' repository
3. Click the green 'Code' button next to the 'Gitpod' button
4. Click 'Open with GitHub desktop'
5. Click the 'Choose...' button and navigate to a local path where you wish to store the cloned repository
6. Click the 'Clone' button

### W3 Nu HTML Validator
The W3 Nu HTML Validator:

* [Home page](/docs/images/homepagehtml.png)
* [Sign Up page](/docs/images/registerpageresult.png)
* [Log In page](/docs/images/loginpageresults.png)
* [Profile & Wishlist page](/docs/images/profilepagewishlist.png)
* [All Products page](/docs/images/allproductspage.png)
* [Product Detail page with review](/docs/images/productdetailwithreview.png)
* [Shopping Bag page](/docs/images/shoppingbag.png)
* [Checkout page](/docs/images/checkoutpage.png)
* [Checkout Success page](/docs/images/checkoutsuccess.png)

### W3C CSS Validation Service
The W3C CSS Validation Service was used to validate the two CSS files contained within the project, the results are as follows:

* [Base.css](/docs/images/basetest.png)
* [Profile.css](/docs/images/profilecss.png)

### JS Hint
JS Hint was used to validate the JavaScript found throughout the project with the results being:

* [Profile](/docs/images/profilejs.png)
* [Stripe](/docs/images/stripe.png)

### Python Linter

The following files were tested with a Python Linter to ensure PEP8 compliance.

* [Bag contexts.py](/docs/images/bagcontext.png)
* [Bag views.py](/docs/images/bagviews.png)
* [Bag urls.py](/docs/images/bagurls.png)
* [Checkout forms.py](/docs/images/checkoutforms.png)
* [Checkout models.py](/docs/images/checkoutmodel.png)
* [Checkout urls.py](/docs/images/checkouturls.png)
* [webhook-handler.py](/docs/images/webhookhandler.png)
* [webhooks.py](/docs/images/webhook.png)
* [Home urls.py](/docs/images/homeurl.png)
* [Home views.py](/docs/images/homeviews.png)
* [Products views.py](/docs/images/productview.png)
* [Products forms.py](/docs/images/productform.png)
* [Products models.py](/docs/images/productmodel.png)
* [Products urls.py](/docs/images/producturls.png)
* [Profile forms.py](/docs/images/profileform.png)
* [Profile urls.py](/docs/images/producturls.png)
* [Profile models.py](/docs/images/profilemodel.png)
* [Profile views.py](/docs/images/profileviews.png)

### Wave Testing?


### Lighthouse Testing
## Desktop
* [Desktop Accessibility](/docs/images/accessibilty.png)

## Mobile
* [Mobile Accessibility](/docs/images/accessibilty2.png)

Both Mobile and Desktop gave me an above 90% score on accessibility which shows that users have the best chance to access the site to its fullest without any trouble


### Flake8
used the command 'python3 -m flake8' in the terminal to further check for anything I may have missed. 

* ![Flake8 1](/docs/images/flake8.png)
* ![Flake8 2](/docs/images/flake81.png)


### **Manual Testing**

I tested my website by navigating around the site as any other user would testing all the nav links, buttons, forms etc to see if they all worked.

<br/>

#### **Links:**

* All links were clicked on and tested and directed me to the correct section of the site.
<br/>

#### **Buttons:**

* All buttons did what they were expected to do such as send data to the database, complete forms and start the order process 

<br/>

#### **Forms:**


* All forms were checked for validation errors by pressing confirm button with no data in the them and all passed.
* The user sees a success message when having successfully submitted a form when the form was successfully completed correctly
* The form will not submit when input types and lengths/amounts are not appropriate by testing every form field that takes a specific input type to see if it would submit with an undesired input type

<br/>

#### **Authentication:**

* Non-logged-in users cannot purchase any items from the site. Unfortunately this didn't work as anyone can do that
* Users cannot view confidential information about other users, such as user account details, wish lists, carts, or commissions. This works fine with no issues.
* Wishlist and reviews can only be created if user signs up. This was tested with a non user and to add and passed as I was directed to the sign up page

<br/>

#### **Database:**

* User data is added and stays over time, including order history, commissions and wishlist. I tested this by adding multiple users with different data and checked that throughout logging in and out, and over the course of weeks, the data remained the same
* User is linked to their order history, wishlist, and commission data. Tested this with multiple users and all info were on their personal profile page 

<br/>


#### **Checkout**

* Adding, editing, and removing products from the bag work as expected
* The signed up users correct details auto-fill in the checkout form
* Payments went through ok through Stripe

<br/>

#### **Wishlist**

* Adding and removing products from the wishlist work as expected
* Editing their wishlist on the profile page worked fine too

<br/>

#### **Products**

* The sorting and filtering functions works fine
* They can be added/edited or deleted from the product management page by the superuser

<br/>


#### **Search**


* The search function works as expected

<br/>

#### **Profile**

* Shows the users editable details
* Shows the users order history
* Shows the users saved wishlist products

### Full Testing

Salon365 site has been continually tested throughout development, including both manual and automated testing as shown above in this document

* Home page:
  * The navbar hamburger icon drops down the navbar menu when clicked on smaller screens and each dropdown within the navbar displays all the links needed to access the site
  * Every product feature clicked links the user to the relevant page described

* Login page:
  * Users must enter the correct username and password to log in or an error will be shown
  * When a user logs in they're redirected to the home page

* Sign up page:
  * The email section has to be in email format using a '@' symbol to submit the form
  * The username must be unique and can only include letters, numbers, and the following symbols @, ., +, -, _, otherwise an error message will appear and you can't sign up
  * Once all details have been created, an email is sent to the user via email that they have to press on and will be directed to the log in page

* My Account dropdown:
  * When Product Management is clicked it allows the superuser to add/delete and edit anything on the site
  * The My profile link will send the user to their personal profile with their delivery information, any orders placed and if any items are in their wishlist

* Product detail page:
  * The product detail page has the product image on there with a short description of it along with an add to wishlist button under the add to bag button
  * To add the product to your bag, there is an add to bag button under the description along with the amount increase button to determine how many you would like.
  * Users must be logged in to actually purchase items
  * On this page also a review can be typed out allowing users to leave a comment on what they think about the product 

* Shopping Bag page:
  * If the user has nothing in their shopping bag the page will be empty aside from a message that states Your bag is empty
  * When a product is added to the shopping bag a success message detailing the bag contents and clicking either 'Secure checkout' or the bag icon brings the user to the shopping bag page. On this page the user can add more of the same product or delete the product altogether

* Checkout page:
  * The checkout form will be already populated if the user is logged in
  * The details on the screen is correct and will populate the total price with the accurate pricing of all the products
  * Clicking complete order button will start the order process and will complete the order

* Checkout Success page:
  * This page displays a confirmation message that the order has been processed with what has been ordered and all other relevant information
  * An email is sent to users confirming their order has been successfully processed


### User Testing
Various friends and family have tested my site out on different devices such as mobile phones, laptops and even desktop PC to allow a good thorough testing as them being the actual user of the site. 


## Credits
### Code Sections/Tutorials
* Footer was properly completed with [Matthew James Taylor's](https://matthewjamestaylor.com/bottom-footer#problem)
* My wishlist and Review model was structured with the help from a mixture of [You Tube](https://youtube.com) and [Chatgpt](https://chatgpt.com). I used a mixture of the 2 to help build the bases of the wishlist and  had to tweak certain areas to work and to also fit around my sites layout once completed

### Media
* Product images were taken from [Qogita Website](https://www.qogita.com)
* The homepage main body image was just a random searched google image

## Acknowledgements
* I would like to thank the CI tutor Support team for continous help throughout this milestone. Without a tutor for around 3 months of this course did take it out of me but without them I would't have gotten anywhere with it.
* Also thank you to everyone that helped me test the site and provide feedback that was needed for the site 