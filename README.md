# BangazonAPI

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contribute](#contribute)
- [Credits](#credits)
- [License](#license)

## Installation
1. `git clone` [https://github.com/PythonicPenguins/bangazon_api.git](https://github.com/PythonicPenguins/bangazon_api.git) into a local directory of your choice.
1. `cd bangazon_api/bangazon/bangazon_api/migrations`
1. Delete all files except `__init__.py`
1. Delete the `db.sqlite3` file at `bangazon_api/bangazon/db.sqlite3`
1. Open the terminal of choice and cd to the following path `bangazon_api/bangazon` and run the following commands:
    1. `python manage.py makemigrations`
    1. `python manage.py migrate`
    1. `python manaage.py createsuperuser` follow the prompt for creating super user.
    1. `python manage.py load_data`

## Usage
1. `python manage.py runserver`
1. Open a browser and go to `127.0.0.1:8000`
1. On the up right had corner click the login button and login with the credentials you just created.
1. Enjoy looking your data!!!

## Contribute
1. Fork it!
1. Submit a pull request :D
1. We'll review and let you know.

## Credits
Project Manager:
 - Steve Brownlee

Maintainers:
- Meg Ducharme
- Gilberto Diaz

## License
[MIT © BANGAZON LLC](./LICENSE)