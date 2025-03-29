# Beluga Voice Assistant

## Project Overview
Beluga is a voice assistant application that allows users to perform various tasks using voice commands. It can browse the web, play music, and recognize commands using an AI model. The assistant is designed to provide a seamless interaction experience with natural speech synthesis and recognition capabilities.

## Installation Instructions
1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   ```
2. **Navigate to the Project Directory**: Change into the project directory.
   ```bash
   cd Beluga
   ```
3. **Install Dependencies**: Install the required Python packages.
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the Application**: Start the voice assistant.
   ```bash
   python Beluga_ai.py
   ```

## Usage Guide
- **Voice Commands**: Interact with Beluga using voice commands such as "open YouTube", "play music", "what time is it", etc.
- **Expected Responses**: Beluga will respond with appropriate actions or information based on the recognized command.

## AI Model Training
- **Data Preparation**: Prepare your training data with text samples and corresponding labels.
- **Training Script**: Run `train_ai.py` to train the AI model.
  ```bash
  python train_ai.py
  ```
- **Model Persistence**: The trained model is saved as `beluga_ai_model.pkl` for future use.

## Contribution Guidelines
- **Coding Standards**: Follow PEP 8 guidelines for Python code.
- **Submitting Changes**: Fork the repository, make your changes, and submit a pull request.

We welcome contributions from the community to enhance the functionality and performance of Beluga.
