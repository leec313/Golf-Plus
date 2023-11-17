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

    <li>
    <a href="#agile-development">Agile Development</a>
    </li>

    </ul>
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
    - [Login/Register Pages](#login-and-register-pages)
    - [Confirm Delete Pages](#confirm-delete-pages)
    - [Contact Page](#contact-page)
    </details></li>

    <li>
    <a href="#features-not-yet-implemented">Features Not Yet Implemented</a>
    </li>
    </ul>
</details>

3. 
    <summary><a href="#technologies-used">Technologies Used</a></summary>

4. <details open>
    <summary><a href="#testing">Testing</a></summary>

    <ul>
    <li><details>
    <summary><a href="#automated-testing">Automated Testing</a></summary>

    - [Validation](#validation)
    - [Python Testing](#python-testing)

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

5. <a href="#deployment">Deployment</a>

6. <a href="#credits-and-acknowledgements">Credits and Acknowledgements</a>

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

## Agile Development

The inception of this project coincided with the creation of a GitHub Projects Page, serving as a pivotal tool for overseeing the anticipated tasks. The primary objective was to portray the expected workload systematically, create user stories, and subsequently break them down into more manageable tasks. This planning process aimed to provide a structured roadmap, facilitating a progression towards the completion of the project within the targeted timeframe. By leveraging the GitHub Projects Page, the project's evolution could be tracked, tasks assigned, and milestones achieved, ensuring a streamlined and organized development process.

To see the project Kanban, [please follow this link here](https://github.com/users/leec313/projects/2/).

I kicked off my project by envisioning its entire journey, starting with fundamental user stories like establishing the repository and workspace, progressing through essential tasks, and concluding with optional enhancements. Once the essentials were in order, I delved into additional features, including the search function and newsletter. What really captivated me was the adaptable approach of agile development. It allowed me to shape and refine the project gradually, embracing an agile mindset that brought excitement to the process. Overall, I found joy in the flexibility and step-by-step progress that agile development brought to the table.

My Kanban board and commit messages were my trusty guides, helping me seamlessly resume my work and understand exactly where I left off. Each commit message acted as a snapshot of my progress, clarifying what I had just finished and outlining the next steps. Ticking off tasks within a user story became a satisfying routine, and once all the pieces fell into place for a user story, I marked it as closed. This action automatically shifted it to the "done" column on my board, signaling the completion of that particular part of the project. This straightforward system kept me organized and provided a clear visual of my accomplishments and the road ahead.

### Core User Stories (Must-Have)

- [USER STORY: Deploy website](https://github.com/leec313/Golf-Plus/issues/1)
- [USER STORY: Admin Panel](https://github.com/leec313/Golf-Plus/issues/7)
- [USER STORY: Create an account](https://github.com/leec313/Golf-Plus/issues/11)
- [USER STORY: Base template](https://github.com/leec313/Golf-Plus/issues/15)
- [USER STORY: Create/like a post/comment](https://github.com/leec313/Golf-Plus/issues/19)
- [USER STORY: Delete user profile](https://github.com/leec313/Golf-Plus/issues/24)
- [USER STORY: Testing](https://github.com/leec313/Golf-Plus/issues/29)

### Additional User Stories (Should/Could-Have)

While not initially integral to the core project, I identified three user stories early on that could significantly enhance both the website's functionality and, more crucially, meet the acceptance criteria for the project. Recognizing the need for a custom model in my database, I proceeded to create the Newsletter and Profile models to fulfill this requirement. Witnessing the final outcome of their implementation left me immensely satisfied, and the experience garnered from their incorporation proved to be highly educational. Additionally, the integration of a search function emerged as a valuable asset, particularly in scenarios where there is an extensive array of blog posts to navigate. This feature substantially improves the overall user experience by simplifying the process of sifting through a potentially large volume of content.

- [USER STORY: Search & Find a post](https://github.com/leec313/Golf-Plus/issues/38)
- [USER STORY: User Profile Page](https://github.com/leec313/Golf-Plus/issues/39)
- [USER STORY: Newsletter Signup Form](https://github.com/leec313/Golf-Plus/issues/44)

### Not Important, Nice to Have User Stories (Could-Have)

Although the potential enhancements outlined in the "could-have" user stories were not integrated into the project due to time constraints, they remain viable options for future implementation. Social logins, for instance, offer a convenient and expedited user experience, facilitating quicker login and registration processes. Comment pagination, another prospective feature, holds the promise of enhancing user experience, especially when dealing with a substantial number of comments on a single post. This not only streamlines the presentation of comments but also simplifies the overall management of comment displays. Additionally, the incorporation of easily implementable icons for account login, profile viewing, and registration stands out as a straightforward yet effective means to elevate the overall user experience. While these features were deferred for now, they hold the potential to be valuable additions in subsequent project iterations.

- [USER STORY: Social Logins](https://github.com/leec313/Golf-Plus/issues/37)
- [USER STORY: Comment Pagination](https://github.com/leec313/Golf-Plus/issues/40)
- [USER STORY: Create an account - Add icons if necessary for ease of use](https://github.com/leec313/Golf-Plus/issues/14)

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


### Login and Register Pages
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

### Confirm Delete Pages
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1699980819/mhhhs5xakvaoquq7wohg.png" alt="Delete confirmation Page">
</div>

The confirm deletion pages are all fairly similar bar the wording and apply to deleting the user's posts, comments and profile. Each page has a corresponding view, url and template. 

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


## Features Not Yet Implemented

#### Social Sharing
- Explore the implementation of a social media sharing feature to allow users to share their favorite posts on various social platforms.

#### Follow/Private Messaging
- Integrate a follow/Private message functionality on user profiles to foster engagement and interaction between users.

#### Analytics
- Consider adding a feature to track and display the number of views on each post, providing users with insights into the popularity of their content.

#### User Admin
- Explore the implementation of a user-friendly admin panel with additional features for content management, user moderation, and analytics.

#### Post Categories or Tags
- Implement a categorization system for posts, enabling users to filter and explore content based on specific topics or tags.

#### Advanced Search Filters
- Enhance the search functionality with advanced filters, allowing users to refine their search based on criteria such as date, author, or post category.

#### User Notifications
- Introduce a notification system to keep users informed about new comments, likes, or interactions on their posts and profile.

#### Interactive Post Editor
- Upgrade the post creation/editing interface to include a more interactive editor with formatting options, image embedding, and a preview feature.

#### Featured Posts Section
- Create a dedicated section to showcase featured or trending posts, providing users with a curated selection of high-quality content.

#### Gamification Elements
- Introduce gamification elements such as badges, achievements, or point systems to incentivize user engagement and contributions.

#### Dark Mode
- Implement a dark mode option for the website to cater to users who prefer a darker color scheme for improved visibility in low-light environments.

#### Collaborative Writing
- Enable multiple users to collaborate on a single post, fostering a sense of community and collective content creation.



## Technologies Used

### Html

 - Used to structure my webpages and the base templating language

### CSS

 - Custom CSS was written on large chunks of this site to make it as close to the wireframes as I felt it needed to be.

### JavaScript

 -  Used to add timeout function for messages as well as to enable the menu on index.html

### Python

 -  Used for the logic in this project.

### Django

 -  Framework used to build this project. Provides a ready installed admin panel and includes many helper template tags that make writing code quick and efficient.

### Font Awesome

 -  Used for the like/comment icons as well as the social media links in the footer.

### Bootstrap 5

 - Used as the base front end framework to work alongside Django

### Jinja Templating with Django

 - Used to render logic within html documents and make the website more dynamic.

### GitHub

 - Used to store the code for this project & for the projects Kanban board used to complete it.

### Heroku

- Used to host and deploy this project

### Heroku PostgreSQL

-Heroku PostgreSQL was used as the database for this project during development and in production.

### Cloudinary

- Used to host the static files for this project including user profile images.

### Git

- Used for version control throughout the project and to ensure a good clean record of work done was maintained.

### Gitpod

- Used as IDE to develop the project.

# Testing

## Automated Testing

### Validation

- HTML has been validated with [W3C HTML5 Validator](https://validator.w3.org/)
- CSS has been validated with [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
- Links checked with [W3C Link Checker](https://validator.w3.org/checklink)
- JavaScript was tested on the site for errors and functionality using the console and with [JSHint](https://jshint.com/)
- Python has been validated using the [PEP8 Python Checker](https://www.pythonchecker.com/) and Flake8 Extension within GitPod.


#### Errors in validation

On my [signup page](https://golf-plus-7affb451de4e.herokuapp.com/accounts/signup/), there's an issue with how the crispy form is rendered, as highlighted by the validator. The problem specifically relates to the help text generated by the form, where the ul element is not allowed as a child of small. This results in the below validation error:
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1700070427/dnwxvyhogn0y4e2my5jb.png" alt="Sign Up validation error">
</div>

It's referring to the help text that the form generates and how the ul element is not allowed as a child element of small, specifically this section of rendered code: 
<div align="center">
 <img src="https://res.cloudinary.com/dc9f7ztkr/image/upload/v1700070778/vcjdnpnralytjvngffyx.png" alt="Sign Up validation error (rendered code)">
</div>

Despite troubleshooting efforts with Code Institute's tutors, fellow students, and online resources, a solution couldn't be found. Interestingly, the login page, which uses form.as_p instead of crispy forms, doesn't encounter this error. Although form.as_p led to more warnings and errors on the signup page, the decision to stick with the crispy form method was made due to this particular error being the only issue.


### Python Testing

#### Notes

* Tests have been written the views and maintaned throughout the project development.
* The tests are contained in blog/tests.py. 
* A testing database has been setup in settings.py and will automatically be utilised when the test command is run.
* This allows for more accurate testing and test views which function on a real Postgres database. 

#### Running Tests

1. Activate the virtual environment with the [deployed](#deployement) code.
2. Input the following code into the terminal:
    ```
    python manage.py test
    ```
3. Results will be shown in the terminal.

## Manual Testing

Each user story was manually tested in line with intended functionality on both desktop & mobile.
As this project was driven by my own User Stories I  felt manual testing was applicable on all logic code.

If the intended outcome completes then this will be flagged as pass. If it does not then this is a fail.

#### Account Registration Tests
| Test |Result  |
|--|--|
| User can create account | Pass |
| User can log into account| Pass|
|User can log out of account|Pass|

---

#### User Navigation Tests

| Test |Result  |
|--|--|
|User can navigate to all pages | Pass |
|User can view navigation items| Pass|
|User access account profile page|Pass|
|User can access posts|Pass|
|SuperUser can access admin panel|Pass|

---

#### Account Security Tests

| Test |Result  |
|--|--|
|Non logged in user cannot like/comment/create a post | Pass |
|Non logged in user cannot access profile page| Pass|
|Non superuser cannot access admin panel|Pass|

---

#### Posting Tests

| Test |Result  |
|--|--|
|User can make a post when all required fields complete | Pass |
|User cannot submit post with empty form |Pass|
|User can view their posts from profile|Pass|
|User can edit post while status is awaiting approval |Pass|
|User can delete post while status is awaiting approval|Pass|
|Edit button does present on posts created by user|Pass|
|Delete button does present on posts created by user |Pass|

--- 

#### Profile Tests

| Test |Result  |
|--|--|
|User can edit their user name and email from the profile page | Pass |
|User can edit / add a profile image from the profile page |Pass|
|User can edit their newsletter subscription status from their profile page| Pass|
|User cannot change username to the same as another user|Pass|
|User cannot change their email to the same as another user |Pass|
|User presented with confirmation when they click delete|Pass|
|User can delete account |Pass|


#### Admin Tests

| Test |Result  |
|--|--|
|Admin can add items to posts|Pass|
|Admin can add items to comments|Pass|
|Admin can add items to profiles|Pass|
|Admin can edit items in posts|Pass|
|Admin can edit items in comments|Pass|
|Admin can edit items in profiles|Pass|
|Admin can delete items in posts|Pass|
|Admin can delete items in comments|Pass|
|Admin can delete items in profiles|Pass|
|Items display correctly on front-end when updated / added|Pass|

---

### General Testing
- Each time a feature was added, all the functions were tested to see if there was an impact.
- The views have been thoroughly manually tested and refined over time, utilising python features to update the database in a useful, flexible structure.
- The site was sent to friends for feedback and testing.
- All forms have validation and will not submit without the proper information.

### Mobile Testing
- I tested the site personally on my Android device, going through the entire process, checking buttons, CRUD functionality etc.
- The site was sent to friends and relatives for them to follow the same process. They have tested on their devices, including iOS.
- Chrome was utilised to inspect the site in mobile format, going through the pages, functions and responsiveness.

### Desktop Testing
- The site was developed on a Dell G3 Laptop and the majority of testing occurred on Chrome.
- The site was tested by friends and relatives on numerous desktop devices.
- The site was marginally tested on other browsers, such as Firefox and Edge.
- Internet Explorer was not tested and the site was not developed with it in mind as support for the browser is gradually being dropped.


## Bugs

### Known Bugs

- After trying to implement email authentication via email within the Gitpod environment, [I found this GitHub issue here](https://github.com/gitpod-io/gitpod/issues/965).
It confirmed the ports used to send emails from Gitpod were blocked. I wanted to set up email confirmation on account creation and also forgot password links etc. 
One user stated: 

"yes, indeed we recently started blocking port 587 to prevent spammers from using it.
Port 25 was never open, because it's blocked by default in Google Cloud Platform."

I was following [this tutorial on YouTube](https://www.youtube.com/watch?v=wB1qOExDsYY) in order to achieve this but since it's not possible via Gitpod, I had to stop. 
Although this did not end up working, I did learn a lot in relation to setting this up within the Django system.
I soon found out later that this issue does not occur on Heroku when deployed as the ports are not blocked by them, however it was too late at this stage. I will be implementing this in a future project for sure. 

### Fixed Bugs

- When setting up the profile image for users Profile page, the placeholder image was showing a broken link. 
After many attempts to fix this, it was not working for me, so I hardcoded the Cloudinary link into the Profile modellike so: 
![Placeholder bug image](https://github.com/leec313/Golf-Plus/assets/1553915/c296285a-30dc-41da-8b85-af83bd152620)

This worked for me. 
I then added #noqa to the end of the line in the model as the line was too long and any attempt to shorten it via line breaks was not working. 

- When I removed the following piece of code from the index.html: 

```html
{% if forloop.counter|divisibleby:3 %}
``` 

And implemented the display of the number of posts via Bootstrap, it caused issues with the search feature. 
When searching for posts, it was not displaying any valid posts related to the search query. 
After hours of trying to find a solution, I decided to revert back to using the forloop counter in order to have my search function work again.
This was not really the outcome I was hoping for, however playing around with different Bootstrap classes got me to where I wanted to be in this situation and the posts display the way I want them to. 


- My tests were failing due to the alert messages. I Searched online and found this:
In Django tests, messages are stored in response.wsgi_request._messages. 

My original code was trying to access response.context['messages'], which resulted in a TypeError because the messages were not directly available in the context.
By changing syntax to response.wsgi_request._messages, it fixed the issue. 

- Static files were not loading on the deployed version of the site. I was confused because the setup looked correct. After inspecting my settings.py file, I realised that there was an issue with one of the cloudinary related lines and made the change to fix it. I resolved this quite quickly and continued on with the project. 

- After implementing the newsletter subscription modal, I soon realised that it was popping up on every page reload of the index.html. I needed to implement some form of JavaScript that captured the current user's browser cookie and stored it. Knowing that if the current session already had the pop up displayed, it would not display again. 

- Because the User account and profiles are two separate models, when a user created an account, they did not have a profile. This meant they could not view the profile page template and Django through an error. I soon fixed this by creating a signal so that when a user registers for an account, a profile is created for them too.


## Google Lighthouse Testing

### Desktop

> index.html

![Google Lighthouse Index](https://res.cloudinary.com/dc9f7ztkr/image/upload/v1700243210/pdgdrzugwkgrslqax7at.png)

> profile.html

![Google Lighthouse Profile](https://res.cloudinary.com/dc9f7ztkr/image/upload/v1700243210/kyutnxcctvfsksn4olzp.png)

In my exploration of Lighthouse performance scores, I identified a potential issue related to serving static assets efficiently, particularly in the context of using Cloudinary. This raised awareness about the significant impact on the performance score due to the choice of media storage solutions. For future projects, I am inclined to explore alternative methods for storing media that align more favorably with performance optimization goals.

Another noteworthy consideration emerged in the context of serving images in next-gen formats. While Lighthouse suggests utilizing next-gen formats like .webp for improved performance, the practical implementation faced challenges in a user-generated content environment. Allowing users to freely upload various image formats complicates enforcing a strict .webp-only policy. While automatic conversion mechanisms exist, implementing such a feature would require additional time and resources. Given the constraints of the project timeline, I opted for a pragmatic approach, acknowledging the trade-off between performance optimization and user convenience.


# Deployment

> I have broken up the deployment into two sections as it is quite extensive and can be hard to follow.

To deploy the project through Heroku I followed these steps:

- Sign up / Log in to  [Heroku](https://www.heroku.com/)
- From the main Heroku Dashboard page select 'New' and then 'Create New App'
- Give the project a name - I decided on Golf Plus and selected EU as that is the closes region to me.
- After this you select select create app. 
- The name for the app must be unique or you will not be able to continue.
- Heroku will create the app and bring you to the deploy tab. 
- From the submenu at the top, navigate to the resources tab.
- Add the database to the app, I created mine via ElephantSQL.
- Open the config vars section copy the DATABASE_URL to the clipboard for use in the Django configuration.
- Inside the Django app repository create a new file called env.py
- within this file import the os library and set the environment variable for the DATABASE_URL pasting in the address copied from ElephantSQL. 
- The line should appear as os.environ["DATABASE_URL"]= "Paste the link in here"
-   Add a secret key to the app using os.environ["SECRET_KEY"] = "your secret key goes here"
-   Add the secret key just created to the Heroku Config Vars as SECRET_KEY for the KEY value and the secret key value you created as the VALUE
-   In the settings.py file within the django app, import Path from pathlib, import os and import dj_database_url
-   insert the line if os.path.isfile("env.py"): import env
-   remove the insecure secret key that django has in the settings file by default and replace it with SECRET_KEY = os.environ.get('SECRET_KEY')
-   replace the databases section with DATABASES = { 'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))} ensure the correct indentation for python is used.
-   In the terminal migrate the models over to the new database connection
---
-   Navigate in a browser to cloudinary, log in, or create an account and log in.
-   From the dashboard - copy the CLOUDINARY_URL to the clipboard
-   In the env.py file - add os.environ["CLOUDINARY_URL"] = "paste in the Url copied to the clipboard here"
-   In Heroku, add the CLOUDINARY_URL and value copied to the clipboard to the config vars
-   Also add the KEY - DISABLE_COLLECTSTATIC with the Value - 1 to the config vars
-   this key value pair must be removed prior to final deployment
-   Add the cloudinary libraries to the list of installed apps, the order they are inserted is important, 'cloudinary_storage' goes above 'django.contrib.staitcfiles' and 'cloudinary' goes below it.
-   in the Settings.py file - add the STATIC files settings - the url, storage path, directory path, root path, media url and default file storage path.
-   Link the file to the templates directory in Heroku TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')
-   Change the templates directory to TEMPLATES_DIR - 'DIRS': [TEMPLATES_DIR]
-   Add Heroku to the ALLOWED_HOSTS list the format will be the app name given in Heroku when creating the app followed by .herokuapp.com
-   In your code editor, create three new top level folders, media, static, templates
-   Create a new file on the top level directory - Procfile
-   Within the Procfile add the code - web: guincorn PROJECT_NAME.wsgi
-   In the terminal, add the changed files, commit and push to GitHub
-   In Heroku, navigate to the deployment tab and deploy the branch manually - watch the build logs for any errors.
-   Heroku will now build the app for you. Once it has completed the build process you will see a 'Your App Was Successfully Deployed' message and a link to the app to visit the live site.

#### Forking the repository

By forking the GitHub Repository you can make a copy of the original repository to view or change without it effecting the original repository.
You can do this by: 
-  Logging into GitHub or create an account. 
- Locate the repository at  [here](https://github.com/leec313/Golf-Plus)  . 
-  At the top of the repository, on the right side of the page, select "Fork" from the buttons available. 
-  A copy of the repository should now be created in your own repository.

#### Create a clone of this repository

Creating a clone enables you to make a copy of the repository at that point in time - this lets you run a copy of the project locally: This can be done by:

-   Navigate to [the repository](https://github.com/leec313/Golf-Plus)
-   click on the arrow on the green code button at the top of the list of files
-   select the clone by https option and copy the URL it provides to the clipboard
-   navigate to your code editor of choice and within the terminal change the directory to the location you want to clone the repository to.
-   type 'git clone' and paste the https link you copied from github
-   press enter and git will clone the repository to your local machine


## Credits and Acknowledgements

### Images

- Hero Slideshow images: 
    * https://unsplash.com/photos/green-grass-field-near-mountain-during-daytime-xyA32yjWFlg
    * https://www.top100golfcourses.com/golf-course/tralee
    * https://www.druidsglenresort.com/book-a-tee-time.html

- About Page image: 
    * https://unsplash.com/photos/golf-ball-on-green-grass-field-during-daytime-awin-9RBlpE

- Logo: 
    * I created the logo myself in Photoshop

### Content and Resources

- I went through the bootstrap documentation to determine how best to approach my desired design. I always find the getbootstrap.com helpful with examples of how best to implement boostrap components.
    * https://getbootstrap.com/docs/5.0/getting-started/introduction/


- I found Corey Schafer's YouTube series on Django extremely helpful in explaining how the fundamentals of Django work and really enjoyed the videos.
    * https://youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&si=D9s9IU-DV2VH6nmg

- Django Documentation
    *  Read through the django documentation multiple times when trying to implement models and other content.
  
-  W3 Schools
    *  Used for reference throughout for simple css examples.
  
-  Code Institute
    - The course content for portfolio project 4 played a crucial role in providing the necessary knowledge and skills to successfully complete this project.
    The structured and comprehensive nature of the course content contributed significantly to my understanding of the project requirements and the Django framework.
    Informative and Well-Paced Walkthroughs:

    - The walkthroughs provided in the course were not only informative but also well-paced, allowing for a step-by-step understanding of the concepts and implementation details.
    The clarity of the walkthroughs helped in grasping complex topics and reinforced a solid foundation in Django development.
    Initial Structure Based on CI Walkthrough:

    - During the early stages of the project, I leaned heavily on the Code Institute (CI) walkthrough for guidance.
    The initial structure of the project was influenced by the CI walkthrough, serving as a scaffold until I gained a deeper understanding of the Django framework and could confidently make personalized modifications.
    Legacy Code Regarding Nav:

    - There are remnants of legacy code related to the navigation structure in the project.
    While these aspects may reflect the early stages of development, I acknowledge the presence of legacy code, and future iterations of the project could involve refactoring and optimizing the navigation structure.


### Acknowledgements

I want to express my gratitude to the exceptional team at Code Institute, particularly my mentor Rory Patrick and my cohort Alan Bushell, for their unwavering support during the entire project. The guidance and encouragement I received were instrumental in overcoming challenges and achieving success.
A heartfelt thank you extends to all the tutors and fellow students at Code Institute. The collaborative and supportive community created a conducive learning environment. The insights, shared experiences, and camaraderie greatly enriched my journey, making it a memorable and rewarding experience.