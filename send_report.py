import smtplib
from email.message import EmailMessage

# --- Email Server Configuration ---
smtp_server = 'smtp.gmail.com'
smtp_port = 587
sender_email = 'emailnanditasingh@gmail.com'
sender_password = 'uofd adkz elkd bnnv'  
receiver_email = 'sumeet.kumar@nexxbase.com'

# --- Allure Report Link ---
report_link = 'https://drive.google.com/file/d/11IL96KU2GeAMkVTnu0Vvtzvl3DPUeJNt/view?usp=sharing'

# --- Email Content ---
msg = EmailMessage()
msg['Subject'] = 'Automation Test Report'
msg['From'] = sender_email
msg['To'] = receiver_email

# Plain-text fallback
msg.set_content(f'''Hi,

Please find the automation test report at the link below:

{report_link}

Regards,
Nandita Singh
''')

# HTML version with styled button/bar
msg.add_alternative(f"""\
<html>
  <body>
    <p>Hi,<br><br>
       Please find the automation test report below:<br><br>
       <a href="{report_link}" style="
           display:inline-block;
           padding: 10px 20px;
           background-color:#4CAF50;
           color:white;
           text-decoration:none;
           font-weight:bold;
           border-radius:5px;
       ">📥 Download Report</a><br><br>
       Regards,<br>
       Nandita Singh
    </p>
  </body>
</html>
""", subtype='html')

# --- Send Email ---
try:
    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

        # ✅ Confirmation message in terminal
        print("\n✅ Email sent successfully!")
        print("📧 Your Allure automation report has been sent to:", receiver_email)
        print("🔗 Link to report:", report_link)

except Exception as e:
    print(f"\n❌ Failed to send email: {e}")
