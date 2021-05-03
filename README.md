# **Fitness Exercise Development**

## **Backend Development Project - Code Institute**

&nbsp;
![website mockup](assets/images/website_mockup.jpg)

The Fitness Exercise Development (FED) is website created to save your exercise program info. The idea is that it works as an application that you can access as an website, and the primarly focus is to the mobile view (as it will be mainly accessed during a gym session)

This project is part one of the four milestone project of Code Institute Full Stack Developer course, and aims to show an interactive website using HTML5, CCS3 and Javascript, using Python and Flask to manage the application backend and MondoDB to store its information.

Access the website here: [Fitness Exercise Development*](http://fitness-exercise-development.herokuapp.com/)

&nbsp;

## **Table Of Contents**

* [User Experience](#user-experience-(ux))
* [Design Process](#design-process)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)
* [Acknowledgments](#acknowledgments)

&nbsp;

## **User Experience (UX)**

### **Project Goals:**

* Display the exercise program in a single page
* Create, read, edit and delete exercises through the application website
* Show User status info
* Show App status info to Admin
* Search exercises and be able to add them to your program

### **User Stories**

#### **New Users:**

* I go to the gym regurlary and looking for a way to save my exercise program info, and be able to update it at the gym.
* I'm a PT and want looking for an application to suggest to my client so he can have the exercises info when I'm not with him.
* I'm a gym owner looking for an App where my clients can find exercises suggestions

#### **Returning User:**

* I sign up for this application and using regularly. Now I want to change my exercise programa, and looking for exercises suggestions
* I want to update my exercises program info and know its duration

#### **Business Owner:**

* I want to gather exercises information to analyse the gathered information and in the future provided tailored exercises programs
* I want to have an application status page to I can understand how many users we have a summary of the saved data.


## **Design Process**

### **Strategy Plane:**

The main objective of this website is to make easier for people to access, add and edit their exercise program wherever they are. For that the application is designed mainly focused on mobile users, letting straight forward where to find information and how to edit it. The main page accessed will be the Program page wher the user can see their exercise list, as well as estimated duration to finish it.

### **Scope Plane:**

The key features that this project aims to attend are:

* Having a Program page easily accessible though a smartphone where the only the necessary info is displayed
* Provide a tool to edit the exercise program, leeting the user to add, edit or delete an exercises
* Show the user status in the application for reference
* Promote exercises saved in the application by other users trough the Search page for inspiration and let the user able to copy it to their own program.

### **Skeleton Plane:**

The wirefram of this project aimed to create simple but effective pages, where the information can be seen and collected easlily, and only necessary elements are displayed. For that it was decided that the website wouldn't much have images, so it can load fast as well.

The layout of the wireframes where designed using Figma, as an starting point of how to display the project goal in a simple and direct format, in any kind of device.

To improve page load speed, it was decided to not add external Font styles in this project. The visual style was developed taking in cosideratin the elements and styles available on the Materialize CSS Framework, that will be used to develope the website.

### **Wireframes**:

The project wireframes can be accesed [clicking here](https://www.figma.com/file/n45E2cE93O04XF5NEsHYW7/Untitled?node-id=0%3A1).

Mobile:

![wireframe mobile](static/images/fed_wireframe_mobile.jpg)

Tablet / Desktop:

![wireframe tablet and desktop](static/images/fed_wireframe_desktop.jpg)


### **Surface Plane:**

As the project aims to simple and fast, it was decided use some componets largely used in the Front End webdesing nowadays to improve its visuals, such as: Aurora effects with gradient colors, Glassmorfism and Collapsibles accordions.

The color scheme aims to have a vibrant feeling that stands out and hype the user for his exercise session, while keeping a modern and not distractive visual.

![collor pallet](static/images/color_scheme.png)

##CONTNUAR DAQUI

The typography used aimed to have complimentry fonts, that are similar but distinct enouch to create some contrast. The fonts used are the **Libre Franklin** and **Khula** imported from Google Fonts, and in case they can't be loaded, the fall back is Sans Serif as it will always be loaded correctly.

The images used are from [Delesign](delesign.com) and were customized to fit the project color scheme and design. They are used as visual reference for the seach pages, and have modern look and feel.

The project layout are stategicly simple, to maintaind the user focus on the experience the website wants to provide. All pages can be easly accesses by a common Header Navigation menu on all pages, and it was decided that there was no need for a Footer at the moment.

The homepage have to cards that stands out to inform the user how the website can be used, and have attractive call to action button. The search pages aims to provide a good user experiences and display the information searched in a simple and direct format.

In the Search map page uses the Open BreweryDB API to find all breweries lagtuded and logitude in the area searched, and the Google Maps API is used to display the breweries found on that location though some Pins added to the Map.

The Search info pages uses the Open BreweryDB API to retrive the breweries information found that matches with the term serched. Than a javascrip code is used to insert that information through cards in this page.


## **Features**

All project features can be accessed at any time throfh the Header Navigation menu that is commom to all pages.

### **Consistent features across all pages:**

* A header with the website logo and name, with a responsive navigation menu that on depenging on the screen size can shriks to be displayed through a hamburger menu.

### **Home:**

* Two cards that informs what can be done in the website, and attract the user attention to its call to action button, so the main project pages are accessed.

### **Search Map:**

* A large title is displayed to suggest the user to search a location, letting clear that **needs to be in the United States**.
* The input field informs though a place holder where the search term needs to be inserted, and clear that it **needs to be a city**.
* A map where the breweries location information found using the search term are displayed thought Pins.

### **Brewery info:**

* A large title is displayed to suggest the user to search a brewery and know more about it.
* The input field informs though a place holder that the search names **needs to be a brewery name**.
* It is alos displayed a card informing that any part of the brewery name can be searched, and that some brewery information can be not found (that's is a known limitation of the Open BreweryDB API, and as a result a limitation of this project at the moment)
* All the inforation retrived on the Open BreweryDB API using the searched term are displayed on cards.

### **Contact us:**

* A form is provided where the used basic information (Name and Email) are collected, letting possible to easily send a message to the website manager. By using the EmailJS API, this messaged is sent the website manager.

### **Features I could implement in the future:**

* Let possible to be searched any location, not only a city and not only in the Unite States.
* Display more breweries information, speciall the beers produced and some individual visual representation (like a logo or product image)

## **Technologies Used**

### **Languages, libraries, frameworks, editors and version control**

* HTML5 - To create and add content to the website.
* CSS3 - To style the website content and provide responsiveness. 
* JavaScript - Used get the terms searched and through the APIs utilized in this project find the brewries information and display it to the user. 
* [Bootstrap](https://getbootstrap.com/) - This framework was used on the website Header and Navigation menu.
* [VS Code](https://code.visualstudio.com/) - The development tool used to write the website code
* [GitHub](https://github.com/) - Used for version control, host files and deploy website.

### APIs**

* [Google Maps Platform](https://developers.google.com/maps/documentation) - Used to display the map and the breweries locations.
* [Open Brewery DB](https://www.openbrewerydb.org/) - Used to get all breweries informations necessary for this project.
* [EmailJS](https://www.emailjs.com/) - Used to get the information send on the website contact form and send it to the website manager.

### **Other Tools Used**

* [Figma](https://figma.com/) - To create website wireframes.
* [Delesign](delesign.com) - Images
* [Google Fonts](https://fonts.google.com/) - Primary website font
* [Logo Maker](https://logomakr.com/)- Used to create the website logo
* [Font Awesome](https://fontawesome.com/) - Icons on Events and Riders page. 

### **Educational Resources**

* [CSS Tricks](http://css-tricks.com/) -  Mainly used as a resource to help with Flexbox positioning
* [Stack Overflow](https://stackoverflow.com/) - Used to find the reason of some errors found during the website development.

//Continuar daqui

## **Testing**

### **Testing User Stories:**

*   New user: 
    *   Looking for a new bicycle on the internet, I found Push & Pedal website. I could find their products easily, since the first banner and link directs me to their product page. 
*   Returning user: 
    *   I bought a Push & Pedal bicycle and have some questions about the necessary maintenance. I’m commuting to my work, and had only my smartphone to access their website, and the contact information and form was very easy to find and access.
*   Business owner: 
    * I’m pleased with the consistency of the design on different devices. Having a banner inviting to join our event helped the promotion and to increase the number of participants.

### **Validating The Code:**

*   All HTML files validated with [W3C Markup Validation Service](https://validator.w3.org/)  - No Errors Found
*   CSS file validated with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - No Errors Found

### **Browsers testing**

Website tested on the following browsers manually, no error found

*   Chrome
*   Safari
*   Mozilla Firefox
*   Microsoft Edge

### **Responsiveness testing**

Website tested on the following devices manually or using Chrome Developer Tools, no error found

*   Iphone X
*   Ipad Pro
*   Google Pixel
*   Macbook Pro 16”
*   Desktop Monitor Philips 25”

## **Deployment**

The code of this project was written using [Gitpod](https://www.gitpod.io/) and deployed and hosted on [GitHub Pages](https://pages.github.com/), following the below steps:

1.   Opened [GitHub](https://github.com/) page and signed in
2.   Accessed the repository [user-centric-FED-project](https://github.com/pcantarelli/user-centric-FED-project)
3.   Go to **Settings**
4.   On the GitHub Pages sections selected on the dropdown menu **'Master Branch' > '/root'**
5.   Clicked on **Save**
6.  Website is live now [here GitHub Pages](https://pcantarelli.github.io/user-centric-FED-project/)

#### **Deploy your version of this project**

1.   Be sure to have GIT instaççed
2.  Clone [this repository](https://github.com/pcantarelli/user-centric-FED-project)
3. Follow the steps above to deploy your project on GitHub Pages

## **Credits**

### **Content**

This website was developed using the Code Institute project templated that can be found on [this repository](https://github.com/Code-Institute-Org/gitpod-full-template).

The Read.me file was based on Code Institute [readme-template](https://github.com/Code-Institute-Solutions/readme-template) and the [README.md](https://github.com/jacksheehy15/milestone-project-1) file created by my fellow colleague Jack Sheehy. Thank you so much for the inspiration.

The base code from the sections: [Header navbar](https://getbootstrap.com/docs/4.5/components/navbar/), [Hero slide](https://getbootstrap.com/docs/4.5/components/carousel/) and [Contact form](https://getbootstrap.com/docs/4.5/components/forms/) were based on the linked documentation from Bootstrap.


### **Media**

All images were taken online on [Unsplash](https://unsplash.com/), [Burst](https://burst.shopify.com/) and [Pure Cycles](https://www.purecycles.com/#) website. Really appreciated that support.

### **Acknowledgments**

I’d like to thank the Code Institute tutors and support staff. Their support definitely helped me to achieve all my goals on this project. 

Thanks to Mark Railton, my mentor, that also supported me during this project. 
