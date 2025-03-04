# AI Web Search Assistant 🔍

An intelligent web search assistant powered by LangChain and Google's Gemini Pro model. This Streamlit-based application provides real-time web search capabilities with AI-enhanced responses.

## 🌟 Features

- **AI-Powered Search**: Utilizes Google's Gemini Pro model for intelligent search processing
- **Real-time Web Search**: Integrated with DuckDuckGo for live web results
- **Smart Rate Limiting**: Built-in rate limit handling with exponential backoff
- **Search History**: Maintains a history of searches and results
- **User-Friendly Interface**: Clean Streamlit UI for seamless interaction
- **Error Handling**: Robust error management for a smooth user experience

## 🛠️ Technology Stack

- **Frontend**: Streamlit
- **AI Model**: Google Gemini Pro
- **Search Engine**: DuckDuckGo
- **Framework**: LangChain
- **Language**: Python 3.9+

## 📁 Project Structure 

## 💻 Usage Guide

### Basic Usage
1. Launch the application
2. Enter your search query
3. Click "Search"
4. View results and search history

### Advanced Features

#### 1. Search History
- Access previous searches through expandable sections
- Each entry shows:
  - Original query
  - Search results
  - Timestamp

#### 2. Rate Limiting Protection
- Automatic handling of rate limits
- Exponential backoff for retries
- User-friendly error messages

#### 3. Result Formatting
- Structured presentation of search results
- Markdown formatting for better readability
- Clear separation between different results

## 🔧 Configuration Options

### Environment Variables
- `GOOGLE_API_KEY`: Your Google API key
- Additional configurations can be added in `.env`

### Search Agent Parameters
- `temperature`: Controls response creativity (0.0-1.0)
- `max_retries`: Maximum retry attempts
- `max_results`: Number of results per search

## 🔍 Technical Details

### Search Process Flow
1. User inputs query
2. Query processed by Gemini Pro
3. DuckDuckGo search executed
4. Results formatted and displayed
5. History updated

### Rate Limiting Strategy
- Initial delay: 1 second
- Exponential backoff: 2^attempt seconds
- Maximum retries: 3

### Error Handling
- Network errors
- API rate limits
- Invalid queries
- Service unavailability

## 📊 Performance Considerations

### Optimization Techniques
- Session state management
- Efficient result caching
- Rate limit avoidance
- Resource cleanup

### Best Practices
- Use specific queries
- Allow time between searches
- Monitor rate limits
- Regular API key rotation

## 🔒 Security Considerations

### API Key Protection
- Stored in `.env`
- Not exposed in UI
- Regular rotation recommended

### Rate Limiting
- Prevents abuse
- Protects resources
- Maintains service stability

## 🔄 Maintenance

### Regular Tasks
- Update dependencies
- Check API key validity
- Monitor error logs
- Clean search history

### Troubleshooting
- Check API key
- Verify network connection
- Review error messages
- Clear session state

## 📈 Future Enhancements

### Planned Features
1. Multi-language support
2. Advanced search filters
3. Result caching
4. Custom search templates
5. Export functionality

### Development Roadmap
- Q2 2024: Multi-language support
- Q3 2024: Advanced filters
- Q4 2024: Caching system
- Q1 2025: Template system

## 📝 License

This project is licensed under the MIT License. See LICENSE file for details.

## 👥 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Submit pull request

## 📫 Support

For issues and questions:
- Open GitHub issue
- Email: [your-email]
- Documentation: [docs-link]

## 🙏 Acknowledgments

- LangChain team
- Google Gemini Pro team
- Streamlit community
- DuckDuckGo API team

---