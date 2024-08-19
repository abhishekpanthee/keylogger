# Keylogger Project

This project demonstrates a basic keylogger that logs keystrokes, encrypts sensitive information, and sends the log file to a specified email address.

## Features
- Logs all keystrokes made on the computer.
- Encrypts sensitive information such as email address, password, and recipient email address.
- Sends the log file as an attachment to the specified email address.

## Requirements
- Python 3.x
- `pynput` library for keyboard input
- `smtplib` library for sending emails
- `cryptography` library for secure encryption

## Installation
1. Install the required libraries:

```
pip install pynput pip install cryptography

```
2. Replace the placeholders in the keylogger script with your own information:
- `"*****@gmail.com"`: Replace with your Gmail email address.
- `"***********"`: Replace with your Gmail password.
- `"************.com.np"`: Replace with the email address of the recipient.

3. Generate encryption keys for the sensitive information:
- Open the encryption script (`encrypt.py`) and run it to generate encryption keys for the email address, password, and recipient email address.
- Replace the placeholders in the keylogger script with the generated encryption keys.

## Usage

1. Run the encrypt file

```
python encrypt.py

```

2. Run the keylogger script:

```
python keylogger.py
```

## Support

For support, email info@abhishekpanthee.com.np 