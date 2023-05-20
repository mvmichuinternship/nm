from flask import Flask, render_template, request, redirect, session, jsonify
import requests
import ibm_db
from textblob import TextBlob





app = Flask(__name__, static_folder='static/' )
app.secret_key= 'something'
connect = ibm_db.connect("database=bludb; hostname = b0aebb68-94fa-46ec-a1fc-1c999edb6187.c3n41cmd0nqnrk39u98g.databases.appdomain.cloud;  port= 31249; uid = mrq79616; password = NlnlwXYmje5kYoS2; security= SSL;sslcertificate = DigiCertGlobalRootCA.crt", "", "")
print("Connection Established")




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spell')
def spell():
    return render_template('spell.html')

@app.route('/spell-check', methods=['POST','GET'])
def spell_check():
    text = request.form.get('text')

    # Split the text into words
    text1 = TextBlob(text)
    return render_template('spell.html',
                            input=text1, output=text1.correct())

@app.route('/grammar')
def grammar():
    return render_template('grammar.html')

@app.route("/check_grammar", methods=["POST"])
def check_grammar():
    text = request.form.get("text")
    text1= TextBlob(text)
    sentence =str(text1.correct())
    

    url = "https://ginger3.p.rapidapi.com/correctAndRephrase"

    querystring = {"text": sentence}
    headers = {
        "X-RapidAPI-Key": "e8e41140e7msh5c7ba67e4cdf74ap1b600bjsn635b84099fab",
	    "X-RapidAPI-Host": "ginger3.p.rapidapi.com"
    }

    response = requests.get(url, params=querystring, headers=headers)
    data1 = response.json()
    print(data1)
    corrected_sentence = data1.get("data", {}).get("text", "")
 
    def paraphraser( corrected_sentence) :
        text = corrected_sentence


        url = "https://rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com/rewrite"

        payload = { 
                    "language": "en",
                    "strength":3,
                    "text": text
                   }

        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "e8e41140e7msh5c7ba67e4cdf74ap1b600bjsn635b84099fab",
            "X-RapidAPI-Host": "rewriter-paraphraser-text-changer-multi-language.p.rapidapi.com"
}

        response = requests.post(url, json=payload, headers=headers)
        data2=response.json()
        paraphrase = data2.get("rewrite",'')
        print(data2)
        return paraphrase
   
    paraphrase =  paraphraser(corrected_sentence)
    return render_template("grammar.html",input=text,  corrected_sentence=corrected_sentence, sentence= paraphrase, error=True)




@app.route('/summary')
def summary():
    return render_template('summary.html')

@app.route('/summarizer', methods=['POST','GET'])
def summarizer():
    text = request.form.get('summary_text')

    # Perform text summarization

    url = "https://gpt-summarization.p.rapidapi.com/summarize"
    payload = { "text": text}

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "e8e41140e7msh5c7ba67e4cdf74ap1b600bjsn635b84099fab",
        "X-RapidAPI-Host":  "gpt-summarization.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    data1=response.json()
    print(data1)
    summary= data1.get("summary",'')

    return render_template('summary.html', input = text, output=summary)




@app.route('/login')
def login():

    return render_template("login.html")


@app.route('/enquiry', methods =["GET", "POST"])
def enquiry():
    global user_email
    if request.method =='POST':
        l_email = request.form['emailid']
        l_password = request.form['password']
        login_list = [l_email, l_password]
        print(login_list)
        sql = "select * from register where email= ? and password = ?"
        stmt = ibm_db.prepare(connect, sql)
        ibm_db.bind_param(stmt, 1, l_email)
        ibm_db.bind_param(stmt, 2, l_password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['LoggedIN'] = True
            session['email'] = account['EMAIL']
            user_email = account['EMAIL']
            return redirect("/")
        else :
            msg = "Email Id and Password do not match"
            return render_template("login.html", log_msg=msg)

@app.route('/signup', methods =["GET", "POST"])
def signup():
    if request.method == 'POST':
        u_email = request.form['emailid']
        u_password = request.form['password']
        u_cpassword = request.form['cpassword']
        signup_list = [u_email, u_password, u_cpassword]
        print(signup_list)
        
        sql = "select * from register where email= ?"
        stmt = ibm_db.prepare(connect, sql)
        ibm_db.bind_param(stmt, 1, u_email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg ="Already Registered"
            return(render_template("login.html", alert = msg))
        else:
            sql = 'insert into register values(?, ? )'
            stmt = ibm_db.prepare(connect, sql)
            ibm_db.bind_param(stmt, 1, u_email)
            ibm_db.bind_param(stmt, 2, u_password)
            ibm_db.execute(stmt)
                
            msg ="Successfully Registered"
            return (render_template("login.html", msg=msg ))
            
@app.route("/logout")
def logout():
    session.pop('LoggedIN', None)
    session.pop("email", None)
    return redirect("enquiry")
    #     return redirect("/")
    # return render_template('login.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)