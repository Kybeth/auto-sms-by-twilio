"""
This script uses the SMS service Twilio API provides.
It asks for the receiver's name, which should be a key in your contact dictionary.
It also asks for the content you want to send.

Author: Kybeth
"""

from twilio.rest import Client

contacts = {'Lisa':'+11111111111', 
            'Lindsey':'+12222222222', 
            'Kristina':'+13333333333'}
receiver = input('To whom you want to send: ')
client = Client("ACxxx", "www") #These two are your ACCOUNT SID and AUTH TOKEN shown on your twilio - Dashboard
client.messages.create(to='{}'.format(contacts[receiver]), 
                       from_="+10000000000",  # This should be the Active Numbers from your twilio - Phone Numbers - Manage Numbers
                       body='【{}】'.format(input('Type in your message: ')))