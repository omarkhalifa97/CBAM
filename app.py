import time
from flask import Flask, render_template,send_from_directory,request,redirect,url_for
import os
import csv
import smtplib, ssl
from email.message import EmailMessage

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "Anonymous"  # Enter your address
receiver_email = "omarkhalifa426@gmail.com"  # Enter receiver address
password = "knoqmuajdwblggkz"

msg = EmailMessage()

msg['Subject'] = "We found an idiot"
msg['From'] = sender_email
msg['To'] = receiver_email

context = ssl.create_default_context()

dict = {
    "Ammonium Nitrate": [33.5,"% Nitrogen",0],
    "Calcium Ammonium Nitrate": [27,"% Nitrogen",0],
    "Ammonium Nitro Sulphate": [26,"% Nitrogen",14,"% Sulphur"],
    "Calcium Nitrate": [15.5,"% Nitrogen",0],
    "Ammonium Sulphate": [21,"% Nitrogen",24,"% Sulphur"],
    "Monoammonium Phosphate": [11,"% Nitrogen",52,"% Phosphorus"],
    "Diammonium Phosphate": [18,"% Nitrogen",46,"% Phosphorus"],
    "Urea": [46,"% Nitrogen",0],
    "Urea Ammonium Nitrate (liquid)": [30,"% Nitrogen",0],
    "NPK 15-15-15": [15,"% Nitrogen",15,"% Phosphorus",15,"% Potassium"],
    "Triple Super Phosphate": [48,"% Phosphorus",0],
    "Muriate of Potash": [60,"% Potassium",0]


 }
hs_dict = {
    "Ammonium Nitrate": [310230,65010320011101271],
    "Calcium Ammonium Nitrate": [31026000,65010320011101272],
    "Ammonium Nitro Sulphate": [31022100,65010320011101273],
    "Calcium Nitrate": [31029090,65010320011101274],
    "Ammonium Sulphate": [31022100,65010320011101275],
    "Monoammonium Phosphate": [310540,65010320011101276],
    "Diammonium Phosphate": [31053000,65010320011101277],
    "Urea": [310210,65010320011101278],
    "Urea Ammonium Nitrate (liquid)": [31028000,65010320011101279],
    "NPK 15-15-15": [31052000,65010320011101280],
    "Triple Super Phosphate": [310310,65010320011101281],
    "Muriate of Potash": [31049000,65010320011101282]


 }
list = list(dict.keys())
print(f'this is  {list}')

# @app.route('/')
# def home():
#     return redirect("https://www.instagram.com/trendyfactory.eg", code=302)

@app.route('/', methods=['GET'])
def home():
     return render_template('index.html', colours=list)


@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        data = request.form.to_dict()
        dropdownval = request.form.get('colour')
        try:
            total = int(data['total'])
            cost = int(data['cost'])
        except:
            total = 0
            cost = 0

        start = data['start']
        fac_name = data['fac_name']
        loc = data['loc']
        start_date = data['start']
        end_date = data['end']
        direct = (int(dict[dropdownval][0])/100)*0.160 + (int(dict[dropdownval][2])/100)*0.178
        indirect = (int(dict[dropdownval][0])/100)*0.028 + (int(dict[dropdownval][2])/100)*0.012
        total_em = round(direct + indirect,4)*total
        result = round((direct +indirect)*total*cost,2)
        print(f"{start} this is rdddddd")
        desc = ' '.join([str(item) for item in dict[dropdownval]])
        return render_template('result.html',c_tax=result,total_em=total_em,p_name=dropdownval,p_desc=desc,hs=hs_dict[dropdownval][0],id=hs_dict[dropdownval][1],fac_name=fac_name,location=loc,start=start_date,end=end_date)
    else:
        return "You havn't submit the data"



def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')

if '__main__' == __name__:
    app.run()



