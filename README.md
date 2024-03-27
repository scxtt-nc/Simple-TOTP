# Simple TOTP Standalone

This repository contains the code for a simple Time-based One-Time Password (TOTP) generator.

## Usage

### Terminal mode

1. Install the required dependencies by running `pip install pyotp`.
2. Run the `main.py` script to generate a TOTP.

### Executable mode

1. Download executable from [Release](https://github.com/Byteintosh/Simple-TOTP/releases)
2. Create secret.env
3. Add secret key to `secret.env` like this `SECRET_KEY=XXXXXXXXXXXXXXXX`

## Build to exe

1. Install pyinstaller by running `pip install pyinstaller`
2. Build by running `pyinstaller main.py --onefile --noconsole`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

Special thanks to the developers of [pyotp](https://github.com/pyotp/pyotp) for providing the library used in this project.