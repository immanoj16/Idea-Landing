# Creating an Idea Landing Page

Launching on your own project:
  1. Create & Activate Virtualenv:
        ```
        $ cd ~/desktop
        $ virtualenv IdeaLanding && cd IdeaLanding
        $ .\Scripts\activate # to activate the virtual environment
        ```
  2. Clone project:
        ```
        $ md src && cd src
        $ git clone https://github.com/immanoj16/Idea-Landing .
        $ pip install -r requirements.txt
        ```
  3. Remove & Start new Git Repo:
        ```
        $ del .git # removes old git repo
        $ git init # creates your new repo
        $ git add --all # or git add . # or git add *
        $ git commit -m "Initial Commit"
        ```
  4. Create Heroku App:
        In src folder:
        ```
        $ heroku create
        ```
        
        In `production.py` add your newly created url such as `https://<yourapp>.herokuapp.com/` to `ALLOWED_HOSTS`. Save `production.py`
        
        ```
        $ git add --all
        $ git commit -m "Updated production"
        ```
   5. Add Database & Deploy:
        ```
        $ heroku addons:create heroku-postgresql:hobby-dev
        $ git push heroku master
        $ heroku run python manage.py migrate
        $ heroku run python manage.py createsuperuser
        ```
