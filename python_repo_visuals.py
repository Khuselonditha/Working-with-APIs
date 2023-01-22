#                               VISUALIZING REPOSITORIES USING PLOTLY
#-- Visualisation using data from an API call to show relative popularity of python projects on
# GitHub.
#-- We'll Create an interactive bar chart: height of each bar will represent the number of stars
# the project has acquired, and you can click the bar's label to go that projects page on GitHub>

# import requests
# from plotly.graph_objs import Bar
# from plotly import offline

# # Make an API call and store the reponse
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers = {'Accept': 'application/vnd.github.v3+json'}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# # Process the results
# response_dict = r.json()
# repo_dicts =response_dict['items']
# repo_names, stars = [], []
# for repo_dict in repo_dicts:
#     repo_names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])

# # Make visualization
# data = [{
#     'type': 'bar',
#     'x': repo_names,
#     'y': stars,
# }]
# my_layout = {
#     'title': "Most-Starred Python Projects Hosted on GitHub",
#     'xaxis': {'title': 'Repository'},
#     'yaxis': {'title': 'Stars'}
# }

# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='python_repos.html')


""""
#-- we first import the Bar class and the offline module plotly.
#-- We don't import the layout because we'll use a dictionary approach when we define the layout like
# in defining data.
#-- We still print the status code for the API call to see if it was successful.
#-- We then create two empty lists to store the data we'll include in our chart.
#-- We assign the label of xaxis as the name of the each project and the amount of stars as the yaxis
#-- Next we define the data list. This contains a dictionary, which defines the type of plot, and 
# provides the data for the x- and y-values.
#-- We also define the layout for this chart using the dictionary approach. We set a title for the
# for the overall chart and we define a label for each axis.
"""


#                               REFINING PLOTLY CHARTS
#-- refine the chart's style

# import requests
# from plotly.graph_objs import Bar
# from plotly import offline

# # Make an API call and store the response
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers = {'Accept': 'application/vnd.github.v3+json'}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# # Process the data
# response_dict = r.json()
# repo_dicts = response_dict['items']
# repo_names, stars = [], []
# for repo_dict in repo_dicts:
#     repo_names.append(repo_dict['name'])
#     stars.append(repo_dict['stargazers_count'])
    
# data = [{
#     'type': 'bar',
#     'x': repo_names,
#     'y': stars,
#     'marker': {
#         'color': 'rgb(60, 100, 150)',
#         'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
#     },
#     'opacity': 0.6,
# }]
# my_layout = {
#     'title': 'Most-starred Python Project Hosted on GitHub',
#     'titlefont': {'size': 28},
#     'xaxis': {
#         'title': 'Repository',
#         'titlefont': {'size': 24},
#         'tickfont': {'size': 14},
#     },
#     'yaxis': {
#         'title': 'Stars',
#         'titlefont': {'size': 24},
#         'tickfont': {'size': 14},
#     },    
# }

# fig = {'data': data, 'layout': my_layout}
# offline.plot(fig, filename='python_repos(1).html')

"""
#-- The marker settings affect the design of the bars.
#-- We set a custom blue color for the bars and specify the they'll be outlined with a dark grey 
# line tha's 1.5 pixel wide
#-- We also set the opacity of the bars to 0.6 to soften the appearance of the chart a little.
#-- We use the 'titlefont' key to define the font size of the overall chart. 
#-- Within the 'xaxis' dictionary, we add settings to control the font size of the of the x-axis
# title 'titlefont'  and also of the tick labels 'tickfont', you can also set the color and font 
# family of the axis title and tick labels since they are nested dictionaries.
#-- We define the same settings for the y-axis.
"""


#                               ADDING CUSTOM TOOLTIPS
#-- Add hover effect when you move over an individual bar to show the infomation the bar represents.
#-- This is called tooltips, in our example, it will show each's project description as we as the 
# projects owner.

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process the data
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    label = f"{owner}<br />{description}"
    labels.append(label)

# Make visualization
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'},
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'Most-Starred Python Projects Hosted on GitHub',
    'titlefont': {'size': 28},
    'xaxis': { 
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
    'yaxis': { 
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos(2).html')

""""
#-- we first define a new empty list to hold the text we want to display for each project.
#-- In the loop where we process data, we pull the owner and the description for each project.
#-- We can use HTML code with Plotly, we use a line break "<br/" between projects owner's username
# and the description and store it in the list of labels.
#-- In the data dictionary, we add the entry with the key "hovertext" and assign it to the 'labels'
# list we've created.
#-- Plotly creates eaach bar and pulls labels from the "labels" list and only display them when the
# viewer hovers over a bar.
"""