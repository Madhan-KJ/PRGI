from app import create_app
import os

app = create_app()

port = int( os.environ.get("PORT") )

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=port)
