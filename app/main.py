import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import StreamingResponse
import io

from app.voice import speech_to_text, text_to_speech
from app.nlp import extract_intent
from app.business_logic import generate_response

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to the AI Voice and Text Interaction API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/voice-input")
async def voice_input(file_upload: UploadFile = File(...)):
    logger.info(f"Received file: {file_upload.filename}")
    logger.info(f"File content type: {file_upload.content_type}")

    if file_upload.content_type not in ["audio/wav", "audio/mpeg"]:
        raise HTTPException(status_code=400, detail="Invalid file type")

    audio_bytes = await file_upload.read()
    logger.info(f"File size: {len(audio_bytes)} bytes")

    try:
        text = speech_to_text(audio_bytes)
        logger.info(f"Transcribed text: {text}")
    except Exception as e:
        logger.error(f"Error during speech-to-text conversion: {e}")
        raise HTTPException(status_code=500, detail="Error during speech-to-text conversion")

    try:
        intent = extract_intent(text)
        response_text = generate_response(intent, text)
        response_audio = text_to_speech(response_text)
    except Exception as e:
        logger.error(f"Error during text-to-speech conversion: {e}")
        raise HTTPException(status_code=500, detail="Error during text-to-speech conversion")

    return StreamingResponse(io.BytesIO(response_audio), media_type="audio/wav")

@app.post("/api/text-input")
async def text_input(input_data: dict):
    text = input_data.get("input")
    if not text:
        raise HTTPException(status_code=400, detail="No input text provided")

    try:
        intent = extract_intent(text)
        response_text = generate_response(intent, text)
    except Exception as e:
        logger.error(f"Error during text input processing: {e}")
        raise HTTPException(status_code=500, detail="Error during text input processing")

    return {"response": response_text}