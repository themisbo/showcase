from app import classify
from flask import Flask, request, render_template

# Initialize the flask class and specify the templates directory
app = Flask(__name__, template_folder="templates")

# Default route
@app.route('/')
def home():
    return render_template('home.html') 

# Route 'classify' 
@app.route('/classify',methods=['POST','GET'])
def classify_type():
    try:
        # get_island = request.args.get('isl') 
        get_bill_length_mm = request.args.get('blmm')
        get_bill_depth_mm = request.args.get('bdmm')
        get_flipper_length_mm = request.args.get('flmm')
        get_body_mass_g = request.args.get('bmg')
        # get_sex = request.args.get('sx')

        # Get the output from the classification model
        # variety = classify(get_island, get_bill_length_mm, get_bill_depth_mm, get_flipper_length_mm, get_body_mass_g, get_sex)

        variety = classify(get_bill_length_mm, get_bill_depth_mm, get_flipper_length_mm, get_body_mass_g)
        
        # Render the output in new HTML page
        return render_template('output.html', variety=variety)
    except:
        return 'Error'

# Run the Flask server
if(__name__=='__main__'):
    app.run()        