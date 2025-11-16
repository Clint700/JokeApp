<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - The Comedy Cellar</title>
    <!-- We'll use the Inter font to match the modern vibe -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    
    <style>
        /* --- General Setup --- */
        body {
            background-color: #0d1117; /* Midnight blue background */
            color: #c9d1d9; /* Light grey text */
            font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            line-height: 1.7;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
        }

        .container {
            width: 100%;
            max-width: 800px;
            padding: 2rem;
            box-sizing: border-box;
        }

        /* --- Header & Typography --- */
        header {
            text-align: center;
            border-bottom: 2px solid #30363d;
            padding-bottom: 1.5rem;
            margin-bottom: 2rem;
        }

        h1 {
            font-size: 2.8rem;
            font-weight: 800;
            color: #ffffff;
            margin: 0 0 0.5rem 0;
        }

        h1 .icon {
            display: inline-block;
            transform: rotate(-10deg);
            margin-right: 0.5rem;
            font-size: 3rem;
        }

        h2 {
            font-size: 1.8rem;
            font-weight: 600;
            color: #ffffff;
            border-bottom: 1px solid #30363d;
            padding-bottom: 0.5rem;
            margin-top: 2.5rem;
        }
        
        .subtitle {
            font-size: 1.25rem;
            color: #8b949e;
            margin: 0;
        }

        a {
            color: #ff9f1c; /* Our fun orange accent */
            text-decoration: none;
            font-weight: 600;
        }

        a:hover {
            text-decoration: underline;
        }

        /* --- App Demo --- */
        .demo-image {
            background: #161b22;
            border: 1px solid #30363d;
            border-radius: 12px;
            margin-top: 2rem;
            overflow: hidden;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }
        .demo-image img {
            width: 100%;
            display: block;
        }
        .demo-image .caption {
            font-size: 0.9rem;
            color: #8b949e;
            text-align: center;
            padding: 0.75rem 0;
        }

        /* --- "Interactive" Collapsible Sections --- */
        details {
            background: #161b22; /* Slate card background */
            border: 1px solid #30363d;
            border-radius: 12px;
            margin-bottom: 1rem;
            transition: all 0.2s ease-in-out;
        }
        
        details[open] {
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }

        summary {
            font-size: 1.1rem;
            font-weight: 600;
            color: #e6edf3;
            padding: 1rem 1.5rem;
            cursor: pointer;
            list-style: none; /* Hides the default arrow */
            display: flex;
            align-items: center;
        }
        
        /* Custom arrow for fun */
        summary::before {
            content: '👉';
            font-size: 1rem;
            margin-right: 0.75rem;
            transition: transform 0.2s ease-in-out;
        }
        
        details[open] summary::before {
            transform: rotate(90deg);
        }

        .details-content {
            padding: 0 1.5rem 1.5rem 1.5rem;
            border-top: 1px solid #30363d;
            background: #21262d; /* Slightly darker inner bg */
            border-bottom-left-radius: 12px;
            border-bottom-right-radius: 12px;
        }
        
        /* --- Code Blocks & Lists --- */
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        ul li {
            position: relative;
            padding-left: 2rem;
            margin-bottom: 0.5rem;
        }
        ul li::before {
            content: '✅';
            position: absolute;
            left: 0;
            top: 0;
        }
        
        code {
            font-family: 'JetBrains Mono', monospace;
            background-color: #30363d;
            color: #ffbf69; /* Orange-yellow code text */
            padding: 0.2em 0.4em;
            border-radius: 6px;
            font-size: 0.9rem;
        }

        pre {
            background-color: #0d1117;
            border: 1px solid #30363d;
            border-radius: 8px;
            padding: 1rem;
            overflow-x: auto;
            font-family: 'JetBrains Mono', monospace;
        }
        
        pre code {
            background: none;
            padding: 0;
            font-size: 0.85rem;
            color: #c9d1d9; /* Plain code in a block */
        }
        
        pre .comment {
            color: #8b949e;
            font-style: italic;
        }
        
        pre .key {
            color: #ff9f1c;
        }

    </style>
