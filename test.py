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
    <br>
    <hr>
    <br>1.<a href=/catAge class="button-link"> Cat Age to Human Age</a><br>
    <br>2.<a href=/catName class="button-link"> Cat Name Generator </a><br>
    <br>3.<a href=/randomMovie class="button-link"> Cat Movie Generator</a><br>
    <br>4.<a href=/aboutCat class="button-link"> About Cats </a><br>
    </br>""")
    
    return render_template('template.html', titleText=titleText, bodyText=bodyText)

@app.route('/catAge')
def catAge():
	titleText="How old is your cat in human years?"
	bodyText=  Markup("""
	If your cat is blank years old, then it is blank human years old
	<br>

	<br>
	
	</br>""")
	return render_template('template.html',titleText=titleText,bodyText=bodyText)
@app.route('/white')
def whiteName():
    cursor = cnx.cursor()
    titleText = "White Cat Names"
    bodyText = Markup("<table><tr><td> Names: </td><td><br>")
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
    bodyText = Markup("<table><tr><td> Names: </td><td><br>")
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
    bodyText = Markup("<table><tr><td> Names: </td><td><br>")
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
    bodyText = Markup("<table><tr><td> Names: </td><td><br>")
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
    bodyText = Markup("<table><tr><td> Names: </td><td><br>")
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
    Please select the color of your cat:<br><br>
    <a href=/white>white</a>
    <br>
    <a href=/orange>orange</a>
    <br>
    <a href=/black>black</a>
    <br>
    <a href=/gray>gray</a>
    <br>
    <a href=/brown>brown</a>
    
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
	10 Cool Facts About Cats:
	<br>
    <br>
    <br>
1. Whisker Navigation: A cat's whiskers are about as wide as its body, helping it navigate through tight spaces.They're extremely<br> sensitive and help cats detect changes in their environment.
<br>
<br>
2. Purring: Cats not only purr when they're content but also when they're injured or stressed. Some researchers believe purring<br> can have healing properties and can help lower stress levels in both cats and humans.
<br>
<br>
3. Feline Agility: Cats are incredibly agile creatures.They have a flexible backbone and lack a collarbone, allowing them to twist<br>and contort their bodies in remarkable ways.
<br>
<br>
4. Communication through Tail: A cat's tail is a significant indicator of its mood. A flicking or twitching tail might mean irritation<br> or excitement, while a tucked tail could signify fear or submission.
<br>
<br>
5. Superior Night Vision: Cats have excellent night vision, about six times better than that of humans.Their eyes contain more<br>rods, specialized cells that work well in low light.
<br>
<br>
6. No Sweet Tooth: Cats lack taste receptors for sweetness. That's why they're not interested in sugary treats like humans are.
<br>
<br>
7. Self-Cleaning Experts: Cats spend about a third of their waking hours grooming themselves. Their tongues have tiny hook-like <br>structures that help remove dirt and loose fur.
<br>
<br>
8. Unique Nose Prints: Like human fingerprints, a cat's nose print is unique to that cat. It can be used for identification,<br> just like a fingerprint for humans.
<br>
<br>
9. Napping Experts: Cats are known for their love of napping.\nOn average, they sleep for about 12-16 hours a day, with some cats<br> sleeping up to 20 hours!
<br>
<br>
10. Unusual Water Preference: Unlike most animals, many cats dislike getting their fur wet. This aversion to water is thought to be<br>because their coats don't dry easily, making them feel uncomfortable.
<br>
<br>
	
	</br>""")
	return render_template('template.html', titleText = titleText, bodyText = bodyText)



if __name__ == '__main__':
    app.run(debug=True)
