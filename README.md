![Golf Plus Logo with blurred background](https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699368596/llt94awaqsuby0glnsgz.png)

![Responsive image](https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699369041/rhudnfd6wvgyaqewlx7h.png)
## A Django based Golf Blog

Golf Plus is a blog website built on Django, offering users the ability to register, create, view, update, and delete posts and comments, as well as manage their accounts. Users can like and search for posts, customize their profiles, subscribe to the newsletter, and enjoy various other features.


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
    - [Icons](#icons)
    - [Colors](#colors)
    - [Images](#images)
    - [Styling](#styling)
    </details></li>

    <li><details>
    <summary><a href="#seamless-design">Seamless Design</a></summary>

    - [Preloader](#preloader)
    - [AJAX](#ajax)
    - [Toasts](#toasts)
    - [Infinite Scroll](#infinite-scroll)
    </details></li>
    </ul>
</details>

2. <details open>
    <summary><a href="#features">Features</a></summary>

    <ul>
    <li><details>
    <summary><a href="#page-elements">Page Elements</a></summary>

    - [All Pages](#all-pages)
    - [Product List Page](#product-list-page)
    - [Product Detail Page](#product-detail-page)
    - [Account Pages](#account-pages)
    - [Likes Pages](#likes-pages)
    - [Cart Pages](#cart-pages)
    - [Checkout Pages](#checkout-pages)
    - [Contact Pages](#contact-pages)
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


