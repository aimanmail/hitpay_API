# HitPay Payment Gateway Testing Application

A Flask-based web application for testing HitPay payment gateway integration. This application demonstrates how to create payment requests and handle payment redirects using the HitPay API.

## Features

- 🌓 **Dark/Light Theme Support** - Toggle between dark and light themes
- 💳 **Payment Processing** - Create payment requests via HitPay API
- 📱 **Responsive Design** - Mobile-friendly interface
- 🚀 **cPanel Deployment Ready** - Configured for shared hosting deployment
- ✅ **Payment Confirmation** - Thank you page with auto-redirect

## Technology Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Payment Gateway**: HitPay API
- **Deployment**: cPanel with Passenger WSGI

## Project Structure

```
Source Code/
├── app.py                 # Main Flask application
├── passenger_wsgi.py      # WSGI configuration for cPanel
├── requirements.txt       # Python dependencies
├── .htaccess             # Apache configuration
└── templates/
    ├── index.html        # Payment form page
    ├── result.html       # Results page
    └── thankyou.html     # Payment confirmation page
```

## Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd hitpay-testing
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r Source\ Code/requirements.txt
   ```

4. **Run the application**
   ```bash
   cd "Source Code"
   python app.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

### cPanel Deployment

1. **Upload files** to your cPanel file manager
2. **Install Python dependencies** via cPanel Python app or terminal
3. **Configure the Python app** to point to `passenger_wsgi.py`
4. **Update redirect URL** in `app.py` to match your domain
5. **Set up SSL certificate** for secure payments

For detailed deployment steps, refer to the screenshots in `Step Implement on Cpanel/` folder.

## Configuration

### API Configuration

Update the following in `app.py`:

```python
API_KEY = "your_hitpay_api_key_here"
BASE_URL = "https://api.sandbox.hit-pay.com/v1/payment-requests"  # Sandbox
# BASE_URL = "https://api.hit-pay.com/v1/payment-requests"  # Production
```

### Redirect URL

Update the redirect URL to match your domain:

```python
payload = {
    "redirect_url": "https://yourdomain.com/thankyou"  # Update this
}
```

## API Integration

The application integrates with HitPay's payment API:

- **Endpoint**: `/v1/payment-requests`
- **Method**: POST
- **Authentication**: API Key in headers
- **Currency**: MYR (Malaysian Ringgit)

### Payment Flow

1. User fills out payment form (amount, name, email)
2. Application creates payment request via HitPay API
3. User is redirected to HitPay payment page
4. After payment, user is redirected to thank you page

## Dependencies

```
Flask==2.0.3
Werkzeug==2.0.3
requests==2.26.0
```

## Features Breakdown

### Theme Switching
- Automatic theme detection based on system preference
- Manual theme toggle button
- Persistent theme selection using localStorage

### Form Validation
- Client-side validation for required fields
- Amount formatting and validation
- Email format validation

### Responsive Design
- Mobile-first approach
- Flexible layouts for different screen sizes
- Touch-friendly interface elements

## Security Notes

⚠️ **Important Security Considerations**:

1. **API Key**: The current implementation uses a test API key. In production:
   - Store API keys in environment variables
   - Never commit real API keys to version control
   - Use production API keys only on production servers

2. **HTTPS**: Always use HTTPS in production for payment processing

3. **Input Validation**: Implement server-side validation for all user inputs

## Testing

The application is configured for HitPay's sandbox environment. To test:

1. Use the test API key provided
2. Fill out the payment form with test data
3. Use HitPay's test payment methods
4. Verify successful redirect to thank you page

## Troubleshooting

### Common Issues

1. **Import Errors**: Ensure all dependencies are installed
2. **Template Not Found**: Check template folder path configuration
3. **API Errors**: Verify API key and endpoint URL
4. **Deployment Issues**: Check cPanel Python app configuration

### Logs

Check application logs in cPanel or use Flask's debug mode for local development:

```python
app.run(debug=True)
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is for testing and educational purposes. Please review HitPay's terms of service before using in production.

## Support

For HitPay API documentation and support:
- [HitPay Developer Documentation](https://hit-pay.com/docs/api)
- [HitPay Support](https://hit-pay.com/support)

---

**Note**: This is a testing application. Ensure proper security measures and testing before using in a production environment.
