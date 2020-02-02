from google.cloud import vision
from google.oauth2 import service_account
import io
import unicodedata
import re
import inflect


credentials = service_account.Credentials.from_service_account_file('keyfile.json')
client = vision.ImageAnnotatorClient(credentials=credentials)


# Takes string parsed from image and returns list of formatted ingredient strings
# def str_to_ingredients_list(string):
#     p = inflect.engine()
#     ingredients_list = string.lower().replace('organic','').replace('(', ',').replace('[', ',').replace('.',',').replace('and',',').split(',')

#     for i in range(len(ingredients_list)):
#         ingredients_list[i] = "".join(c for c in ingredients_list[i] if c.isalnum() or c == " ").strip()
#         if len(ingredients_list[i].split()) > 3:
#             ingredients_list[i] = ""
#     print([p.singular_noun(x) for x in ingredients_list if x])
#     return [p.singular_noun(x) for x in ingredients_list if x]


def str_to_ingredients_list(string):
    # test_str = 'Ingredients: wheat**, peanuts, [apple], peanut butter, oil and butter, pears, milk--*, Áccěntěd, Organic cashews, geese, partially hydrogenated shortening'
    test_str = unicodedata.normalize('NFKD', string).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    test_str = test_str.lower()
    # test_str = test_str.split('ingredients',1)[1]
    test_str = re.sub('\sand|\sorganic|\spartially|\sunbleached|\senriched|\snatural|\sskim|\snonfat|\sartificial|\ssharp|\ssalted|\sunsalted|\sbleached|\swhole|\syolk|\swhite|\sroasted',", ",test_str)
    test_lis = re.split("[^a-zA-Z1-9 ]", test_str)

    p = inflect.engine()
    ing_list = []
    for word in test_lis:
        stripped_word = word.strip()
        if len(stripped_word) > 0:
            singular_word = p.singular_noun(stripped_word) if p.singular_noun(stripped_word) != False else stripped_word
            ing_list.append(singular_word)
    print("ingredients list:", ing_list)
    return(ing_list)



# Takes list of formatted ingredient strings and returns set of only the ingredients that would cause an allergic reaction
def get_problem_ingredients(allergies, ingredients_list):
    allergens = open("allergens.txt", "r")
    # user_allergies = open("user_allergies.txt", "r")

    allergens_dict = eval(allergens.read())
    # user_allergies_set = eval(user_allergies.read())
    print(str(allergies))
    user_allergies_set = set(allergies)

    user_allergies_set = {x.lower() for x in user_allergies_set}
    allergens_dict = {k.lower(): {x.lower() for x in v} for (k, v) in allergens_dict.items()}

    allergens.close()
    # user_allergies.close()

    disallowed_ingredients = set()
    for allergy in user_allergies_set:
        print(str(user_allergies_set))
        for ingredient in ingredients_list:
            if ingredient in allergens_dict[allergy]:
                disallowed_ingredients.add(ingredient) 

    print("dissalowed_ingredients:", str(disallowed_ingredients))
    return disallowed_ingredients


# Takes path to image file, parses all text in the picture, and returns its string
def detect_text(img):

    image = vision.types.Image(content=img)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    if(len(texts) > 0):
        print(texts[0].description)
        return texts[0].description
    else:
        return ''
