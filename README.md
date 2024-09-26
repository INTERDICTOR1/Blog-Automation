Blog Automation with GPT-4

This project automates the generation and publishing of blog posts using OpenAI's GPT-4, integrated with Medium via the Medium API. It also leverages Selenium for web scraping and interaction with online platforms, hosted on an AWS EC2 instance for continuous operation.
Features

    GPT-4 Integration: Automatically generates blog content using OpenAI's GPT-4 API.
    Web Scraping: Uses Selenium for scraping article topics, trends, and relevant information to create engaging blog posts.
    Medium API Integration: Automatically publishes generated blog posts to your Medium account.
    Scheduled Posting: Automates the posting process at specified intervals to maintain a regular content schedule.

Project Status

This project is currently paused. Some key blockers include:

    ChromeDriver Version Mismatch: Issues with compatibility between ChromeDriver and the browser version on the EC2 instance.
    Pending API Key: GPT-4 API key is yet to be integrated.

Roadblocks and Solutions

    ChromeDriver Mismatch:
        Use the latest stable version of ChromeDriver and keep it synchronized with the installed version of Chrome on the EC2 instance.
        Automate the update process for Chrome and ChromeDriver to avoid future mismatches.

    OpenAI API Key:
        Sign up for OpenAI API access and generate the necessary key to integrate GPT-4.

Future Enhancements

    Error Handling: Improve error handling for failed API calls, Selenium operations, and posting to Medium.
    Analytics: Integrate tracking to monitor the performance of published articles, such as views, likes, and comments, directly in Medium.

Prerequisites

    AWS EC2 instance (or any other server hosting environment)
    Python 3.8+
    Chrome browser and compatible ChromeDriver
    OpenAI GPT-4 API key
    Medium Developer API token

Installation

1. Clone the repository:

```
    git clone https://github.com/yourusername/blog-automation.git
    cd blog-automation
```

Create a virtual environment:

```
    python3 -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
```

Install the required dependencies:

```

    pip install -r requirements.txt
```

Set up environment variables: Create a .env file and add your API keys and other sensitive information.

```

OPENAI_API_KEY=your_openai_api_key
MEDIUM_API_TOKEN=your_medium_api_token
```

Configure Selenium: Ensure that the Chrome browser and ChromeDriver versions match. Use this command to install ChromeDriver:

bash

    wget https://chromedriver.storage.googleapis.com/<version>/chromedriver_linux64.zip
    unzip chromedriver_linux64.zip
    sudo mv chromedriver /usr/local/bin/

Usage

To run the automation:

Start your virtual environment:

    

```
source venv/bin/activate
```
Run the main script:


    python automate_blogs.py

This will generate a blog post using GPT-4 and post it on your Medium account.
Troubleshooting

    ChromeDriver errors: Ensure that your ChromeDriver version matches your Chrome browser version. Update ChromeDriver or Chrome as needed.
    OpenAI API: Verify that your API key is correct and has sufficient quota.
    EC2 Setup: Make sure all ports are open for accessing Medium's API, and the instance has internet access.


