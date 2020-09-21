from socket import *
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(description= 'minitweet client side')
    mul = parser.add_mutually_exclusive_group(required = True)
    mul.add_argument('-u',action="store_true")
    mul.add_argument('-d',action="store_true")
    parser.add_argument('ServerIP', type = str)
    parser.add_argument('ServerPort', type = int)


    parser.add_argument('-m', type = str, required = '-u' in sys.argv)
    parser.set_defaults(func=run)
    args = parser.parse_args()

    args.func(args)


def run(args):
    try:
        IP = inet_aton(sys.argv[2])
        serverIP = str(sys.argv[2])
    except:
        print("Error, invalid server ip")
        exit()

    try:
        #print(sys.argv)
        serverPort = int(sys.argv[3])

        if serverPort < 1000 or serverPort > 65535:
            raise ValueError

        message = sys.argv[1]
        if message == "-u":
            if len(sys.argv[5]) > 150:
                raise ValueError
            else:
                message = message + sys.argv[5]

        clientSocket = socket(AF_INET, SOCK_STREAM)
        clientSocket.settimeout(5)
        clientSocket.connect((serverIP, serverPort))
        sentence = message
        clientSocket.send(sentence.encode())
        serverMsg = clientSocket.recv(1024)
        if sys.argv[1] == 'u':
            print("\""+serverMsg.decode()+"\"")
        else:
            print(serverMsg.decode())
        clientSocket.close()
    except ConnectionRefusedError:
        print("Error Message: Server Not Found")
        exit()
    except ValueError:
        print("message length over 150 limit")
        exit()

if __name__=="__main__":
	main()