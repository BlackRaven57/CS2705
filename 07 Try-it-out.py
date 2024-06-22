import requests

## 1 & 2 ##
# Connect
r = requests.get("http://icarus.cs.weber.edu/~dweidman/CS2705HTMLLab.html")
# Status Code
print()
print("The status code returned is: ")
output = r. status_code
print(output)
# Complete Header
output = r.headers
print()
print("The HEAD command returns the header information. This is the header information: ")
print(output)
# Content Length
output = r.headers["Content-Length"]
print()
print("The length of the data in the web page is: ")
print(output)
# Content Encoding
output = r.headers["Content-encoding"]
print()
print("The content encoding is: ")
print(output)
# Last Modified
output = r.headers['last-modified']
print()
print("The web page was last modified on: ")
print(output)
# Current Date
output = r.headers["Date"]
print()
print("The current date is: ")
print(output)
# Server Info
output = r.headers["Server"]
print()
print("The type of server for the web server and the version is: ")
print(output)
# HTML Coding
output = r.text
print()
print("The HTML coding of the web page is as follows: ")
print(output)


## 3 & 4 ##
# Connect
r = requests.get("http://icarus.cs.weber.edu/~dweidman/CS2705HTMLLab2.html")
# Status Code
print()
print("The status code returned is: ")
output = r. status_code
print(output)
# Complete Header
output = r.headers
print()
print("The HEAD command returns the header information. This is the header information: ")
print(output)
# Content Length
output = r.headers["Content-Length"]
print()
print("The length of the data in the web page is: ")
print(output)
# Content Encoding
output = r.headers["Content-encoding"]
print()
print("The content encoding is: ")
print(output)
# Last Modified
output = r.headers['last-modified']
print()
print("The web page was last modified on: ")
print(output)
# Current Date
output = r.headers["Date"]
print()
print("The current date is: ")
print(output)
# Server Info
output = r.headers["Server"]
print()
print("The type of server for the web server and the version is: ")
print(output)
# HTML Coding
output = r.text
print()
print("The HTML coding of the web page is as follows: ")
print(output)

# 5
print()
print("The HEAD command prints out the Header and what is in the Header whereas the GET command gives you a little view of the webpage.")

# 6
print()
print("The content type is needed in the Header because it helps specifiy to computers/devices accessing the page what types need to be supported or 'dealt with.'")

# 7
print()
print("In simplier terms there were quite a few differences in the HTML coding of the page (as it is a different page) and there were a couple different values in the header which were cool to compare between.")
