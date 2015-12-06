#!/usr/bin/python
import boto.ses
import sys, getopt

AWS_ACCESS_KEY = '<access_key>'  
AWS_SECRET_KEY = '<secret>'

class Email(object):  
    def __init__(self, to, subject):
        self.to = to
        self.subject = subject
        self._html = None
        self._text = None
        self._format = 'html'

    def html(self, html):
        self._html = html

    def text(self, text):
        self._text = text

    def send(self, from_addr=None):
        body = self._html

        if isinstance(self.to, basestring):
            self.to = [self.to]
        if not from_addr:
            from_addr = 'me@example.com'
        if not self._html and not self._text:
            raise Exception('You must provide a text or html body.')
        if not self._html:
            self._format = 'text'
            body = self._text

        connection = boto.ses.connect_to_region(
            'us-east-1',
            aws_access_key_id=AWS_ACCESS_KEY, 
            aws_secret_access_key=AWS_SECRET_KEY
        )

        return connection.send_email(
            from_addr,
            self.subject,
            None,
            self.to,
            format=self._format,
            text_body=self._text,
            html_body=self._html
        )
        
opts, args = getopt.getopt(sys.argv[1:],"t:s:",["to=","subject="])
to = ''
subject = ''
froma = 'monitor@transparent-blue.com'
for opt, value in opts:
    if opt in ('-t', '--to'):
        to = value
    elif opt in ('-s', '--subject'):
        subject = value


body = sys.stdin.read()
email = Email(to=to, subject=subject)  
email.html('<html><body>' + body + '</body></html>')  # Optional  
email.send(froma)    
     
