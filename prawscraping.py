# import praw


# reddit = praw.Reddit(
#     client_id="SodeENmMV1K6OPTwgwyN-Q",
#     client_secret="9ycoQMI-eJLObD4PJTAvdeIfzZz2nw",
#     password="scraping threads",
#     user_agent="u/scrapingthreads",
#     username="scrapingthreads",
# )

# print(reddit.user.me())

import pickle
import os

comments = [1,2,3,4]
pickle.dump(comments, open("comments.dat", "wb"))