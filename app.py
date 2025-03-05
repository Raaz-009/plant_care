from flask import Flask, render_template, request, redirect, url_for
from PIL import Image
from ultralytics import YOLO
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
# Initialize Flask app
app = Flask(__name__)
load_dotenv()
# Load the YOLOv8 model
model = YOLO('best(1).pt')

# Initialize ChatGroq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=os.getenv('GROQ_API_KEY'),                                                                                                                                            
    max_tokens=200,
    timeout=10,
    max_retries=2
)

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if "file" not in request.files:
            return "No file part"
        file = request.files["file"]
        if file.filename == "":
            return "No selected file"
        
        image = Image.open(file)
        results = model(image)

        # Extract detected disease names
        detected_classes = [int(box.cls.item()) for box in results[0].boxes]
        if detected_classes:
            disease_name = results[0].names.get(detected_classes[0], "Unknown Disease")

            # Query the LLM with the detected disease name
            prompt = f"Explain the plant disease '{disease_name}' and provide potential cures."
            response = llm.invoke(prompt)
            disease_info = response.content

            # Save the result image with bounding boxes
            results[0].save("static/result.jpg")

            return redirect(url_for("result", info=disease_info))
        else:
            return render_template("result.html", info="No disease detected in the uploaded image.")

    return render_template("index.html")


# Result route
@app.route("/result")
def result():
    info = request.args.get("info", "No information available.")
    return render_template("result.html", info=info)


#for development
# if __name__ == "__main__":
#     app.run(debug=True)

#for deployment
# if __name__ == '__main__':
#     app.run(host="0.0.0.0",port=4001)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4001))  # Default to 4001 if PORT is not set
    app.run(host="0.0.0.0", port=port)
