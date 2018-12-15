import tweepy
print('test')

CONSUMER_KEY = 'Ddkqk4550f8aH0R7UxX3W3HLF'
CONSUMER_SECRET = 'wmMj0lahzYYep2j40XzfSBYDMCPEKeQgGCEal70eDwFCOqVhdt'
ACCESS_KEY = '927618808440901632-fbHTSzKxKscM7FZnBtcGKju4iy4RwzZ'
ACCESS_SECRET = 'hgPoEKEEdDeiWtEMEPmwmWgZR9TqCYJ2b3JqMah06yItY'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


mentions = api.mentions_timeline()

for mention in mentions:
    print(str(mention.id) + ' - ' + mention.text)
