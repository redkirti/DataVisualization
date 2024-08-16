---

# Graph Visualization Web App

## Overview

This web application allows users to upload CSV files and create customizable graphs based on different separators. The app is built using Django for the backend, with graph visualization functionalities powered by Matlab and matplotlib. Data is stored in a PostgreSQL database.

## Features

- **CSV Data Upload**: Users can upload CSV files with varying separators.
- **Customizable Graph Creation**: The app supports creating different types of graphs based on the uploaded data.
- **Graph Types**:
  - Line
  - Bar
  - Pie
  - Histogram
- **Graph Export**: Graphs can be exported in various formats for use in reports and presentations.

## Technologies Used

- **Django**: Backend framework for handling web requests and database interactions.
- **Matlab**: Used for advanced data processing and visualization.
- **matplotlib**: Python library for creating static, animated, and interactive visualizations.
- **PostgreSQL**: Relational database system used for data storage.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/graph-visualization-webapp.git
   cd graph-visualization-webapp
   ```

2. Install the necessary dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:

   ```bash
   python manage.py migrate
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

5. Access the web app at `http://127.0.0.1:8000/` in your web browser.

## Usage

1. Upload a CSV file through the provided interface.
2. Select the desired separator for your CSV file.
3. Choose the type of graph you want to generate (line, bar, pie, or histogram).
4. Customize the graph settings (if necessary).
5. Generate the graph.
6. Export the graph in the desired format.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [Django](https://www.djangoproject.com/)
- [matplotlib](https://matplotlib.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [Matlab](https://www.mathworks.com/products/matlab.html)

---
