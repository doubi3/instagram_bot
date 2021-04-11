from instapy import InstaPy
from instapy import smart_run
import config


session = InstaPy(username=config.username,
                  password=config.password, headless_browser=True)
# session.login()
with smart_run(session):

    session.set_relationship_bounds(enabled=True, max_followers=100)

    session.set_do_follow(True, percentage=10)

    session.like_by_tags([
        "bmw", "python", "ronaldo", "messi", "javascript", "music", "uefa", "football", "playstation",
        "manchesterunited", "samsung", "android", "iPhone", "Tesla", "bitcoin", "btc", "webdev", "science", "heroku", "cryptocurrency", "artificial intelligence"], amount=3)
    session.set_dont_like(["nsfw"])
    session.set_do_comment(enabled=True, percentage=80)
    session.set_comments([
        u'What an amazing shot! :heart_eyes: What do '
        u'you think of my recent shot?',
        u'What an amazing shot! :heart_eyes: I think '
        u'you might also like mine. :wink:',
        u'Wonderful!! :heart_eyes: Would be awesome if '
        u'you would checkout my photos as well!',
        u'Wonderful!! :heart_eyes: I would be honored '
        u'if you would checkout my images and tell me '
        u'what you think. :wink:',
        u'This is awesome!! :heart_eyes: Any feedback '
        u'for my photos? :wink:',
        u'This is awesome!! :heart_eyes:  maybe you '
        u'like my photos, too? :wink:',
        u'I really like the way you captured this. I '
        u'bet you like my photos, too :wink:',
        u'I really like the way you captured this. If '
        u'you have time, check out my photos, too. I '
        u'bet you will like them. :wink:',
        u'Great capture!! :smiley: Any feedback for my '
        u'recent shot? :wink:',
        u'Great capture!! :smiley: :thumbsup: What do '
        u'you think of my recent photo?'],
        media='Photo')
    # session.end()
