# Python client and server for file sync across multiple machines

## Requirements

Ptyhon 3.6 or later

## Installation
Create virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

```bash
source venv/bin/activate
```

Install the requirements:

```bash
pip install -r requirements.txt
```

## Building the client:

The client is built with the `install.sh` script.
You will need`pyinstaller` installed. 

```bash
cmod +x install.sh
./install.sh
```

This will create a `dist` directory with the client executable.
Add the executable to your PATH.

```bash
export PATH=$PATH:$PWD/dist
```

## Running the server:
Run the server with the `uvicorn` command.

```bash
uvicorn server:app
```

This will start the server on port 8000.

**[OPTIONAL]** - You can be notified when a file is uploaded to the server by email.

To enable email notifications add the following environment variables to your shell:

```bash
export GMAIL_USER='<your_gmail_user>'
export GMAIL_PASSWORD='<your_gmail_password>'
```

It will use those to connect to your gmail account and send an email when a file is uploaded.

Read more about it [in this article](https://realpython.com/python-send-email/)




