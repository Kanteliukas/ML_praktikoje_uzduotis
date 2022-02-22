from flask import Flask, render_template, request
from prediction import make_prediction
app = Flask(__name__)

setosa_url = \
    'https://render.fineartamerica.com/images/images-profile-flow/400/images/artworkimages/mediumlarge/2/iris-setosa-arctic-iris-or-beach-iris-c-bill-pusztai.jpg'
versicolor_url = \
    'https://vysniauskugeles.lt/wp-content/uploads/2015/11/Vilkdalgiai-Kernesina-2.jpg'
virginica_url = \
    'https://vysniauskugeles.lt/wp-content/uploads/2021/12/Iris-virginica.jpg'

def validate_inputs(*args):
    for input_ in args:
        try:
            input_ = float(input_)
        except TypeError:
            return False
        if input_ < 0.5 or input_ > 5:
            return False
        continue
    return True

@app.route("/", methods=["POST", "GET"])
def index():
    image = False
    prediction = False
    if request.method == "POST":
        sl = request.form["sepal_length"]
        sw = request.form["sepal_width"]
        pl = request.form["petal_length"]
        pw = request.form["petal_width"]
        if not validate_inputs(sl, sw, pl, pw):
            prediction = "Ilgis ir plotis turi būti tarp 0.5 ir 5"
            image = ""
        else:
            prediction = make_prediction(sl, sw, pl, pw)
            if prediction == 'virginica':
                image = virginica_url
            elif prediction == 'versicolor':
                image = versicolor_url
            else:
                image = setosa_url
    return render_template('prediction.html', prediction=prediction, image=image)


if __name__ == "__main__":
    app.run(debug=True)