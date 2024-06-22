import pandas as pd
import random
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# Read the CSV file into a DataFrame
df = pd.read_csv('data.csv')

# Access data in the DataFrame using column names or indexing

print(df.iloc[0]["headword"])  # Access first row
i = 0
word = []
while i < 5:
    a = random.randint(0,7799)
    word.append(str(a))
    i = i + 1 

print(word)



sender_email = "englishwordslearning@hotmail.com"
receiver_email = "enesbayraktar15@gmail.com"
password = "learnenglishword_pass?q=idon'tknow"

message = MIMEMultipart("alternative")
message["Subject"] = "İngilizce Kelimelerin"
message["From"] = sender_email
message["To"] = receiver_email

# Create the plain-text and HTML version of your message
text = """\
Bugünkü ingilizce kelimelerin işte burada:"""
html = f"""\
<html>
    <head>
        <meta charset="UTF-8">
        <style>
            table, th, td {{
                border: 2px solid blue;
                border-collapse: collapse;
                padding: 15px;
            }}
        </style>
    </head>
    <body style="padding: 0; margin: 0; font-family: Arial, Helvetica, sans-serif;">
        <div style="margin-top: 0; margin-left: 0; margin-right: 0; height: 20vh; background-color: blue; color: white; ">
            <span style="font-size: 50px; margin-bottom: 0;">Your English Word</span>
        </div>
        <table style="width:70%; font-size: 36px; margin-left: 10vw; margin-top: 10vh;">
            <tr>
                <th>Word</th>
                <th>Pos</th>
                <th>CEFR</th>
            </tr>
            <tr>
                <td>{df.iloc[int(word[0])]["headword"]}</td>
                <td>{df.iloc[int(word[0])]["pos"]}</td>
                <td>{df.iloc[int(word[0])]["CEFR"]}</td>
            </tr>
            <tr>
                <td>{df.iloc[int(word[1])]["headword"]}</td>
                <td>{df.iloc[int(word[1])]["pos"]}</td>
                <td>{df.iloc[int(word[1])]["CEFR"]}</td>
            </tr>
            <tr>
                <td>{df.iloc[int(word[2])]["headword"]}</td>
                <td>{df.iloc[int(word[2])]["pos"]}</td>
                <td>{df.iloc[int(word[2])]["CEFR"]}</td>
            </tr>
            <tr>
                <td>{df.iloc[int(word[3])]["headword"]}</td>
                <td>{df.iloc[int(word[3])]["pos"]}</td>
                <td>{df.iloc[int(word[3])]["CEFR"]}</td>
            </tr>
            <tr>
                <td>{df.iloc[int(word[4])]["headword"]}</td>
                <td>{df.iloc[int(word[4])]["pos"]}</td>
                <td>{df.iloc[int(word[4])]["CEFR"]}</td>
            </tr>
        </table>
    </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

# Create secure connection with server and send email
context = ssl.create_default_context()
server = smtplib.SMTP("smtp.office365.com", 587) 
server.ehlo()
server.starttls()
server.ehlo()
server.login(sender_email, password)
    
server.sendmail(
    sender_email, receiver_email, message.as_string()
)
server.quit()
