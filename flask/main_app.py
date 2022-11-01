from flask import Flask, request, jsonify
import logging
from datetime import datetime

app_name = "check"
logger = logging.getLogger(app_name)

app = Flask(app_name)


@app.route("/check_get", methods=["GET"])
def get_api():
    curr_time = datetime.utcnow()
    logger.error("GET API is called @ %s", curr_time)
    return f"GET API CALLED @ {curr_time}"


@app.route("/check_post", methods=["POST"])
def post_api_check():
    data = request.get_json("data")
    logger.error(str(data))
    req = {"incoming_data": str(data)}
    return jsonify(req)


if __name__ == "__main__":
    app.run(port='3005')
