[View the live project here](https://salon-wholesale-b203aeb779cf.herokuapp.com/)

# Salon365 Wholesales Website

The Salon365 website is a wholesale website that allows users to buy a range of beauty products at a lower cost. To start purchasing products, user will have to create an account with Salon365. Without a log in or password then all they would be able to do is browse the site. Once registration has been completed, user can then search for products by category, price and alphabetically. Products then can be bought by adding to cart, saved on their own personal wishlist on their profile page and also leave reviews on products they like or dislike. 

![Image of my responsive site]()

## Contents 

* [User Experience (UX)](#user-experience-ux)
  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
* [Design](#design)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Icons and Images](#icons-and-images)
  * [Models](#models)
  * [Features](#features)
  * [Accessibility](#accessibility)
  * [Wireframes](#wireframes)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries-and-programs-used)

* [Deployment](#deployment)

* [Testing](#testing)
  * [Automated Testing](#automated-testing)
    * [W3 Nu HTML Validator](#w3-nu-HTML-validator)
    * [W3C CSS Validation Service](#w3c-css-validation-service)
    * [Wave](#wave-testing)
    * [Lighthouse](#lighthouse-testing)
    * [Flake8](#flake8)
  * [Manual Testing](#manual-testing)
  * [Bugs](#bugs)

* [Credits](#credits)
  * [Code Sections/Tutorials](#code-sectionstutorials)
  * [Media](#media)
  * [Text](#text)
  * [Acknowledgements](#acknowledgements)

## User Experience (UX)
### Project Goals
For Salon365, the main goal is to create a fully functional e-commerce website that allows users to create an account, browse products that they can then add to cart, add to wishlist or create a review and receive order confirmation on their orders. 

* The goal of the e-commerce website was to develop additional features to improve user experience and extend the use of the site. These additional features are as follows:
  * Wishlist functionality
  * Review functionality for any products
  * Creating an easy flowing and accessible website with basic black and white colours to allow images and important text to be seen clearly so nothing goes amiss. 

### User Stories
#### Viewing and Navigation
* View the website on a range of device sizes and have it be aesthetically pleasing and functional.
* View a range of beauty products that are for sale.
* View each product in detail onn their own product page.
* View the total of my purchases at any time.
* View products that maybe are on the wishlist
* View and create reviews 
#### Registration and User Accounts
* Register for an account
* Log in or log out
* Recover passwords in case it is forgotten
* Receive an email confirmation after registering
* Have a personalised user profile
#### Sorting and Setting
* Sort the list of available products
* Sort by specific category of products
* See what was searched for
#### Purchasing and Checkout
* Select the quantity of products when purchasing it
* View items in my bag to be purchased
* Adjust the quantity of individual items in my bag
* Easily enter my payment information
* View an order confirmation after checkout
#### Admin and Store Management
* Add Products
* Edit/update products
* Delete products

## Design
### Colour Scheme

![Image of colour scheme](/docs/images/colour-palette.png)

The colour scheme of the site is simply black and white.

* The background is white to ensure the site is clean and readable and that the users' focus is always the products instead of them being distracted
* The site text is black which again ensures readability but also to provide enough contrast with the white background

### Typography

[Google Fonts](https://fonts.google.com/) was used to import the fonts featured in the site, both fonts used are of the type sans-serif to maintain consistency

![Image of Stripe Element Font]()
* TO DO!

![Image of Body and Title Font]()
* TO DO!

### Icons and Images

* All icons used throughout the site were provided by [FontAwesome](https://fontawesome.com/) as they are while consistent and easily understandable
* All product images will be attributed in the credits section, along with the hero image on the home page
* The home page image is a simple image that shows the user that it is a beauty style site

### Models
For this website I created 2 new models of a Wishlist and Product Review. This wishlist is linked to the product model allowing users to view a product and save it on their own personal profile. The wishlist model uses the relationship of the product id to work with the users log in data to achieve this. Same with the Review model, the products is linked to the model as well as the user model to allow the logged in user to select the product from the product list and use the text field to input their review which will then be shown on the frontend along with a date and time stamp. 
![Model image]()

### Features
is comprised of 12 core sections: Home page, Signup, Login, Profile, Wishlist, Products view, Book Detail, Book Reviews, Shopping Bag view, Checkout, Checkout Success, Contact Us

* All pages feature the main nav bar, on desktop this includes the title, and search bar which can search for terms in book titles, blurbs, or information like the author of a book. The My Account drop-down features Product Management which is only accessible to the superuser (or site management) and can be used to add, edit, or delete products. The My Wishlist page and My Profile pages can also be accessed through this dropdown, along with being able to log out if a user is logged in. The Contact form is accessible through the Contact Us icon, and the bag icon displays up to date bag total information which can be clicked to bring the user to the Shopping Bag page. The main navbar also features a Home page link for users on mobile, and the All Books link to show all products which can be filtered in the menu. Books by Genre allows users to select and view only books from specific genres, and the Special Offers button allows users to view the New Releases and Clearance sections.
* All pages on the site are responsive across multiple different screen sizes, on smaller screens like mobile phones the top navbar is condensed into a hamburger menu to ensure the screen isn't cluttered while maintaining the same functionality as that found on larger screens.
* For all actions a user performs on the site a pop-up message will appear either confirming that their requested action has been successful or giving them details of the action they've just performed. For example, adding, removing, or altering a product in the shopping bag will all be accompanied by messages unique to the action performed.


* Future Implementations:

### Accessibility
* Throughout the development of this site accessibility was a priority, semantic HTML, alt tags, and aria-labels are used wherever possible to assist screen readers. The fonts chosen are ones I believe to be dyslexia friendly and readable no matter what screen size the user is on.
* Lighthouse...
![Lighthouse Accessibility Score]() 
* [WAVE](https://wave.webaim.org/) was utilised to test the web accessibility of each page on the site.

### Wireframes
Before development began I designed wireframes to aid in the creation of my site, when these were created I didn't intend on including a contact form so unfortunately this is missing from the wireframes


### Languages Used
* HTML, CSS, Python, and JavaScript

### Frameworks, Libraries, and Programs Used
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

deployed using Heroku and elephantsql

## Testing
### Automated Testing

### W3 Nu HTML Validator
The W3 Nu HTML Validator:

* [Home page]()
* [Sign Up page]()
* [Log In page]()
* [Product Management page]()
* [Wishlist page]()
* [Profile page]()
* [Contact Us page]()
* [All Books page]()
* [Book Detail page]()
* [Shopping Bag page]()
* [Checkout page]()
* [Checkout Success page]()

### W3C CSS Validation Service
The W3C CSS Validation Service was used to validate the two CSS files contained within the project, the results are as follows:

* [Base.css](/)
* [Profile.css]()

REPORT...

### JS Hint
JS Hint was used to validate the JavaScript found throughout the project with the results being:

* [Profile]()
* [Stripe]()
* [Quality Price Calculator]()
* [Quantity Input Calculator]()

REPORT...

### Python Linter

The following files were tested with a [Python Linter]() to ensure PEP8 compliance.

* [Bag contexts.py]()
* [Bag views.py]()
* [Bag urls.py]()
* [Checkout admin.py]()
* [Checkout context.py]()
* [Checkout forms.py]()
* [Checkout models.py]()
* [Checkout urls.py]()
* [webhook-handler.py]()
* [webhooks.py]()
* [Contact admin.py]()
* [Contact forms.py]()
* [Contact models.py]()
* [Contact urls.py]()
* [Contact views.py]()
* [Home urls.py]()
* [Home views.py]()
* [Products views.py]()
* [Products admin.py]()
* [Products forms.py]()
* [Products models.py]()
* [Products urls.py]()
* [Profile forms.py]()
* [Profile urls.py]()
* [Profile models.py]()
* [Profile views.py]()

### Wave Testing?


### Lighthouse Testing
## Desktop
* [Home page]()
* [Sign up page]()
* [Log in page]()
* [Profile page]()
* [Wishlist page]()
* [Contact page]()
* [Book detail page]()
* [Shopping bag page]()
* [Checkout page]()
* [Checkout Success page]()

## Mobile
* [Home page]()
* [Sign up page]()
* [Log in page]()
* [Profile page]()
* [Wishlist page]()
* [Contact page]()
* [Book detail page]()
* [Shopping bag page]()
* [Checkout page]()
* [Checkout Success page]()


### Flake8
used the command 'python3 -m flake8' in the terminal to further check for anything I may have missed. 

REPORT...

## Manual Testing
### Testing User Stories


### Full Testing

The Second Hand Shelf site has been continually tested throughout development, including both manual and automated testing as shown above in this document

* General:
  * All navbar links direct the user to the correct page when clicked and items like Product Management do not appear unless the superuser is logged in
  * All links throughout the site were tested and all brought users to the correct page or initiate the expected action
  * For all actions taken on the page (i.e logging in, adding a book to your bag) will trigger a message in the top right corner confirming the action has been registered
  * When a term is entered into the search bar and the search button is clicked it will display the products that match this query in terms of the title, author, or blurb
  * All social media links in the footer direct the user to a new page when clicked 
* Home page:
  * The navbar hamburger icon drops down the navbar menu when clicked on mobile/smaller screens and each dropdown within the navbar displays correctly with links bringing users to the correct pages
  * Each book feature when clicked links the user to the relevant page described on the feature card
* Login page:
  * Users must enter the correct username and password to log in or they're met with an error message stating that this is not correct
  * The 'forgot password' link brings users to the correct page and they are sent an email with a link to reset their password
  * The 'remember me' radio button when clicked means that the user's login information is saved for the next time they try to access their account
  * When a user logs in they're redirected to the home page
* Sign up page:
  * The email address must be in email format using a '@' symbol to submit the form, the email address must be entered the same way twice for validation to occur
  * The username must be unique and can only include letters, numbers, and the following symbols @, ., +, -, _, otherwise an error message will appear
  * The value of the password (again) field much match the value of the password field for the form to be submitted
  * When the form is submitted the user is sent an email to confirm and validate their account, when the link in this email is clicked the user is able to log in with their details
* My Account dropdown:
  * When Product Management is clicked it brings the superuser to the add book form where all required fields must be filled in to submit the form. The 'edit' and 'delete' links on the all books and book detail pages direct to the correct pages/actions and can only be accessed or seen by the superuser
  * Clicking 'add to wishlist' on the book detail page for a product adds this book to the user's wishlist which can be viewed by clicking the 'My Wishlist' tab, this also updates the button to say 'remove from wishlist'. When the remove from wishlist button is clicked the book is removed from the wishlist
  * If a user clicks the 'My Profile' link, enters their default delivery information and clicks 'update information' this information is saved and will be used to autofill the checkout details form
  * Each time a user who is logged in places an order it will appear in the order history section of the My Profile page, all information shown here is correct and clicking the order number brings the user to the order confirmation page shown when checkout was finalised
* Contact Us page:
  * The contact us page can be accessed regardless of whether a user is logged in, all fields are required and must be filled in to submit the form, the email address must be in a valid format or an error message will show
  * The content field has a maximum character limit of 2000 to allow users to submit a reasonably in-depth message to the site owners. Any characters above 2000 will not be registered by the field
  * When the user clicks the 'send your message' button they are redirected to the home page with a success message appearing and an email being sent confirming their message has been received
* All Books page: 
  * Clicking all books in the navbar allows users to filter books based on price, rating, language, and year of release, or to view all books. By clicking 'all books' users can choose to view different genres (also possible from the navbar dropdown) or special offers. There's a 'sort by' dropdown where users can choose to sort from price, or rating, high to low, and title or genre alphabetically or in reverse. If a user chooses to sort by rating the rating given by other users determines a book's position
  * The back-to-top button sits on the bottom right side of the screen and when clicked brings the user back to the top of the page
* Book detail page:
  * The book detail page features the 'add to wishlist' button which does as it suggests and changes to 'remove from wishlist' when clicked
  * A button stating 'Click here to rate or review' brings users to the review section of the page
  * Choosing a book quality from the quality selector alters the price displayed based on internal calculations, and the quantity can be adjusted by using the quantity selector
  * The 'Add to bag' button adds an item in its selected quality and quantity to the shopping bag and triggers a message confirming this action
  * Users must be logged in to rate or review a book
  * If there are no reviews for a book text describing this will be shown, otherwise, all reviews left for that particular book are displayed with edit and delete buttons on each that are visible and accessible only to the user who submitted the review. If a user leaves a review then clicks 'edit' the review form will be pre-populated based on the details of their original review 
  * The star rating field logs the correct value according to how many stars are coloured in green when the user clicks the star they wish to rate the book 
  * The written review is optional and the form can therefore be submitted without this being filled in, though the star rating is required and the form will not submit without it
  * The written review field has a maximum length of 3000 characters to ensure users have as much freedom as possible in writing their review
  * A superuser can leave multiple reviews per book for development and testing purposes but other users are only permitted to leave 1 review per book, if they attempt to add another they are given a warning message
* Shopping Bag page:
  * If the user has nothing in their shopping bag the page will be empty aside from a message that states 'Your bag is empty' with a button encouraging the user to view the books on offer
  * When a book is added to the shopping bag a success message detailing the bag contents is shown, clicking either 'Secure checkout' or the bag icon brings the user to the shopping bag page. Here a summary is shown and users can adjust the quantity of items, or remove them, clicking 'Secure checkout' here brings the user to the checkout page
* Checkout page:
  * If users are logged in and have saved information via their profile the checkout details form will be pre-populated with this data, all required fields must be filled in in the correct format
  * Ticking the 'save this delivery information to my profile' radio box updates the saved information stored in the user's profile
  * The correct information is displayed as calculated by the item quality and quantity in the bag
  * Clicking 'Complete order' when the form has been correctly filled out initiates a spinning green overlay to indicate the order is being processed and then users are redirected to the checkout success page
* Checkout Success page:
  * The checkout success page displays a confirmation that the order has been processed along with an order summary featuring key information 
  * An email is sent to users confirming their order has been successfully processed


### User Testing
REPORT...

## Bugs 


## Credits
