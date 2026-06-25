<p align = "center" draggable=”false” ><img src="https://github.com/AI-Maker-Space/LLM-Dev-101/assets/37101144/d1343317-fa2f-41e1-8af1-1dbb18399719" 
     width="200px"
     height="auto"/>
</p>


## <h1 align="center" id="heading"> 👋 Welcome to the AI Engineer Challenge</h1>

## 🤖 Your First Vibe Coding LLM Application

> If you are a novice, and need a bit more help to get your dev environment off the ground, check out this [Setup Guide](docs/GIT_SETUP.md). This guide will walk you through the 'git' setup you need to get started.

> For additional context on LLM development environments and API key setup, you can also check out our [Interactive Dev Environment for LLM Development](https://github.com/AI-Maker-Space/Interactive-Dev-Environment-for-AI-Engineers).

In this repository, we'll walk you through the steps to create a LLM (Large Language Model) powered application with a vibe-coded frontend!

Are you ready? Let's get started!

<details>
  <summary>🖥️ Accessing "gpt-4.1-mini" (ChatGPT) like a developer</summary>

1. Head to [this notebook](https://colab.research.google.com/drive/1sT7rzY_Lb1_wS0ELI1JJfff0NUEcSD72?usp=sharing) and follow along with the instructions!

2. Complete the notebook and try out your own system/assistant messages!

That's it! Head to the next step and start building your application!

</details>


<details>
  <summary>🏗️ Forking & Cloning This Repository</summary>

Before you begin, make sure you have:

1. 👤 A GitHub account (you'll need to replace `YOUR_GITHUB_USERNAME` with your actual username)
2. 🔧 Git installed on your local machine
3. 💻 A code editor (like Cursor, VS Code, etc.)
4. ⌨️ Terminal access (Mac/Linux) or Command Prompt/PowerShell (Windows)
5. 🔑 A GitHub Personal Access Token (for authentication)

Got everything in place? Let's move on!

1. Fork [this](https://github.com/AI-Maker-Space/The-AI-Engineer-Challenge) repo!

     ![image](https://i.imgur.com/bhjySNh.png)

1. Clone your newly created repo.

     ``` bash
     # First, navigate to where you want the project folder to be created
     cd PATH_TO_DESIRED_PARENT_DIRECTORY

     # Then clone (this will create a new folder called The-AI-Engineer-Challenge)
     git clone git@github.com:<YOUR GITHUB USERNAME>/The-AI-Engineer-Challenge.git
     ```

     > Note: This command uses SSH. If you haven't set up SSH with GitHub, the command will fail. In that case, use HTTPS by replacing `git@github.com:` with `https://github.com/` - you'll then be prompted for your GitHub username and personal access token.

2. Verify your git setup:

     ```bash
     # Check that your remote is set up correctly
     git remote -v

     # Check the status of your repository
     git status

     # See which branch you're on
     git branch
     ```

     <!-- > Need more help with git? Check out our [Detailed Git Setup Guide](docs/GIT_SETUP.md) for a comprehensive walkthrough of git configuration and best practices. -->

3. Open the freshly cloned repository inside Cursor!

     ```bash
     cd The-AI-Engineering-Challenge
     cursor .
     ```

4. Check out the existing backend code found in `/api/index.py`

</details>

<details>
  <summary>⚙️ Backend Setup with uv</summary>

1. Install the [`uv`](https://github.com/astral-sh/uv) package manager (`pip install uv`). `uv` will download and manage Python 3.12 for you the first time you run a project command.
2. From the project root, install dependencies with `uv sync`. This creates `.venv/` (and fetches Python 3.12 automatically if needed).
3. Set your OpenAI API key in the shell before running the server, for example `export OPENAI_API_KEY=sk-...`.
4. Start the backend directly from the project root with `uv run uvicorn api.index:app --reload`. The server will run on `http://localhost:8000` with auto-reload enabled for development.
5. Additional backend details live in `api/README.md`.

</details>

<details>
  <summary>🔥Setting Up for Vibe Coding Success </summary>

While it is a bit counter-intuitive to set things up before jumping into vibe-coding - it's important to remember that there exists a gradient betweeen AI-Assisted Development and Vibe-Coding. We're only reaching *slightly* into AI-Assisted Development for this challenge, but it's worth it!

1. Check out the rules in `.cursor/rules/` and add theme-ing information like colour schemes in `frontend-rule.mdc`! You can be as expressive as you'd like in these rules!
2. We're going to index some docs to make our application more likely to succeed. To do this - we're going to start with `CTRL+SHIFT+P` (or `CMD+SHIFT+P` on Mac) and we're going to type "custom doc" into the search bar. 

     ![image](https://i.imgur.com/ILx3hZu.png)
3. We're then going to copy and paste `https://nextjs.org/docs` into the prompt.

     ![image](https://i.imgur.com/psBjpQd.png)

4. We're then going to use the default configs to add these docs to our available and indexed documents.

     ![image](https://i.imgur.com/LULLeaF.png)

5. After that - you will do the same with Vercel's documentation. After which you should see:

     ![image](https://i.imgur.com/hjyXhhC.png) 

</details>

<details>
  <summary>😎 Vibe Coding a Front End for the FastAPI Backend</summary>

1. Use `Command-L` or `CTRL-L` to open the Cursor chat console. 

2. Set the chat settings to the following:

     ![image](https://i.imgur.com/LSgRSgF.png)

3. Ask Cursor to create a frontend for your application. Iterate as much as you like!

4. Run the frontend using the instructions Cursor provided. 

> NOTE: If you run into any errors, copy and paste them back into the Cursor chat window - and ask Cursor to fix them!

> NOTE: You have been provided with a backend in the `/api` folder - please ensure your Front End integrates with it!

</details>

<details>
  <summary>🚀 Deploying Your First LLM-powered Application with Vercel</summary>

1. Ensure you have signed into [Vercel](https://vercel.com/) with your GitHub account.

2. Ensure you have `npm` (this may have been installed in the previous vibe-coding step!) - if you need help with that, ask Cursor!

3. Run the command:

     ```bash
     npm install -g vercel
     ```

4. Run the command:

     ```bash
     vercel
     ```

5. Follow the in-terminal instructions. (Below is an example of what you will see!)

     ![image](https://i.imgur.com/D1iKGCq.png)

6. Once the build is completed - head to the provided link and try out your app!

> NOTE: Remember, if you run into any errors - ask Cursor to help you fix them!

### Vercel Link to Share

You'll want to make sure you share you *domains* hyperlink to ensure people can access your app!

![image](https://i.imgur.com/mpXIgIz.png)

> NOTE: Test this is the public link by trying to open your newly deployed site in an Incognito browser tab!

</details>

<details>
     <summary>🧪 Vibe Check Your LLM App</summary>

### 🤔 What is a Vibe Check?

Now that you’ve built and deployed your first LLM-powered application, it’s time to evaluate it.

In this section, you’ll run a **“vibe check”** — a lightweight, practical way to test how well your application performs across common tasks.

Think of it as a **first pass to catch obvious issues** before deeper evaluation.

> 💡 You will complete this directly in this README. 

---

## 🏗️ Activity #1: General Capability Vibe Check

Run the following prompts through your app.

For each prompt Identify what capability is being tested (e.g., *summarization ability, reasoning, creativity*)

---

**1. Prompt:**  
What is Newton's second law?  
**Aspect Tested:** Conceptual explanation + ability to present equations and structured formatting

**Response:**  
The assistant gave a well-structured answer: stated the law in plain English ("net force = mass × acceleration"), presented the vector equation **F_net = ma**, and defined each term with SI units (N, kg, m/s²). It highlighted that force and acceleration are both vectors so direction matters, showed the two rearrangements (a = F/m and m = F/a), and used a shopping cart vs. car comparison to make the mass-acceleration trade-off intuitive. It closed by offering a practice problem or a link to Newton's other laws.

---

**2. Prompt:**  
Explain the difference between velocity and speed.  
**Aspect Tested:** Distinguishing closely related concepts

**Response:**  
The assistant clearly separated the two concepts: speed is a scalar (magnitude only, s = d/t) while velocity is a vector (magnitude + direction, v = Δx/Δt). It used a comparison table, then grounded the distinction with a concrete example — driving 100 km East then 100 km West gives speed = 50 km/h but velocity = 0 km/h. It also noted that speed is never negative, velocity can be, and that an object in circular motion has constant speed but continuously changing velocity.

---

**3. Prompt:**  
A ball is dropped from 20m. How long until it hits the ground?  
**Aspect Tested:** Quantitative reasoning / step-by-step problem solving

**Response:**  
The assistant identified the givens (h = 20 m, v₀ = 0, g = 9.8 m/s²), selected the kinematic equation h = v₀t + ½gt², simplified to h = ½gt² since initial velocity is zero, rearranged to t = √(2h/g), and computed t ≈ 2.02 seconds. It finished with an intuitive sanity check — noting that at t = 1s the ball has only fallen 4.9 m, so most of the distance is covered in the final moments as gravity continuously accelerates it.

---

**4. Prompt:**  
Why does ice float on water?  
**Aspect Tested:** Applying physics to everyday phenomena

**Response:**  
The assistant explained that ice floats because it is less dense than liquid water (ρ_ice ≈ 917 kg/m³ vs ρ_water ≈ 1000 kg/m³). It went deeper by describing how hydrogen bonds lock water molecules into a rigid hexagonal lattice with more empty space than the disordered liquid state — the opposite of most substances. It applied Archimedes' Principle (object floats if ρ_object < ρ_fluid) to explain why ~9/10 of ice is submerged, and noted the real-world significance: this unusual property insulates lakes in winter and makes aquatic life possible.

---

**5. Prompt:**  
What's the capital of France?  
**Aspect Tested:** Off-topic handling — does it redirect back to physics?

**Response:**  
The assistant politely declined to answer, noting it's a geography question outside its scope. It redirected with a brief menu of physics topics it can help with (mechanics, electromagnetism, thermodynamics, modern physics) and invited the user to ask anything physics-related. No hallucination, no awkward refusal — clean and on-brand.

---

### ❓Question #1

Do the answers appear to be correct and useful?

**Your Answer:**  
Yes — the answers are accurate, well-structured, and appropriately formatted. Equations are presented clearly, each response breaks concepts down step by step, and the explanations are relevant to a student audience. The assistant also handles off-topic questions correctly by redirecting back to physics.

---


### ❓Question #2

Are the vibes of your assistant aligned with your expectations? Why or why not?

**Your Answer:**  
Yes, the assistant appears upbeat and friendly which is what you want from a phsyics tutor to make learning engaging

---

## 🏗️ Activity #3: Capability Gaps Vibe Check

Now test your app with prompts that require **capabilities it may not have yet**, such as:
- Real-time data
- Memory
- External tools

Examples:
- “What does my schedule look like tomorrow?”
- “What time should I leave for the airport?”

---

**Prompt:**  
What does my schedule look like tomorrow?

**Result:**  
The assistant correctly flagged it has no access to personal schedule or calendar data, declined gracefully, and redirected to its physics scope with a topic menu (mechanics, electricity & magnetism, waves & optics, thermodynamics, quantum physics, relativity).

---

**Prompt:**  
What time should I leave for the airport?

**Result:**  
The assistant declined the travel planning question but found a clever physics angle — it offered to help calculate travel time using t = d/v if given distance and speed, and listed related physics concepts (kinematics, relative motion, special relativity/time dilation). It turned a capability gap into a teaching moment rather than a flat refusal.

---

### ❓Question #3

What are some limitations of your application?

**Your Answer:**  
The main limitation is that the app has no conversation history — each message is sent to the API in isolation, so the model has no memory of previous exchanges. To fix this, the backend would need to maintain session state and pass the full message history with every request, enabling continuous multi-turn conversations rather than treating each question independently.

---

## 🚀 (Optional) Improve Your App

Based on your vibe check, try improving your application:
- Adjust your prompt
- Change the model
- Add features

Then rerun your vibe check and document:

---

**Adjustments Made:**  
<!-- Describe what you changed -->

**Results:**  
<!-- What improved? What didn’t? -->

---

## Deployment Notes

This application runs fully on localhost using the Accenture Azure Claude endpoint (lgts1tetamapi01.azure-api.net). The backend requires an internal Accenture subscription key passed as a query parameter. Because the Azure endpoint is only accessible within the Accenture corporate network, the live Vercel deployment cannot reach the backend from external servers. The app works correctly when run locally with the backend on http://localhost:8000. For demonstration purposes, the GitHub repository contains the full working code and the Vercel deployment serves the frontend successfully.

## 📦 Submission Instructions

1. Complete this section directly in your README
2. Commit and push your changes to GitHub
3. Share your **repo link + deployed Vercel app**








</details>

### 🎉 Congratulations! 

You just deployed your first LLM-powered application! 🚀🚀🚀 Get on linkedin and post your results and experience! Make sure to tag us at @AIMakerspace!

Here's a template to get your post started!

```
🚀🎉 Exciting News! 🎉🚀

🏗️ Today, I'm thrilled to announce that I've successfully built and shipped my first-ever LLM using the powerful combination of , and the OpenAI API! 🖥️

Check it out 👇
[LINK TO APP]

A big shoutout to the @AI Makerspace for all making this possible. Couldn't have done it without the incredible community there. 🤗🙏

Looking forward to building with the community! 🙌✨ Here's to many more creations ahead! 🥂🎉

Who else is diving into the world of AI? Let's connect! 🌐💡

#FirstLLMApp 
```
