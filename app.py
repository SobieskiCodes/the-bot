from flask import Flask
from models import Guild
from database import db_session
import threading
import botthread
import asyncio
import os
from flask_bootstrap import Bootstrap
import json

with open(f"../config.json", 'r') as f:
    config = json.load(f)

token = config.get('token')

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'my_secret_key'


async def start_bot():
    try:
        await botthread.bot.start(token)
    except Exception as e:
        exc = f'{type(e).__name__}: {e}'
        print(f'Failed to start bot:\n{exc}')


def loop_in_thread(loop):
    asyncio.set_event_loop(loop)
    loop.run_until_complete(start_bot())


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


@app.route('/')
def hello_world():
    guild = Guild.query.order_by(Guild.GuildID).all()
    print(guild)
    return f'{guild[0].Prefix}'


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop_in_thread, args=(loop,))
    t.start()
    app.run(port="5555", debug=False)
