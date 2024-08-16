
# Graph Visualization Web App

This web application is built using Django, Matlab, and PostgreSQL, allowing users to upload CSV files and create customizable graphs. The app leverages `matplotlib` to generate and export graphs in various formats, such as line, bar, pie, and histogram.

## Features

- **CSV File Upload**: Users can upload CSV files to the app.
- **Graph Customization**: Based on the uploaded data, users can select different graph types (line, bar, pie, histogram).
- **Matplotlib Integration**: The app uses `matplotlib` to generate graphs and export them in different formats.
- **Database**: PostgreSQL is used to store information about the uploaded files.

## Requirements

- Python 3.x
- Django 3.x
- PostgreSQL
- Matplotlib
- Matlab (optional for specific features)

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure your PostgreSQL database in the `settings.py` file:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'your_db_name',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

4. Run migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django server:
    ```bash
    python manage.py runserver
    ```

6. Access the web application by navigating to `http://127.0.0.1:8000` in your web browser.

## Usage

- Upload a CSV file via the upload form.
- Select the type of graph you want to generate.
- The app will process the CSV data and display the graph.
- You can export the graph in various formats.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
