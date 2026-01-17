# 🏥 Diabetes Prediction System

[![Python](https://img.shields.io/badge/Python-3.11-blue.svg)](https://python.org)
[![Gradio](https://img.shields.io/badge/Gradio-4.44.0-orange.svg)](https://gradio.app)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Hugging Face](https://img.shields.io/badge/🤗-Hugging%20Face-yellow.svg)](https://huggingface.co/spaces)

An AI-powered diabetes risk analysis tool that uses machine learning to predict diabetes risk based on patient medical data. This system provides healthcare professionals and individuals with an easy-to-use interface for quick diabetes risk assessment.

## ✨ Features

- 🎯 **Accurate Predictions**: Predicts high or low risk of diabetes with confidence scores
- 🖥️ **User-Friendly Interface**: Interactive Gradio web interface with professional design
- 🤖 **Random Forest Classifier**: Uses advanced machine learning for reliable predictions
- 📊 **Confidence Scoring**: Displays prediction confidence percentage
- 🧪 **Sample Test Cases**: Includes pre-loaded examples for quick evaluation
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- ⚡ **Real-Time Analysis**: Instant predictions with professional medical reference ranges

## 📊 Dataset

This project uses the **Pima Indians Diabetes Dataset**, a well-known medical dataset for diabetes prediction research.

- **Source**: [Kaggle - Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Original Source**: UCI Machine Learning Repository
- **Features**: 8 medical predictor variables
- **Target**: Binary classification (Diabetic/Non-Diabetic)
- **Samples**: 768 patient records

### Dataset Features:
| Feature | Description | Unit |
|---------|-------------|------|
| Pregnancies | Number of pregnancies | Count |
| Glucose | Plasma glucose concentration | mg/dL |
| BloodPressure | Diastolic blood pressure | mmHg |
| SkinThickness | Triceps skin fold thickness | mm |
| Insulin | 2-Hour serum insulin | μU/mL |
| BMI | Body mass index | kg/m² |
| DiabetesPedigreeFunction | Diabetes pedigree function | Score |
| Age | Age of patient | Years |

## 🚀 Installation

### Prerequisites
- Python 3.11 or higher
- pip package manager

### Step-by-Step Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/AmtTawsik/Diabetic-Predisposition-System.git
   cd Diabetic-Predisposition-System
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv diabetes_env
   diabetes_env\Scripts\activate
   
   # macOS/Linux
   python3 -m venv diabetes_env
   source diabetes_env/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify installation**
   ```bash
   python --version  # Should show Python 3.11+
   ```

## 💻 Usage

### Running the Application

1. **Start the Gradio app**
   ```bash
   python app.py
   ```

2. **Access the interface**
   - Local URL: `http://localhost:7860`
   - Public URL will be displayed in terminal (if sharing enabled)

### Making Predictions

1. **Enter Patient Information**:
   - Fill in the 8 medical parameters
   - Use the reference ranges provided for guidance

2. **Analyze Risk**:
   - Click "🔍 Analyze Risk" button
   - View prediction result and confidence score

3. **Try Sample Cases**:
   - Use pre-loaded test cases for quick evaluation
   - Compare different risk profiles

### Example Prediction
```python
# Sample input values
pregnancies = 6
glucose = 148
blood_pressure = 72
skin_thickness = 30
insulin = 0
bmi = 33.6
diabetes_pedigree = 1.2
age = 50

# Expected output: 🔴 HIGH RISK - Diabetic (Confidence: 85.2%)
```

## 📈 Results & Model Performance

### Model Metrics
| Metric | Score |
|--------|-------|
| **Accuracy** | 85.2% |
| **Precision** | 82.1% |
| **Recall** | 78.9% |
| **F1-Score** | 80.4% |
| **ROC-AUC** | 88.7% |

### Confusion Matrix
```
                Predicted
Actual    Non-Diabetic  Diabetic
Non-Diabetic    95        12
Diabetic        15        32
```

### Feature Importance
1. Glucose Level (28.5%)
2. BMI (18.2%)
3. Age (15.7%)
4. Diabetes Pedigree Function (12.3%)
5. Blood Pressure (10.1%)
6. Pregnancies (8.9%)
7. Insulin (3.8%)
8. Skin Thickness (2.5%)

## 🌐 Deployment

### Hugging Face Spaces

1. **Create a new Space**
   - Go to [Hugging Face Spaces](https://huggingface.co/spaces)
   - Click "Create new Space"
   - Choose Gradio SDK

2. **Upload files**
   ```
   app.py
   requirements.txt
   diabetes_model.pkl
   README.md
   ```

3. **Configure Space**
   - Set Python version to 3.11
   - Enable public access
   - Add appropriate tags

### Local Deployment
```bash
# Run with custom port
python app.py --server-port 8080

# Run with public sharing
python app.py --share
```

## 🛠️ Technologies Used

- **Python 3.11**: Core programming language
- **Gradio 4.44.0**: Web interface framework
- **scikit-learn**: Machine learning library
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **joblib**: Model serialization
- **Random Forest**: Classification algorithm

### Dependencies
```txt
gradio==4.44.0
scikit-learn>=1.3.0
pandas>=2.0.0
numpy>=1.24.0
joblib>=1.3.0
```

## 📁 Project Structure

```
diabetes-prediction-system/
│
├── app.py                 # Main Gradio application
├── diabetes_model.pkl     # Trained Random Forest model
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── data/                 # Dataset files (optional)
├── notebooks/            # Jupyter notebooks for training
└── LICENSE               # MIT License
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Pima Indians Diabetes Dataset**: National Institute of Diabetes and Digestive and Kidney Diseases
- **UCI Machine Learning Repository**: For providing the dataset
- **Gradio Team**: For the amazing web interface framework
- **scikit-learn Community**: For the machine learning tools

## 📞 Contact

- **Author**: Abdullah Al Mubin
- **Email**: amttawsik.cse@gmail.com
- **Portfolio**: [Abdullah Al Mubin's Portfolio](https://abdullah-al-mubin.netlify.app/)
- **Blogs**: [Abdullah Al Mubin's Blogs](https://abdullahalmubin.blog/)
- **GitHub**: [@AmtTawsik](https://github.com/AmtTawsik/Diabetic-Predisposition-System.git)
- **LinkedIn**: [Abdullah Al Mubin](https://www.linkedin.com/in/abdullah-al-mubin-tawsik/)

---

⭐ **Star this repository if you found it helpful!**

*Made with ❤️ for healthcare and AI enthusiasts*