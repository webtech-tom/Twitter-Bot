# Twitter Bot
This is my Twitter bot in Python. Twitter me with ```#HelloWorld``` and the bot retweet back to you.

# Set up notes
How to install Tweepy
First, check your Python version with ```python3 --version``` or ```python --version``` on console (terminal/shell/command prompt).

## If you don't have Python 3 installed (if the above command fails):
Install Python 3 on your computer or use something like PythonAnywhere.

## If you have Python 3.6, you can just run:
```pip3 install tweepy```

## If you have Python 3.7, run the following instead:
```pip3 install -U git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b```

If the above command doesn't work, try replacing pip3 with pip also.

## If you have Python 3.7 and want to use pipenv, use:
```pipenv install -e```
```git+https://github.com/tweepy/tweepy.git@2efe385fc69385b57733f747ee62e6be12a1338b#egg=tweepy```

# Files
- **my_twitter_bot.py** -- This is the main file that includes all the logic.
- **last_seen_id.txt** -- This will contain the ID of the tweet that my_twitter_bot.py has seen last. If you see any errors when running the main file, try replacing the content with the ID of one of the tweets you want to examine.

Put your Twitter API keys in a file named keys.py. That way, my_twitter_bot.py will be able to use this information.

**keys.py format**:

CONSUMER_KEY = 'Include your Twitter Consumer Key'

CONSUMER_SECRET = 'Include your Twitter Consumer Secret'

ACCESS_KEY = 'Include your Twitter Access Key'

ACCESS_SECRET = 'Include your Twitter Access Key'
