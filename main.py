from flask import Flask,render_template,request

app = Flask(__name__)

recent_chat = []
recent_history = []
@app.route("/",methods=["GET","POST"])
def home():

    MORSE_CODE_DICT = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..',
        '0': '-----', '1': '.----', '2': '..--', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', '/': '-..-.',
        '-': '-....-', '(': '-.--.', ')': '-.--.-'
    }
    if request.method=="POST":
        text = request.form.get("sentence")
        recent_chat.append(text)
        code = ""
        for ch in text:
            s_code = MORSE_CODE_DICT.get(ch.upper())
            if (s_code):
                code+=s_code
        recent_history.append(code)
        return render_template("home.html",morse=recent_chat,history=recent_history,length=len(recent_chat))
    return render_template("home.html",morse=recent_chat,history=recent_history,length=len(recent_chat))

if __name__ == "__main__" :
    app.run()