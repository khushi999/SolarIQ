# Google Analytics Setup Guide for SolarIQ

## What's Already Added

I've already added Google Analytics tracking code to your `frontend/index.html` file with the following features:

1. **Basic Page Tracking**: Tracks all page views automatically
2. **Custom Events**: Tracks specific user interactions:
   - Form submissions for solar forecasts
   - Location detection attempts
   - Successful location detection
   - Location errors
   - Geolocation support issues

## Setup Steps

### 1. Create a Google Analytics Account

1. Go to [Google Analytics](https://analytics.google.com/)
2. Click "Start measuring"
3. Follow the setup wizard to create your account
4. Choose "Web" as your property type
5. Enter your website details:
   - Website name: "SolarIQ"
   - Website URL: Your deployed URL (e.g., `https://solariq.onrender.com`)
   - Industry category: "Technology"
   - Business size: Choose appropriate option

### 2. Get Your Measurement ID

1. After creating your property, you'll get a Measurement ID that looks like `G-XXXXXXXXXX`
2. Copy this ID

### 3. Update Your HTML File

Replace the placeholder `G-XXXXXXXXXX` in your `frontend/index.html` file with your actual Measurement ID:

```html
<!-- Replace both instances of G-XXXXXXXXXX with your actual Measurement ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-XXXXXXXXXX');
</script>
```

### 4. Deploy Your Changes

After updating the Measurement ID, redeploy your application to make the tracking live.

## What You'll Be Able to Track

### Basic Metrics
- **Page Views**: How many times your website is visited
- **Users**: Unique visitors to your site
- **Sessions**: Individual browsing sessions
- **Bounce Rate**: Percentage of users who leave after viewing one page
- **Session Duration**: How long users stay on your site

### Custom Events
- **Solar Forecast Requests**: When users submit the form to get predictions
- **Location Detection**: When users try to auto-detect their location
- **Location Success/Errors**: Success and failure rates of location detection
- **Geographic Data**: Where your users are located (if they allow location access)

### Advanced Insights
- **Traffic Sources**: How users find your website (search, social media, direct, etc.)
- **Device Types**: Desktop vs mobile usage
- **Browser Information**: Which browsers your users prefer
- **Real-time Data**: Live visitor activity

## Privacy Considerations

- The tracking code respects user privacy settings
- Users can opt out through browser settings
- Consider adding a privacy policy to your website
- The tracking is GDPR-compliant as it uses Google's standard implementation

## Testing

After setup:
1. Visit your website
2. Submit a solar forecast request
3. Try the location detection feature
4. Check your Google Analytics dashboard (may take 24-48 hours for data to appear)

## Troubleshooting

- **No data appearing**: Wait 24-48 hours for initial data
- **Events not tracking**: Check browser console for JavaScript errors
- **Measurement ID issues**: Verify the ID is correct and properly formatted

## Next Steps

Once you have data flowing, you can:
1. Set up custom dashboards for solar forecasting metrics
2. Create conversion goals (e.g., form submissions)
3. Set up email reports for regular insights
4. Use the data to optimize your user experience 