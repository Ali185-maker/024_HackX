VisionBias: Multimodal Counterfactual Auditing
A toolkit for detecting demographic bias in Vision-Language Models using SAM and SDXL.

📖 Overview
In 2025, AI "Agents" are increasingly making decisions based on what they see. However, Vision-Language Models (VLMs) often carry "Contextual Bias"—for example, associating "Doctor" only with specific skin tones or genders.

VisionBias is an auditing tool that uses Counterfactual Generative Testing. It isolates a human subject in a high-stakes image and swaps their demographic attributes while keeping the professional context (tools, clothing, environment) identical. By comparing an AI's confidence scores across these versions, we can mathematically prove and visualize bias.

🚀 The Pipeline
Our system leverages three state-of-the-art AI technologies:

Segment Anything (SAM): Precisely isolates the human subject from the background.

Stable Diffusion XL (SDXL) Inpainting: Re-paints the masked area with a new demographic attribute while preserving the original lighting and posture.

The Auditor (CLIP/ResNet): (Your next step) Analyzes how the classification confidence changes across the generated variations.

🛠️ Installation & Setup
Clone the repository:

Bash

git clone https://github.com/your-username/vision-bias-reflector.git
cd vision-bias-reflector
Install dependencies:

Bash

pip install replicate pillow numpy requests
Set your API Key: Get your key from Replicate and export it:

Bash

export REPLICATE_API_TOKEN='your_token_here'
💻 Usage
The core script takes a base image (e.g., a "Software Engineer") and generates a suite of counterfactual images.

Python

# Run the auditor script
python audit_bias.py
Core Logic:
Segment: Uses meta/sam to detect the largest person in the frame.

Inpaint: Uses stability-ai/sdxl-inpainting to iterate through demographic prompts.

Compare: Saves cf_0.png through cf_4.png for side-by-side analysis.

⚖️ Ethical Implications
This project aims to provide a "Stress Test" for companies deploying AI in:

Hiring: Do resume scanners "see" professionalism differently across genders?

Healthcare: Does diagnostic accuracy drop for underrepresented skin tones?

Security: Does a "suspicion" score change based on race?

👥 Contributors
Your Name - ML Pipeline & Integration

Teammate Name - Data Curation & Bias Analysis

🔮 Future Roadmap
[ ] Automated Scoring: Integrate CLIP to automatically graph the "Bias Gap."

[ ] Video Support: Extend counterfactual testing to video frames.

[ ] Interactive Dashboard: A Streamlit interface for non-technical auditors.
