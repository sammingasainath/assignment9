from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///score.db'
db = SQLAlchemy(app)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    marks = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Score %r>' % self.id


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        score_subject = request.form['subject']
        score_marks = request.form['marks']
        new_score = Score(subject = score_subject, marks = score_marks)

        try:
            db.session.add(new_score)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your Score'

    else:
        scores = Score.query.order_by(Score.date_created).all()
        return render_template('index.html', scores=scores)


@app.route('/delete/<int:id>')
def delete(id):
    score_to_delete = Score.query.get_or_404(id)

    try:
        db.session.delete(score_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that Score'

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    score = Score.query.get_or_404(id)

    if request.method == 'POST':
        score.marks = request.form['marks']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your score'

    else:
        return render_template('update.html', score=score)


if __name__ == "__main__":
    app.run(debug=True)