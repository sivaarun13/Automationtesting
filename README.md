# Automation Exercise Test Cases - Python Selenium

This repository contains automated test scripts written in Python using Selenium WebDriver for the [Automation Exercise](https://automationexercise.com/) website. The test cases are based on the predefined scenarios available on the website.

## 📌 Project Overview

- Developed Selenium-based automation scripts to validate the functionality of the Automation Exercise website.
- Implemented test cases covering various user actions, including login, signup, cart functionality, checkout, and more.
- Used Python and Selenium for automation.

## ⚠️ Issues Faced

I encountered issues with **Add to Cart** functionality in multiple test cases:

1. **Test Case 12**:
   - **Step 5 & Step 7**: Clicking the "Add to Cart" button is failing due to element interaction issues.
   
2. **Test Case 22**:
   - **Dynamically Changing Products**: The "Add to Cart" button does not work consistently, possibly due to changing elements.

These issues are likely related to:
- Elements not being interactable.
- Elements being dynamically loaded or hidden.
- XPath or locator strategy needing improvement.
- Page requiring a delay or explicit wait.

### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Selenium WebDriver
- ChromeDriver (if using Chrome)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/automation-exercise-selenium.git
   cd automation-exercise-selenium

🚀 How to Contribute
If you have suggestions or solutions for the Add to Cart issue, feel free to:

Fork this repository.
Fix the issue and submit a Pull Request.
Report issues under the "Issues" tab.
Any help in debugging the Add to Cart issue is highly appreciated! 🙌

📞 Contact
If you have any questions, feel free to open an issue or reach out via GitHub or Mail 
Mail:- sivaarun.girika@gmail.com
