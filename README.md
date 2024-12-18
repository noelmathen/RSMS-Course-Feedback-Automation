﻿# RSMS Course Feedback Automation

<a href="https://colab.research.google.com/drive/1bfAsV0ZV2N6rq-mf9UJsdkMOh_bxKbri#scrollTo=7Ej573meCjNg" target="_blank"><strong>Course_Feedback.ipynb</strong></a>

Easily run this script on Google Colab with the provided notebook.

## Overview

This script automates the process of filling out course feedback on the RSMS platform. It uses Selenium WebDriver to interact with the webpage and complete the feedback form by selecting the highest rating for all feedback options.

### Features

- **Automated Login**: Logs in using the provided user credentials.
- **Course Selection**: Iterates through the list of available subjects for feedback.
- **Feedback Submission**: Automatically selects the highest rating (`5`).
- **Error Handling**: Detects missing elements and provides feedback if questions are not added for a particular course.

### Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- `webdriver_manager` library for managing the ChromeDriver
- Selenium library

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Install Required Libraries**:
   ```bash
   pip install selenium webdriver-manager
   ```

### Usage

1. **Run the Script**:
   ```bash
   python feedback_automation.py
   ```

2. **Provide Credentials**:
   - Enter your **username** and **password** when prompted.

3. **Script Execution**:
   - The script logs in, navigates to the course feedback section, and fills out feedback for each course.

### Google Colab Version

If you prefer not to install anything locally, you can use the Colab version of this script:

[**Course_Feedback.ipynb**](https://colab.research.google.com/drive/1bfAsV0ZV2N6rq-mf9UJsdkMOh_bxKbri#scrollTo=7Ej573meCjNg)

Simply open the link, follow the instructions, and run the cells to complete your feedback.

### Important Notes

- This script is designed for educational purposes and personal use. Ensure you have permission to automate tasks on the RSMS platform.
- Use it responsibly and do not share your credentials with anyone.
- The script may need updates if there are changes in the RSMS platform's UI or structure.

### Troubleshooting

- **NoSuchElementException**: This error may occur if the webpage elements are not found. Ensure the webpage has loaded fully before running the script.
- **TimeoutException**: If the script waits too long for an element, increase the timeout duration in the `WebDriverWait` calls.
- **Incorrect Credentials**: If you receive an "Incorrect credentials" message, verify your username and password.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

### Acknowledgements

- Selenium WebDriver
- [WebDriver Manager](https://github.com/SergeyPirogov/webdriver_manager)

### Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

---

Feel free to customize this README further based on your needs!
