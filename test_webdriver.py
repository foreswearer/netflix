from selenium import webdriver

# Path to ChromeDriver
chrome_driver_path = './chromedriver.exe'

# Set up WebDriver
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Open a webpage
driver.get("https://www.google.com")

# Print the page title
print(driver.title)

# Close the browser
driver.quit()
