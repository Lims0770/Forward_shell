# Forward_shell
## Description

This script creates a reverse shell over HTTP using a PHP backdoor hosted on a web server. It allows remote command execution on a compromised machine by sending commands via HTTP requests and handling input/output through FIFO pipes.

## Features

Executes remote shell commands via HTTP.

Uses Base64 encoding to evade detection.

Implements a pseudo-terminal mode.

Stores input/output in temporary files (/dev/shm/).

Supports custom command options (e.g., enum suid).

## Installation

### Requirements:

Python 3

requests library

termcolor library

### Install dependencies:

`pip install requests termcolor`

## Usage

Run the script:

`python3 forward_shell.py`

Once the script starts, enter commands, and they will be executed remotely.

## Example
```bash
> whoami
root
> ls -la
-rw-r--r-- 1 root root 1234 Mar 12 10:00 secret.txt
```
## Security Warning

This script is for educational and research purposes only. Unauthorized use is illegal and punishable by law.
