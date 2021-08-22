import datetime
from flask import Flask, render_template, Response


def create_app():
    app = Flask(__name__)

    def get_current_time(timezone_offset=3):
        timezone_info = datetime.timezone(datetime.timedelta(hours=timezone_offset))
        current_time = datetime.datetime.now(timezone_info)
        return current_time.strftime("%H:%M:%S")

    @app.route('/')
    def get_main_page():
        return render_template("index.html", time=get_current_time())

    @app.route('/api/time')
    def get_time():
        return Response(get_current_time())

    return app
