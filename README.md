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

