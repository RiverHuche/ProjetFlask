import random, string, os
#"".join([random.choice(string.printable) for _ in os.urandom(24)])
SECRET_KEY="ff69c544-0134-4cca-9a7d-b23726b9e1c5"
ABOUT = "Bienvenue sur la page à propos de Flask !"
CONTACT = "Pour tout autres questions, veuillez nous laisser un message via notre adresse mail : bonjour@iutO.fr"
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'monApp.db')
BOOTSTRAP_SERVE_LOCAL = True