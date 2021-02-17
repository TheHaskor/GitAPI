# GitAPI
Python webservice to get all branches from Git - even with pagination and authentication

For when you need all branches from github and the API only gets you 100 per page.
This JSON webservice combine all pages into a nice format.

How to use:
1) in client.py change the token to your Github token.
2) run the server.py

After running the server you can simply (in cmd):
curl -H "repo:<enter repo name>" localhost:8008
to get all branches :)
  
  
