#                               PROCESSING AN API RESPONSE
#-- We'll write a program that automatically issues an API call and processes the results by
# identifying the most popular Python project on GitHub

# import requests

# # Make an API call and store the response.
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers = {'Accept': 'application/vnd.github.v3+json'}
# r = requests.get(url, headers=headers)
# print(f"Status code: {r.status_code}")

# # Store API response in a variable
# response_dict = r.json()

# # Process the results
# print(response_dict.keys())

""""
#-- We first import the requests module.
#-- We then store the API's url in the variable called "url"
#-- Github is on its 3rd version, so in headers we specify that we want to use this version for the
# API call then use requests to make the call to the API
#-- We call get() and pass it the url and the header that we defined and store that in a variable "r"
#-- The response object has an attribute called status code, which tells us whether a request was
# successful. (200= successful) We then print the status code to check 
#-- The API returen info in a JSON format, so we use the json() method to convert to a python 
# dictionary and store that in variable 'response_dict'
#-- Finally we print the keys from the response_dict and see the output

Output: 
Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])

#-- Request as successful.
"""

#                               wORKIG WITH THE REPSONSE DICTIONARY
#-- With the information from the API call stored as a dictionary, we can work with the stored there.
#-- Lets generate some output that sumarizes the information.

# import requests

# # Make an API call and store the response
# url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
# headers = {'Accept': 'application/vnd.github.v3+json'}
# r = requests.get(url, headers=headers)
# print(f"Status code:{r.status_code}")

# # Store API response in a variable.
# response_dict = r.json()
# print(f"Total repositories: {response_dict['total_count']}")

# # Explore information about the repositories
# repo_dicts = response_dict['items']
# print(f"Repositories returned: {len(repo_dicts)}")

# # Examine the first repository
# repo_dict = repo_dicts[0]
# print(f"\nKeys: {len(repo_dict)}")
# for key in sorted(repo_dict.keys()):
#     print(key)

""""
#-- We first print the value associated with "total_count", which represents the number of
# repositories on GitHub.
#-- The value associated with "items" is a list containing a number of dictionaries, each of which 
# contains data about an individual Python repository.
# We store the list of dictionaries in 'repo_dict', we then print the lenght of repo_dicts to see 
# how many repositories we have so far.
#-- To look closer at the info returned about each repository, we pull out the first item from
# 'repo_dicts' and store it in 'repo_dict'.
#-- We print keys on each repository to see how much information we have.
#-- Finally we then print all the dictionary keys to see what information is included.
"""


#                               SUMMARIZING THE FIRST REPOSITORY

import requests

# MAke an API call and store the response
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"status code: {r.status_code}")

# Store API in a variable
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore the informtion about the repositories
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository
repo_dict = repo_dicts[0]

print('\nSelected information about first repository')
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")

""""
this is our most started repository on Github
Output:

status code: 200
Total repositories: 8993728
Repositories returned: 30

Selected information about first repository
Name: awesome-python
Owner: vinta
Stars: 153952
Repository: https://github.com/vinta/awesome-python
Created: 2014-06-27T21:00:06Z
Updated: 2023-01-20T09:08:29Z
Description: A curated list of awesome Python frameworks, libraries, software and resources
"""

