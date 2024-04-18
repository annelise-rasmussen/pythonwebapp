from flask import Flask, request, render_template, redirect, url_for, flash, session
from markupsafe import Markup
from random import randint
import datetime
import mysql.connector
import configparser
from werkzeug.security import generate_password_hash, check_password_hash

#you will change the static folder path here to your own static folder path
# Initialize Flask app
app = Flask(__name__)


# Read configuration file for database connection settings
config = configparser.ConfigParser()
configFile = 'contacts.cfg'
config.read(configFile)
database = config['database']

# Database configuration dictionary
db_config = {
    'host': database['host'],
    'user': database['user'],
    'password': database['pass'],
    'database': database['db']
}

db = database['db']
dbHost=database['host']
dbUser=database['user']
dbPass=database['pass']
app.secret_key = database['key']
cnx = mysql.connector.connect(user=dbUser, password = dbPass, host= dbHost, database= db)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash("Both username and password are required.")
            return redirect(url_for('login'))

        try:
            with mysql.connector.connect(**db_config) as conn:
                with conn.cursor() as cursor:
                    cursor.execute("SELECT password_hash FROM contactsTable WHERE name = %s", (username,))
                    user = cursor.fetchone()

            if user and check_password_hash(user[0], password):
                session['username'] = username
                return redirect(url_for('index'))
            else:
                flash("Invalid username or password.")
        except mysql.connector.Error as err:
            flash(f"MySQL Connection Error: {err}")

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)  # Remove the username from the session
    flash("You have been logged out.")
    return redirect(url_for('login'))

@app.route('/')
def index():
    if 'username' not in session:
        flash("You need to log in to view this page.")
        return redirect(url_for('login'))
    titleText = "CatLoversRus"
    bodyText = Markup("""
    <br>
    <h1>We love all things about cats!</h1>
    <nav>
      <ul>
        <li><a href="/convert" class="button-link">Calculate Cat Age in Human Years</a></li>
        <li><a href="/catName" class="button-link">Find the Perfect Cat Name</a></li>
        <li><a href="/randomMovie" class="button-link">Get a Random Cat Movie Suggestion</a></li>
        <li><a href="/aboutCat" class="button-link">Learn More About Cats</a></li>
      </ul>
    </nav>

    """)

    return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/convert', methods=['GET', 'POST'])
def convert():
    if request.method == 'POST':
        age = int(request.form['age'])
        if age == 1:
            human_age = 15
        elif age == 2:
            human_age = 24
        else:
            human_age = 21 + (age - 2) * 4

        titleText = "Conversion Result"
        bodyText = f"Your Cat's age in human years is = {human_age}"
        return render_template('convert.html', titleText=titleText, bodyText=bodyText)

    return render_template('convert.html', titleText="Convert Cat Age", bodyText="Please select your cat's age from the dropdown menu.")


@app.route('/white')
def whiteName():
    cursor = cnx.cursor()
    titleText = "White Cat Names"
    bodyText = Markup("<table><tr><td> For your purrfect snow-white pals, a name that's simply purrfection. <br><br> Names: </td><td><br>")
    query = '''select name from nameTable AS n join colorTable AS c ON n.colorid = c.id where c.colordesc = 'white' '''
    cursor.execute(query)
    for row in cursor:
        name = row[0]  # Accessing the first element of the tuple
        newRow = "<br><tr><td><br>"
        newRow = newRow + name + "</td></td> \n "
        bodyText = bodyText + Markup(newRow)
    bodyText = bodyText + Markup('''</table>
    <br>
    <br>
    <a href=/catName>Back to Colors</a> <!-- Assuming you want to return to the catName function -->
    </br>
    ''')
    return render_template('template.html',titleText=titleText,bodyText=bodyText)

@app.route('/orange')
def orangeName():
    cursor = cnx.cursor()
    titleText = "Orange Cat Names"
    bodyText = Markup("<table><tr><td> For your purrfect sunshine pals, a name that's simply divine. <br><br> Names: </td><td><br>")
    query = '''select name from nameTable AS n join colorTable AS c ON n.colorid = c.id where c.colordesc = 'orange' '''
    cursor.execute(query)
    for row in cursor:
        name = row[0]  # Accessing the first element of the tuple
        newRow = "<br><tr><td><br>"
        newRow = newRow + name + "</td></td> \n "  # Here is the correction: "</td></tr> \n "
        bodyText = bodyText + Markup(newRow)
    bodyText = bodyText + Markup('''</table>
    <br>
    <br>
    <a href=/catName>Back to Colors</a> <!-- Assuming you want to return to the catName function -->
    </br>
    ''')
    return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/black')
def blackName():
    cursor = cnx.cursor()
    titleText = "Black Cat Names"
    bodyText = Markup("<table><tr><td> For your purrfect shadowy pals, a name that's as mysterious as the night! <br><br> Names: </td><td><br>")
    query = '''select name from nameTable AS n join colorTable AS c ON n.colorid = c.id where c.colordesc = 'black' '''
    cursor.execute(query)
    for row in cursor:
        name = row[0]  # Accessing the first element of the tuple
        newRow = "<br><tr><td><br>"
        newRow = newRow + name + "</td></td> \n "
        bodyText = bodyText + Markup(newRow)
    bodyText = bodyText + Markup('''</table>
    <br>
    <br>
    <a href=/catName>Back to Colors</a> <!-- Assuming you want to return to the catName function -->
    </br>
    ''')
    return render_template('template.html',titleText=titleText,bodyText=bodyText)

