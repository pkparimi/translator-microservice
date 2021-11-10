from flask import Flask, request
from translator import Translator

# Configuration

app = Flask(__name__)

# Routes

@app.route("/", methods=['GET'])
def translate_text():
    try:
        text_to_translate = request.args.get("text")
        target_lang = request.args.get("target")
        source_lang = request.args.get("source")
        if not source_lang:
            source_lang = "auto"
        new_translator = Translator(text_to_translate, target_lang, source_lang)
        
        translate_text = new_translator.translate()
        
        return translate_text
    except:
        return "<h1> Please retry with different parameters. Unable to process <h1>"

# Listener

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6238, debug=True)