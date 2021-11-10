from app import app

if __name__ == '__main__':
    app.run()

# make app persist after logging on:
# gunicorn --bind 0.0.0.0:<your-desired-port-here> wsgi:app -D
# TO KILL:
# ps ax | grep gunicorn
# kill <processid>