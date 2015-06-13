import logging
import os

from flask import Flask, request

app = Flask(__name__)
log = logging.getLogger(__name__)


@app.route('/')
def listen():
    print '*' * 40
    log.info(request.values.get)
    log.info(request.values.post)
    return ''


if __name__ == '__main__':
    app.run()
