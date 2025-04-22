import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def cat_info():
    url = "https://api.freeapi.app/api/v1/public/cats/cat/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        sub_data = data["data"]
        name = sub_data["name"]
        image = sub_data["image"]
        origin = sub_data["origin"]
        return render_template("cat.html", cat_name=name, cat_origin=origin, cat_image_url=image)
    else:
        return "Failed to fetch cat data.", 500

if __name__ == "__main__":
    app.run(debug=False)
