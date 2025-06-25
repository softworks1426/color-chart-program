
from flask import Flask, render_template, request, jsonify
from utils import fetch_image_urls, get_dominant_color

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/load")
def load():
    query = request.args.get("q", "")
    offset = int(request.args.get("offset", 1))
    api_key = "704b1cc7b277311c7f61a6751943058d40e3561203698db3ed64f96c4c9ccc8d"
    results = fetch_image_urls(query, api_key, num=30, page=offset)
    colors = [{"color": '#%02x%02x%02x' % get_dominant_color(thumbnail), "link": link} for thumbnail, link in results]
    return jsonify(colors)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(debug=False, host="0.0.0.0", port=port)
