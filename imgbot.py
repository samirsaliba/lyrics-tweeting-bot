import random
import tweepy
import os

from tweepy import OAuthHandler

CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_KEY = os.environ['ACCESS_KEY']
ACCESS_SECRET = os.environ['ACCESS_SECRET']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


def post_img():
	path = 'images/' #the bot will search through a folder of images
	files = os.listdir(path)

	try_tweet = True

	while try_tweet:
		index = random.randrange(0, len(files)) #radomly it selects an episode from the file
		print(len(files))
		path_new = 'images/' +str(files[index])#then it creates a new path to the selected episode
		print("nome  "+path_new)
	
		try:
			api.update_with_media(path_new)
			try_tweet = False
		except tweepy.TweepError as error:
			if error.api_code == 187:
				print('Duplicate tweet. Trying again...')
				try_tweet = True
			else:
				raise error

def main():
	post_img()

if __name__ == '__main__':
	main()

