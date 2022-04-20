from flask import Flask
from flask import jsonify
from flask import request
from flask_restx import Resource, Api, reqparse

import random

app = Flask(__name__)
api = Api(app, version='1.0', title='Inspirational Content API', description='A free API to get some Inspirational '
                                                                             'Content by VampSlayer', )


def get_random_feed_item(feed_query, feed):
    feeds_split = feed_query.split(',')

    feed_items = []
    if len(feeds_split) == 1:
        feed_items = feed[int(feeds_split[0])]

    for feed_split in feeds_split:
        feed_items.extend(feed[int(feed_split)])

    feed_item = feed_items[random.randint(0, len(feed_items) - 1)]

    return feed_item


mantra_ns = api.namespace('mantras', description='Mantras')

mantra_feeds = [{'id': 0, 'name': 'Happiness'}, {'id': 1, 'name': 'Inspiration'}, {'id': 2, 'name': 'Motivation'},
                {'id': 3, 'name': 'Focus'}]


@mantra_ns.route('/feeds')
class GetMantraFeeds(Resource):
    def get(self):
        """Get all the mantra feeds"""
        response = jsonify(mantra_feeds)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response


mantras = {
    0: [{'mantra': 'Enjoy the present moment.'},
        {'mantra': 'Enjoy today.'}
        ],
    1: [{'mantra': 'Aim for excellence, not perfection.'}],
    2: [{'mantra': 'Yes, you can.'}],
    3: [{'mantra': 'Focus on the positive.'}],
}

mantra_parser = reqparse.RequestParser()
mantra_parser.add_argument('feeds', help='Comma seperated mantra feed IDs to select random mantra from e.g. `0,1,'
                                         '2`. If not supplied will return a random mantra from any feed.',
                           required=False, location='args')


@mantra_ns.route('/mantra')
class GetAMantra(Resource):
    @mantra_ns.expect(mantra_parser)
    def get(self):
        """Get a random mantra from the mantra feeds"""
        args = request.args

        feeds_query = '0,1,2,3'
        if "feeds" in args:
            feeds_query = args.get('feeds')

        mantra = get_random_feed_item(feeds_query, mantras)

        response = jsonify(mantra)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response


quotes_ns = api.namespace('quotes', description='Quotes')

quote_feeds = [{'id': 0, 'name': 'Stoicism'}, {'id': 1, 'name': 'Buddhism'}, {'id': 2, 'name': 'Rumi'},
               {'id': 3, 'name': 'Forbes Top 100'}]


@quotes_ns.route('/feeds')
class GetQuoteFeeds(Resource):
    def get(self):
        """Get all the quote feeds"""
        response = jsonify(quote_feeds)
        response.headers.add('Access-Control-Allow-Origin', '*')
        return response


quotes = {
    0: [{'quote': 'You have power over your mind – not outside events. Realize this, and you will find strength.',
         'source': 'Marcus Aurelius'},
        {'quote': 'It’s not what happens to you, but how you react to it that matters.', 'source': 'Epictetus'}
        ],
    1: [{'quote': 'There is no fear for one whose mind is not filled with desires.', 'source': 'Buddha'}],
    2: [{'quote': 'Raise your words, not voice. It is rain that grows flowers, not thunder.', 'source': 'Rumi'}],
    3: [{'quote': 'Life is about making an impact, not making an income.', 'source': 'Kevin Kruse'},
        {'quote': 'Whatever the mind of man can conceive and believe, it can achieve.', 'source': 'Napoleon Hill'},
        {'quote': 'Strive not to be a success, but rather to be of value.', 'source': 'Albert Einstein'},
        {
            'quote': 'Two roads diverged in a wood, and I—I took the one less traveled by, And that has made all the difference.',
            'source': 'Robert Frost'},
        {'quote': 'I attribute my success to this: I never gave or took any excuse.', 'source': 'Florence Nightingale'},
        {'quote': 'You miss 100% of the shots you don’t take.', 'source': 'Wayne Gretzky'},
        {
            'quote': "I've missed more than 9000 shots in my career. I've lost almost 300 games. 26 times I've been trusted to take the game winning shot and missed. I've failed over and over and over again in my life. And that is why I succeed.",
            'source': 'Michael Jordan'},
        {'quote': 'The most difficult thing is the decision to act, the rest is merely tenacity.',
         'source': 'Amelia Earhart'},
        {'quote': 'Definiteness of purpose is the starting point of all achievement.', 'source': 'W. Clement Stone'},
        {'quote': "Life isn't about getting and having, it's about giving and being.", 'source': 'Kevin Kruse'},
        {'quote': "Life is what happens to you while you’re busy making other plans.", 'source': 'John Lennon'},
        {'quote': "We become what we think about.", 'source': 'Earl Nightingale'},
        {
            'quote': "Twenty years from now you will be more disappointed by the things that you didn’t do than by the ones you did do, so throw off the bowlines, sail away from safe harbor, catch the trade winds in your sails.  Explore, Dream, Discover.",
            'source': 'Mark Twain'},
        {'quote': "Life is 10% what happens to me and 90% of how I react to it.", 'source': 'Charles Swindoll'},
        {'quote': "The most common way people give up their power is by thinking they don’t have any.",
         'source': 'Alice Walker'},
        {'quote': "The mind is everything. What you think you become.", 'source': 'Buddha'},
        {'quote': "The best time to plant a tree was 20 years ago. The second best time is now.",
         'source': 'Chinese Proverb'},
        {'quote': "An unexamined life is not worth living.", 'source': 'Socrates'},
        {'quote': "Eighty percent of success is showing up.", 'source': 'Woody Allen'},
        ],
}

quote_parser = reqparse.RequestParser()
quote_parser.add_argument('feeds', help='Comma seperated quote feed IDs to select random quote from e.g. `0,1,2`. If '
                                        'not supplied will return a random quote from any feed.',
                          required=False, location='args')


@quotes_ns.route('/quote')
class GetAQuote(Resource):
    @quotes_ns.expect(quote_parser)
    def get(self):
        """Get a random quote from the quote feeds"""
        args = request.args

        feeds_query = '0,1,2,3'
        if "feeds" in args:
            feeds_query = args.get('feeds')

        quote = get_random_feed_item(feeds_query, quotes)

        response = jsonify(quote)
        response.headers.add('Access-Control-Allow-Origin', '*')

        return response


if __name__ == '__main__':
    app.run()