</head>
<body>

    <div class="container">
        
        <header>
            <h1><span class="icon">🎤</span> The Comedy Cellar</h1>
            <p class="subtitle">Our AI comedian is off the leash. No two jokes are the same.</p>
        </header>

        <main>
            <!-- A placeholder for a screenshot or GIF -->
            <div class="demo-image">
                <!-- Replace this with a real screenshot or GIF of your app! -->
                <img src="Screenshot 2025-11-16 at 02.53.57.png" alt="Screenshot of the Comedy Cellar app">
                <div class="caption">It's funnier when it's running, trust us.</div>
            </div>

            <h2>What is this contraption?</h2>
            <p>
                This is not your grandpa's joke-book. This is a 100% AI-powered stand-up comedian, built with 
                <a href="https://streamlit.io/" target="_blank">Streamlit</a> and a very creative 
                <a href="https://langchain.com/" target="_blank">LangChain</a> prompt. 
            </p>
            <p>
                We got tired of the same old "Q&A" robot jokes. So we ripped off the digital handcuffs. Our AI is now free to tell:
            </p>
            <ul>
                <li>Hilarious one-liners</li>
                <li>Witty observations</li>
                <li>Short, funny stories</li>
                <li>...and the occasional "clever" pun. We're working on that.</li>
            </ul>

            <h2>🚀 The Tech Stack (What's holding this thing together?)</h2>
            <ul>
                <li><code>🐍 Python 3.10+</code> - The snake that runs the show.</li>
                <li><code>🌊 Streamlit</code> - For the pretty, pretty web app.</li>
                <li><code>🔗 LangChain</code> - The "manager" that talks to the AI.</li>
                <li><code>🤖 OpenAI (gpt-4o-mini)</code> - The (mostly) unhinged comedian's brain.</li>
            </ul>

            <h2><span class="icon">🛠️</span> How to Run This Thing (The "Interactive" Part)</h2>
            <p>Want to run your own comedy club? Just follow these steps. Click each one to expand!</p>

            <details>
                <summary>Step 1: Clone the Repo (aka "Steal the code")</summary>
                <div class="details-content">
                    <p>You know the drill. Get this code onto your local machine.</p>
<pre><code>git clone https://your-repo-url-here.git
cd your-project-directory</code></pre>
                </div>
            </details>

            <details>
                <summary>Step 2: Create a Virtual Environment</summary>
                <div class="details-content">
                    <p>It's good practice. Like washing your hands. Don't be gross.</p>
<pre><code><span class="comment"># On macOS/Linux</span>
python3 -m venv .venv
source .venv/bin/activate

<span class="comment"># On Windows (something like this... good luck)</span>
python -m venv .venv
.\.venv\Scripts\activate</code></pre>
                </div>
            </details>
            
            <details>
                <summary>Step 3: Install the Pile of Libraries</summary>
                <div class="details-content">
                    <p>We need all this stuff to make the magic happen. (A <code>requirements.txt</code> file is ideal, but for now...)</p>
<pre><code>pip install streamlit langchain langchain-openai python-dotenv</code></pre>
                </div>
            </details>
            
            <details>
                <summary>Step 4: The SUPER SECRET API Key</summary>
                <div class="details-content">
                    <p>The AI comedian doesn't work for free. You need an OpenAI API key.</p>
                    <p>1. Create a file named <code>.env</code> in the main project folder.</p>
                    <p>2. Open it and add this ONE line (with your *actual* key):</p>
<pre><code><span class="key">OPENAI_API_KEY</span>="sk-YourS3cr3tK3yGoesHere"</code></pre>
                    <p>The <code>.gitignore</code> file (if you have one) should block this file, so you don't accidentally share your key with the world. Don't be that person.</p>
                </div>
            </details>
            
            <details>
                <summary>Step 5: OPEN THE CURTAINS!</summary>
                <div class="details-content">
                    <p>This is it. The big moment. Run this command in your terminal:</p>
<pre><code>streamlit run app.py</code></pre>
                    <p>Your browser should magically open, and the show will begin. Enjoy!</p>
                </div>
            </details>

            <h2>🗺️ File Structure (The "Blueprints")</h2>
            <details>
                <summary>What's in the box?</summary>
                <div class="details-content">
<pre><code>comedy-cellar/
├── <span class="key">app.py</span>          <span class="comment"># The main stage! Our Streamlit app lives here.</span>
├── <span class="key">llm_utils/</span>
│   └── <span class="key">lc_llm.py</span>     <span class="comment"># The AI's brain. This is where we poke the LLM.</span>
├── <span class="key">.env</span>            <span class="comment"># Your SECRET API key. Don't share this!</span>
└── <span class="key">README.html</span>     <span class="comment"># You are here! Staring at this beautiful file.</span>
</code></pre>
                </div>
            </details>

        </main>
    </div>

</body>
</html># JokeApp
