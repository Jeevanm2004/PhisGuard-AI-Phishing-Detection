# 🛡️ PhisGuard: AI-Powered Phishing Detection System

## 📋 Project Overview

PhisGuard is an intelligent phishing detection system that leverages machine learning algorithms to identify malicious URLs and protect users from cyber threats. The system analyzes URL patterns, domain characteristics, and web content features to achieve high-accuracy phishing detection.

## 🎯 Problem Statement

- **Phishing attacks** cost businesses over **$12 billion annually**
- Traditional blacklist-based methods are **reactive** and **incomplete**
- Need for **real-time, proactive** detection system
- **95% of successful cyber attacks** start with phishing emails

## 🧠 Technical Approach

### Machine Learning Pipeline
1. **Data Collection**: PhishTank Dataset + URL-2016 Dataset
2. **Feature Engineering**: 30+ URL-based and domain-based features
3. **Model Training**: Multiple ML algorithms comparison
4. **Model Evaluation**: Cross-validation and performance metrics
5. **Deployment Ready**: Optimized for real-time inference

### Feature Categories
- **URL-based Features**: Length, special characters, redirects
- **Domain Features**: Age, registration details, reputation
- **Content Features**: HTML/JavaScript analysis
- **Network Features**: WHOIS data, DNS records

## 🔧 Technologies Used

- **Python 3.8+**
- **Machine Learning**: Scikit-learn, XGBoost
- **Data Processing**: Pandas, NumPy
- **Deep Learning**: TensorFlow (Autoencoder)
- **Visualization**: Matplotlib, Seaborn
- **Web Scraping**: BeautifulSoup, Requests

## 📊 Model Performance

| Algorithm | Accuracy | Precision | Recall | F1-Score |
|-----------|----------|-----------|--------|----------|
| **XGBoost** | **96.2%** | **95.8%** | **96.5%** | **96.1%** |
| Random Forest | 94.7% | 94.2% | 95.1% | 94.6% |
| SVM | 92.8% | 92.1% | 93.4% | 92.7% |
| Autoencoder | 91.5% | 90.8% | 92.2% | 91.5% |

## 🚀 Key Features

- ✅ **Real-time URL Analysis** (< 200ms response time)
- ✅ **Multi-model Ensemble** approach for higher accuracy
- ✅ **Feature Importance Analysis** for interpretability
- ✅ **Scalable Architecture** for production deployment
- ✅ **API-ready Design** for integration with browsers/applications

## 📁 Project Structure

```
PhisGuard-AI-Phishing-Detection/
├── data/                   # Dataset storage
├── notebooks/              # Jupyter notebooks for analysis
├── src/                    # Source code modules
├── models/                 # Trained model files
├── results/                # Performance metrics and visualizations
└── docs/                   # Technical documentation
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation Steps
```bash
# Clone the repository
git clone https://github.com/yourusername/PhisGuard-AI-Phishing-Detection.git
cd PhisGuard-AI-Phishing-Detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

## 🎮 Usage

### Quick Start
```python
from src.models import PhishingDetector

# Initialize the detector
detector = PhishingDetector()

# Load pre-trained model
detector.load_model('models/xgboost_model.pkl')

# Predict URL
url = "http://suspicious-website.com"
result = detector.predict(url)
print(f"Phishing Probability: {result['probability']:.2%}")
```

### Training New Model
```bash
# Run the training pipeline
python src/train_model.py --dataset data/processed/features.csv --model xgboost
```

## 📈 Results & Insights

### Key Findings
- **URL Length** is the most important feature (23% importance)
- **Domain Age** significantly impacts phishing likelihood
- **HTTPS presence** alone is not a reliable indicator
- **Ensemble methods** outperform individual algorithms

### Performance Metrics
- **Training Time**: ~45 seconds on standard laptop
- **Inference Time**: < 200ms per URL
- **Model Size**: 15.2 MB (optimized for deployment)
- **Memory Usage**: < 100MB during inference

## 🔮 Future Enhancements

- [ ] **Browser Extension** for real-time protection
- [ ] **Deep Learning Models** (LSTM, Transformer)
- [ ] **Real-time Threat Intelligence** integration
- [ ] **Mobile App Development**
- [ ] **API Service** with rate limiting
- [ ] **Dashboard** for threat monitoring

## 📚 Learning Outcomes

- **Machine Learning Pipeline** development
- **Feature Engineering** for cybersecurity domain
- **Model Comparison** and evaluation techniques
- **Real-world Problem Solving** with AI
- **Software Engineering** best practices

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Jeevan M**  
📧 jeevanm.bit@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/JeevanM) | [GitHub](https://github.com/Jeevanm2004)

---

⭐ **Star this repository if you found it helpful!**
