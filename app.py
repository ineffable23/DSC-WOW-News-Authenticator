from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np
from sklearn.metrics import confusion_matrix

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))


@app.route('/')
def hello_world():
    return render_template("NA.html")


@app.route('/predict',methods=['POST','GET'])
def predict():
    # int_features=[int(x) for x in request.form.values()]
    # final=[np.array(int_features)]
    # print(int_features)
    # print(final)
    prediction=pac.predict(tfidf_test)
    cf_matrix = confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])
    print(cf_matrix)
    import seaborn as sns

    output = sns.heatmap(cf_matrix / np.sum(cf_matrix), annot=True,
                fmt='.2%', cmap='Blues')


    # if output>str(0.5):
    #     return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
    # else:
    #     return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")


if __name__ == '__main__':
    app.run(debug=True)
