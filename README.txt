Name: Wanli Qian Email: wqian39@gatech.edu
CS3251, 2020 9.23 PA1

PA1/
README.txt  -description of the project and semantics of implementation
Sample.txt  -list of test scenarios and correlating commands and outputs
ttweetcl.py -client side of simple tweet application
ttweetsrv.py -server side of simple tweet application

Instructions for running client and server programs:
1.unzip the PA1.zip zipfile,
2.open up command line, note that this program uses argparse to do commandline parsing if you don't have argparse module for your python, install it with "pip install argparse"
3.go under the directory of PA1, which contains ttweetcl.py and ttweetsrv.py
4.Now setup the server by following the command usage
python ttweetsrv.py [-h] ServerPort     For example: python ttweetsrv.py 13500
5.Once you see the message "Server Starts at (the port number you entered)", you can start another terminal(under same directory) and use the client side
6. To use the client side, you must follow the below command format
python ttweetcl.py [-h] (-u | -d) [-m M] ServerIP ServerPort
For example: for download mode: python ttweetcl.py -d 127.0.0.1 13500
             for upload mode: python ttweetcl.py -u -m 'hi' 127.0.0.1 13500 or
                              python ttweetcl.py -u 127.0.0.1 13500 -m 'hi'

note that you can put -m 'message' at any place just make sure that your intended message follows -m, and
since we are on localhost, we only accept 127.0.0.1 or 0.0.0.0 as serverIP, otherwise programs is going to have an error
and the server port its best to enter values between 13000 and 14000, the program is going to have an error when it is less than 1000 or greater than 65535
Finally message length can't be longer than 150

output sample: please refer to the Sample.txt for the list of scenarios and their corresponding commands and outputs

Once the server is started, it will enter an infinite loop to receive messages that client sent us
For the client side, we first assign '-u' or '-d' to upload message according to the client modes,
this is going to help server know which mode the client is in. In the '-u' case we append the message immediately after '-u'
So '-d' for download mode, '-u(tweetcontent)' for upload mode
Then we send this encoded message to server
The server knows how to respond by first read the first two characters of the decoded message
if first two character is '-u' then we send the client a success message 'Upload Successful' then update the buffer with the rest of client message to store the updated tweet content
if first two character is '-d' then we send the client of the buffer content
After the content is sent to client, close the connection between client socket and server socket
The client then format the message according to client modes then display the message
Finally close the client socket

no known bugs or limitations