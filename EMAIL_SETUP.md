# 📧 Email Notification Setup Guide

This guide explains how to configure email notifications for FormLog contact form submissions.

## 🎯 What happens when configured

When a user submits the contact form, the system will:
1. ✅ Save the submission to MongoDB database
2. 📧 Send an email notification to `pietrodelfranco00@gmail.com`
3. 🎉 Show success message to the user

## 🔧 Gmail Configuration (Recommended)

### Step 1: Enable 2-Factor Authentication
1. Go to your Google Account settings
2. Navigate to **Security** → **2-Step Verification**
3. Enable 2-Step Verification if not already enabled

### Step 2: Generate App Password
1. Go to Google Account settings
2. Navigate to **Security** → **App passwords**
3. Select **Mail** and **Other (custom name)**
4. Enter "FormLog" as the app name
5. Copy the 16-character app password (e.g., `abcd efgh ijkl mnop`)

### Step 3: Configure Environment Variables
Edit the `backend/.env` file and add your credentials:

```env
# Email Configuration
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-gmail@gmail.com
SMTP_PASSWORD=abcd efgh ijkl mnop
RECIPIENT_EMAIL=pietrodelfranco00@gmail.com
```

**Important:** 
- Use your full Gmail address for `SMTP_USERNAME`
- Use the 16-character App Password (not your regular password)
- Remove spaces from the app password

## 🧪 Testing Email Configuration

1. **Start the backend server:**
   ```bash
   cd backend
   python main.py
   ```

2. **Submit a test form:**
   ```bash
   curl -X POST http://localhost:8000/api/contacts \
     -H "Content-Type: application/json" \
     -d '{
       "name": "Test User",
       "email": "test@example.com", 
       "message": "This is a test email notification"
     }'
   ```

3. **Check the logs** for email status:
   - ✅ Success: "Email notification sent successfully"
   - ⚠️ Warning: "SMTP credentials not configured"
   - ❌ Error: "Failed to send email notification"

## 📧 Email Template

The notification email includes:
- **Subject:** "🔔 New Contact Form Submission - FormLog"
- **Content:** Beautiful HTML template with:
  - Sender's name and email
  - Submission timestamp
  - Full message content
  - Professional styling

## 🔒 Security Notes

- ✅ App passwords are safer than regular passwords
- ✅ Credentials are stored in environment variables
- ✅ Email sending runs asynchronously (doesn't slow down form submission)
- ⚠️ Never commit `.env` file to version control

## 🚨 Troubleshooting

### "Authentication failed"
- Double-check your Gmail address and app password
- Ensure 2-Factor Authentication is enabled
- Verify the app password is correct (16 characters, no spaces)

### "Connection refused"
- Check your internet connection
- Verify SMTP server and port (smtp.gmail.com:587)
- Some networks block SMTP traffic

### "SMTP credentials not configured"
- Make sure the `.env` file exists in the `backend/` folder
- Verify `SMTP_USERNAME` and `SMTP_PASSWORD` are set
- Restart the backend server after changing `.env`

## 🔄 Alternative Email Services

If Gmail doesn't work, you can use other SMTP services:

### SendGrid
```env
SMTP_SERVER=smtp.sendgrid.net
SMTP_PORT=587
SMTP_USERNAME=apikey
SMTP_PASSWORD=your-sendgrid-api-key
```

### Outlook/Hotmail
```env
SMTP_SERVER=smtp-mail.outlook.com
SMTP_PORT=587
SMTP_USERNAME=your-email@outlook.com
SMTP_PASSWORD=your-password
```

---

**💡 Pro Tip:** Test the email configuration with a simple contact form submission before going live!
