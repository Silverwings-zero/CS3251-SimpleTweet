from socket import *
import sys
import argparse

def run(args):
    serverPort = int(sys.argv[1])
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(("", serverPort))
    serverSocket.listen(1)
    print("ServerPort Starts at %s"%serverPort)
    buffer = ""
    while True:
        connectionSocket, address = serverSocket.accept()
        fromClient = connectionSocket.recv(1024).decode()
        if fromClient[0:2] == "-u":
            print('client upload mode, with upload message %s' %fromClient[2:])
            uploadSuccess = "Upload Successful"
            connectionSocket.send(uploadSuccess.encode())
            buffer = fromClient[2:]

        if fromClient[0:2] == "-d":
            print('client download mode')
            connectionSocket.send(buffer.encode())
        connectionSocket.close()



def main():
    parser = argparse.ArgumentParser(description= 'minitweet server side')
    parser.add_argument('serverPort', type=int)
    parser.set_defaults(func=run)
    args = parser.parse_args()
    args.func(args)

if __name__=="__main__":
	main()