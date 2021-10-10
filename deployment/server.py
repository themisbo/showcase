from app import classify
from flask import Flask, request, render_template

app = Flask(__name__, template_folder="templates")

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/classify',methods=['POST','GET'])
def classify_type():
    try:
        get_bill_length_mm = request.args.get('blmm')
        get_bill_depth_mm = request.args.get('bdmm')
        get_flipper_length_mm = request.args.get('flmm')
        get_body_mass_g = request.args.get('bmg')

        variety = classify(get_bill_length_mm, get_bill_depth_mm, get_flipper_length_mm, get_body_mass_g)
        
        return render_template('output.html', variety=variety)
    except:
        return 'Error'

if(__name__=='__main__'):
    app.run()        
