from flask import Flask, request, jsonify

app = Flask(__name__)


def add_key_to_tree(tree, key, validators):
    parts = key.split(".")

    for i, part in enumerate(parts):
        if part == "*":
            # Si on rencontre un '*', on initialise un tableau
            if "items" not in tree:
                tree["type"] = "array"
                tree["validators"] = ["array"]
                tree["items"] = {
                    "type": "object",
                    "validators": ["object"],
                    "properties": {},
                }
            tree = tree["items"]
        else:
            # Si c'est la dernière partie de la clé, on ajoute les validateurs
            if i == len(parts) - 1:
                tree[part] = {"type": "leaf", "validators": validators.split("|")}
            else:
                # Si la clé n'existe pas encore, on initialise un objet
                if part not in tree:
                    tree[part] = {
                        "type": "object",
                        "validators": ["object"],
                        "properties": {},
                    }
                # Vérifier que 'properties' existe avant d'y accéder
                if "properties" not in tree[part]:
                    tree[part]["properties"] = {}
                # Se déplacer au niveau suivant
                tree = tree[part]["properties"]


def create_tree(data):
    tree = {}
    for key, value in data.items():
        add_key_to_tree(tree, key, value)
    return tree


@app.route("/expand_validator", methods=["POST"])
def expand_validator():
    data = request.get_json()
    response = jsonify(create_tree(data))
    return response, 200


if __name__ == "__main__":
    app.run(debug=True)
