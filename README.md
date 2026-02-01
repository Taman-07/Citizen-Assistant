# Bharat Citizen Assistant 🇮🇳

An AI-powered multilingual citizen assistance system designed specifically for Indian citizens to access information about government schemes and public services. The system supports Hindi, English, and other regional Indian languages, making government services more accessible to citizens with varying levels of digital literacy.

## 🎯 Features

### Core Capabilities
- **Multilingual Support**: Hindi, English, Bengali, Telugu, Marathi, Tamil, Gujarati, Kannada, Malayalam, and Odia
- **Intelligent Query Processing**: Understands user intent and provides relevant government scheme information
- **Low Bandwidth Optimized**: Designed to work efficiently in low-bandwidth environments
- **Simple Interface**: User-friendly web interface suitable for users with low digital literacy
- **Government Schemes Database**: Comprehensive information about major Indian government schemes

### Supported Government Schemes
- **PM-KISAN**: Direct income support for farmers
- **Ayushman Bharat**: Health insurance for poor families
- **MUDRA Yojana**: Micro-finance for small businesses
- **Extensible**: Easy to add more schemes

### Query Types Supported
- Scheme eligibility criteria
- Application processes
- Required documents
- Benefits and coverage
- General scheme information

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- Internet connection (for initial setup)
- 2GB RAM minimum
- 1GB free disk space

### Installation

1. **Clone or download the project files**
2. **Run the setup script**:
   ```bash
   python setup.py
   ```
   This will:
   - Install all required dependencies
   - Download necessary ML models
   - Initialize the database with sample schemes
   - Verify the installation

3. **Start the application**:
   ```bash
   python bharat_citizen_assistant.py
   ```

4. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## 💡 Usage Examples

### Hindi Queries
- "PM किसान योजना के लिए कैसे आवेदन करें?"
- "आयुष्मान भारत के लिए कौन से documents चाहिए?"
- "मुद्रा लोन के लिए मैं eligible हूं क्या?"

### English Queries
- "What is Ayushman Bharat scheme?"
- "How to apply for MUDRA loan?"
- "Am I eligible for PM-KISAN scheme?"

### Mixed Language Queries
- "MUDRA loan के लिए क्या documents चाहिए?"
- "Ayushman Bharat scheme में कितना coverage मिलता है?"

## 🏗️ Architecture

### System Components
1. **Web Frontend**: Simple, responsive HTML/CSS/JavaScript interface
2. **Flask Backend**: RESTful API for query processing
3. **Language Detection**: FastText-based automatic language identification
4. **NLP Processing**: Intent classification and entity extraction
5. **Knowledge Base**: SQLite database with government scheme information
6. **Response Generation**: Context-aware response formatting

### Data Flow
```
User Query → Language Detection → Intent Analysis → Scheme Search → Response Generation → Translation → User
```

## 📊 Technical Specifications

### Performance
- **Response Time**: < 2 seconds for typical queries
- **Concurrent Users**: Up to 100 simultaneous users
- **Memory Usage**: ~500MB RAM
- **Storage**: ~200MB for base installation

### Supported Languages
| Language | Code | Script |
|----------|------|--------|
| Hindi | hi | Devanagari |
| English | en | Latin |
| Bengali | bn | Bengali |
| Telugu | te | Telugu |
| Marathi | mr | Devanagari |
| Tamil | ta | Tamil |
| Gujarati | gu | Gujarati |
| Kannada | kn | Kannada |
| Malayalam | ml | Malayalam |
| Odia | or | Odia |

## 🔧 Configuration

### Basic Configuration (`config.json`)
```json
{
    "supported_languages": ["hi", "en", "bn", "te", "mr", "ta", "gu", "kn", "ml", "or"],
    "server": {
        "host": "0.0.0.0",
        "port": 5000,
        "debug": false
    },
    "performance": {
        "max_query_length": 500,
        "response_timeout": 30,
        "max_concurrent_users": 100
    }
}
```

### Adding New Government Schemes

1. **Database Method** (Recommended):
   ```python
   # Add to the database directly
   cursor.execute('''
       INSERT INTO government_schemes 
       (scheme_id, name, description, eligibility, documents_required, 
        application_process, benefits, ministry, category, target_audience, keywords)
       VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
   ''', scheme_data)
   ```

2. **Code Method**:
   - Edit the `_populate_sample_schemes()` method in `bharat_citizen_assistant.py`
   - Add your scheme data to the `sample_schemes` list
   - Restart the application

## 🌐 Deployment Options

### Local Development
```bash
python bharat_citizen_assistant.py
```

### Production Deployment
```bash
# Using Gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 bharat_citizen_assistant:app

# Using Docker (create Dockerfile)
docker build -t bharat-assistant .
docker run -p 5000:5000 bharat-assistant
```

### Cloud Deployment
- **AWS EC2**: For scalable web hosting
- **Google Cloud Platform**: Using App Engine or Compute Engine
- **Azure**: Using App Service or Virtual Machines
- **Heroku**: For simple deployment

## 🔒 Security & Privacy

### Data Privacy
- No personal information is stored permanently
- Query logs contain only anonymized data
- No external API calls for sensitive data
- Local processing ensures data privacy

### Security Features
- Input sanitization to prevent injection attacks
- Rate limiting to prevent abuse
- CORS protection for web security
- Optional HTTPS support

## 📈 Analytics & Monitoring

### Built-in Analytics
- Query frequency tracking
- Language usage statistics
- Popular scheme inquiries
- Response accuracy metrics

### Monitoring
- Health check endpoint: `/api/health`
- System status monitoring
- Error logging and tracking

## 🤝 Contributing

### Adding New Languages
1. Add language code to `supported_languages` in config
2. Update language detection mapping
3. Add translation support
4. Test with native speakers

### Adding New Schemes
1. Research official government scheme details
2. Structure data according to the database schema
3. Add relevant keywords for search
4. Test query matching and responses

### Improving NLP
1. Enhance intent classification rules
2. Add more entity extraction patterns
3. Improve response templates
4. Add context-aware responses

## 🐛 Troubleshooting

### Common Issues

**1. FastText model not downloading**
```bash
# Manual download
wget https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin
```

**2. Database initialization fails**
```bash
# Delete and recreate database
rm bharat_schemes.db
python setup.py
```

**3. Port already in use**
```bash
# Change port in config.json or kill existing process
lsof -ti:5000 | xargs kill -9
```

**4. Memory issues**
```bash
# Reduce model size or increase system memory
# Consider using lighter models for resource-constrained environments
```

## 📞 Support

### Getting Help
- Check the troubleshooting section above
- Review the configuration options
- Ensure all dependencies are installed correctly
- Verify Python version compatibility

### System Requirements
- **Minimum**: 2GB RAM, 1GB storage, Python 3.7+
- **Recommended**: 4GB RAM, 2GB storage, Python 3.8+
- **Network**: Internet required for initial setup only

## 📄 License

This project is designed for public benefit and educational purposes. Please ensure compliance with relevant government data usage policies when deploying in production environments.

## 🙏 Acknowledgments

- Government of India for open data initiatives
- Open source ML community for tools and models
- Contributors to multilingual NLP research
- Indian language computing community

---

**Made with ❤️ for Bharat's digital inclusion**#   C i t i z e n - A s s i s t a n t  
 