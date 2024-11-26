# DES Implementation

A Python implementation of the Data Encryption Standard (DES) algorithm. This project demonstrates how to encrypt and decrypt messages using DES, a symmetric-key block cipher. It also includes a Bash script to test the implementation and compare it with OpenSSL outputs.

## Features

- Implements DES encryption and decryption from scratch in Python.
- Handles key generation, initial/final permutations, expansion, S-box substitutions, P-box permutation, and XOR operations.
- Provides a `descheck.txt` Bash script for testing the functionality of the DES implementation and compares with OpenSSL DES encryption.
- Demonstrates encryption and decryption of messages with validation against OpenSSL results.
