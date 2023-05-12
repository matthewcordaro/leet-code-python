import time  # use time.time_ns()
from typing import List, Dict
from bisect import insort_right


class Tweet:
  def __init__(self, tweetId: int, nanoTime: int, tweet: str = ""):
    self.tweetId: int = tweetId
    self.nanoTime: int = nanoTime
    self.tweet: str = tweet

  def __lt__(self, other):
    return self.nanoTime > other.nanoTime


class User:
  def __init__(self, idNumber: int, name: str = ""):
    self.id: int = idNumber
    self.name: str = name
    self.follows: set[int] = set()
    self.tweets: List[Tweet] = []


def convertTweetListToIDList(tweets: List[Tweet]) -> List[int]:
  tweet_ids = []
  for tweet in tweets:
    tweet_ids.append(tweet.tweetId)
  return tweet_ids


class Twitter:
  def __init__(self):
    # key: `userId`  val: `User`
    self.users: Dict[int, User] = {}

  def makeUserExist(self, userId: int) -> bool:
    if userId not in self.users:
      self.users[userId] = User(userId)
      return True
    return False

  def postTweet(self, userId: int, tweetId: int) -> None:
    self.makeUserExist(userId)
    self.users[userId].tweets.append(Tweet(tweetId, time.time_ns()))

  def getNewsFeed(self, userId: int) -> List[int]:
    if self.makeUserExist(userId):
      return []

    # Start with the user's tweets
    tweet_list: List[Tweet] = self.users[userId].tweets[-10:]
    tweet_list.reverse()  # to put in proper order

    # for every followee we search their last 10 tweets,
    for followee in self.users[userId].follows:
      for tweet in self.users[followee].tweets[-10:]:
        # add it if less than 10 tweets
        if len(tweet_list) < 10:
          insort_right(tweet_list, tweet)
          continue
        # if newer than oldest, new one added, oldest dropped
        if tweet_list[9].nanoTime < tweet.nanoTime:
          tweet_list = tweet_list[:8]
          insort_right(tweet_list, tweet)

    return convertTweetListToIDList(tweet_list)

  def follow(self, followerId: int, followeeId: int) -> None:
    self.makeUserExist(followerId)
    self.makeUserExist(followeeId)
    self.users[followerId].follows.add(followeeId)

  def unfollow(self, followerId: int, followeeId: int) -> None:
    self.makeUserExist(followerId)
    self.makeUserExist(followeeId)
    self.users[followerId].follows.discard(followeeId)


def main():
  commands = ["postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
              "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
              "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "getNewsFeed",
              "follow", "getNewsFeed", "unfollow", "getNewsFeed"]

  data = [[1, 5], [2, 3], [1, 101], [2, 13], [2, 10], [1, 2], [1, 94], [2, 505], [1, 333], [2, 22], [1, 11],
          [1, 205], [2, 203], [1, 201], [2, 213], [1, 200], [2, 202], [1, 204], [2, 208], [2, 233], [1, 222], [2, 211],
          [1], [1, 2], [1], [1, 2], [1]]

  t = Twitter()

  for i in range(len(commands)):
    if commands[i] == "getNewsFeed":
      print(t.getNewsFeed(*data[i]))
      continue
    getattr(t, commands[i])(*data[i])
    time.sleep(0.001)


if __name__ == '__main__':
  main()
