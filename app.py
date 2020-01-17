from flask import Flask, jsonify, request, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('localhost:27017')
db = client.annotatedImages

@app.route("/save_image", methods = ['POST'])
def save_image():
    metadata = request.get_json()

    saved_metadata = {"image_url" : metadata["image_url"], "bounding_poly" : metadata["bounding_poly"], "annotation": metadata["annotation"], "top" : metadata["top"], "left": metadata["left"]}
    db.metadata.insert(saved_metadata)
    return jsonify({'status': 200})
@app.route("/view")
def view_annotated_images():
    metadata_all = db.metadata.find()
    return render_template('annotate.html', metadata=metadata_all)

if __name__ == '__main__':
      app.run(host='127.0.0.1', port=7000)