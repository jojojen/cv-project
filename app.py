from flask import Flask, jsonify
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

app.logger.addHandler(logging.StreamHandler(sys.stdout))
app.logger.setLevel(logging.ERROR)

@app.route('/')
def api_index():
    return redirect("https://cv-project-maverick.herokuapp.com/apidocs/")

@app.route('/v1/img_for_word', methods=['GET'])
def test_api():
  """
    Get img for word
    ---
    tags:
      - Node APIs
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
  return jsonify(ans={"main_color":"red", "main_shape":["00100", "01010", "10001", "01010", "00100"]})