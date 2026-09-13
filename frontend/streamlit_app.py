import streamlit as st
import requests


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------

st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------

st.markdown(
    """
    <style>

    /* Main background */
    .stApp {
        background-color: #f7f9fc;
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 17px;
        color: #64748b;
        margin-bottom: 30px;
    }

    /* Cards */
    .info-card {
        padding: 20px;
        border-radius: 15px;
        background: white;
        border: 1px solid #e2e8f0;
        box-shadow: 0 4px 12px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    .result-card {
        padding: 25px;
        border-radius: 18px;
        background: white;
        border: 1px solid #e2e8f0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.08);
        text-align: center;
        margin-top: 25px;
    }

    .result-title {
        font-size: 28px;
        font-weight: 700;
    }

    .probability {
        font-size: 40px;
        font-weight: 700;
        margin: 10px 0;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-size: 17px;
        font-weight: 600;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------

API_URL = "http://127.0.0.1:8000/predict"


# ---------------------------------------------------------
# SIDEBAR
# ---------------------------------------------------------

with st.sidebar:

    st.markdown("## 🩺 Diabetes AI")

    st.markdown("---")

    st.markdown(
        """
        ### About

        This application uses a Machine Learning model
        through a FastAPI backend to estimate diabetes risk.

        **Technology**

        - Python
        - Scikit-learn
        - FastAPI
        - Pydantic
        - Streamlit
        """
    )

    st.markdown("---")

    st.info(
        "This application is for educational purposes "
        "and should not be used as a medical diagnosis."
    )


# ---------------------------------------------------------
# HEADER
# ---------------------------------------------------------

st.markdown(
    '<div class="main-title">🩺 Diabetes Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Enter the patient health information to estimate diabetes risk.'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# INPUT SECTION
# ---------------------------------------------------------

st.markdown(
    '<div class="info-card">',
    unsafe_allow_html=True
)

st.subheader("📋 Patient Information")

col1, col2 = st.columns(2)


with col1:

    glucose = st.number_input(
        "Glucose Level (mg/dL)",
        min_value=1.0,
        max_value=299.0,
        value=120.0,
        step=1.0,
        help="Blood glucose concentration."
    )

    blood_pressure = st.number_input(
        "Blood Pressure (mmHg)",
        min_value=1.0,
        max_value=199.0,
        value=70.0,
        step=1.0,
        help="Diastolic blood pressure."
    )

    bmi = st.number_input(
        "BMI",
        min_value=1.0,
        max_value=99.0,
        value=25.5,
        step=0.1,
        help="Body Mass Index."
    )


with col2:

    pedigree = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.01,
        max_value=2.49,
        value=0.50,
        step=0.01,
        help="Diabetes hereditary risk score."
    )

    age = st.number_input(
        "Age (years)",
        min_value=1,
        max_value=119,
        value=30,
        step=1,
        help="Patient's age."
    )


st.markdown("</div>", unsafe_allow_html=True)


# ---------------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------------

predict_button = st.button(
    "🔍 Predict Diabetes Risk",
    type="primary"
)


# ---------------------------------------------------------
# API REQUEST
# ---------------------------------------------------------

if predict_button:

    payload = {
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "BMI": bmi,
        "DiabetesPedigreeFunction": pedigree,
        "Age": age
    }

    with st.spinner("Analyzing patient information..."):

        try:

            response = requests.post(
                API_URL,
                json=payload,
                timeout=10
            )

            # Successful response
            if response.status_code == 200:

                result = response.json()

                prediction = result["prediction"]
                result_text = result["result"]
                probability = result["probability"]

                probability_percentage = probability * 100


                # -------------------------------------------------
                # RESULT
                # -------------------------------------------------

                st.markdown(
                    '<div class="result-card">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    '<div class="result-title">Prediction Result</div>',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="probability">'
                    f'{probability_percentage:.1f}%'
                    f'</div>',
                    unsafe_allow_html=True
                )

                st.progress(
                    min(max(probability, 0.0), 1.0)
                )

                st.markdown(
                    f"### {result_text}"
                )

                if prediction == 1:

                    st.error(
                        "⚠️ The model indicates a higher diabetes risk."
                    )

                else:

                    st.success(
                        "✅ The model indicates a lower diabetes risk."
                    )

                st.markdown("</div>", unsafe_allow_html=True)


                # -------------------------------------------------
                # INPUT SUMMARY
                # -------------------------------------------------

                st.subheader("📊 Input Summary")

                summary_col1, summary_col2, summary_col3 = st.columns(3)

                summary_col1.metric(
                    "Glucose",
                    f"{glucose:.0f} mg/dL"
                )

                summary_col2.metric(
                    "Blood Pressure",
                    f"{blood_pressure:.0f} mmHg"
                )

                summary_col3.metric(
                    "BMI",
                    f"{bmi:.1f}"
                )

                summary_col4, summary_col5 = st.columns(2)

                summary_col4.metric(
                    "Age",
                    f"{age} years"
                )

                summary_col5.metric(
                    "Pedigree Function",
                    f"{pedigree:.2f}"
                )


            else:

                st.error(
                    f"API Error: {response.status_code}"
                )

                try:
                    error_details = response.json()
                    st.json(error_details)

                except Exception:
                    st.write(response.text)


        except requests.exceptions.ConnectionError:

            st.error(
                "❌ Cannot connect to FastAPI backend."
            )

            st.info(
                "Please make sure the FastAPI server is running "
                "on http://127.0.0.1:8000"
            )


        except requests.exceptions.Timeout:

            st.error(
                "⏳ API request timed out. "
                "Please try again."
            )


        except Exception as e:

            st.error(
                f"Unexpected error: {str(e)}"
            )


# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------

st.markdown("---")

st.caption(
    "Diabetes Prediction System • "
    "FastAPI + Machine Learning + Streamlit"
)