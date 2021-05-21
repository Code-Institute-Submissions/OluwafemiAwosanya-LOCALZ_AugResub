<!--Project Name-->
# Localz
**version 1.0.0.**

Localz is a platform that connects local businesses to customers.
Businesses and service providers within localities can list their businesses and services on Localz where potential customers can see and reachout to them.

**Business goals of this website**
* Build brand awareness.
* Showcase local businesses and services.
* Be the go to website for local businesses search and listings.

**Customer goals for this website**
* Looking for a certain service provider within my locality.
* Have a need to advertise a business.

<!--UX-->
## UX
*   Home : All business listings appear on this page for all users.
*   Log In: Registered users can sign in to the platform to edit existing ads or place new ones.
*   Log Out: logged in users can exit.
*   Sign Up: New business can register to start listing their services.
*   Place Ads: Registerd users can place new ads.
*   Manage Categories: Enable Admin user to add or delete categories.
**Web layout**
Simple well laid out Home page, accessible to all users (service providers and service users) with a search bar for a quick search of listings .

Each listing is placed on a card with business name, descriptions, address and phone numbers with a link for easy dial, especially for users accessing the platform via mobile phone.

To place an ad on the platform, user needs to be registerd, i.e. place ad tab is not visible to all users except registered users.

There is a Manage categories page which is only accessible to admin user.
username: Admin
password: Admin

**Prospective website users**

The ideal visitors to this website are;

* Any web user in need of a certain services  within locality.
* Business owner looking to reach a wider audience.

**Wireframe**

[Localz](https://github.com/OluwafemiAwosanya/LOCALZ/blob/master/static/localz_wf.pdf)


<!--Technologies Used-->
## Technologies Used
* HTML5
* CSS3
* Materialize-css 1.0.0.
* MongoDB
* Python + Flask
* Javascript
* Heroku
* Font Awesome 5.15.3.
* jQuery
* Git
* GitPod
* GitHub
* Chrome DevTools
* Balsamiq wireframe 
* Lighthouse    

<!--Testing-->
## Testing

*   As an unregisterd user, I can view all ads on the app.
*   As an unregistered user, I can search for a service or business on the app.
*   As an unregistered user, I can call the number provided on ad cards straight from the app.
*   As a business owner, I can register on the app.
*   As a business owner, I can place an ad on the app after registration.
*   As a registered user, I can view my existing ads and new ads.
*   As a registered user, I can edit or delete my existing ads.
*   As an admin user, I can view all ads on the app.
*   As an Admin user, I can add or delete Ad categories.


* I tested the website on the following browsers;
    * Chrome
    * Edge
    * Firefox
    * Safari

The user experience on all listed browsers is satisfying.

### Bugs
*   Ads placed were written to DB but not displayed on web page.
    *   I re-wrote the code on the ad card and that was fixed.

<!--Deployment-->
## Deployment

### GitHub pages

The website has been deployed with the following steps;

* Create Procfile and requirements.txt file and push to github
* Log in on Heroku
* Click on Create a New App with project Name
* Click connect to Github button
* Add github repository name and click search
* ensure Heroku validates your entry and click connect
* Scroll up the page and click settings
* Select reveal config Vars
* Add variables from env.py file
* Back to Deploy tab
* Scroll down and click enable automatic deployment
* Click Deploy branch for Heroku to receive the codes from Github
* You will now find a link that says "Your app was successfully deployed " view tab
* Click the view tab to see live app.

### Fork the code 

To work on this code on your own, follow these steps;

* Log in on GitHub
* Find the project repository
* On the top-right of the page, you will find a button with the name "Fork"
* Click on it and it will automatically fork the code to your GitHub

### Local Clone

To make a local clone of this website, follow these steps;

* Log in on GitHub
* Find the Project repository
* Locate a button with the name "code"
* Click on the "code" button
* On the dropdown selection,you will find a link to clone the code with HTTPS
* Copy the HTTPS link
* Open Git bash
* Open the directory you want to work on the cloned code 
* Type git clone followed by the previously copied HTTPS link
* Press Enter


### Acknowledgements

Thanks to Spence Barriball for guidance and Freecode camp channel on youtube.

<!--Copyright-->
## Copyright
© Localz 2021
