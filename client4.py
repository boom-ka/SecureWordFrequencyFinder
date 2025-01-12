from socket import *
import ssl

serverName = "localhost"
serverPort = 12000

# Create an SSL context for the client
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE

try:
    # Establish a connection to the server using SSL
    with socket(AF_INET, SOCK_STREAM) as clientSocket:
        with ssl_context.wrap_socket(clientSocket, server_hostname=serverName) as secure_socket:
            secure_socket.connect((serverName, serverPort))

            sentence = input("Input sentence: ")
            word = input("Input word to be found: ")

            secure_socket.send(sentence.encode())
            secure_socket.send(word.encode())

            modifiedSentence = secure_socket.recv(1024)
            print("From Server:", modifiedSentence.decode())

except Exception as e:
    print(f"Error: {e}")
