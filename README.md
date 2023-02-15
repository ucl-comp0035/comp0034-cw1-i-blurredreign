[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=10018240&assignment_repo_type=AssignmentRepo)
# COMP0034 Coursework 1 template repository

To set up your project:

1. Clone this repository in your IDE (e.g. PyCharm, Visual Studio Code) from GitHub. Follow the help in your IDE
   e.g. [clone a GitHub repo in PyCharm.](https://www.jetbrains.com/help/pycharm/manage-projects-hosted-on-github.html#clone-from-GitHub)
2. Create and then activate a virtual environment (venv). Use the instructions for your IDE
   or [navigate to your project directory and use python.](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
3. Install the requirements from requirements.txt. Use the instructions for your IDE
   or [the pip documentation](https://pip.pypa.io/en/latest/user_guide/#requirements-files).
4. Edit .gitignore to add any config files and folders for your IDE. 


# Set-up instructions

Install the requirements.txt file using "py -m pip install -r requirements.txt"
Can also run the setup.py file using "pip install -e ."
Then typing typing "python app.py" in command will open the app

Add the URL to your GitHub repo here:
https://github.com/ucl-comp0035/comp0034-cw1-i-blurredreign

# Visualisation design

(in visualisation_design.pdf)

# Dash app

When "All" and "Bar" are selected at the same time, the graph looks faint but this is because of the number of data points- if you zoom in manually, each individual bar can be seen.

I manually added "All" to the list of years for each resource, so that this would appear in the dropdown menu and I could code this to show the full dataset, as originally I had issues with it only appearing when I cleared the dropdown value.

The function "yearlist_func" was used to extract the years in the datasets, as then I could use this for the dropdown menu and allow the user to choose which year they wish to look at.

I was planning to add a histogram as well, by looping through the monthly datasets and finding which month in each year had the greatest and lowest values and adding this to a respective counter, then plotting this counter against a list of the months, into the px.hist function, but I did not have time to finish this.

Added clearable=False to the options of every dropdown so that the user does not have the option to clear the value - I found that trying to implement this caused more errors with drawing the graph, and it was more intuitive to remove the option to clear, and ensure all options to graphing were coded.

# Testing

Add evidence here (groups).
