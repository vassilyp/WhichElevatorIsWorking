# WhichElevatorIsWorking

This is a simple website (HTML/CSS) to show whether the elevators in Marine Drive are operational. The project was inspired by one of the elevators in my dorm being down for 3-4 months, and the other being less than reliable!

Check out the website here: https://vassily-petrousevitch.github.io/WhichElevatorIsWorking/


### Moving parts:

This site is mobile responsive!

I have a basic html file containing markup, with vanilla CSS for styling.
One neat part is the "(not) working" section (eg. line 37-39) where a CSS class hides text based on whether the elevator is working. 

Not much to explain for CSS, mainly just styling. The only clever part is changing the colours/text based on whether the 'working' class exists.

I have a python script (update_elevators.py) that parses index.html using the BeautifulSoup library, modifies the left_lift/right_lift elements to either include the 'working' class. This is used by update_elevators.yml, which then automatically pushes the changes to master.

Feel free to shoot me a message if you'd like to know more about this project :smile: