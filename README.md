# Sentiment Analysis Tool | Backend API

Frontend repo can be found [here](https://github.com/UltanBlack/frontEndAI)

Project for AI and Customer Engagement Conference 2025, hosted by Lilly Leadership Institute Cohort XII more info on the [conferences website](https://aiforcustomers.com).

Authors:

- Sam Bowers
- Ultan Black
- Jacob Malibiran

---

# Build Instructions

1.  Clone and enter the repo
    `git clone https://github.com/bowerss5/sat`
    `cd sat`

2.  First set up python virtual environment

    `python3 -m venv <myenvpath>`

    <!--TODO: Add instructions for other shells-->

    For bash:
    `source <myenvpath>/bin/activate`

3.  `pip3 install -r requirements.txt`

4.  Get a valid API key from [groq](https://console.groq.com/keys)

5.  Add `API_KEY={YOUR API KEY HERE}` to a `.env` file with

    - `echo "API_KEY={YOUR API KEY HERE}" > .env`

6.  `python3 api.py` to run
