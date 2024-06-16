
# Home Handler

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Django CI](https://github.com/MenasheKoren/homehandler/actions/workflows/django.yml/badge.svg)](https://github.com/MenasheKoren/homehandler/actions/workflows/django.yml)

Home Handler is a Django-based web application designed to help users manage and organize their home-related tasks efficiently.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Home Handler is a web application built with Django to help users manage their home-related tasks. It currently features a to-do list that allows users to add, edit, and delete tasks. This project aims to provide a comprehensive solution for household task management, with plans to include features such as calendars, grocery lists, and reminders in future updates.

### Built with TDD

Home Handler has been developed using Test-Driven Development (TDD) principles. This approach ensures that all features are thoroughly tested and that the codebase remains maintainable and free of bugs. By writing tests before implementing functionality, we aim to deliver a robust and reliable application.

## Installation

### Prerequisites
- Python 3.12+
- Django 5.x

### Steps

```sh
git clone https://github.com/MenasheKoren/homehandler.git
cd homehandler
python -m venv env

# On Windows
.\env\Scriptsctivate
# On Unix or MacOS
source env/bin/activate

pip install -r requirements.txt
python manage.py migrate
```

## Usage

After setting up the project, follow these steps to use the application:

1. **Start the development server:**
   ```sh
   python manage.py runserver
   ```

2. **Access the application:**
   Open your web browser and navigate to `http://127.0.0.1:8000/`.

3. **Using the To-Do List:**
   - **Add a Task**: Click on the "Add Task" button, fill in the task details, and submit.
   - **Update a Task**: Click on the "Update" button next to the task you want to modify, update the details, and save.
   - **Delete a Task**: Click on the "Delete" button next to the task you want to remove.

Feel free to explore the application and test its features. As the project develops, more functionality will be added to enhance the user experience.

4. **Run Tests**:
   Since the project uses TDD, you can run the test suite to ensure everything is working correctly.
   ```sh
   python manage.py test
   ```

## Features

- Add tasks to the to-do list
- Update existing tasks
- Delete tasks from the list
- View all tasks in a list format

### Planned Features

- Calendar integration for scheduling tasks
- Grocery list management
- Reminders and notifications for tasks

## Contributing

If you have a suggestion that would improve this project, please fork the repo and create a pull request. You can also open an issue with the tag "enhancement".

1. Fork the Project
2. Create your Feature Branch (`git switch -c feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Reporting Issues

If you find a bug, please open an issue [here](https://github.com/MenasheKoren/homehandler/issues) and include details about the bug and steps to reproduce it.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
