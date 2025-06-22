# SolarIQ Vercel Deployment Guide

## Overview
This guide will help you deploy your SolarIQ solar forecasting app to Vercel using FastAPI.

## Prerequisites
- A GitHub account
- A Vercel account (free tier available)
- Your trained model file (`models/solar_lstm.pth`)

## Project Structure
After conversion, your project should have:
```
SolarIQ/
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── vercel.json            # Vercel configuration
├── templates/
│   └── index.html         # Web interface
├── static/
│   └── style.css          # Additional styles
├── models/
│   └── solar_lstm.pth     # Your trained model
├── backend/               # Your existing backend modules
└── assets/               # Your existing assets
```

## Step-by-Step Deployment

### 1. Prepare Your Repository

1. **Ensure your model file is included:**
   - Make sure `models/solar_lstm.pth` is in your repository
   - The `.gitattributes` file should handle large files with Git LFS

2. **Verify all files are present:**
   ```bash
   # Check that these files exist
   ls main.py requirements.txt vercel.json
   ls templates/index.html
   ls models/solar_lstm.pth
   ```

### 2. Deploy to Vercel

#### Option A: Using Vercel CLI (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Login to Vercel:**
   ```bash
   vercel login
   ```

3. **Deploy from your project directory:**
   ```bash
   cd /path/to/your/SolarIQ
   vercel
   ```

4. **Follow the prompts:**
   - Link to existing project or create new
   - Confirm deployment settings
   - Wait for deployment to complete

#### Option B: Using Vercel Dashboard

1. **Push your code to GitHub:**
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push origin main
   ```

2. **Go to Vercel Dashboard:**
   - Visit [vercel.com](https://vercel.com)
   - Click "New Project"
   - Import your GitHub repository

3. **Configure deployment:**
   - Framework Preset: Other
   - Build Command: Leave empty (Vercel will auto-detect)
   - Output Directory: Leave empty
   - Install Command: `pip install -r requirements.txt`

4. **Deploy:**
   - Click "Deploy"
   - Wait for build to complete

### 3. Environment Variables (Optional)

If you need to add environment variables (e.g., API keys):

1. **In Vercel Dashboard:**
   - Go to your project settings
   - Navigate to "Environment Variables"
   - Add any required variables

2. **Common variables you might need:**
   ```
   NASA_API_KEY=your_key_here
   IPINFO_TOKEN=your_token_here
   ```

### 4. Verify Deployment

1. **Check the health endpoint:**
   ```
   https://your-app.vercel.app/health
   ```

2. **Test the main application:**
   ```
   https://your-app.vercel.app/
   ```

3. **Test prediction functionality:**
   - Enter coordinates (e.g., 28.6139, 77.2090 for Delhi)
   - Click "Get Solar Forecast"
   - Verify results are displayed

## Troubleshooting

### Common Issues

1. **Model file not found:**
   - Ensure `models/solar_lstm.pth` is committed to your repository
   - Check file size (should be handled by Git LFS)

2. **Build failures:**
   - Check Vercel build logs
   - Ensure all dependencies are in `requirements.txt`
   - Verify Python version compatibility

3. **Import errors:**
   - Ensure all backend modules are properly structured
   - Check that `__init__.py` files exist in directories

4. **Memory/timeout issues:**
   - The model loading might take time on first request
   - Consider optimizing model size if needed

### Performance Optimization

1. **Model loading:**
   - The model is loaded on each request (cold start)
   - Consider implementing model caching for production

2. **API rate limits:**
   - NASA POWER API has rate limits
   - Implement caching for weather data

3. **Response times:**
   - Monitor Vercel function execution time
   - Optimize data processing if needed

## Post-Deployment

### 1. Custom Domain (Optional)
- In Vercel dashboard, go to "Domains"
- Add your custom domain
- Configure DNS settings

### 2. Monitoring
- Use Vercel Analytics to monitor performance
- Set up error tracking if needed

### 3. Updates
- Push changes to GitHub
- Vercel will automatically redeploy
- Monitor deployment status

## Local Testing

Before deploying, test locally:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the FastAPI app
python main.py

# Visit http://localhost:8000
```

## Support

If you encounter issues:
1. Check Vercel build logs
2. Verify all files are properly committed
3. Test locally first
4. Check Vercel documentation for Python deployments

## Next Steps

After successful deployment:
1. Share your live URL
2. Monitor performance
3. Consider adding more features
4. Implement caching for better performance 