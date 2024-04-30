# IDM-Compatible Download Server

This project provides a simple and efficient solution to set up a download server on your Virtual Private Server (VPS). It is specifically optimized for use with Internet Download Manager (IDM) to enable fast and reliable file downloads. By supporting HTTP range requests, the server facilitates IDM's ability to download files in segments, enhancing download speeds significantly.

## Features

- **HTTP Range Requests**: Supports partial content delivery, allowing IDM to download files in concurrent segments.
- **Easy Integration**: Simple setup on any VPS running a Python environment.
- **Efficiency**: Optimized to handle large file transfers with minimal memory overhead.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.6+
- FastAPI
- Uvicorn

You can install FastAPI and Uvicorn using pip:

```bash
pip install fastapi uvicorn
```
### Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/idm-compatible-download-server.git
cd idm-compatible-download-server
```

### Usage

Start the server by running:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Now, your server is ready to handle download requests. Navigate to:

http://<server-ip>:8000/df/


Replace `<server-ip>` with the IP address of your server. Use IDM to start downloading the file by specifying the above URL.


