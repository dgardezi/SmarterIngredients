from flask import Flask, request, Response
import numpy as np
import json
import cv2
import base64
from determine_allergic import str_to_ingredients_list,get_problem_ingredients,detect_text


# Initialize the Flask application
app = Flask(__name__)

@app.route('/api/allergens', methods=['GET'])
def get_allergens():
    allergens = open("allergens.txt", "r")
    allergens_dict = eval(allergens.read())
    allergens.close()

    allergens_string = ','.join(set(allergens_dict.keys()))


    return allergens_string

# route http posts to this method
@app.route('/api/allergens', methods=['POST'])
def post_allergens():
    r = request
    # convert string of image data to uint8
    file = open("request.txt", 'w')
    file.write(str(r.data))
    file.close()
    data = json.loads(r.data)
    new_data = {}
    for dic in data:
        for key,value in dic.items():
            new_data[key] = value
    data = new_data
    img = base64.b64decode(data['img'])
    # nparr = np.fromstring(img_uncoded, np.uint8)
    # decode image
    # img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    
    

    # do some fancy processing here....
    allergies = data["allergies"]
    print(type(allergies), allergies)
    ingredients_string = detect_text(img)
    ingredients_list = str_to_ingredients_list(ingredients_string)

    reactions = get_problem_ingredients(allergies, ingredients_list)

    reactions = ','.join(reactions)
    # build a response dict to send back to client
    response = {'message': 'image received.',
                'reactions': reactions,
                'ingredients list': str(ingredients_list)}
    # encode response using jsonpickle


    return Response(response=json.dumps(response), status=200, mimetype="application/json")


# start flask app
if __name__ == '__main__':
    app.run(debug=True, port = 5000)