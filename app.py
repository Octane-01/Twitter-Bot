import streamlit as st
from bot import search_and_reply

st.title("Twitter Bot")

keywords = st.text_area("Enter keywords (comma-separated)")
response = st.text_input("Enter response message")

if st.button("Run Bot"):
    if not keywords or not response:
        st.warning("Please enter both keywords and a response.")
    else:
        keyword_list = [kw.strip() for kw in keywords.split(",") if kw.strip()]
        st.write(f"Searching for tweets with: {keyword_list}")
        st.write(f"Replying with: {response}")
        
        # Run the bot and get responses
        replied_tweets = search_and_reply(keyword_list, response)
        
        if replied_tweets:
            st.success(f"Replied to {len(replied_tweets)} tweets!")
            for tweet_id in replied_tweets:
                st.write(f"✅ Replied to Tweet ID: {tweet_id}")
        else:
            st.warning("No tweets found to reply to.")
