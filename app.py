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
    
    prediction=pac.predict(tfidf_test)
    cf_matrix = confusion_matrix(y_test, y_pred, labels=['FAKE', 'REAL'])
    print(cf_matrix)
    import seaborn as sns

    output = labels = [‘True Neg’,’False Pos’,’False Neg’,’True Pos’]
             labels = np.asarray(labels).reshape(2,2)
             sns.heatmap(cf_matrix, annot=labels, fmt=‘’, cmap='Blues')


if __name__ == '__main__':
    app.run(debug=True)
