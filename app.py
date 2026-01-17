import gradio as gr
import joblib
import pandas as pd

print("App starting...")

# -------------------------
# Load the trained model
# -------------------------
try:
    print("⏳ Loading model...")
    model = joblib.load("diabetes_model.pkl")
    print("Model loaded successfully")
except Exception as e:
    print("Model loading failed:", e)
    model = None


# -------------------------
# Prediction function
# -------------------------
def predict_diabetes(
    pregnancies,
    glucose,
    blood_pressure,
    skin_thickness,
    insulin,
    bmi,
    diabetes_pedigree,
    age,
):
    if model is None:
        return "Model not loaded."

    try:
        features = pd.DataFrame({
            "Pregnancies": [pregnancies],
            "Glucose": [glucose],
            "BloodPressure": [blood_pressure],
            "SkinThickness": [skin_thickness],
            "Insulin": [insulin],
            "BMI": [bmi],
            "DiabetesPedigreeFunction": [diabetes_pedigree],
            "Age": [age],
        })

        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] * 100

        result = "🔴 HIGH RISK - Diabetic" if prediction == 1 else "🟢 LOW RISK - Non-Diabetic"
        return f"{result}\nConfidence: {probability:.1f}%"

    except Exception:
        return "❌ Model compatibility issue. Please retrain with current scikit-learn version."


# -------------------------
# Custom CSS
# -------------------------
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


# -------------------------
# Interface
# -------------------------
with gr.Blocks(css=css, title="Diabetes Prediction System") as interface:

    gr.HTML("""
    <div style="text-align:center;padding:20px;
         background:linear-gradient(90deg,#667eea,#764ba2);
         border-radius:15px;margin-bottom:20px;">
        <h1 style="color:white;margin:0;font-size:2.5em;">🏥 Diabetes Risk Analysis</h1>
        <p style="color:white;margin-top:10px;font-size:1.2em;">
            AI-Powered Diabetes Prediction System
        </p>
    </div>
    """)

    with gr.Row():
        with gr.Column(scale=2):
            gr.Markdown("### 📊 Patient Information")

            with gr.Row():
                pregnancies = gr.Number(
                    label="👶 Pregnancies",
                    value=0,
                    minimum=0,
                    maximum=17,
                )
                age = gr.Number(
                    label="🎂 Age (years)",
                    value=30,
                    minimum=21,
                    maximum=81,
                )

            with gr.Row():
                glucose = gr.Slider(
                    label="🩸 Glucose (mg/dL)",
                    value=120,
                    minimum=0,
                    maximum=300,
                )
                blood_pressure = gr.Slider(
                    label="💓 Blood Pressure (mmHg)",
                    value=80,
                    minimum=20,
                    maximum=200,
                )

            with gr.Row():
                bmi = gr.Number(
                    label="⚖️ BMI (kg/m²)",
                    value=25.0,
                    precision=1,
                )
                insulin = gr.Slider(
                    label="💉 Insulin (μU/mL)",
                    value=80,
                    minimum=0,
                    maximum=1000,
                )

            with gr.Row():
                skin_thickness = gr.Dropdown(
                    label="📏 Skin Thickness (mm)",
                    choices=[12, 20, 30, 40],
                    value=20,
                )
                diabetes_pedigree = gr.Radio(
                    label="🧬 Family History",
                    choices=[0.05, 0.2, 0.6, 1.2],
                    value=0.2,
                )

            with gr.Row():
                clear_btn = gr.Button("🔄 Reset Form")
                predict_btn = gr.Button("🔍 Analyze Risk")

        with gr.Column(scale=1):
            gr.Markdown("### 🎯 Prediction Result")
            result_output = gr.Textbox(
                lines=3,
                interactive=False,
                show_label=False,
            )

            gr.Markdown("""
            ### 📋 Reference Ranges
            - **Glucose**: Normal <100, Pre-diabetes 100–125, Diabetes ≥126  
            - **Blood Pressure**: Normal <120, High ≥130  
            - **BMI**: Normal 18.5–24.9, Overweight 25–29.9, Obese ≥30  
            - **Insulin**: Normal 16–166 μU/mL
            """)

    gr.Markdown("### 🧪 Quick Test Cases")

    gr.Examples(
        examples=[
            [6, 148, 72, 30, 0, 33.6, 1.2, 50],
            [1, 85, 66, 20, 0, 26.6, 0.2, 31],
            [0, 137, 40, 40, 168, 43.1, 0.6, 33],
        ],
        inputs=[
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age,
        ],
    )

    predict_btn.click(
        predict_diabetes,
        [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age,
        ],
        result_output,
    )

    clear_btn.click(
        lambda: (0, 120, 80, 20, 80, 25.0, 0.2, 30, ""),
        [
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            diabetes_pedigree,
            age,
            result_output,
        ],
    )


# -------------------------
# Launch (HF Spaces ready)
# -------------------------
if __name__ == "__main__":
    interface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        show_error=True,
    )
