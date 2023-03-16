 Badware-Detective

Created by: Hope Tracy Njoroge

find the link to my project on Heroku here: 

Find the Github repository here:

# Introduction

This is an imagined program for a Cyber Security organization, in partial fulfilment with the Code Institute Full Stack Software Development course. It is targeted towards the Security Analysts, to check which malicious indicators are present in the company’s database and allow them to add any malicious indicators if not present to the database to protect the organization’s information assets. 

<br>

## [User Stories](#User-Stories)
## [FlowChart](#flowchart)
## [Design and Implementation](#design-and-implementation)
  ### [Features](#features)
## [Future Development](#future-development)
## [Technologies Used](#technologies-used)
## [Testing](#testing)
## [Deployment](#deployment)
## [Credits and Acknowledgements](#credits-and-acknowledgements)

<br>

## User Stories
### AS a user:
- I want to be able to run the program
- I want to understand what to do through the instructions
- I want to choose what to do when I start the program
- I want to query the database to check if any malicious indicators already exit   
- I want to get the results of the indicator after querring the database
- I want to be able to add an indicator(s) to the database
- I want to exit the program as when I am done and satisfied after performing an action 

<br>

## FlowChart
 Find logic chart ![here]()

<br>

## Design and Implementation
  ### Features

### Existing Features

- Program start:
  - When the program starts, the badware-detective banner is printed.
  - The program menu is displayed with options for the user to pick the action they'd like to perform.
  - Once they choose an option, they are given instructions on how to write their input.
  - If option one is choosen, they search for the indicator in the database and get all it's info if found.
  - If it's not in the databse, they are given they option to add it to the database.
  - if they choose option 2, they can add indicator directly to the databse. 
  - Afterwhich, they are able to exit the program.
  - a goodbye message is printed after exiting the program. 

![Welcome banner]()
![Instructions]()
![Program menu]()
![Option 1]()
![Option 2]()
![End program]()

<br>

## Future Development

- I would like to add a validation to avoid entry of duplicate values.
- I would like to add automation to detect indicator type and prefill the database.
- I would like to allow for multiple entries in the database.

<br>

## Technologies Used
- Git - Was used for version control, the Gitpod terminal to commit and push to GitHub.

- [GitHub](https://github.com/) - Was used to store the project code 

- [Lucid](https://lucid.app/documents#/dashboard) -  Was used to create the logic flowchart.

- [Heroku](https://www.heroku.com) - Was used to deploy the program.

- [Ascii Art](https://ascii.mastervb.net/) - Was used to design the welcome banner.

- [Regex101](https://regex101.com/r/fU2d35/1) - Used to verify that the regex patterns are correct.

- [Google Cloud API](https://cloud.google.com/apis) - API service used

- Googlesheets - Used as the database


<br>

## Deployment

  ###  Deployment via gitpod
- Log into GitHub.
- Make a repository
- Click the green button at the top of the page that says Gitpod.
- After letting Gitpod load an alert pops up on the top of the screen, click cancel.
- Then click the button that says More Actions.
- Hereafter click Open in Browser.
- Now right click with your mouse over the big box on the left that has your repository name over it.
- Click new file.
- Then make an index.html file. 
- Go to the top of the index file and click ! and enter. This will make a start template.
- Make a basic structure for your index page.
- Click on terminal at the bottom of the page.
- write 'git add .'
- Then for your first commit write 'git commit -m "Initial commit".
- Hereafter write 'git push'.
- Your code have now been pushed back and saved on your GitHub repository.

  ### Deployment via Heroku
- Log into your Heroku page on [Heroku website](https://www.heroku.com)
- Go to your dashboard click "new" and then click "create new app".
- Give your app a unique name and make sure it's availble and then choose a region.
- Click "create app" button.
- Go to the "settings page".
- If you are using a creds.js file, follow the next steps:
    1. Scroll down and find the button that says "reveal config vars" and click it.
    2. Then write "CREDS" inside the box that says "KEY".
    3. With you github open find the creds.js file and copy paste it into the box beside "KEY" that says "VALUE".
    4. Now click the "add" button.
- If not, scroll to find the buildpacks and click on "add buildpacks"  
- Click on "python" and then click "save changes" button.
- Repeat the last two steps but add the nodejs buildpack.
- Now click on "deploy page".
- Click connect to Github in the deployment method.
- Then you search in your repository for the one yo need. Ensure the name is exactly the same.
- Click the button "serch" and then click "connect"
- Choose between automatic deployment or manual deplpyment.
- If you choose manual, wait for it to finish.
- Now click the button "view"

<br>

## Credits


<br>


## Acknowledgements

- My Mentor Mitko Bachvarov, who walked me through my project idea, and gave me resources to help with different stages.
- Tutor support, who helped me debug my validation function.
- My husband, who has supported me this far in my course.
- Slack, which has been an endless pool of informational resources through this project. 