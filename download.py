from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse
from starlette.responses import StreamingResponse
import os

app = FastAPI()

@app.get("/df")
def download_file(request: Request):
    file_path = "/home/admin111/serv.zip"  # Update the path to your file
    file_size = os.path.getsize(file_path)

    range_header = request.headers.get('range')
    if range_header:
        range_start, range_end, *_ = range_header.replace('bytes=', '').split('-')
        range_start = int(range_start)
        range_end = int(range_end) if range_end else file_size - 1

        if (range_start >= file_size or range_end >= file_size):
            return HTTPException(status_code=416, detail="Range Not Satisfiable")

        length = range_end + 1 - range_start
        with open(file_path, 'rb') as f:
            f.seek(range_start)
            data = f.read(length)
            return StreamingResponse(
                iter([data]), 
                media_type='application/octet-stream',
                status_code=206,
                headers={
                    'Content-Range': f'bytes {range_start}-{range_end}/{file_size}',
                    'Accept-Ranges': 'bytes'
                }
            )
    return FileResponse(file_path, filename="serv.zip", media_type='application/octet-stream')
