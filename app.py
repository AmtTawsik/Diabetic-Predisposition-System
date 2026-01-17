import gradio as gr
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('diabetes_model.pkl')

def predict_diabetes(pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age):
    """Predict diabetes based on input features"""
    try:
        # Create input DataFrame with proper feature names
        features = pd.DataFrame({
            'Pregnancies': [pregnancies],
            'Glucose': [glucose],
            'BloodPressure': [blood_pressure],
            'SkinThickness': [skin_thickness],
            'Insulin': [insulin],
            'BMI': [bmi],
            'DiabetesPedigreeFunction': [diabetes_pedigree],
            'Age': [age]
        })
        
        # Make prediction
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] * 100
        
        # Return formatted result
        result = "🔴 HIGH RISK - Diabetic" if prediction == 1 else "🟢 LOW RISK - Non-Diabetic"
        confidence = f"Confidence: {probability:.1f}%"
        return f"{result}\n{confidence}"
    
    except Exception as e:
        return "❌ Error: Model compatibility issue. Please retrain with current scikit-learn version."

# Custom CSS for professional styling
css = """
.gradio-container {
    max-width: 1200px !important;
    margin: auto !important;
}
.input-group {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    padding: 20px;
    border-radius: 15px;
    margin: 10px 0;
}
.output-group {
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 18px;
    font-weight: bold;
}
"""

# Create professional interface using Blocks
with gr.Blocks(css=css, theme=gr.themes.Glass(), title="Diabetes Prediction System") as interface:
    
    gr.HTML("""
    <div style="text-align: center; padding: 20px; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 15px; margin-bottom: 20px;">
        <h1 style="color: white; margin: 0; font-size: 2.5em;">🏥 Diabetes Risk Analysis</h1>
        <p style="color: white; margin: 10px 0 0 0; font-size: 1.2em;">AI-Powered Diabetes Prediction System</p>
    </div>
    """)
    
    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("### 📊 Patient Information")
            
            with gr.Row():
                pregnancies = gr.Number(label="👶 Pregnancies", value=0, minimum=0, maximum=17, info="Number of pregnancies")
                age = gr.Number(label="🎂 Age (years)", value=30, minimum=21, maximum=81, info="Patient's age")
            
            with gr.Row():
                glucose = gr.Slider(label="🩸 Glucose (mg/dL)", value=120, minimum=0, maximum=300, info="Fasting glucose level")
                blood_pressure = gr.Slider(label="💓 Blood Pressure (mmHg)", value=80, minimum=20, maximum=200, info="Diastolic pressure")
            
            with gr.Row():
                bmi = gr.Number(label="⚖️ BMI (kg/m²)", value=25.0, minimum=0, maximum=67, precision=1, info="Body Mass Index")
                insulin = gr.Slider(label="💉 Insulin (μU/mL)", value=80, minimum=0, maximum=1000, info="Serum insulin level")
            
            with gr.Row():
                skin_thickness = gr.Dropdown(
                    label="📏 Skin Thickness (mm)", 
                    choices=[("Thin (10-15mm)", 12), ("Normal (16-25mm)", 20), ("Thick (26-35mm)", 30), ("Very Thick (36mm+)", 40)],
                    value=20,
                    info="Triceps skin fold"
                )
                diabetes_pedigree = gr.Radio(
                    label="🧬 Family History",
                    choices=[("No Risk (0.0-0.1)", 0.05), ("Low Risk (0.1-0.3)", 0.2), ("Medium Risk (0.4-0.8)", 0.6), ("High Risk (0.9+)", 1.2)],
                    value=0.2,
                    info="Diabetes pedigree function"
                )
            
            with gr.Row():
                clear_btn = gr.Button("🔄 Reset Form", variant="secondary", size="lg")
                predict_btn = gr.Button("🔍 Analyze Risk", variant="primary", size="lg")
        
        with gr.Column(scale=1):
            gr.Markdown("### 🎯 Prediction Result")
            result_output = gr.Textbox(
                label="Analysis Result",
                lines=3,
                max_lines=3,
                interactive=False,
                show_label=False
            )
            
            gr.Markdown("""
            ### 📋 Reference Ranges
            - **Glucose**: Normal <100, Pre-diabetes 100-125, Diabetes ≥126
            - **Blood Pressure**: Normal <120, High ≥130
            - **BMI**: Normal 18.5-24.9, Overweight 25-29.9, Obese ≥30
            - **Insulin**: Normal 16-166 μU/mL
            """)
    
    gr.Markdown("### 🧪 Quick Test Cases")
    gr.Examples(
        examples=[
            [6, 148, 72, 30, 0, 33.6, 1.2, 50, "High Risk Patient"],
            [1, 85, 66, 20, 0, 26.6, 0.2, 31, "Low Risk Patient"],
            [0, 137, 40, 40, 168, 43.1, 0.6, 33, "Medium Risk Patient"]
        ],
        inputs=[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age],
        label="Sample Cases"
    )
    
    # Event handlers
    predict_btn.click(
        fn=predict_diabetes,
        inputs=[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age],
        outputs=result_output
    )
    
    clear_btn.click(
        fn=lambda: (0, 120, 80, 20, 80, 25.0, 0.2, 30, ""),
        outputs=[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age, result_output]
    )

if __name__ == "__main__":
    interface.launch(share=True)