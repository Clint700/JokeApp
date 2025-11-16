🎤 The Comedy Cellar

<p align="center">
<strong>Our AI comedian is off the leash. No two jokes are the same.</strong>
</p>

<p align="center">
<!-- You can replace this with a screenshot or, even better, a GIF of the app working! -->
<img src="Screenshot 2025-11-16 at 02.53.57.png" width="700">





<em>It's funnier when it's running, trust us.</em>
</p>

What is this contraption?

This is not your grandpa's joke-book. This is a 100% AI-powered stand-up comedian, built with Streamlit and a very creative LangChain prompt.

We got tired of the same old "Q&A" robot jokes. So we ripped off the digital handcuffs. Our AI is now free to tell:

Hilarious one-liners

Witty observations

Short, funny stories

...and the occasional "clever" pun. We're working on that.

🚀 The Tech Stack (What's holding this thing together?)

🐍 Python 3.10+: The snake that runs the show.

🌊 Streamlit: For the pretty, pretty web app.

🔗 LangChain: The "manager" that talks to the AI.

🤖 OpenAI (gpt-4o-mini): The (mostly) unhinged comedian's brain.

🛠️ How to Run This Thing (The "Interactive" Part)

Want to run your own comedy club? Just follow these steps. Click each one to expand!

<details>
<summary><strong>👉 Step 1: Clone the Repo (aka "Steal the code")</strong></summary>





You know the drill. Get this code onto your local machine.
<pre><code>git clone https://your-repo-url-here.git
cd your-project-directory</code></pre>
</details>

<details>
<summary><strong>👉 Step 2: Create a Virtual Environment</strong></summary>





It's good practice. Like washing your hands. Don't be gross.
<pre><code># On macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

On Windows (something like this... good luck)

python -m venv .venv
..venv\Scripts\activate</code></pre>

</details>

<details>
<summary><strong>👉 Step 3: Install the Pile of Libraries</strong></summary>





We need all this stuff to make the magic happen. (A requirements.txt file is ideal, but for now...)
<pre><code>pip install streamlit langchain langchain-openai python-dotenv</code></pre>
</details>

<details>
<summary><strong>👉 Step 4: The SUPER SECRET API Key</strong></summary>





The AI comedian doesn't work for free. You need an OpenAI API key.

Create a file named .env in the main project folder.

Open it and add this ONE line (with your actual key):

<pre><code>OPENAI_API_KEY="sk-YourS3cr3tK3yGoesHere"</code></pre>

The .gitignore file (if you have one) should block this file, so you don't accidentally share your key with the world. Don't be that person.

</details>

<details>
<summary><strong>👉 Step 5: OPEN THE CURTAINS!</strong></summary>





This is it. The big moment. Run this command in your terminal:
<pre><code>streamlit run app.py</code></pre>
Your browser should magically open, and the show will begin. Enjoy!
</details>

🗺️ File Structure (The "Blueprints")

<details>
<summary><strong>What's in the box?</strong></summary>





<pre><code>comedy-cellar/
├── <b>app.py</b>          <i># The main stage! Our Streamlit app lives here.</i>
├── <b>llm_utils/</b>
│   └── <b>lc_llm.py</b>     <i># The AI's brain. This is where we poke the LLM.</i>
├── <b>.env</b>            <i># Your SECRET API key. Don't share this!</i>
└── <b>README.md</b>     <i># You are here! Staring at this beautiful file.</i>
</code></pre>
</details>