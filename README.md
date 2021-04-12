# devops-wa
Sending a WhatsApp (WA) message for GitHub push

# 1 Google is your best friend!
Since I don't use Telegram, I decided to see if there was something out there for Whatsapp<br>
Found this from GitHub user <a href="https://github.com/ishween/whatsapp-push-notify-action">ishween</a>

# 2 What is going on?
Looked through her repo files to make sense of things<br>
Twilio is needed, so I signed up and looked up a few more articles, namely:<br>
<a href="https://www.twilio.com/blog/send-whatsapp-message-30-seconds-python">Send Whatsapp Message</a><br>
<a href="https://www.twilio.com/blog/how-to-send-whatsapp-media-messages-with-python">How to Send Whatsapp Media Messages</a>

# 3 Can I do this?
Her code is quite similar to the Twilio "How To" articles<br>
So I figure instead of using her code I can try following the article<br>

Create my folders<br>
![](folder.jpg)<br>

I get stuck at the Python part<br>
Unable to activate the virtual environment<br>
![](powershell.jpg)<br>

I push ahead<br>
Setup environment variables<br>
![](envvar.jpg)<br>

Run python whatsapp.py<br>
Nothing happens<br>
![](powershell2.jpg)<br>

Try it out on GitHub anyway<br>
Commit change<br>
Running stops at "whatsapp-notify" and no message is received<br>
![](actions.jpg)<br>

# 4 Failure
After 4 hours of abject failure<br>
I am back to square 1<br>
Using her code<br>
It works

# 5 Follow the instructions

![](ishween.jpg)<br>

Sign up for Twilio and create 3 secrets in GitHub repo<br>

![](twilio.jpg)<br>
![](secrets.jpg)<br>
![](secrets2.jpg)<br>

Add a new file and commit changes<br>
Wait for new WhatsApp message!<br>
Success!<br>

![](whatsapp.jpg)
