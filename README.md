# Email Campaign Management Service

Email Campaign Management Service is a web application built using Django that allows users to create, schedule, and manage email
distributions.

## Table of Contents

- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
    - [Creating a Message](#creating-a-message)
    - [Scheduling Distribution](#scheduling-distribution)
    - [Managing Distributions](#managing-distributions)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

Before you begin, make sure you have the following installed:

- Python (3.6 or higher)
- Redis Server (for caching and background tasks)

You can start the Redis Server with the following command:

  ```shell
  sudo service redis-server start
  ```

### Installation

1. Clone the repository to your local machine:

  ```shell
  git clone https://github.com/Khasanov1988/Coursework6.git
  ```

2. Navigate to the project directory:

  ```shell
  cd messaging-service
  ```

3. Create a virtual environment and activate it:

  ```shell
  python -m venv venv
  source venv/bin/activate
  ```

4. Install the project dependencies:

  ```shell
  pip install -r requirements.txt
  ```

5. Apply migrations to set up the database:

  ```shell
  python manage.py migrate
  ```
6. Fill out the models required for work:

  ```shell
  python manage.py fill_interval
  python manage.py fill_status
  ```

7. Start the development server:

  ```shell
  python manage.py runserver
  ```

The project should now be running at http://localhost:8000.

## Features

Create and save email messages with subjects and content.
Schedule email distributions at specific times and intervals.
View distribution logs to track sent emails and delivery status.

## Usage

### Creating a Message

1. Log in to the application.
2. Click on "Create Message" in the navigation menu.
3. Fill in the subject and content of the message.
4. Click "Save" to create the message.

### Scheduling Distribution

1. After creating a message, click on "Schedule Distribution" for that message.
2. Set the distribution start time, stop time, and periodicity.
3. Click "Save" to schedule the distribution.

### Managing Distributions

* View a list of scheduled distributions on the home page.
* To edit or delete a scheduled distribution, click on the distribution title and use the respective buttons.

## Contributing

Contributions are welcome!

## License

This project is licensed under the MIT License