from flask import Flask
from flask import jsonify
from flask import request
import random

from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app, version='1.0', title='Inspirational Content API', description='A free API to get some Inspirational Content by Sayam Hussain',)


ns = api.namespace('mantras', description='Mantras')  # Mantra Namespace

feeds = [{'id': 0, 'name': 'Stoicism'}, {'id': 1, 'name': 'Buddhism'}, {'id': 2, 'name': 'Rumi'}, {'id': 3, 'name': 'Forbes Top 100'}]


@ns.route('/feeds')
class GetMantraFeeds(Resource):
    def get(self):
        return jsonify(feeds)


mantras = {
    0: [{'quote': 'You have power over your mind – not outside events. Realize this, and you will find strength.',
         'source': 'Marcus Aurelius'},
        {'quote': 'It’s not what happens to you, but how you react to it that matters.', 'source': 'Epictetus'}
        ],
    1: [{'quote': 'There is no fear for one whose mind is not filled with desires.', 'source': 'Buddha'}],
    2: [{'quote': 'Raise your words, not voice. It is rain that grows flowers, not thunder.', 'source': 'Rumi'}],
}


@ns.route('/mantra')
class GetAMantra(Resource):
    def get(self):
        args = request.args

        feeds_query = '0,1,2'
        if "feeds" in args:
            feeds_query = args['feeds']

        feeds_split = feeds_query.split(',')

        mantra = ''

        if len(feeds_split) == 1:
            feed_mantras = mantras[int(feeds_split[0])]
            mantra = feed_mantras[random.randint(0, len(feed_mantras) - 1)]

        # random_feed = random.randint()

        return jsonify(mantra)
#
#
# @app.route('/mantras/<int:id>')
# def get_mantra():
#     return 'Hello World!'
#
#
# @app.route('/quotes/feed')
# def get_quote_feeds():
#     return 'Hello World!'
#
#
# @app.route('/quotes/quote')
# def get_a_quote():
#     return 'Hello World!'
#
#
# @app.route('/quotes/<int:id>')
# def get_quote():
#     return 'Hello World!'


if __name__ == '__main__':
    app.run()
