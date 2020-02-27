# lyrics-tweeting-bot
## Twitter bot that tweets song lyrics!
## Check it out here: [twitter/@theyeezybot](https://twitter.com/theyeezybot)

run 'python lybot.py' for lyrics

run 'imgbot.py' for images

Twitter bot that tweets lyrics from a database, ~~or an image from a folder.~~  
Since I'm a big Kanye West fan, this one specifically posts Kanye West's songs lyrics and pictures.

lybot.py:  
I split the lyrics from each album into a text file (not all lyrics, just the ones I personally picked that would be a good tweet); Each lyric from the text files should be separated with a blank line (\n\n);  
The lyrics were added to a database on heroku through the insert_lyrics_into_db.py script.  
Every run it chooses randomly one of the 100 lyrics that were tweeted earliest so it doesn't repeat itself a lot.

imgbot.py:
Just opens the images (or any other set) folder and selects one image randomly to tweet.
TODO:
Also upload the images to a db and choose which one to tweet based on when they were last tweeted.

I followed [**this**](https://www.freecodecamp.org/news/building-a-twitter-lyric-bot-12468255a4ee/) incredible yet simple tutorial made by [**@ShawnToubeau**](https://github.com/ShawnToubeau) (thanks, Shawn!): 

Some indisposable references:
[Managing the environment variables](https://devcenter.heroku.com/articles/config-vars)
[Setting up the database properly](https://devcenter.heroku.com/articles/heroku-postgresql)

Also had some help at tweeting pictures from my good friend Lucas Zatta @LucasZatta (you should also check his AMAZING framebot [**here**](https://github.com/LucasZatta/FrameBot) )


