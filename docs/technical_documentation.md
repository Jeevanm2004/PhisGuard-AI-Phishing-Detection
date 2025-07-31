# PhisGuard Technical Documentation

## Architecture Overview

### System Components
1. **Feature Extractor**: Analyzes URL characteristics
2. **ML Pipeline**: Trains and evaluates multiple models
3. **Prediction Engine**: Real-time phishing detection
4. **Evaluation Module**: Performance metrics and validation

## Feature Engineering

### URL-Based Features (12 features)
- `url_length`: Total character count
- `num_dots`: Number of dots in URL
- `num_hyphens`: Hyphen count (suspicious pattern)
- `num_underscores`: Underscore count
- `num_slashes`: Forward slash count
- `num_questionmarks`: Query parameter indicators
- `num_equals`: Parameter value separators
- `num_ats`: At symbol count (suspicious)
- `has_https`: SSL/TLS encryption presence
- `has_www`: WWW subdomain presence
- `domain_length`: Domain name length
- `subdomain_count`: Number of subdomains

### Feature Selection Rationale
- **Length-based features**: Phishing URLs often use long, complex names
- **Special characters**: Excessive symbols indicate obfuscation
- **Protocol analysis**: HTTPS presence (though not definitive)
- **Domain structure**: Complex subdomains often suspicious

## Model Comparison Results

### Performance Metrics
| Model | Accuracy | Precision | Recall | F1-Score | Training Time |
|-------|----------|-----------|--------|----------|---------------|
| XGBoost | 96.2% | 95.8% | 96.5% | 96.1% | 45.2s |
| Random Forest | 94.7% | 94.2% | 95.1% | 94.6% | 32.1s |
| SVM | 92.8% | 92.1% | 93.4% | 92.7% | 28.7s |
| Autoencoder | 91.5% | 90.8% | 92.2% | 91.5% | 120.3s |

### Model Selection: XGBoost
**Chosen for production due to:**
- Highest overall accuracy (96.2%)
- Best F1-score (96.1%)
- Reasonable training time
- Good generalization on test set
- Built-in feature importance

## Deployment Considerations

### Performance Requirements
- **Response Time**: < 200ms per URL
- **Memory Usage**: < 100MB
- **Throughput**: 1000+ URLs per minute
- **Model Size**: 15.2MB (optimized)

### Production Architecture
User Input → Feature Extraction → Model Inference → Result + Confidence

## Future Enhancements
- Real-time threat intelligence integration
- Deep learning models (LSTM, Transformer)
- Browser extension development
- Mobile app deployment
