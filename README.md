# lyrics-tweeting-bot
Twitter bot that tweets song lyrics! 

Twitter bot that tweets lyrics from a text file. Since I'm a big Kanye West fan, this one specifically posts Kanye West's songs lyrics.

I split the lyrics from each album into a text file (not all lyrics, just the ones I personally picked that would be a good tweet); Each lyric from the text files should be separated with a blank line (\n\n);


Firstly, the albums.csv file is opened to check how many lyrics there are in total.
Then, a number between 0 and the total number of lyrics is randomly selected;
Using the randomly selected number an album is chosen (by consulting the rows in the albums.csv file);
The random number is adjusted so it matches a lyric within an album (so it won't be out of range in the album context);
This selected lyric is then extracted and tweeted.

PS. If any lyrics are added or removed, the status file (status.csv) should be updated, so the probabilities can be recalculated;

I followed this incredible yet simple tutorial made by @ShawnToubeau (thanks, Shawn!): https://www.freecodecamp.org/news/building-a-twitter-lyric-bot-12468255a4ee/

And also did some reading on managing the environment variables here (your bot won't work if you don't set the environment variables correctly): https://devcenter.heroku.com/articles/config-vars
