from fastapi import FastAPI, UploadFile, File
from fastapi.responses import Response
from rembg import remove
import uvicorn

app = FastAPI(title="Background Remover")

@app.post("/remove")
async def remove_background(file: UploadFile = File(...)):
    image_data = await file.read()
    output_data = remove(image_data)
    return Response(content=output_data, media_type="image/png")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
