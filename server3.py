from socket import *
import ssl

def find_word_frequency(word, input_string):
    words = input_string.split()

    if word in words:
        frequency = words.count(word)
        return f"The word '{word}' is present in the string, and its frequency is {frequency}."
    else:
        return f"The word '{word}' is not found in the string."

# SSL setup
ssl_context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
ssl_context.load_cert_chain(certfile="your_certificate.crt", keyfile="your_private_key.key")

# Server socket setup
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(5)

# Wrap the socket with SSL
serverSocket = ssl_context.wrap_socket(serverSocket, server_side=True)

print("The server is ready to receive")


while True:
    connectionSocket, addr = serverSocket.accept()  
    print("the connection from ",addr)
    sentence = connectionSocket.recv(1024).decode()
    word = connectionSocket.recv(1024).decode()

    result = find_word_frequency(word, sentence)

    connectionSocket.send(result.encode())

    # Close the connection after sending the result
    connectionSocket.close()
