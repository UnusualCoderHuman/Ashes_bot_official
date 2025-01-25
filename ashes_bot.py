import tweepy
import os
from datetime import date, datetime

# Fetch Twitter API credentials from environment variables
API_KEY = os.getenv('API_KEY')
API_SECRET_KEY = os.getenv('API_SECRET_KEY')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')



# Authenticate with the Twitter API
client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Dates to calculate elapsed days
last_day_england_won_ashes = date(2015, 8, 8)  
last_day_england_held_ashes = date(2017, 12, 18)  

#twitter_account: https://x.com/englands_urn

def daily_tweet():
    today = date.today()
    # Calculate the number to tweet based on days elapsed since start_date
    days_elapsed_since_winning = (today - last_day_england_won_ashes).days
    days_elapsed_since_holding = (today - last_day_england_held_ashes).days
    timestamp = datetime.now().strftime("%H:%M:%S")
    try:
        # Post the tweet
        client.create_tweet(
            text=(
                f"{days_elapsed_since_winning} days since England last regained the Ashes.\n"
                f"{days_elapsed_since_holding} days since they held it.\n"
                f"This was tweeted at {timestamp}.\n"
               
                
            )
        )
        print(f"Tweeted successfully!")
    except Exception as e:
        print(f"Error while tweeting: {e}")
    
if __name__ == "__main__":
    try:
        user = client.get_me()
        print(f"Authenticated as: {user.data['username']}")
        daily_tweet()
    except Exception as e:
        print(f"Error: {e}")
        
