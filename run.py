from goodhabits import create_app
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/goodhabits')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

app = create_app()

if __name__ == '__main__':
	app.run(debug=True)