from flask import Flask, jsonify, redirect, request
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def api_index():
    return redirect('/apidocs/')

@app.route('/v1/img_for_word/', methods=['GET'])
def get_img_for_word():
    """
      Get img for word
      ---
      tags:
        - Computer Vision APIs
        - restart time:
      produces: application/json,
      parameters:
      - name: word
        in: query
        type: string
        required: true
      responses:
        200:
          description: Retrieve image for word
          examples:
            ans: {"main_color":"red", "main_shape":["00100", "01010", "10001", "00100", "01010"]}
    """
    word = request.args.get('word', 1)
    return jsonify(ans={"main_color":"red", "main_shape":["00100", "01010", word, "01010", "00100"]})