# SecureWordFrequencyFinder
# Secure Word Frequency Finder

This repository contains a client-server application to securely find the frequency of a specific word in a given sentence. The communication between the client and the server is encrypted using SSL/TLS.

## Features
- **Secure Communication**: All communication between the client and the server is encrypted using SSL/TLS.
- **Word Frequency Analysis**: The server calculates the frequency of a word in a given sentence and sends the result back to the client.
- **Error Handling**: The application gracefully handles exceptions and provides meaningful error messages.

---

## Prerequisites

1. **Python**: Ensure Python 3.6+ is installed.
2. **SSL Certificate and Key**:
   - Generate an SSL certificate and private key for secure communication:
     ```bash
     openssl req -new -x509 -days 365 -nodes -out your_certificate.crt -keyout your_private_key.key
     ```
   - Replace `your_certificate.crt` and `your_private_key.key` in the server script with your certificate and key filenames.

---

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/secure-word-frequency-finder.git
   cd secure-word-frequency-finder
