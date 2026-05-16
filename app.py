from flask import Flask, render_template

app = Flask(__name__)

skills = [
    {"name": "Python", "level": 85},
    {"name": "Flask", "level": 85},
    {"name": "JavaScript", "level": 70},
    {"name": "HTML & CSS", "level": 80},
    {"name": "AI / ML", "level": 60},
]

projects = [
    {"name": "Nigeria Map Game", "description": "An interactive game to help users learn about Nigerian states and capitals. It provides a fun and engaging way to test one's knowledge of Nigeria's geography.", "link": "https://nigeriamapgamebyjosh.onrender.com/"},
    {"name": "ChemistryLab", "description": "A web application for chemistry students to visualize molecular structures. It allows users to explore and interact with various molecular models of chemical compounds.", "link": "https://chemistrylab.onrender.com"},
]

@app.route("/")
def index():
    return render_template("index.html", skills=skills, projects=projects)

if __name__ == "__main__":      
    app.run(port=5005,debug=True)