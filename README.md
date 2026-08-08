# 🤖 Personal Data Assistant — Enterprise RAG Document Chatbot

[![IBM Certification](https://img.shields.io/badge/IBM-AI%20Developer%20Program-blue?style=for-the-badge&logo=ibm)](https://cognitiveclass.ai/)
[![Docker CI/CD Pipeline](https://img.shields.io/github/actions/workflow/status/HAMED-PAYANDA/langchain-document-assistant/docker-publish.yml?branch=main&style=for-the-badge&logo=docker&label=Docker%20CI%2FCD)](https://github.com/HAMED-PAYANDA/langchain-document-assistant/actions)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg?style=for-the-badge)](https://opensource.org/licenses/Apache-2.0)
[![Python 3.10](https://img.shields.io/badge/Python-3.10-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.3.27-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)](https://www.langchain.com/)
[![Flask](https://img.shields.io/badge/Flask-Framework-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)

An end-to-end **Retrieval-Augmented Generation (RAG)** web application capable of ingesting PDF documents, chunking and vectorizing text in real time, and delivering context-grounded answers. Built with **LangChain**, **Flask**, **Chroma DB**, and dual backend integration for **Hugging Face** (Llama-3.1-8B-Instruct) and **IBM Watsonx**.

---

## 📸 The Visual Proof & Demo Showcase

| Feature / Step | Screenshot Preview | Description |
| :--- | :--- | :--- |
| **1. PDF Ingestion & Analysis** | ![PDF Upload](demo6.png) | Uploading and parsing `AP CS Principles Syllabus.pdf` with Chroma vector storage initialization. |
| **2. Document Summarization** | ![Summary Query](demo7.png) | Asking the chatbot to summarize the uploaded document into a concise 2-sentence breakdown. |
| **3. Contextual RAG Retrieval** | ![Structure Query](demo8.png) | Asking specific structural questions about the internet, pulling directly from *Episode 3*. |
| **4. Deep Context Extraction** | ![UX Design Query](demo9.png) | Querying user experience design principles grounded in *Big Idea 1: Creative Development*. |
| **5. Anti-Hallucination Guardrails** | ![Out of Scope Query](demo10.png) | Demonstrating strict context constraints: admitting unknown facts vs. extracting project lists. |

---

## 🏗️ System Architecture

```mermaid
graph TD
    User([🌐 Web Client / UI]) -->|1. Upload PDF| Server[🐍 Flask API Server]
    User -->|2. Post Query| Server
    
    subgraph Modular Backend Workers
        Server --> WorkerChoice{Worker Module}
        WorkerChoice -->|worker_hf.py| HF[🤗 Hugging Face API / Llama-3.1]
        WorkerChoice -->|worker.py| WatsonX[🏢 IBM Watsonx LLM]
    end
    
    subgraph RAG Pipeline
        PDF[📄 PDF Document] --> Loader[PyPDF Loader]
        Loader --> Splitter[RecursiveCharacterTextSplitter]
        Splitter --> Embeddings[sentence-transformers / MiniLM-L6-v2]
        Embeddings --> VectorDB[(🗄️ Chroma Vector Store)]
    end
    
    Server -->|Query Retrieval| VectorDB
    VectorDB -->|Top-k Relevant Chunks| Chain[RetrievalQA Chain]
    HF --> Chain
    WatsonX --> Chain
    Chain -->|Grounded Response| Server
    Server -->|JSON Response| User
```
## ✨ Key Features

* 🎯 **Grounded RAG Pipeline:** Eliminates AI hallucinations by restricting response generation strictly to the uploaded PDF context chunks ($k=3$).
* 🔄 **Dual Backend Support:** Modular worker design allowing seamless switching between the **Hugging Face Inference API** (Llama 3.1) and **IBM Watsonx**.
* ⚡ **Real-time Vector Search:** Fast, in-memory vector database powered by **ChromaDB** and `sentence-transformers/all-MiniLM-L6-v2`.
* 🌐 **Full-Stack REST Architecture:** Responsive, asynchronous JavaScript frontend communicating with a lightweight **Flask** web backend.
* 🐳 **Containerized & CI/CD Ready:** Fully packaged via **Docker** and automatically built and published to the **GitHub Container Registry (GHCR)** using GitHub Actions.
    
## 🛠️ Core Tech Stack

**Languages & Frontend:**<br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)

**AI & Machine Learning:**<br>
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=for-the-badge&logo=langchain&logoColor=white)
![Hugging Face](https://img.shields.io/badge/Hugging%20Face-FFD21E?style=for-the-badge&logo=huggingface&logoColor=000)
![Meta Llama](https://img.shields.io/badge/Meta%20Llama%203.1-0467DF?style=for-the-badge&logo=meta&logoColor=white)
![IBM Watsonx](https://img.shields.io/badge/IBM%20Watsonx-052FAD?style=for-the-badge&logo=ibm&logoColor=white)

**Backend & Vector Storage:**<br>
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF4F00?style=for-the-badge)

**DevOps & Deployment:**<br>
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/github%20actions-%232671E5.svg?style=for-the-badge&logo=githubactions&logoColor=white)

## 📁 Repository Structure
```text
langchain-document-assistant/
├── .github/
│   └── workflows/
│       └── docker-publish.yml     # GitHub Actions CI/CD workflow
├── static/
│   ├── script.js                 # Async frontend REST logic
│   └── style.css                 # Dark/Light theme styles
├── templates/
│   └── index.html                # Application UI template
├── AP CS Principles Syllabus.pdf  # Sample test document
├── Dockerfile                    # Container configuration
├── LICENSE                       # Apache-2.0 License
├── README.md                     # Repository documentation
├── requirements.txt              # Frozen dependency list
├── server.py                     # Primary Flask REST server
├── worker.py                     # IBM Watsonx LLM worker logic
├── worker_hf.py                  # Hugging Face LLM worker logic
├── demo6.png                     # Visual proof screenshot
├── demo7.png                     # Visual proof screenshot
├── demo8.png                     # Visual proof screenshot
├── demo9.png                     # Visual proof screenshot
└── demo10.png                    # Visual proof screenshot
```

## ⚙️ Local Setup & Execution

Option 1: Running via Local Python Environment
	1.	Clone the Repository:
  ```bash
git clone [https://github.com/HAMED-PAYANDA/langchain-document-assistant.git](https://github.com/HAMED-PAYANDA/langchain-document-assistant.git)
cd langchain-document-assistant
```

  2.	Create and Activate a Virtual Environment:
  ```bash
python3 -m venv my_env
source my_env/bin/activate
```

  3.	Install Dependencies:
  ```bash
pip install --no-cache-dir -r requirements.txt
```

  4.	Configure API Token:
  ```bash
In worker_hf.py, replace the placeholder with your active Hugging Face token:
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "YOUR_HUGGINGFACE_TOKEN"
```

  5.	Start the Flask Server:
  ```bash
python3 server.py
```

Access the web application at http://localhost:8000.

Option 2: Running via Docker Container
	1.	Build the Docker Image:
  ```bash
docker build --no-cache -t langchain-document-assistant .
```
  2.	Run the Container:
  ```bash
docker run -p 8000:8000 langchain-document-assistant
```

Option 3: Pulling from GitHub Container Registry (GHCR)
You can run the pre-built container directly from GitHub Packages without local compilation:
```bash
docker pull ghcr.io/hamed-payanda/langchain-assistant:latest
docker run -p 8000:8000 ghcr.io/hamed-payanda/langchain-assistant:latest
```

## How to get watsonx API key and Project ID

Here, we initialize a language model and its embeddings. Here's a brief description of each section of the script:

- API and Project ID: Watsonx_API and Project_id are variables storing the API key and project ID required to access IBM's cloud services.


- WatsonX LLM parameters Initialization: Inside the function, a dictionary named params is created, which holds various parameters like maximum and minimum number of tokens to generate, temperature (controlling randomness), and others for configuring the generation behavior of the language model.

- Credentials: A dictionary named credentials is defined with the URL of IBM's cloud service and the API key to authenticate requests to the service.
- LLM Initialization: A model object, `LLAMA2_model`, is created using the Model class, which is initialized with a specific model ID, credentials, parameters, and project ID. Then, an instance of WatsonxLLM is created with `LLAMA2_model` as an argument, initializing the language model hub `llm_hub`.


We also initialize embeddings. The embeddings are used to represent text data in a form that machines can understand. They convert human-readable text into numbers (vectors) that capture the semantic meaning of the text.

- The embeddings are initialized using a class called `HuggingFaceInstructEmbeddings` pre-trained model named `sentence-transformers/all-MiniLM-L6-v2` list of leaderboard of embeddings are available [here](https://huggingface.co/spaces/mteb/leaderboard). This embedding model has shown a good balance in both performance and speed.

## Get Your Watsonx API and Project ID
Since watsonx is an IBM Cloud service, credentials such as an API key and a project ID are required when accessing from the outside. 

To access the credentials, we've provided a special code for you to claim a USD 200 credit on IBM Cloud at no charge! Here's how to get started:
1. **IBM Cloud Trial Access:**
- Proceed to the "IBM Cloud Trial" section for the unique code and detailed instructions.
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0XPBEN/ezgif.com-video-to-gif-converted.gif)
- Follow these instructions to sign up for a non-expiring Lite account at IBM Cloud, which includes the USD 200 credit.
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0XPBEN/ezgif.com-video-to-gif-converted%20%281%29.gif)
2. **Create Your Watsonx Project:**
- Sign in to [IBM watsonx](https://dataplatform.cloud.ibm.com/registration/stepone?utm_source=skills_network&utm_content=in_lab_content_link&utm_id=Lab-test1_v1_1702536549&context=wx&apps=data_science_experience%2Cwatson_data_platform%2Ccos) and [create a project](https://dataplatform.cloud.ibm.com/projects/?utm_source=skills_network&utm_content=in_lab_content_link&utm_id=Lab-test1_v1_1702536549&context=wx).
![Getting IBM watsonx project ID](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0PPIEN/createProject.gif)
- Inside your project on watsonx, navigate to `Manage` > `General` to find your project ID for your later use.
![Create a project ID](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0XPBEN/id.gif)
3. **Associate Watson Machine Learning Service:**
After you create a project, you can go to the project’s `Manage` tab > select the `Services and integrations` page > click `Associate Service` > add the `Watson Machine Learning` service to it.
![](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0PPIEN/associate.gif)
4. **Generate IBM Cloud User API Key:**
Lastly, you can follow the below demonstration to create/get your [IBM Cloud user API key](https://cloud.ibm.com/iam/apikeys?utm_source=skills_network&utm_content=in_lab_content_link&utm_id=Lab-test1_v1_1702536549). Be sure to write your API key down somewhere right after you create it, because you won’t be able to see it again!

![Getting IBM cloud user API key](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-GPXX0PPIEN/ezgif.com-video-to-gif.gif)

5. **Update Code:** 
In server.py, switch the import to import worker as worker, and set your credentials in worker.py:
```python
Watsonx_API = "YOUR_WATSONX_API_KEY"
Project_id = "YOUR_PROJECT_ID"
```
📜 License
Distributed under the Apache-2.0 License. See LICENSE for more information.

👤 Author
Hamed Payanda
•	GitHub: @HAMED-PAYANDA
•	Completed as part of the IBM AI Developer Program






