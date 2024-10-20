🌱 PlantCare - Plant Disease Detection Website


Overview

PlantCare is a web-based application that allows users to upload images of plant leaves to detect potential diseases. The system uses a YOLOv8 model trained on a dataset of multiple plant diseases to provide accurate predictions. This project aims to assist farmers, gardeners, and plant enthusiasts in identifying diseases early, promoting healthier plant growth.
🔥 Features

    Upload plant leaf images to detect diseases.
    Supports multiple plant types (e.g., bell pepper, tomato, potato).
    Displays bounding boxes and labels over detected regions.
    Provides quick and reliable disease classification using YOLOv8.
    Simple, user-friendly interface with Flask backend.

📂 Project Structure

bash

📂 plant_care/
│
├── 📁 static/
│   ├── result.jpg                # Result image (generated)
│   └── styles.css                # CSS styles
├── 📁 templates/
│   ├── index.html                # Home page with upload form
│   └── result.html               # Display prediction results
├── app.py                        # Flask backend logic
├── requirements.txt              # Project dependencies
└── best.pt                       # YOLOv8 trained model


🛠️ Installation
Prerequisites

Ensure you have Python installed (version 3.10.12 recommended). Install the dependencies listed below.
Step 1: Clone the Repository

bash

git clone https://github.com/Raaz-009/plant_care.git
cd plant_care

Step 2: Create a Virtual Environment

bash

python -m venv venv
source venv/bin/activate      # On macOS/Linux
venv\Scripts\activate         # On Windows

Step 3: Install Dependencies

bash

pip install -r requirements.txt

Step 4: Place the Model

Ensure your best.pt YOLOv8 model is in the project root directory.
🔧 Usage
Step 1: Start the Flask Server

bash

python app.py

Step 2: Access the Website

Open your browser and go to:

arduino

http://127.0.0.1:5000/

Step 3: Upload an Image

    Upload a plant leaf image.
    The result will display the uploaded image with detected diseases marked with bounding boxes and labels.

🖼️ Screenshots
![Screenshot 2024-10-20 231633](https://github.com/user-attachments/assets/1d5160ed-7495-4874-8c88-17110e81835e)

Detection Result

📑 Technologies Used

    Python: Backend logic
    Flask: Web framework
    YOLOv8: Model for object detection
    HTML/CSS: Frontend UI
    Pillow: Image processing

📋 Requirements

    Python 3.10.x
    Flask
    Ultralytics (YOLOv8)
    Torch

⚠️ Troubleshooting

    CUDA-related Issues: Ensure your system supports GPU acceleration, or install CPU-compatible versions of torch.
    FileNotFoundError: Ensure the best.pt model is placed in the correct directory.
    Dependency Issues: If torch fails to install, use the following command:

    bash

    pip install torch --index-url https://download.pytorch.org/whl/cu121

📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request.
🌟 Acknowledgments

    Special thanks to the Ultralytics team for the YOLOv8 model.
    Inspired by real-world agricultural applications.

