from flask import Flask, request, jsonify

app = Flask(__name__)

ALPHABET = set("abcdefghijklmnopqrstuvwxyz")


@app.route("/", methods=["GET", "POST"])
def check_alphabet():
    """Handles both GET and POST methods"""
    try:
        input_string = None
        if request.method == "POST":
            input_string = request.get_json().get("input_string")
        else:
            input_string = request.args.get("input_string")

        if not input_string or not isinstance(input_string, str):
            raise Exception("Invalid input")

        result = ALPHABET.issubset(set(input_string.lower()))
        return jsonify({"contains_all_alphabets": result})
    except Exception as e:
        print(e)
        return jsonify({"error": "Invalid input: a valid input_string is required"}), 400


if __name__ == "__main__":
    app.run(port=3000)
