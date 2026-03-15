from database import SessionLocal
import models

db = SessionLocal()

questions = [

models.Question(
question="What does ML stand for?",
option1="Machine Learning",
option2="Model Learning",
option3="Machine Logic",
option4="Modern Learning",
answer="Machine Learning"
),

models.Question(
question="Which library is commonly used for Machine Learning in Python?",
option1="NumPy",
option2="scikit-learn",
option3="Matplotlib",
option4="Flask",
answer="scikit-learn"
),

models.Question(
question="Which type of learning uses labeled data?",
option1="Supervised Learning",
option2="Unsupervised Learning",
option3="Reinforcement Learning",
option4="Deep Learning",
answer="Supervised Learning"
),

models.Question(
question="Which algorithm is used for classification?",
option1="Linear Regression",
option2="Logistic Regression",
option3="K-Means",
option4="PCA",
answer="Logistic Regression"
),

models.Question(
question="Which library is mainly used for data analysis in Python?",
option1="TensorFlow",
option2="Pandas",
option3="PyTorch",
option4="Keras",
answer="Pandas"
),

models.Question(
question="Which plot is used to visualize data distribution?",
option1="Histogram",
option2="Pie Chart",
option3="Line Graph",
option4="Bar Chart",
answer="Histogram"
),

models.Question(
question="Which algorithm is used for clustering?",
option1="K-Means",
option2="Linear Regression",
option3="Decision Tree",
option4="Random Forest",
answer="K-Means"
),

models.Question(
question="Which library is used for numerical computing in Python?",
option1="NumPy",
option2="Seaborn",
option3="Django",
option4="Flask",
answer="NumPy"
),

models.Question(
question="What is the process of cleaning and preparing data called?",
option1="Data Wrangling",
option2="Data Mining",
option3="Data Extraction",
option4="Data Injection",
answer="Data Wrangling"
),

models.Question(
question="Which visualization library is commonly used with Python?",
option1="Matplotlib",
option2="React",
option3="NodeJS",
option4="Spring",
answer="Matplotlib"
),

models.Question(
question="Which ML model is used for predicting continuous values?",
option1="Linear Regression",
option2="KNN",
option3="Naive Bayes",
option4="Decision Tree",
answer="Linear Regression"
),

models.Question(
question="Which term describes training a model with data?",
option1="Model Training",
option2="Data Rendering",
option3="Model Rendering",
option4="Model Structuring",
answer="Model Training"
),

models.Question(
question="Which library is widely used for deep learning?",
option1="TensorFlow",
option2="Pandas",
option3="OpenCV",
option4="Requests",
answer="TensorFlow"
),

models.Question(
question="Which metric is used to evaluate classification models?",
option1="Accuracy",
option2="Speed",
option3="Memory",
option4="Latency",
answer="Accuracy"
),

models.Question(
question="What does CSV stand for?",
option1="Comma Separated Values",
option2="Computer Stored Values",
option3="Central System Values",
option4="Control Separated Variables",
answer="Comma Separated Values"
),

models.Question(
question="Which technique reduces the number of features in data?",
option1="PCA",
option2="KNN",
option3="SVM",
option4="Regression",
answer="PCA"
),

models.Question(
question="Which learning method finds patterns in unlabeled data?",
option1="Unsupervised Learning",
option2="Supervised Learning",
option3="Reinforcement Learning",
option4="Transfer Learning",
answer="Unsupervised Learning"
),

models.Question(
question="Which library is used for advanced data visualization?",
option1="Seaborn",
option2="NumPy",
option3="Flask",
option4="Tkinter",
answer="Seaborn"
),

models.Question(
question="Which algorithm is commonly used for decision making models?",
option1="Decision Tree",
option2="K-Means",
option3="Linear Regression",
option4="Naive Bayes",
answer="Decision Tree"
),

models.Question(
question="What is the main goal of Data Analysis?",
option1="Extract insights from data",
option2="Delete data",
option3="Hide information",
option4="Compress data",
answer="Extract insights from data"
)

]

for q in questions:
    db.add(q)

db.commit()

print("20 ML & Data Analysis questions inserted successfully.")