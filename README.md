# Mailing Client

This script is used to send emails from a Python environment, allowing you to customize your message content and attachments easily. Whether you need to send reports, notifications, or any other form of communication, this script will help you automate the process. The script loads email credentials securely from an `.env` file to ensure that sensitive data like email addresses and passwords are not hardcoded.

### Features:

* **Secure Authentication**: Loads email credentials from an `.env` file.
* **Customizable Message**: Reads the email body from a text file.
* **File Attachments**: Allows sending image files as attachments.
* **SSL Encryption**: Uses `SMTP_SSL` to ensure the security of your connection while sending the email.

### How it Works:

1. **Environment Variables**: The script starts by loading email credentials from the `credentials.env` file using the `dotenv` package.
2. **Email Configuration**: The script sets up the subject, sender, and receiver for the email. It reads the body of the message from a text file and attaches it to the email. You can create text file in the same directory as the script or give the path of the text file. If you want to give the path of the text file, you need to make the guven changes in the code:

   ```python
   message = 'path/to/your/message.txt'
  
   with open(message, 'r') as f:
        send_message = f.read()

   msg.attach(MIMEText(send_message, 'plain'))
   ```
   
4. **Attachment**: An image file (or any other file) is attached by reading it in binary mode, encoding it in base64, and adding it to the email as a MIMEBase object.
5. **Sending the Email**: The email is sent through Gmail's SMTP server using a secure connection (`SMTP_SSL`), ensuring the integrity and privacy of your data.

### Requirements:

* Python 3.x
* `smtplib`
* `email.mime`
* `dotenv` (to load credentials from `.env` file)

### Installation

You’ll need to install the `python-dotenv` package if you haven’t already. You can do that by running:

```bash
pip install python-dotenv
```

### `.env` File Structure:

Make sure you create a `.env` file in the same directory as the script with the following structure:

```
EMAIL_ADDRESS=sender's_email@gmail.com
EMAIL_PASSWORD=sender's_email_password
TOADDR=recipient_email@gmail.com
```

### Example Usage:

1. Create a `.env` file with your credentials.
2. Create a text file (`message.txt`) with the content you want in the email body (if your text file is in the same directory as the script. if it's in a different location, amke the necessary modifications in code and specify the path of the text file)
3. Specify the path of the image you want to attach in the script.
4. Run the script:

```bash
python send_email.py
```

### Notes:

* Replace `SENDER` and `RECIEVER` in the `msg` header with the actual email addresses if needed, or use the variables set in the `.env` file. It is preferable to use Google App Passwords rather than the sender's real password to enhance security.
* Make sure the file path for the attachment is correctly specified, and ensure the file exists in the provided location.
* This script uses Gmail’s SMTP server. For other providers, update the SMTP server and port details accordingly.

### Troubleshooting:

* **Missing Credentials**: If you get an error related to missing credentials, check that your `.env` file is correctly set up with the necessary information.
* **Invalid Attachment Path**: Ensure that the file path you provide for the image attachment is correct.
* **Login Failure**: If the script fails to log in, check that you’ve enabled less secure apps or use an app-specific password if using two-factor authentication.
