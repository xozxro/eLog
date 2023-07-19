# eLog: Notion-based Error Logging

`eLog` is a Python library designed to help you log errors to a specific Notion database. It takes an error and the filename where the error originates from as input, then uses the Notion API to either update an existing page in the database or create a new one, depending on whether a page with matching error and filename already exists.

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
git clone https://github.com/username/eLog.git
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

Execute the created script to set env variables:
```
./set_env.sh
```
Or
```
set_env.bat
```

Done!

## Usage

### As an external script

Run the script from the command line (or any other language):

```
elog "filename.py" "This is your error message"
```

### As a Python library

Import and use the library in your Python script:

```
from eLog import eLog
e = eLog('test.py')
e.log('Succesfully pushed an error!')
```

## Contributing

We welcome contributions! Please see our contributing guidelines for more details.

## License

This project is licensed under the terms of the MIT license. See LICENSE for more details.

