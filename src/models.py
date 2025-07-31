"""
PhisGuard ML Models Module
Contains model definitions and prediction functions
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import xgboost as xgb
import joblib
import requests
from urllib.parse import urlparse

class PhishingDetector:
    """Main class for phishing detection"""
    
    def __init__(self):
        self.model = None
        self.feature_names = [
            'url_length', 'num_dots', 'num_hyphens', 'num_underscores',
            'num_slashes', 'num_questionmarks', 'num_equals', 'num_ats',
            'has_https', 'has_www', 'domain_length', 'subdomain_count'
        ]
    
    def extract_features(self, url):
        """Extract features from URL for phishing detection"""
        features = {}
        
        # Basic URL features
        features['url_length'] = len(url)
        features['num_dots'] = url.count('.')
        features['num_hyphens'] = url.count('-')
        features['num_underscores'] = url.count('_')
        features['num_slashes'] = url.count('/')
        features['num_questionmarks'] = url.count('?')
        features['num_equals'] = url.count('=')
        features['num_ats'] = url.count('@')
        
        # Protocol and domain features
        features['has_https'] = 1 if 'https' in url.lower() else 0
        features['has_www'] = 1 if 'www.' in url.lower() else 0
        
        # Domain analysis
        try:
            parsed = urlparse(url)
            domain = parsed.netloc
            features['domain_length'] = len(domain)
            features['subdomain_count'] = domain.count('.') - 1
        except:
            features['domain_length'] = 0
            features['subdomain_count'] = 0
        
        return features
    
    def load_model(self, model_path):
        """Load pre-trained model"""
        try:
            self.model = joblib.load(model_path)
            print(f"Model loaded successfully from {model_path}")
        except Exception as e:
            print(f"Error loading model: {e}")
    
    def predict(self, url):
        """Predict if URL is phishing"""
        if not self.model:
            return {"error": "Model not loaded"}
        
        try:
            # Extract features
            features = self.extract_features(url)
            feature_vector = [features[name] for name in self.feature_names]
            
            # Make prediction
            probability = self.model.predict_proba([feature_vector])[0][1]
            prediction = "Phishing" if probability > 0.5 else "Legitimate"
            
            return {
                "url": url,
                "prediction": prediction,
                "probability": probability,
                "confidence": "High" if abs(probability - 0.5) > 0.3 else "Medium"
            }
        except Exception as e:
            return {"error": f"Prediction failed: {e}"}

# Example usage
if __name__ == "__main__":
    detector = PhishingDetector()
    
    # Test URLs
    test_urls = [
        "https://www.google.com",
        "http://suspicious-bank-login.phishing-site.com/secure/update"
    ]
    
    for url in test_urls:
        features = detector.extract_features(url)
        print(f"\nURL: {url}")
        print(f"Features: {features}")
