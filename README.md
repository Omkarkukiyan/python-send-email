**Sending Emails With Python**

Modern python library for email.

Build message:

```
import emails
message = emails.html(html="<p>Hi!<br>Here is your receipt...",
                       subject="Your receipt No. 567098123",
                       mail_from=('Some Store', 'store@somestore.com'))
message.attach(data=open('bill.pdf', 'rb'), filename='bill.pdf')
```
send message and get response from smtp server:

```
r = message.send(to='s@lavr.me', smtp={'host': 'aspmx.l.google.com', 'timeout': 5})
assert r.status_code == 250
```

Documentation:[a link] https://python-emails.readthedocs.io/en/latest/