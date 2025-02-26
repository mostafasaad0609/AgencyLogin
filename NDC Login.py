from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://admin-v2.ndceg.com/auth/login")

wait = WebDriverWait(driver, 20)

# Locate username & password fields
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
username_field.send_keys("m.farag")

password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
password_field.send_keys("M@stafa_2717")

# Try different login methods
try:
    # Click login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    driver.execute_script("arguments[0].click();", login_button)  # JavaScript click

    # Alternative: Press Enter key
    # password_field.send_keys(Keys.ENTER)

    # Wait for successful login (Check dashboard class)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "dashboard-container")))
    print("Login successful!")
except:
    # Capture error message if login fails
    try:
        error_message = driver.find_element(By.CLASS_NAME, "error-message")  # Adjust selector
        print("Login failed: ", error_message.text)
    except:
        print("Login failed, no error message detected.")

# Close browser
driver.quit()
