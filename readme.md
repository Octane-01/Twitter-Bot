# Twitter Bot

This is a simple Twitter bot that searches for tweets containing specified keywords and replies with a predefined response. It uses the Twitter API via Tweepy and provides a Streamlit-based frontend.

## Features
- Searches for recent tweets containing specific keywords
- Avoids retweets
- Replies to found tweets with a predefined message
- Uses environment variables for API credentials
- Includes a Streamlit UI for easy interaction

## Prerequisites
- Python 3.7+
- A Twitter Developer account with API access
- Tweepy library
- dotenv library (for managing environment variables)
- Streamlit for the frontend

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/twitter-bot.git
   cd twitter-bot
   ```

2. Create a virtual environment (optional but recommended):
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Create a `.env` file and add your Twitter API credentials:
   ```ini
   API_KEY=your_api_key
   API_SECRET=your_api_secret
   ACCESS_TOKEN=your_access_token
   ACCESS_SECRET=your_access_secret
   BEARER_TOKEN=your_bearer_token
   ```

## Usage

### Running the Bot via Command Line
1. Edit `bot.py` to specify your keywords and response:
   ```python
   keywords = ["keyword1", "keyword2"]
   response = "This is a bot reply"
   ```

2. Run the bot:
   ```sh
   python bot.py
   ```

### Running the Bot via Streamlit UI
1. Run the Streamlit app:
   ```sh
   streamlit run app.py
   ```
2. Open the local Streamlit URL in your browser.
3. Enter keywords (comma-separated) and a response message.
4. Click "Run Bot" to search for tweets and reply.

## Notes
- The bot replies to **multiple tweets** found in a single search.
- A `time.sleep(5)` delay is added between replies to avoid rate limits.
- API credentials **do not expire** unless manually regenerated.
- If you hit a `429 Too Many Requests` error, wait for the rate limit reset.

