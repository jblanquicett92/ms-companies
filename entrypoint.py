import os
from application import create_app

app = create_app()
app.config.update(
    TESTING=True,
    SECRET_KEY='192b9bdd22ab9ed4d12e236c78afcb9a393ec15f71bbf5dc987d54727823bcbf'
)

if __name__ == '__main__':
    app.run(host=os.getenv("API_HOST"), port=os.getenv("API_PORT"), debug=True)