from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
db = SQLAlchemy(app)
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

#database schema
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=False, nullable=False)
#  we print this return as object
    def __repr__(self) -> str:
        return f"{self.username}-{self.email}"
 

with app.app_context():
     db.create_all()

@app.route('/')
def hello_world():
    
    user=User(username='admi', email='admn@example.com')
    db.session.add(user)
    db.session.commit()
    allquery=User.query.all()
    # print(allquery)
    return render_template('index.html',allQuery=allquery)



if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
