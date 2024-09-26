import openai
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import mysql.connector  # Use psycopg2 for PostgreSQL

# Step 1: Set OpenAI API Key
openai.api_key = 'your-openai-api-key'

# Step 2: Set up Chrome WebDriver (headless mode)
options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

# Step 3: Connect to MySQL Database (or PostgreSQL)
db = mysql.connector.connect(
    host="localhost",
    user="myuser",
    password="mypassword",
    database="mydatabase"
)
cursor = db.cursor()

# Function to fetch trending topics using Google Trends
def get_trending_topics():
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list=['Technology', 'Finance', 'Startups'], timeframe='now 1-d')
    trending_data = pytrends.related_queries()
    # Extract the top 5 trending queries under 'Technology'
    topics = [query['query'] for query in trending_data['Technology']['top'][:5]]
    return topics

# Function to generate blog content using GPT-4
def generate_blog_content(title, topic):
    response = openai.Completion.create(
      model="gpt-4",
      prompt=f"Write a detailed blog post on {topic}. The title is {title}. Include an introduction, main content, and conclusion.",
      max_tokens=2000
    )
    return response.choices[0].text

# Function to generate an image using DALL·E
def generate_blog_image(topic):
    response = openai.Image.create(
        prompt=f"An artistic representation of {topic} in a modern, futuristic style",
        n=1,
        size="1024x1024"
    )
    return response['data'][0]['url']

# Function to login to Medium and publish the blog
def login_and_publish(title, content, image_url):
    driver.get("https://medium.com/login")
    time.sleep(5)

    # Manual or automated login to Medium (you can automate login with your credentials)
    email_input = driver.find_element_by_name('email')
    email_input.send_keys('your-email')
    email_input.send_keys(Keys.RETURN)
    time.sleep(2)

    password_input = driver.find_element_by_name('password')
    password_input.send_keys('your-password')
    password_input.send_keys(Keys.RETURN)
    time.sleep(5)

    # Navigate to new story creation page
    driver.get("https://medium.com/new-story")
    time.sleep(5)

    # Insert title and content
    title_input = driver.find_element_by_tag_name('h1')
    title_input.send_keys(title)

    content_input = driver.find_element_by_tag_name('p')
    content_input.send_keys(content)

    # Insert image using JavaScript
    driver.execute_script(f"document.execCommand('insertImage', false, '{image_url}')")

    # Publish the post
    publish_button = driver.find_element_by_xpath("//button[text()='Publish']")
    publish_button.click()
    time.sleep(2)

    # Confirm and notify followers
    confirm_button = driver.find_element_by_xpath("//button[text()='Confirm']")
    confirm_button.click()

# Main function that coordinates the entire process
def main():
    # Step 1: Get trending topics
    topics = get_trending_topics()

    for topic in topics:
        title = f"How {topic} is Transforming Technology"
        
        # Step 2: Generate blog content
        content = generate_blog_content(title, topic)
        
        # Step 3: Generate blog image
        image_url = generate_blog_image(topic)
        
        # Step 4: Log in to Medium and publish
        login_and_publish(title, content, image_url)

    print("All blogs published successfully!")

# Execute the script
if __name__ == "__main__":
    main()

# Close the driver
driver.quit()
