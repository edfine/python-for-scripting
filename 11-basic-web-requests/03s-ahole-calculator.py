import requests


# Get the top posts from today.
all_listings_response = requests.get(
    'https://www.reddit.com/r/AmItheAsshole/top/.json?t=day',
    headers={
        'User-Agent': 'top-daily-ahole-calculator-bot'
    }
)


# Extract today's top n posts (set to 3 here to reduce rate limiting):
n_posts = 3
top_n_post_urls = []
for post in all_listings_response.json()['data']['children'][:3]:
    top_n_post_urls.append(post['data']['url'])

post_to_votes = {}
for url in top_n_post_urls:
    # fetch the comments
    comment_response = requests.get(
        url + '.json',
        headers={
            'User-Agent': 'top-daily-ahole-calculator-bot'
        }
    )
    comments_json = comment_response.json()

    votes = {
        'YTA': 0,
        'NTA': 0,
        'ESH': 0,
        'NAH': 0
    }

    # The comments listing is always the second item in the post.
    comments = comments_json[1]['data']
    for comment in comments['children']:
        if comment['kind'] != 't1': continue # t1 is the comment type, sometimes other types appear like "more"
        text = comment['data']['body']
        
        for vote_type in votes.keys():
            if vote_type in text:
                votes[vote_type] += 1

     # Some API's have deeply nested (and weird) data patterns, look at this monstrosity:
    votes['situation'] =  comments_json[0]['data']['children'][0]['data']['selftext']
    post_to_votes[url] = votes



ahole_format_string = """
URL: {url}
The Situation: {situation}

Votes:
YTA: {YTA}
NTA: {NTA}
ESH: {ESH}
NAH: {NAH}
"""
print('f======Top {n_posts} Daily AHole Judgements====')
for url, votes in post_to_votes.items():
    print(ahole_format_string.format(url=url, **votes))

