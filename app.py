from flask import Flask, request, render_template, redirect, url_for
from ultralytics import YOLO
from PIL import Image
import torch

# Load the trained model
model = YOLO('best(1).pt')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the uploaded image
        image = request.files['image']
        img_path = f"./static/uploads/{image.filename}"
        image.save(img_path)

        # Perform inference
        results = model(img_path)

        # Access the first result from the list
        result = results[0]

        # Draw bounding boxes and labels
        annotated_img = result.plot()  # `plot()` returns the annotated image as a numpy array
        
        # Save the annotated image
        output_path = f"./static/uploads/annotated_{image.filename}"
        Image.fromarray(annotated_img).save(output_path)

        # Redirect to the result page with the annotated image
        return redirect(url_for('result', img=output_path))

    return render_template('index.html')

@app.route('/result')
def result():
    img_path = request.args.get('img')
    return render_template('result.html', img_path=img_path)

if __name__ == '__main__':
    app.run(debug=True)
