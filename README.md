# Project RedHorse

# Table of Contents
1. [What the?](#what-the)
1. [Quickstart](#quickstart)
1. [Documentation](#documentation)
1. [Pre-Commit](#pre-commit)
1. [Testing](#testing)
1. [Linting](#linting)
1. [File Formatter](#file-formatter)

## What the?
This is a POC for QA Test Case generator using OpenAI.
The collected images are stored in the `./images` folder which will be encoded into base64.
The software will set the AI's role and generate a prompt along with the images collected and feeds into OpenAI.
OpenAI then creates test cases for each of the images provided.
These test cases are stored in a text file - `./test-cases.txt`

## Quickstart
1. Fork the repo
1. Navigate to the project folder
1. Create your Python environment `python -m venv ./env`
1. Activate your Python environment `./env bin activate` (`.\env\Scripts\activate.bat` on Windows)
1. Run `pip install -r requirement.txt`
1. Run `python main.py`

## Example Generated Test Cases from the `./images` example path
### Test Cases for Image 1 (Sign in to X)

#### General Functional Tests

1. **Test Case:** Check Google Sign-In button functionality
   - **Steps to Reproduce:**
     1. Click on the "Sign in with Google" button.
     2. Observe if the Google sign-in page opens.
     
2. **Test Case:** Check Apple Sign-In button functionality
   - **Steps to Reproduce:**
     1. Click on the "Sign in with Apple" button.
     2. Observe if the Apple sign-in page opens.

3. **Test Case:** Verify form submission with valid credentials
   - **Steps to Reproduce:**
     1. Enter valid email/phone/username in the text box.
     2. Click on the "Next" button.
     3. Observe if it navigates to the password input page.

4. **Test Case:** Verify form submission with invalid credentials
   - **Steps to Reproduce:**
     1. Enter invalid email/phone/username in the text box.
     2. Click on the "Next" button.
     3. Observe if an error message is displayed.

5. **Test Case:** Check "Forgot password?" link functionality
   - **Steps to Reproduce:**
     1. Click on the "Forgot password?" link.
     2. Observe if it navigates to the password reset page.

6. **Test Case:** Check "Sign up" link functionality
   - **Steps to Reproduce:**
     1. Click on the "Sign up" link.
     2. Observe if it navigates to the registration page.

#### Usability and UI Tests

7. **Test Case:** Check accessibility of all clickable elements
   - **Steps to Reproduce:**
     1. Navigate through buttons and links using the keyboard (Tab key).
     2. Observe if elements are accessible.

8. **Test Case:** Verify placeholder text in input field
   - **Steps to Reproduce:**
     1. Check for presence of placeholder text "Phone, email, or username" in the input field.
     2. Observe if the placeholder text is displayed.

9. **Test Case:** Validate the color contrast of the text
   - **Steps to Reproduce:**
     1. Check the contrast ratio of the text against the background.
     2. Use a contrast checker tool to verify it meets accessibility standards.

10. **Test Case:** Check the responsiveness of the layout
    - **Steps to Reproduce:**
      1. Resize the browser window.
      2. Observe if the layout adjusts properly without overlapping elements.

#### Negative Tests

11. **Test Case:** Test form submission with an empty input field
    - **Steps to Reproduce:**
      1. Leave the email/phone/username field empty.
      2. Click on the "Next" button.
      3. Observe if an error message is displayed.

12. **Test Case:** Enter special characters in the input field
    - **Steps to Reproduce:**
      1. Enter special characters like "!@#$%" in the input field.
      2. Click on the "Next" button.
      3. Observe if an error message is displayed.

13. **Test Case:** Enter very long input in the input field
    - **Steps to Reproduce:**
      1. Enter a long string (more than 100 characters) in the input field.
      2. Click on the "Next" button.
      3. Observe if an error message is displayed.

### Test Cases for Image 2 (Facebook Login Page)

#### General Functional Tests

14. **Test Case:** Check "Log In" button functionality
    - **Steps to Reproduce:**
      1. Enter valid email/phone and password.
      2. Click on the "Log In" button.
      3. Observe if the homepage loads.

15. **Test Case:** Check "Create new account" button functionality
    - **Steps to Reproduce:**
      1. Click on the "Create new account" button.
      2. Observe if the registration form opens.

16. **Test Case:** Check "Forgot password?" link functionality
    - **Steps to Reproduce:**
      1. Click on the "Forgot password?" link.
      2. Observe if it navigates to the password recovery page.

#### Usability and UI Tests

17. **Test Case:** Verify initial focus on the input field
    - **Steps to Reproduce:**
      1. Reload the page.
      2. Observe if the cursor is in the "Email or phone number" input field.

18. **Test Case:** Validate the text alignment in the input fields
    - **Steps to Reproduce:**
      1. Check that the entered text is aligned to the left within the input fields.
      2. Observe for inconsistencies.

19. **Test Case:** Check for consistent button styles
    - **Steps to Reproduce:**
      1. Inspect the "Log In" and "Create new account" buttons.
      2. Observe if they have consistent styling (font, size, color).

20. **Test Case:** Verify the visibility of all text on the page
    - **Steps to Reproduce:**
      1. Check that all text is clearly visible and readable against the page background.
      2. Use a screen reader to check for accessibility.

#### Negative Tests

21. **Test Case:** Test form submission with incorrect credentials
    - **Steps to Reproduce:**
      1. Enter incorrect email/phone and password.
      2. Click on the "Log In" button.
      3. Observe if an error message is displayed.

22. **Test Case:** Submit form with empty password field
    - **Steps to Reproduce:**
      1. Enter a valid email/phone number.
      2. Leave the password field empty.
      3. Click on the "Log In" button.
      4. Observe if an error message is displayed.

### Test Cases for Image 3 (Google Search Page)

#### General Functional Tests

23. **Test Case:** Verify Google Search button functionality
    - **Steps to Reproduce:**
      1. Enter a search term in the input field.
      2. Click on the "Google Search" button.
      3. Observe if the search results page loads.

24. **Test Case:** Verify "I'm Feeling Lucky" button functionality
    - **Steps to Reproduce:**
      1. Enter a search term in the input field.
      2. Click on the "I'm Feeling Lucky" button.
      3. Observe if it navigates to the top result page.

#### Usability and UI Tests

25. **Test Case:** Verify that the microphone icon is functional
    - **Steps to Reproduce:**
      1. Click on the microphone icon in the input field.
      2. Observe if it starts voice search.

26. **Test Case:** Check the availability of language options
    - **Steps to Reproduce:**
      1. Observe the "Google offered in: [languages]" section.
      2. Click on a different language.
      3. Observe if the page language changes correctly.

27. **Test Case:** Verify autopopulate search suggestions
    - **Steps to Reproduce:**
      1. Start typing a common search term in the input field.
      2. Observe if search suggestions are displayed below the input field.

28. **Test Case:** Test Google Doodles functionality
    - **Steps to Reproduce:**
      1. Observe if Google Doodle is displayed.
      2. Click on the Doodle.
      3. Observe if it navigates to the related Doodle page.

#### Negative Tests

29. **Test Case:** Enter an extremely long string in the search input
    - **Steps to Reproduce:**
      1. Enter a search query with more than 1000 characters.
      2. Click on the "Google Search" button.
      3. Observe if the search executes without errors.

30. **Test Case:** Enter special characters in the search input
    - **Steps to Reproduce:**
      1. Enter a string of special characters (!@#$%^&*()) in the search input.
      2. Click on the "Google Search" button.
      3. Observe if the search results page loads correctly.