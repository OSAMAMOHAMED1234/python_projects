import tweepy
import pandas as pd


consumer_key = '' # https://developer.twitter.com/en/apps
consumer_secret = ''
callback_uri = 'oob'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback_uri)
redirect_url = auth.get_authorization_url()
print(redirect_url)
user_pint_input = input("What's the pin value? ")
auth.get_access_token(user_pint_input)
# print(auth.access_token, auth.access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
me = api.verify_credentials()
# print(me.screen_name)


# make tweet text & img
img_obj = api.media_upload("image.png")
new_status = api.update_status('Hello world from python what up?', media_ids=[img_obj.media_id_string])
new_status.destroy() # delete tweet


def extract_timeline_as_df(timeline_list):
  columns = set()
  allowed_types = [str, int]
  tweets_data = []
  for status in timeline_list:
    status_dict = dict(vars(status))
    keys = status_dict.keys()
    single_tweet_data = {'user': status.user.screen_name, 'author': status.author.screen_name}
    for k in keys:
      try:
        v_type = type(status_dict[k])
      except:
        v_type = None
      if v_type != None:
        if v_type in allowed_types:
          single_tweet_data[k] = status_dict[k]
          columns.add(k)
    tweets_data.append(single_tweet_data)
  header_cols = list(columns)
  header_cols.append('user')
  header_cols.append('author')
  df = pd.DataFrame(tweets_data, columns=header_cols)
  return df

user = api.get_user(screen_name='code')
user_timeline = user.timeline()
df = extract_timeline_as_df(user_timeline)

user_timeline_status_obj = user_timeline[0]
status_obj_id = user_timeline_status_obj.id
status_obj_screen_name = user_timeline_status_obj.user.screen_name
status_obj_url = f'https://twitter.com/{status_obj_screen_name}/status/{status_obj_id}'
status_obj = api.get_status('1468697516593930242')
print(status_obj.text)
api.retweet(status_obj_id) # retweet
api.create_favorite(status_obj_id) # like
api.destroy_favorite(status_obj_id) # dislike

# reply on a tweet
og_tweet = api.get_status('1468697516593930242')
my_reply = api.update_status(f'@{og_tweet.user.screen_name} Wow this cool!', og_tweet.id)
print(my_reply.id, my_reply.user.screen_name)


# follow
user = api.get_user(screen_name='code')
print(user.followers_count, user.friends_count)
my_new_friends = []
user_friends = user.friends()
for friend in user_friends:
  if friend.followers_count > 300 and friend.friends_count < 300:
    my_new_friends.append(friend.screen_name)
    relationship_ = api.create_friendship(friend.screen_name)


# unfollow
to_remove = my_new_friends[:-1]
for username in to_remove:
  api.destroy_friendship(username)


len(api.home_timeline(count=40))
for i, status in enumerate(tweepy.Cursor(api.home_timeline, count=50).items(50)):
  print(i, status.text)


# profile
other_user = 'code'
for i, status in enumerate(tweepy.Cursor(api.user_timeline, screen_name=other_user).items(20)):
  print(i, status.text)


# followers
the_rock_user = api.get_user(screen_name=other_user)
the_rocks_friends = []
for i, _id in enumerate(tweepy.Cursor(api.get_friend_ids, screen_name=other_user).items(30)):
  print(i, _id)
  the_rocks_friends.append(_id)


# search tweets
query = '#django -Discount' # -word => remove word from search results
for i, status in enumerate(tweepy.Cursor(api.search_tweets, q=query).items(50)):
  print(i, status.text, status.author.screen_name)


# search users
query_username = 'code'
search_results = set()
for i, user in enumerate(tweepy.Cursor(api.search_users, q=query_username).items(50)):
  print(i, user.screen_name)
  search_results.add(user.screen_name)
print(list(search_results))


# search users
query_username = 'code'
def process_page(page_results):
  for i, user in enumerate(page_results):
    print(i, user.screen_name)
for i, page in enumerate(tweepy.Cursor(api.search_users, q=query_username, per_page=10).pages(3)):
  print(i, 'page')
  process_page(page)


# custom rate limit handler
import time
def limit_handled(cursor):
  while True:
    try:
      yield cursor.next()
    except tweepy.RateLimitError:
      time.sleep(15 * 60)
for follower in limit_handled(tweepy.Cursor(api.followers).items()):
  print(follower.screen_name)