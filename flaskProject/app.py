from flask import Flask, render_template, send_from_directory,redirect, url_for,request
import mysql.connector
import sys
sys.path.insert(0, '/own_mysql/')
from own_mysql import utilities as utils
app = Flask(__name__)
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True

# Connecting Database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="toor",
  database="vaccine"
)
mydb.close()


# Token Initialization
n = 1




@app.route('/', methods = ["GET", "POST"])
def center():
    global n
    specific_rec = utils.filter_rec(n)
    # Detecting the submit button press to change the phone number and dose number
    if request.method == "POST":

        new_D1 = request.form.get('dose1')
        new_D2 = request.form.get('dose2')
        print(f"form data DOSE 1 : {new_D1}")
        print(f"form data DOSE 2 : {new_D2}")
        if new_D1 == None: # if form data returns None -> take old value from db
            new_D1 = specific_rec[3]
        if new_D2 == None: # if form data returns None -> take old value from db
            new_D2 = specific_rec[4]

        print(f"Backend data DOSE 1 : {specific_rec[3]}")
        print(f"Backend data DOSE 2 : {specific_rec[4]} ")
        # form_data = list(request.form.get('dose1'))
        # form_data.append(request.form.getlist('dose2'))
        # print(form_data)
        utils.update_record(specific_rec, new_D1, new_D2 )

        print("Submit Pressed")
        file = open("temp.txt", "w")
        file.write(str(n+1))
        file.close()
        # update_record(specific_rec, )
        return redirect('/')
    if len(specific_rec)>0: # if record is present in the database
        return render_template("center.html", rec=specific_rec)
    else:
        return render_template("center.html", rec=["Waiting", "Waiting", "Waiting", "Waiting", "Waiting"])





@app.route('/prev', methods = ["GET", "POST"])
def prev():
    global n
    specific_rec = utils.filter_rec(n-1)
    if request.method == "POST":
        print(request.form.get('dose1'))
        print(request.form.get('dose2'))

    if n == 1: # if n is at token 1 then decrese it so if someone clicks next then n would increase by 1 and not 2
        n = 0
    if len(specific_rec)>0: # if record is present in the database
        n = n - 1
        print(f'In prev n = {n}')
        return redirect('/')
        #return render_template("center.html", rec=specific_rec)
    else:
        return render_template("center.html", rec=["NA", "NA", "NA", "NA", "NA"])




@app.route('/next', methods = ["GET", "POST"])
def next():
    global n
    specific_rec = utils.filter_rec(n + 1)
    if request.method == 'POST':
        print(request.form.get('dose1'))
        print(request.form.get('dose2'))
    if len(specific_rec)>0: # if record is present in the database
        n = n + 1
        print(f'In next n = {n}')
        return redirect('/') # This redirects to the center page with no change in url but data changes accordingly
    else:
        return render_template("center.html", rec=["Waiting", "Waiting", "Waiting", "Waiting", "Waiting"])



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)
