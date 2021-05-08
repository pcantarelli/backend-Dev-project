# **Fitness Exercise Development**

## **Backend Development Project - Code Institute**

&nbsp;
![website mockups](documentation/mockups.jpg)

The Fitness Exercise Development (FED) is a website created to save your exercise program info. The idea is that it works as an application that you can access like a website, and the primary focus is on the mobile view (as it will be mainly accessed during a gym session)

This project is part one of the four milestone projects of the Code Institute Full Stack Developer course and aims to show an interactive website using HTML5, CCS3, and Javascript, using Python and Flask to manage the application backend and MongoDB to store its information.

Access the website here: [Fitness Exercise Development](http://fitness-exercise-development.herokuapp.com/)

&nbsp;

## **Table Of Contents**

- [User Experience](<#user-experience-(ux)>)
- [Design Process](#design-process)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Testing](#testing)
- [Deployment](#deployment)
- [Credits](#credits)
- [Acknowledgments](#acknowledgments)

&nbsp;

## **User Experience (UX)**

### **Project Goals:**

- Display the exercise program on a single page
- Create, read, edit and delete exercises through the application website
- Show User status info
- Show App status info to Admin
- Search exercises and be able to add them to your program

### **User Stories**

#### **New Users:**

- I go to the gym regularly and looking for a way to save my exercise program info, and be able to update it at the gym.
- I'm a PT and want an application to suggest to my client so he can have the exercise info when I'm not with him.
- I'm a gym owner looking for an App where my clients can find exercises suggestions

#### **Returning User:**

- I sign up for this application and using regularly. Now I want to change my exercise program, and looking for exercises suggestions
- I want to update my exercises program info and know its duration

#### **Business Owner:**

- I want to gather exercises information to analyze the gathered information and in the future provided tailored exercises programs
- I want to have an application status page, so I can understand how many users we have a summary of the saved data.

## **Design Process**

### **Strategy Plane:**

The main objective of this website is to make it easier for people to access, add and edit their exercise program wherever they are. For that the application is designed mainly focused on mobile users, letting straight forward where to find information and how to edit it. The main page accessed will be the Program page where the user can see their exercise list, as well as the estimated duration to finish it.

### **Scope Plane:**

The key features that this project aims to attend are:

- Having a Program page easily accessible through a smartphone where only the necessary info is displayed
- Provide a tool to edit the exercise program, letting the user add, edit or delete an exercises
- Show the user status in the application for reference
- Promote exercises saved in the application by other users through the Search page for inspiration and let the user able to copy it to their own program.

### **Skeleton Plane:**

The wireframes of this project aimed to create simple but effective pages, where the information can be seen and collected easily, and only necessary elements are displayed. For that, it was decided that the website wouldn't have many images, so it can load fast as well.

The layout of the wireframes was designed using Figma, as a starting point of how to display the project goal in a simple and direct format, on any kind of device.

To improve page load speed, it was decided to not add external Font styles in this project. The visual style was developed taking into consideration the elements and styles available on the Materialize CSS Framework, that will be used to develop the website.

### **Wireframes**:

The project wireframes can be accessed [clicking here](https://www.figma.com/file/n45E2cE93O04XF5NEsHYW7/Untitled?node-id=0%3A1).

Mobile:

![wireframe mobile](documentation/fed_wireframe_mobile.jpg)

Tablet / Desktop:

![wireframe tablet and desktop](documentation/fed_wireframe_desktop.jpg)

### **Surface Plane:**

As the project aims to simple and fast, it was decided to use some components largely used in the Front End web design nowadays to improve its visuals, such as Aurora effects with gradient colors, Glassmorfism, and Collapsible accordions.

The color scheme aims to have a vibrant feeling that stands out and hypes the user for his exercise session while keeping a modern and not distractive visual.

![collor pallet](documentation/color_scheme.png)

The icons used in the website are from [Font Awesome](https://fontawesome.com/) and were used in the project logo and as a visual reference for each page.

All pages can be easily accessed through the cards on the Home page or through the application navigation menu, which in the mobile view is displayed through a hamburger icon and side menu for the best usage of space.

In the Program page and Editor, it was used collapsible accordions to don't pollute the page information, and display only the information the user really wants to see. The Search page is provided for users to find exercise inspirations and a button to easily copy the card information to your own Program. Lastly, the profile page shows the user info registered as well as their info status.

The Admin user has access to the App Status page, where he can verify some information from this application project, which can be used for future project upgrades.

## **Features**

Through the Header Navigation menu that is common to all pages, the user can access all project features that are displayed on different pages.

### **Consistent features across all pages:**

- Header section with a responsive menu and logo. The menu can be accessed only by users that logged in to the application.
- Footer section with project information and social logo.

### **Home:**

- Four cards where the user can access any of the application's features (Program list, Program Editor, User profile and Search functionality).
- The Admin user can see the fifth card to access the App Status page.

### **Index:**

- Index page shows a responsive and animated card where users can select either to register in the application or to log in.

### **Programa:**

- On this page users can see all their exercises registered in the application, separated by muscle group. The exercise cards are presented in a collapsible accordion. At the top is displayed an estimated time to complete the whole program.

### **Editor:**

- On the Editor page, the user can add a new exercise to their program through a button that links to the Add Exercise page. It is also presented their current exercises card similarly to the Program page, but with two extra buttons to Edit or Delete an exercise.

### **Add Exercise:**

- This page displays a form where the user can add a new exercise to their program. The form is presented with the same card layout from the Program page, so the user can have a better understanding of how the information will be displayed after saved. There is a button to cancel the creation of a new exercise and a button to save it.

### **Edit Exercise:**

- This page displays the same form and feature of the Add Exercise page, but with the exercise information registered previously by the user that he wants to change.

### **Profile:**

- This page shows the user information added through the Register form
- It is also displayed some application status from the specific used logged.

### **Search:**

- The Search page shows a search box input and a brief explanation of how the user can use this page.
- Upon searching a word, the page shows the search result with the same layout used on the Program page, where the cards displayed contain the search query word. To test it, you can search for "Shoulder" or "Legs"

### **App Status:**

- On this page, the Admin can see some applications status information, such as the quantity of user registred, quantity of exercises registered, etc.
	

### **Features I could implement in the future:**

- Add the possibility to have more than one program per user
- Personalized exercises recommendations
- Add videos to exercises cards
- Add contact page

## **Technologies Used**

### **Database**

Due to the current simplicity of this project, it was decided to use a NoSQL Database. All databases and datasets are storeged on [MongoDB](https://www.mongodb.com/), where the application can consult all the necessary information as objects.

#### **Database structure:**

![Database Structure](documentation/db_diagram.jpg)

### **Languages, libraries, frameworks, editors, and version control**

- HTML5 - To create and add content to the website.
- CSS3 - To style the website content and provide responsiveness.
- [Materialize CSS](https://materializecss.com/) - This framework was used on the website Header and Navigation menu.
- JavaScript - Used to display displayed the components from Materialize CSS and to animate the Index form slider.
- [jQuery](https://jquery.com/) - Javascript library to manipulate the website content
- Python - To write the backend code
- [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Python Framework to manage templates, routes, and queries
- PyMongo - Python library to query Mongo Databases
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Template language to create all pages
- [MongoDB](https://www.mongodb.com/) - To create and store application databases
- [VS Code](https://code.visualstudio.com/) - The development tool used to write the website code
- [GitHub](https://github.com/) - Used for version control and host files.
- [Heroku](https://www.heroku.com/) - To deploy application

### **Other Tools Used**

- [Figma](https://figma.com/) - To create website wireframes.
- [Trianglify.io](https://trianglify.io/p/w:1440!h:900!x:f72585.b5179e.7209b7.560bad.3a0ca3.3f37c9.4361ee.4895ef.4cc9f0!v:0.87!c:0.1!s:maok0j!f:sp!i:0.11) - Index page image
- [Glassmorphism](https://glassmorphism.com/) - To create glassmorphism effects
- [Youtube](https://www.youtube.com/watch?v=gBWRCe0HuQU&ab_channel=TheWebShala) - Inspiration for the index form desing
- [Font Awesome](https://fontawesome.com/) - Icons on Events and Riders page
- [dbdiagram.io](https://dbdiagram.io/) - Used to create databases diagrams on Readme file

### **Educational Resources**

- [Code Institue](https://courses.codeinstitute.net/) - Main source of content where the project inspiration and code design came from-
- [CSS Tricks](http://css-tricks.com/) - Mainly used as a resource to help with Flexbox positioning
- [Stack Overflow](https://stackoverflow.com/) - Used to find the reason for some errors found during the website development and for code inspiration to create the background aurora effect.

## **Testing**

### **Testing User Stories:**

- New user:
  - Looking for a new exercise web application on the internet, I found FED and could register my account and add new exercises to it.
- Returning user:
  - I accessed the web application at the Gym through my smartphone and could access my exercise program and modify it when I needed it.
- Business owner:
  - I’m pleased with the consistency of the design on different devices. Having the App Status page information is really helpful to understand how many users I have at the moment.

### **Manual testing**

- CRUD functionalities tested on Program, Editor, Add and Edit Exercises pages:
  - Add Exercise button
  - Add Exercise form
  - Edit Exercise button
  - Edit Exercise form
  - Delete Exercise button
  - Read Exercises lists through application pages
- Navigation tests:
  - Tested Navigation menu links on Desktop
  - Tested Navigations sidebar links menu on Mobile
  - Tested Page cards on the Home page
- Tested error pages
- Tested access to the App Status page only for Admin user
- Tested on all input fields forms to accept only characters acceptable by the code pattern
- Tested Search page looking for "Triceps", "Squal", "Biceps" and adding the found exercises cards to my own program
- Tested Profile page comparing information loaded with Database information

### **Validating The Code:**

- All HTML files validated with [W3C Markup Validation Service](https://validator.w3.org/) - No real HTML code errors found
- CSS file validated with [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) - No real CSS code errors found
- The Javascrip files viladated with [JSHint](https://jshint.com/) - No real Javascrip code errors found
- Python code files validaded with [PEP 8 online](http://pep8online.com/) - No Python code errors found

### **Browsers testing**

Website tested on the following browsers manually, no error found

- Chrome
- Safari
- Mozilla Firefox
- Microsoft Edge

### **Responsiveness testing**

Website tested on the following devices manually or using Chrome Developer Tools, no error found

- iPhone X
- Ipad Pro
- Google Pixel
- MacBook Pro 16”
- Desktop Monitor Philips 25”

## **Deployment**

The project was written using VS Code, all files hosted on Github, Databases stored in MongoDB and deployed on Heroku, which can be accessed [clicking here](http://fitness-exercise-development.herokuapp.com/).

### **Local development**

To clone this project in your local machine you should certify that you have Git and Python installed locally, and follow the below steps:

1. Clone this repository in your machine using the command:

   ```
   gh repo clone pcantarelli/backend-Dev-project
   ```

2. Access / create an account on [MongoDB](https://www.mongodb.com/) to create your own databases to be used in this project.
3. Return to your Terminal and enter the following to install all required dependencies:

   ```
   pip3 install -r requirements.txt
   ```

4. Create an env.py file with the following content, replacing the 'mongo_secret_key', username','password', 'cluster_name' and 'database_name' with your MongoDB database values:

   ```
   import os

   os.environ.setdefault("IP", "0.0.0.0")
   os.environ.setdefault("PORT", "5000")
   os.environ.setdefault("SECRET_KEY", "<mongo_secret_key>")
   os.environ.setdefault("MONGO_URI", ""mongodb+srv://<username>:<password>@<cluster_name>.5urck.mongodb.net/<database_name>?retryWrites=true&w=majority&ssl=true&ssl_cert_reqs=CERT_NONE")
   os.environ.setdefault("MONGO_DBNAME", "database_name")
   ```

5. Add your env.py file to .gitignore to make sure your database information is not viewable to others
6. Your cloned version is now ready to run locally with the following command:

   ```
   python3 app.py
   ```

### **Deploying project to Heroku**

To deploy this project, create your repository of this project in your Github account, create an account on [Heroku](https://www.heroku.com/), and follow the below steps:

1. On your Terminal, in the project directory folder create a requirements.txt file with the below command:

   ```
   pip3 freeze --local > requirements.txt
   ```

2. Created a Procfile with the below command, and ensures that it has an extra empty line on the last line of the file created:

   ```
   echo web: python app.py > Procfile
   ```

3. Commit and Push those changes to your repository on Github.
4. On your Heroku account, create a new app with the desired name.
5. On the 'Deployment Method' section of Heroku, link your GitHub profile and repository.
6. On the Config Vars section in the Settings tab, add the relevant key/value information from my env.py (IP, PORT, MONGO_URI, MONGO_DBNAME, SECRET_KEY).
7. On the "Deploy" tab. select Master Branch under "Choose a branch to deploy" and click "Enable Automatic Deploys".
8. Once de deployment is finished, clicked "View" to launch the app and see it on your browser.
9. All new Pushs to your Github repository will be automatically deployed on Heroku.

## **Credits**

### **Content**

This website was developed using the Code Institute project template that can be found on [this repository](https://github.com/Code-Institute-Org/gitpod-full-template). The Read.me file was based on Code Institute [readme-template](https://github.com/Code-Institute-Solutions/readme-template) on my previous projects Read.me files and on [Chloe's Read.me](https://github.com/chloelewisdev/milestone-project-3#Technologies-Used) file. Thank you so much for the inspiration.

Some base code sections are from [Materialize CSS](https://materializecss.com/) documentation, such as the Header, Navigation menu, Alert pop-up, and Collapsible accordions. The background aurora gradient color was inspired by the Stackoverflow discussion about [Instagram new logo CSS background](https://stackoverflow.com/questions/37751375/instagram-new-logo-css-background).

### **Media**

All icons are from [Font Awesome](https://fontawesome.com/).

### **Acknowledgments**

I’d like to thank the Code Institute tutors and support staff. Their support definitely helped me to achieve all my goals on this project. Thanks to Aaron Sinnott, my mentor, that also supported me during this project.