@app.route('/gray')
def grayName():
    cursor = cnx.cursor()
    titleText = "Gray Cat Names"
    bodyText = Markup("<table><tr><td> For your purrfect misty pals, a name as soft as the morning fog! <br><br> Names: </td><td><br>")
    query = '''select name from nameTable AS n join colorTable AS c ON n.colorid = c.id where c.colordesc = 'gray' '''
    cursor.execute(query)
    for row in cursor:
        name = row[0]  # Accessing the first element of the tuple
        newRow = "<br><tr><td><br>"
        newRow = newRow + name + "</td></td> \n "
        bodyText = bodyText + Markup(newRow)
    bodyText = bodyText + Markup('''</table>
    <br>
    <br>
    <a href=/catName>Back to Colors</a> <!-- Assuming you want to return to the catName function -->
    </br>
    ''')
    return render_template('template.html',titleText=titleText,bodyText=bodyText)

@app.route('/brown')
def brownName():
    titleText = "Brown Cat Names"
    cursor = cnx.cursor()
    titleText = "Brown Cat Names"
    bodyText = Markup("<table><tr><td> For your purrfect caramel-coated pals, a name as sweet as honey! <br><br> Names: </td><td><br>")
    query = '''select name from nameTable AS n join colorTable AS c ON n.colorid = c.id where c.colordesc = 'brown' '''
    cursor.execute(query)
    for row in cursor:
        name = row[0]  # Accessing the first element of the tuple
        newRow = "<br><tr><td><br>"
        newRow = newRow + name + "</td></td> \n "
        bodyText = bodyText + Markup(newRow)
    bodyText = bodyText + Markup('''</table>
    <br>
    <br>
    <a href=/catName>Back to Colors</a> <!-- Assuming you want to return to the catName function -->
    </br>
    ''')
    return render_template('template.html',titleText=titleText,bodyText=bodyText)

@app.route('/catName')
def catName():
	titleText="Choose Your Cat Name"
	bodyText= Markup(""".
	<br>
	<br>
    Looking for a name that's simply purrfection? Look no futher for your purrfect pals! <br><br> Please select the color of your cat:<br><br>
    <a href=/white>White</a>
    <br>
    <a href=/orange>Orange</a>
    <br>
    <a href=/black>Black</a>
    <br>
    <a href=/gray>Gray</a>
    <br>
    <a href=/brown>Brown</a>

	</br>""")
	return render_template('template.html',titleText=titleText,bodyText=bodyText)


def getMovie(random):
    cursor= cnx.cursor()
    query = f"SELECT name FROM movieTable WHERE id = {random}"
    print(random)
    name = ''
    cursor.execute(query)
    name = cursor.fetchone()[0]
    return name  # Return the fetched movie name

@app.route('/randomMovie')
def randomMovie():
    titleText = "Today's Movie Pick"
    name = getMovie(randint(1, 16))
    bodyText = f"You should watch '{name}' today."

    bodyText = bodyText + Markup("""
    <br>

    </br>""")

    return render_template('template.html', titleText=titleText, bodyText=bodyText)


@app.route('/aboutCat')
def aboutCat():
	titleText = "About Cats"
	bodyText= Markup("""
    <h1>10 Cool Facts About Cats</h1>

    <ol>
      <li>
        <strong>Whisker Navigation:</strong> A cat's whiskers are about as wide as its body, helping it navigate through tight spaces. They're extremely sensitive and help cats detect changes in their environment.
      </li>
      <li>
        <strong>Purring:</strong> Cats not only purr when they're content but also when they're injured or stressed. Some researchers believe purring can have healing properties and can help lower stress levels in both cats and humans.
      </li>
      <li>
        <strong>Feline Agility:</strong> Cats are incredibly agile creatures. They have a flexible backbone and lack a collarbone, allowing them to twist and contort their bodies in remarkable ways.
      </li>
      <li>
        <strong>Communication through Tail:</strong> A cat's tail is a significant indicator of its mood. A flicking or twitching tail might mean irritation or excitement, while a tucked tail could signify fear or submission.
      </li>
      <li>
        <strong>Superior Night Vision:</strong> Cats have excellent night vision, about six times better than that of humans. Their eyes contain more rods, specialized cells that work well in low light.
      </li>
      <li>
        <strong>No Sweet Tooth:</strong> Cats lack taste receptors for sweetness. That's why they're not interested in sugary treats like humans are.
      </li>
      <li>
        <strong>Self-Cleaning Experts:</strong> Cats spend about a third of their waking hours grooming themselves. Their tongues have tiny hook-like structures that help remove dirt and loose fur.
      </li>
      <li>
        <strong>Unique Nose Prints:</strong> Like human fingerprints, a cat's nose print is unique to that cat. It can be used for identification, just like a fingerprint for humans.
      </li>
      <li>
        <strong>Napping Experts:</strong> Cats are known for their love of napping. On average, they sleep for about 12-16 hours a day, with some cats sleeping up to 20 hours!
      </li>
      <li>
        <strong>Unusual Water Preference:</strong> Unlike most animals, many cats dislike getting their fur wet. This aversion to water is thought to be because their coats don't dry easily, making them feel uncomfortable.
      </li>
    </ol>
  """)
	return render_template('template.html', titleText = titleText, bodyText = bodyText)



if __name__ == '__main__':
    app.run(debug=True)
