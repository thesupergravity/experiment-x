import tweepy

# Create variables for each key, secret, token
consumer_key = 'Ouyx998tepAvVyCOkxsgxbYL4'
consumer_secret = '0g8QBcHaWxdZwnpWI9zRel9A4gQjeC9zcv9GlIeps70OnOoNSp'
access_token = '21464828-TYXTU020SVOKPSoiVcO4rohzIngenfiZ6kJSMcSsK'
access_token_secret = '2UQisdiCmC8igrCzviYPZkFoLA0A9LqYgtQYX3R5uvRfE'

# Set up OAuth and integrate with API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Write a tweet to push to our Twitter account
tweet = 'Incoming: pegasus-x-test'
api.update_status(status=tweet)