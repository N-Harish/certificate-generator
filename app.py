from flask import Flask, render_template, request, send_file
from PIL import Image, ImageFont, ImageDraw
app = Flask(__name__)
import time

@app.route("/",methods=["GET"])
def index():

        return render_template("quiz_result.html")


@app.route("/quiz_result_response", methods=["POST"])
def quiz_result_response():
    name = request.form["username"]
    img = Image.open('./Certificate/new.jpg')
    font = ImageFont.truetype('arial.ttf', 60)
    draw = ImageDraw.Draw(img)
    li = name.split(' ')
    if len(li) >= 2:
        draw.text(xy=(365, 320), text=name, fill=(0, 0, 0), font=font)
    else:
        draw.text(xy=(459, 320), text=name, fill=(0, 0, 0), font=font)

    img = img.convert("RGB")
    img.save(f'./Certificate/{name}.pdf')

    time.sleep(30)

    return send_file(f"./Certificate/{name}.pdf", as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)





