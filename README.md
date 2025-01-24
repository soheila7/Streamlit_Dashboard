# Password Generator Streamlit App

This is a simple Streamlit-based web application that allows users to generate different types of passwords. It supports three types of password generators:

- Random Password
- Memorable Password
- Pin Code

The app provides an interactive interface to specify parameters for each password type and generates a password based on the user's choices.

## Features

- **Random Password**: Generates a random password with customizable length and options to include symbols and numbers.
- **Memorable Password**: Generates a password made up of multiple words, customizable with a separator and capitalization options.
- **Pin Code**: Generates a numeric pin code with a customizable length.

## Prerequisites

Before running this app, make sure you have the following installed:

- Python 3.10 or higher
- Streamlit library
- Any required dependencies for password generators (these should be installed via `pip`)

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/password-generator-app.git
   ```
2. Navigate into the project directory:
   ```bash
   cd streamlit_example/src
   ```
3. Install the required dependencies:
    ```bash
    pip install streamlit
    ```
4. Make sure the directory structure is correct, including:

    - The src/password_generators.py file
    - The banner.png image in the src folder (or update the image path in the code if you want to use a different image).

## Running the App

To run the Streamlit app, use the following command:

```bash
streamlit run streamlit_dashboard.py
```
This will start a local server, and you can view the app by opening http://localhost:8501 in your web browser.

## How It Works

The app allows you to choose one of the following password generators via a radio button:

- **Random Password**
- **Memorable Password**
- **Pin Code**

Depending on the selected option, the app prompts the user to provide additional settings:

- **For Random Password**: Select length, and toggle options to include symbols and numbers.
- **For Memorable Password**: Choose the number of words, separator, and toggle capitalization.
- **For Pin Code**: Select the length of the pin code.

After specifying the parameters, the app generates the password and displays it on the page.

## Customizing the Banner

The app displays a banner image located at `src/banner.png`. You can replace this image with your own by placing it in the `src` folder or modifying the image path in the code.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.