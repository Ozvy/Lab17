import requests
from operator import itemgetter
'''
Refactoring and Catching Errors of Existing Script
Ender Whittington
5/10/2025
'''
# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    # Make a separate API call for each submission.
    url= f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary from each article. 
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),
        }
    except KeyError as e:
        print(f'Error: {e} is missing from an article')
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Print out each of the articles.
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")