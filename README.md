# One-Way Camera Streaming using Python

This project demonstrates a simple one-way camera streaming application using Python and the VidStream library. 
It allows one device to stream its camera feed while another device views the live video over a local network (LAN).

## Features
- Live camera streaming over LAN
- Uses VidStream and threading

## Installation
`pip install vidstream`

## Requirements
- Python 3.10
- vidstream
- Devices connected on the same network

## How to Run
1. Start the streaming server on the camera device.
2. Update the server IP address in the client code.
3. Run the script to view the live camera feed.
4. Type `STOP` to end streaming.

## Note
This project supports **one-way video streaming only**. It does not provide two-way video calling.
