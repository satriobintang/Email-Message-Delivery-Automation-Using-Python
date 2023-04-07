<p align="center">
  <h2 align="center" style="margin-top: -4px !important;">Email Message Delivery Automation Using Python</h2>
  <p align="center">
    <a href="https://www.python.org/">
    	<img src="https://img.shields.io/badge/python-v3.8-informational">
    </a>
  </p>
</p>


## Requirements:
To run Email Message Delivery Automation, you'll need to have Python and some python pips installed on your system. You can install the necessary requirements using pip:
```
pip install xlrd
pip install email
pip install smtplib
```


## Requirements File:
To run Email Message Delivery Automation, you'll need to have Python and some python pips installed on your system. You can install the necessary requirements using pip:
1. email_account_recipient.xls (contains the recipient's e-mail)
2. message.txt (Contains the text message to be sent)
3. Some document attachments (Optional)


## How to Use:
To use Email Message Delivery Automation, simply download the repository and make edits to **email_sender** and **password_sender**. After editing, the file is ready to be executed

**Activate 2 step verification on the sender's google account**
> I took this gif from the video https://www.youtube.com/@ThePyCoach
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/Enable 2 step verification.gif">
</p>

**Activate app passwords in google account**
> I took this gif from the video https://www.youtube.com/@ThePyCoach
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/Use app passwords in google account.gif">
</p>

Edit the **email_sender** and **password_sender** values ​​in the python code automate_message_email.py
**Activate app passwords in google account**
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/user_credential_settings.png">
</p>

Enter the message sentence that will be sent into the file **message.txt**. Below is an example of the message I will send.
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/sample_message_file_contents.png">
</p>

Make sure the recipient's email has been entered into the excel file **email_account_recipient.xls**. Make sure the email is in the first column.
> The position of the recipient email column in the excel file can be adjusted by editing line 28 in the automate_message_email.py python file
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/column_location.png">
</p>

Make sure the name of the file or attachment to be sent matches yours. Whether it's jpg, png, pdf, doc, excel, and others.
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/attachment_name.png">
</p>

Make sure all existing files such as **email_account_recipient.xls**, **message.txt**,**automate_message_email.py** and **file attachments** are in one directory.
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/location_all_file.png">
</p>

After everything is correct, the python file can be executed. The output if the message is successfully sent will be as below.
<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/message_successful_sent.png">
</p>


## Execution:
1.  Clone this repository using
```
https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python
```
**OR**
- Zip Download the Repository and Extract it's contents.
2.  Now run the [Email Message Delivery Automation](https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python) file directly in your Terminal using
```
python automate_message_email.py
```
**OR**
```
python3 automate_message_email.py
```


## Possible Errors That Will Occur:
1.  Error due to incorrect **User Credential**
Make sure **email_sender** and **password_sender** values ​​in the python code are correct.

<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/error_user_credential.png">
</p>

2.  Error due to incorrect **File Name**
Make sure **file name** values ​​in the python code are correct.

<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/error_file_name_incorrect.png">
</p>

3.  Error due to unsupported files
Make sure **email_account_recipient** is in .xls file format.

<p align="center">
	<img src="https://github.com/satriobintang/Email-Message-Delivery-Automation-Using-Python/blob/main/ImageContent/xlsx_not_supported.png">
</p>