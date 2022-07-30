from flask import Flask, jsonify, redirect, request
from flasgger import Swagger
import psycopg2
import numpy as np
import os
import pandas as pd
import json


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
    
    conn = psycopg2.connect(database = os.environ.get('DATABASE_NAME', None), 
                            user = os.environ.get('DATABASE_USER', None),
                            password = os.environ.get('DATABASE_PASS', None),
                            host = os.environ.get('DATABASE_HOST', None),
                            port = os.environ.get('DATABASE_PORT', None))
    print("Opened database successfully")
    
    word = request.args.get('word', 1)
    sql_str = "SELECT * FROM word_symbol_map WHERE word = \'%s\';" % (word)
    print(sql_str)
    
    df = pd.read_sql(sql_str, conn)
    
    if(len(df) == 0):
        mat = np.zeros((5, 5)).astype(int)
        return jsonify(ans={"main_color": "not apple color", "main_shape": json.dumps(mat.tolist())})
    
    lst = df['symbol_shape_detail'][0].split('*')
    print(lst)
    
    m = int(lst[0])
    n = int(lst[1])
    
    content = df['symbol_shape_content'][0]
    print(content)
    
    mat = np.zeros((m, n)).astype(int)
    for i in range( len(content) ):
        row = int(i / n)
        col = int(i % n)
        mat[[row], [col]] = int(content[i])

    print(mat)
    
    main_color = df['symbol_main_color'][0]
    
    return jsonify(ans={"main_color": main_color, "main_shape": json.dumps(mat.tolist())})