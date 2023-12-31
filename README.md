![Screenshot 2023-07-19 141657](https://github.com/xozxro/eLog/assets/91173681/cfb9c09e-f56e-4b56-844d-b52aca21f4cd)

# eLog: Notion-based Error Logging

`eLog` is a Python library designed to help you log errors to a Notion database, where they can be sorted by file and any other provided data point. It takes an error and the filename as input, then uses the Notion API to either update an existing page in the database or create a new one, depending on whether a page with a matching error and filename already exists. 

This allows you to stay on top of each and every error, between all of your applications and projects. 

## Features

- Searches for existing pages in a Notion database with the same error and filename.
- If a match is found, updates the 'Count' property, records the current time in the 'Last Seen' field, sets the 'Status' property to 'Not Resolved', and overwrites the body with the latest error.
- If no match is found, creates a new page in the database with the provided error and filename, and adds the error details in the body.
- Returns a status code indicating the success or failure of the operation.
- Can be imported as a library or executed as a standalone Python script, making it versatile and compatible with multiple languages.

## Requirements

- Python 3.7+
- [Notion API Key](https://www.notion.so/my-integrations)
- Duplicated [Error Log Notion Page](https://flytlabs.notion.site/255a9161424c473a91c8c2d36678a53b?v=b46290c3087f44b58d93e60d090976e9&pvs=4)

## Installation

Clone the repository:
```
git clone https://github.com/xozxro/eLog.git
cd eLog
```

Install the package:
```
pip install .
```

Configure your Notion API Key and error page:
```
py configure.py
```

Execute the created script as admin to set env variables:
```
sudo ./set_env.sh
```
Or, from an elevated Windows terminal:
```
set_env.bat
```

Done!

## Usage

### As an external script

Run the script from the command line (or any other language):

```
elog filename.py "This is your error message"
```

### As a Python library

Import and use the library in your Python script:

```
from eLog import eLog
e = eLog('test.py')
e.log('Succesfully pushed an error!')
```

## Contributing

We welcome contributions! Please feel free to submit a PR.

## License

This project is licensed under the terms of the MIT license.

