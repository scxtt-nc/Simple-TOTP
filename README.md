# Simple-TOTP

This repository contains the code for a simple Time-based One-Time Password (TOTP) generator.

## Usage

1. Install the required dependencies by running `pip install -r requirements.txt`.
2. Add secret and password in `secret key` `password here`
3. Run the `main.py` script to generate a TOTP.

## Build to exe

1. Install pyinstaller by running `pip install pyinstaller`
2. Build by running `pyinstaller main.py --onefile --noconsole`

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Acknowledgements

Special thanks to the developers of [pyotp](https://github.com/pyotp/pyotp) for providing the library used in this project.
