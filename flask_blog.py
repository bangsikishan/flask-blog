from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'Author':'Kishan',
        'Title':'Book 1',
        'Content':'Posts 1',
        'Date':'Today'
    },
    {
        'Author':'Ajax',
        'Title':'Book 2',
        'Content':'Posts 2',
        'Date':'Yesterday'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)