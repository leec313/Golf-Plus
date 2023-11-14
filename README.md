<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699368596/llt94awaqsuby0glnsgz.png" alt="Golf Plus Logo with background">
</div>

![Responsive image](https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699369041/rhudnfd6wvgyaqewlx7h.png)
## A Django based Golf Blog

[Golf Plus](https://golf-plus-7affb451de4e.herokuapp.com/) is a blog website built on Django, offering users the ability to register, create, view, update, and delete posts and comments, as well as manage their accounts. Users can like and search for posts, customize their profiles, subscribe to the newsletter, and enjoy various other features.


## Table of Contents
1. <details open>
    <summary><a href="#ux">UX</a></summary>

    <ul>
    <li><details>
    <summary><a href="#goals">Goals</a></summary>

    - [Visitor Goals](#visitor-goals)
    - [Business Goals](#business-goals)
    - [User Stories](#user-stories)
    </details></li>

    <li><details>
    <summary><a href="#visual-design">Visual Design</a></summary>

    - [Wireframes](#wireframes)
    - [Fonts](#fonts)
    - [Colors](#colors)
    </details></li>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#page-elements">Page Elements</a></summary>

    - [All Pages](#all-pages)
    - [Homepage](#homepage)
    - [Create Post Page](#create-post-page)
    - [Post Detail Page](#post-detail-page)
    - [Profile Page](#profile-page)
    - [About Page](#about-page)
    - [Login/Register Pages](#login/register-pages)
    - [Confirm Delete Pages](#confirm-delete-pages)
    - [Contact Page](#contact-page)
    </details></li>

    <li><details>
    <summary><a href="#additional-features">Additional Features</a></summary>

    - [General](#general)
    - [Products](#products)
    - [Users](#users)
    - [Search Features](#search-features)
    </details></li>

    <li><details>
    <summary><a href="#features-not-yet-implemented">Features Not Yet Implemented</a></summary>

    - [Basic](#basic)
    - [Content](#content)
    - [User Features](#user-features)
    </details></li>
    </ul>
</details>

3. <details open>
    <summary><a href="#information-architecture">Information Architecture</a></summary>

    <ul>
    <li><details>
    <summary><a href="#database-structure">Database Structure</a></summary>

    - [Details](#details)
    - [Diagram](#diagram)
    </details></li>    

    <li><details>
    <summary><a href="#data-models">Data Models</a></summary>

    - [Checkout App](#checkout-app)
    - [Contact App](#contact-app)
    - [Products App](#products-app)
    - [Users App](#users-app)
    </details></li>
    </ul>
</details>

4. <details open>
    <summary><a href="#technologies-used">Technologies Used</a></summary>

    - [Languages](#languages)
    - [Frameworks](#frameworks)
    - [Libraries](#libraries)
    - [Packages](#packages)
    - [Platforms](#platforms)
    - [Other Tools](#other-tools)
</details>

5. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>
    <li><details>
    <summary><a href="#automated-testing">Automated Testing</a></summary>

    - [Validation](#validation)
    - [Python Testing](#python-testing)
    - [Coverage](#coverage)
    - [Travis CI](#travis-ci)
    - [Coveralls](#coveralls)
    </details></li>

    <li><details>
    <summary><a href="#manual-testing">Manual Testing</a></summary>

    - [General Testing](#general-testing)
    - [Mobile Testing](#mobile-testing)
    - [Desktop Testing](#desktop-testing)
    </details></li>

    <li><details>
    <summary><a href="#bugs">Bugs</a></summary>

    - [Known Bugs](#known-bugs)
    - [Fixed Bugs](#fixed-bugs)
    </details></li>
    </ul>
</details>

6. <details open>
    <summary><a href="#deployment">Deployment</a></summary>

    <ul>
    <li><details>
    <summary><a href="#local-deployment">Local Deployment</a></summary>

    - [Local Preparation](#local-preparation)
    - [Local Instructions](#local-instructions)
    </details></li>

    <li><details>
    <summary><a href="#heroku-deployment">Heroku Deployment</a></summary>

    - [Heroku Preparation](#heroku-preparation)
    - [Heroku Instructions](#heroku-instructions)
    </details></li>
    </ul>
</details>

7. <details open>
    <summary><a href="#credit-and-contact">Credit and Contact</a></summary>

    - [Images](#local-preparation)
    - [Code](#local-instructions)
    - [Contact](#contact)
</details>

----

# UX
## Goals
### Visitor Goals

The target audience for Golf Plus are:
- Golf enthusiasts of all skill levels.
- Individuals looking for a community to share their golfing experiences.
- Those interested in staying updated on the latest trends, tips, and news in the golfing world.
- Golfers seeking a platform to connect with like-minded individuals.

User Goals are:
- Share personal golfing experiences and insights through blog posts.
- Connect with other golf enthusiasts and build a virtual golfing community.
- Stay informed about the latest trends, tips, and news in the golfing industry.
- Easily navigate the website to find relevant content.
- Customize their profiles and engage with the community through likes and comments.

How Golf Plus Fulfills These Needs:
- The blog platform allows users to seamlessly create, view, update, and delete posts, fostering a sense of community and sharing.
- Robust search functionality helps users find specific topics, tips, or posts of interest.
- User-friendly account management features enable customization of profiles and easy engagement with the community.
- A newsletter subscription option keeps users informed about the latest in the golfing world.
- The platform follows standard web design conventions for easy navigation while incorporating golf-themed elements to create a unique and engaging user experience.

### Business Goals

- Establish a vibrant and engaging platform that combines golfing information with a sense of community.
- Sustain consistent user traffic by providing non-blog engagement features, such as forums or discussion boards.
- Regularly update the blog with fresh content, ensuring users always find something new and relevant.
- Foster a sense of trust and credibility, positioning Golf Plus as a reliable source for golf-related insights and information by only publishing reviewed/approved posts.
- Prioritize and highlight the most engaging and relevant content to maintain user interest and potentially attract sponsorships or partnerships within the golfing industry.

### User Stories

- As a user interested in Golf, I expect to see lots of different posts that could interest me.
- As a user interested in Blogs, I expect to see unique posts from various authors to gain different perspectives.
- As a user, I expect to be able to contact the admin via a contact form.
- As a user, I expect to be able to read about the Blog website.
- As a user, I expect to be able to create an account.
- As a user, I expect to be able to search for posts, authors and content I might find interesting.
- As a user, I expect to be able to sign up for a newsletter to keep up to date on anything new.
- As a user, I expect to be able to unsubscribe to the newsletter from my profile.
- As a user with an account, I expect to be able to create posts.
- As a user with an account, I expect to be able to like/unlike posts.
- As a user with an account, I expect to be able to comment on posts. 
- As a user with an account, I expect to be able to delete my comments on posts.
- As a user with an account, I expect to be able to update my comments on posts.
- As a user with an account, I expect to be able to delete any posts I create. 
- As a user with an account, I expect to be able to update any posts I create.
- As a user with an account, I expect to be able to delete my account.
- As a user with an account, I expect to be able to update my account.
- As a user with an account, I expect to be able to see my posts within the profile page.

## Visual Design
### Wireframes

[Please follow this link to the Google Drive folder containing the wireframes](https://drive.google.com/drive/folders/1cYNyMMGgbE30l99TTqeWaAS3I05Bkjmw?usp=sharing)

### Fonts
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699628429/zpfx0lknhocqaqbm0myh.png" alt="fonts">
</div>

- Clean Aesthetic: [Lato](https://fonts.google.com/specimen/Lato) (used for my headings) is a sans-serif font with a clean and modern aesthetic, making it suitable for a wide range of design applications. Its simplicity and readability contribute to a professional and polished look for the project. 
- Versatility: [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto), (used for my paragraphs, labels and links) another sans-serif font, offers versatility and readability across various screen sizes and resolutions. Its geometric shapes and open letterforms make it well-suited for both headlines and body text, ensuring a cohesive and adaptable typographic hierarchy.
- Universal Legibility: Choosing sans-serif as the backup ensures universal legibility, especially on screens and digital platforms. Sans-serif fonts are known for their clarity and readability, making them a reliable fallback option in case any issues arise with the primary or secondary font choices.


### Colors
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699965843/fwtahed8yimk96205yff.png" alt="colors">
</div>

- The combination of #2f4550 and #586f7c provides a cool and calming backdrop, creating a serene environment that aligns with the leisurely nature of golf.
- Incorporating #b8dbd9 and #8c2f39 adds a touch of sophistication and contrast, making the design visually appealing and engaging for readers interested in both the sport and its lifestyle.


# Features

## Page Elements

### All Pages

#### Navbar
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699966901/gecdfbn6hie2f6dd8vij.png" alt="Desktop Navbar">
</div>
<div align="center">
  <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699966901/c12gcr0by3emrloi66bv.png" alt="Mobile Navbar">
</div>

- The Navbar and footer are the two persistent items across the site. 
- The logo is central on desktop and links to pages are on the left and the search function is on the right. 
- On smaller screens, the logo is pushed to the left and the links to pages/search function is within a drop down menu. 
- The well-known burger icon is used for the toggler. 
- Authorisation functions switch depending on whether or not the user is logged in.

#### Search Function
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699975055/dlopm6kanfhrue0ic3ek.png" alt="Desktop Search">
</div>
<div align="center">
  <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699975055/ef2vgpkvpykpebtentnp.png" alt="Mobile Search">
</div>

- The search function is something I was quite proud of since it allows the user to search via the: 
    * Title
    * Content
    * Author
    * Excerpt
- This means that if there is any mention of one golf course in another's post - it will also display in the search.
- I did however find a flaw in this, whereby the priority of sorting was not in place. This meant if a user searched for "Ballybunnion", the actual Ballybunnion post may not display first. 
- I implemented some sorting logic to fix this and we'll run through the code that does this within the PostListView in blog/views.py: 
    * The method that handles the search functionality is called get_queryset, which is a common method used in Django viewsets to retrieve the queryset of objects to be displayed.
    * queryset = super().get_queryset() retrieves the initial queryset using the super() function, which is typically the queryset of all posts.
    * search_query = self.request.GET.get('search', None) retrieves the search query parameter from the request's GET parameters. It defaults to None if the 'search' parameter is not present.
    * Then, onto the search logic: 
        * If a search query is provided, the queryset is filtered using the filter method, combining multiple conditions with OR logic.
        * The conditions check if the search query is present in the title, author's username, content, or excerpt of the posts. 
        * The __icontains lookup is used for case-insensitive partial matching.
    * The sorting logic is next: 
        * The queryset is further ordered using the order_by method.
        * The Case expression is used to prioritize matches in the title. If the title contains the search query, it's given a priority of 0 or 1. Other posts are given a priority of 2 by default.
        * The final ordering is by created_on in descending order, denoted by the - before created_on.
    * The modified queryset, incorporating search and sorting logic, is returned.

- How we display the search results in the template can be found on lines 9-15 in the index.html template: 
    *  {% if no_results %}: If no matching result is found, it will display "No posts found": 
<div align="center">
  <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699975078/nwcbrwnpxhcdrjk7fw25.png" alt="Mobile Search - No results found">
</div>

- {% elif request.GET.search %}: If the search finds a result, it display - Search results for: "{{ request.GET.search }}" as shown in the images at the start of this section.
- And the final {% else %} displays if the user has not actually gone and searched for anything - it displays the standard homepage with the Hero Slideshow and Latest Posts sections. 


#### Footer
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699967356/ykadgdfbmcnmbppaxluf.png" alt="Footer">
</div>

- The footer styling is the same across mobile and desktop, nothing really changes.
- The dark background color and bright text allow for great contrast for users to easily make out the text and icon links.
- The footer content includes the creator, the name of the website and the year of creation along with a copyright symbol.
- Underneath, it includes social links: Facebook, Twitter, Instagram and YouTube.


### Homepage

#### Hero Slideshow
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699967835/aawpphvty3xtii3uogue.png" alt="Hero Slideshow">
</div>

- The Hero Slideshow includes 3 generic golf course images and utilises JavaScript in order to change image. 
- This JavaScript code found within static/js/script.js is designed specifically for the index.html page or the root path (/).
- Firstly, the code inside the function runs when the DOM (Document Object Model) has fully loaded.
- It checks if the current page's URL path is either /index.html or just the root /. If true, the code proceeds to set up the slideshow.
- It selects the HTML element with the class hero-carousel and all img elements within it. This assumes that the slideshow is implemented as a carousel with images.
- It initializes a variable to keep track of the current index of the displayed image (let currentIndex = 0;).
- The showImage function takes an index as an argument and shows the corresponding image while hiding the others. It adds the class active to the currently displayed image.
- It initially shows the image at the index specified by currentIndex (showImage(currentIndex);).
- The nextSlide function increments the currentIndex to display the next image. It uses the modulo operator to loop back to the first image when the end is reached.
- This: setInterval(nextSlide, 5000); -  sets up an interval to call the nextSlide function every 5 seconds, creating an automatic slideshow effect.
- The slideshow and styling of this element works the same on mobile. Obviously being responsive to the size of the screen. 


#### Latest Posts
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699967834/gs6emyhaqhpytmeciyec.png" alt="Latest Posts Desktop">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699967834/t1ur953ugc92qohrzgha.png" alt="Latest Posts Mobile">
</div>

- The latest posts section displays 6 posts and orders them from newest to oldest. 
- The pagination implmentation can be found on lines 85-105 of the index.html template.
- It will display only published posts, so when a user creates a post, it will not display here right away. 
- The superuser would need to approve these unpublished posts in the admin. (from status 0 (draft) to status 1 (published) as per the Post model)
- Each post includes the:
    * uploaded image (or the placeholder if no image was uploaded by the user)
    * author
    * title
    * excerpt (this is limited to 80 charactars as per line 62 on the index.html)
    * creation date
    * number of comments/likes
- The latest posts section utilises the ListView from Django's Generic Views. I called it PostListView in blog/views.py.
- It takes the information from the Post model in blog/models.py and allows us to display it on the index.html template.


#### Newsletter
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699974302/xiaqanrogowgryyf4bcv.png" alt="Newsletter Desktop">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699974301/xf9iypexkcjmxws9oewh.png" alt="Newsletter Mobile">
</div>

- From the view mentioned above (PostListView), we also call the get_context_data function in which we can display the newsletter form. 
- This newsletter form only pops up once per user as we utilise some JavaScript to get the cookie data from the user's browser.
- The code in static/js/script.js from lines 5-39 ensures that the newsletter modal is displayed to the user after a delay of 5 seconds on the website, but only if the modal hasn't been shown before (tracked by a cookie). The modal can be closed by clicking outside its content or the X, and a cookie is set to remember that the modal has been shown.
- I've created a model for this in blog/models.py named NewsletterSubscription so that when if the user enter's their email into the newsletter form, it will show under the NewsletterSubscription in the admin. 
- This would allow the admin/superuser to track all emails entered and send out newsletters.
- The implementation of the newsletter can be seen at the end of the index.html template as {% include 'subscribe_modal.html' %}.


### Create Post Page
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699976252/y2usu3zsr5ixugbhy879.png" alt="Create post Desktop">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699976252/zfclela77zkhskydfgfj.png" alt="Create post Mobile">
</div>

- This PostCreate View defines a Django class-based view for creating new posts. 
- We set up the necessary attributes and then override the methods to customize the behavior of the view, including assigning the author, generating a slug, and providing feedback to the user upon successful post creation.
- The PostForm consists of the following fields/elements: 
    * Title
    * Content
    * Image
    * Excerpt
    * Submit
- All are required except for the excerpt, this is optional. 
- Upon submission, the user will be brought to the post-detail page of this post however it will need to be approved before other users can view it. 
- It will not show on the Latest Posts section of the homepage until published and the user is notified of this upon creation via an alert message.


### Post Detail Page
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699977027/icqlku6amaikglmj0vwi.png" alt="Post detail">
</div>

- PostDetailView: 
    * Inherits from Django's DetailView.
    * Specifies the Post model and the template to use ("post_detail.html").
    * Overrides get_context_data to provide additional context data for comments, liked status, and comment form.
    * Overrides get and post methods to handle GET and POST requests for the post detail view, respectively.

- post_detail.html: 
    * Displays post details, including title, author, creation date, and featured image.
    * Allows users to like a post using heart icons.
    * Displays the number of likes and comments.
    * Displays post content and provides update/delete buttons for the post's author.
    * Shows comments, aligning them left and right alternatively - providing an almost messaging type app feel.
    * For each comment, displays the commenter's name, profile image, and creation date.
    * Provides update/delete buttons for comments posted by the logged-in user.
    * Includes a comment form for authenticated users to leave new comments.
    * Provides a message to inform users when a comment is posted.

In summary, the code implements a detailed view for a post with features like liking, commenting, and CRUD operations for both posts and comments. The HTML template is well-structured, incorporating conditional logic to customize the display based on user authentication and post/comment ownership.


### Profile Page
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699977556/kdwcrswu0ouophz6pdq3.png" alt="Profile Desktop">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699977555/k8uzxfznjavof6cipzg1.png" alt="Profile Mobile">
</div>

- profile.html:
    * Displays the user's profile information, including their username, email, and profile image.
    * Allows the user to update their profile information, including the profile image.
    * Provides a form for updating newsletter subscription preferences.
    * Displays the user's posts in a grid layout, with details such as title, excerpt, creation date, and status (published or pending approval).
    * Implements pagination for the user's posts, showing 6 posts per page.
    * If the user has no posts, provides a link to create their first post:
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699977555/jwpjrro8hb6ymn0hdfkt.png" alt="Profile - no posts yet">
</div>
    
- ProfileView: 
    * Retrieves the user's profile, posts, and initial newsletter subscription status.
    * Paginates the user's posts.
    * Handles form submissions for updating the user profile, profile image, and newsletter subscription.
    * Renders the profile.html template with the necessary context.

- Profile Model: 
    * Defines a Profile model with a one-to-one relationship with the built-in User model.
    * Includes fields for the user's profile image, using the CloudinaryField.
    * Provides signals (create_user_profile and save_user_profile) to automatically create and save a user profile when a new user is registered.


### About Page
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699978202/rz2p5xggpf3yuouphqbl.png" alt="About Desktop">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699978202/xfbmprr0hwabfarxgupt.png" alt="About Mobile">
</div>

- The about page is just a simple page with text outlining the purpose of the site and an image underneath. 


### Login/Register Pages
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699978958/puj5zvo1kuaxuqlznqot.png" alt="Login">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699978959/oqc5mftoodfsqsentzp6.png" alt="Register">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699978958/enmyc1ns2chwvq4szlbu.png" alt="Sign Out confirm">
</div>

This Django application utilizes the django-allauth package for user account management and registration. django-allauth extends the built-in Django authentication system, providing features for user registration, authentication, password management, and account management. By using this package, the application streamlines the process of handling user accounts, offering a customizable and user-friendly interface for sign-up, login, and profile management. Additionally, the code snippet from django.contrib.auth.models import User suggests the usage of the default Django User model for handling user authentication and authorization. This combination of django-allauth and the User model from django.contrib.auth.models ensures a robust and secure user authentication system with extended functionality for user registration and account management.


### Contact Page
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699978446/u5jctmvdnxpfgsnm270x.png" alt="Contact Desktop">
</div>
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699978446/zuslyrabhnmplont346n.png" alt="Contact Mobile">
</div>

- ContactView:
    * Defines a view function named ContactView for the contact page.
    * Handles both GET and POST requests.
    * If the request method is POST, it processes the submitted form, saves the data to the database using the ContactForm, and redirects the user to the home page with a success message.
    * If the request method is GET, it renders the contact.html template with an empty ContactForm.

- ContactModel:
    * Defines a model named ContactModel for storing contact information.
    * Includes fields for the contact's name, email, and message.
    * Provides a human-readable representation for the model.
    * Specifies names for use in the Django admin.

- contact.html:
    * Extends a base template (base.html).
    * Displays a contact form with fields for name, email, and message.
    * Utilizes the crispy_forms template tags for improved form rendering.
    * Submits the form data to the same view (ContactView) using the POST method.
    * Includes a "Submit" button for form submission.

- ContactForm:
    * Defines a form class named ContactForm using Django's ModelForm.
    * Specifies the model as ContactModel and includes fields for name, email, and message.

In summary, this implements a contact page with a form for users to submit their name, email, and a message. The form data is processed, saved to the database, and a success message is displayed upon successful submission. The contact model provides a structured way to store this information in the database.

























