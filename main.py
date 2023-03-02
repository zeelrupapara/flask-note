from website import create_app
import os

port = os.environ.get('PORT') | "5000"
app = create_app()

if __name__ == '__main__':
    app.run(debug=True, port=port)
