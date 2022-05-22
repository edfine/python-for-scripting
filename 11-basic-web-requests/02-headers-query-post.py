import requests

# Sometimes HTTP requests include "query parameters" to indicate
# additional information that is not meant to be in the URL.
# For example, the github API allows you to search for repositories
# using the 'q' parameter. 
# Reference: https://docs.github.com/en/rest/reference/search
# Reference 2: https://docs.github.com/en/search-github/searching-on-github/searching-for-repositories

# Note the "params" option is a dictionary.
# 'q' is the name of the query parameter, and the value is 'org:Tebs-Lab+language:python'
response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'org:Tebs-Lab'}
)

# Query parameters are ultimately expressed as part of the URL:
print(response.url, "\n")

# Again, the Github API is returning JSON
content = response.json()
print(content)


# Lets look at the names and urls of the matched repositories.
for repo in content['items']:
    print(f'Name: {repo["name"]}\n{repo["html_url"]}\n')

# That last repo looks interesting... 
# lets save it for later.
cool_repo = content['items'][-1]['html_url']

# Another way you may want to modify your requests is by 
# adding header values. This is also done using a dictionary.

# In this example we're setting the User-Agent header, which 
# is used to tell the server what kind of program is making the 
# request. Many APIs use this data to rate limit bad acting user
# agents, track bots, or calculate metrics about who is using the
# service.
# 
# We're also setting the 'Accept' header, which tells the server
# what kind of data we're willing to get back. Some APIs can send
# their response in multiple formats, and they can accommodate our
# request for a particular kind of data.
# 
# This API, the dad jokes API, asks that we send both of these in it's
# documentation: https://icanhazdadjoke.com/api

# Many APIs will not respond, or will severely rate limit programs that 
# do not respect the API's requests.
response = requests.get(
    'https://icanhazdadjoke.com/',
    headers={
        'Accept': 'text/plain',
        'User-Agent': 'Tebs Lab Learn Python Bot|contact:https://www.tebs-lab.com/contracting'
    }
)

# Here's your random dad joke.
print(response.text, '\n')

# That was hilarious, lets save it for later...
dad_joke = response.text

# Finally, there are other kinds of requests besides GET.
# The second most common (behind GET) is POST, which is 
# typically used to send data, rather than receive it.
# Postman-echo is an API that simply returns whatever data
# you send to it, and can be useful in testing your code
# (or learning the basics...)
# Reference: https://www.postman.com/postman/workspace/published-postman-templates/documentation/631643-f695cab7-6878-eb55-7943-ad88e1ccfd65

# In addition to a url, POST needs you to specify the actual
# content you wish to send to the server.
 
response = requests.post(
    'https://postman-echo.com/post',
    headers={
        'Content-Type': 'application/json'
    },
    data={
        'name': "Tyler Bettilyon",
        'favorite_joke': dad_joke,
        'favorite_repo': cool_repo
    }
)

# Did we get the same data back?
print(response.json())


# Micro-exercise: Make a GET or POST request to the Postman Echo API.
# If you are making a GET, set some query parameters. If you are making
# a POST set some data. Either way, set at least the User-Agent header.