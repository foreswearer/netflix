import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get sensitive data from environment variables
netflix_email = os.getenv('NETFLIX_EMAIL')
netflix_password = os.getenv('NETFLIX_PASSWORD')

# Path to your ChromeDriver
chrome_driver_path = './chromedriver.exe'

# Set up download directory
download_dir = os.path.join(os.getcwd(), "NetflixDownloads")  # Save in the same directory as the script

if not os.path.exists(download_dir):
    os.makedirs(download_dir)  # Create the directory if it doesn't exist

# Setting up Chrome WebDriver with download preferences
chrome_options = Options()
prefs = {
    "download.default_directory": download_dir,  # Set the download directory
    "download.prompt_for_download": False,  # Do not prompt for download
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
}
chrome_options.add_experimental_option("prefs", prefs)
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Netflix URL for viewing activity
netflix_viewing_activity_url = 'https://www.netflix.com/viewingactivity'


# Function to log into Netflix
def netflix_login(email, password):
    driver.get("https://www.netflix.com/login")
    time.sleep(2)

    # Use CSS selectors for the email and password input fields
    email_input = driver.find_element(By.CSS_SELECTOR, "input[name='userLoginId']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")

    # Enter credentials
    email_input.send_keys(email)
    password_input.send_keys(password)

    # Click on the login button
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    time.sleep(5)


# Function to download viewing activity CSV
def download_viewing_activity():
    driver.get(netflix_viewing_activity_url)

    try:
        # Wait for the "Download All" button to appear (we assume a button exists for this)
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.LINK_TEXT, 'Download all')))

        # Click the "Download All" button
        download_button = driver.find_element(By.LINK_TEXT, 'Download all')
        download_button.click()

        # Wait for a few seconds to allow the download to complete
        time.sleep(10)

        print(f"Viewing history has been saved to: {download_dir}")

    except Exception as e:
        print(f"Error occurred while trying to download the viewing activity CSV: {e}")


# Main function to log in and download viewing history
def export_viewing_history(email, password):
    # Log into Netflix
    netflix_login(email, password)

    # Download the viewing activity CSV
    download_viewing_activity()

    # Quit the driver
    driver.quit()


# Run the export function
export_viewing_history(netflix_email, netflix_password)
