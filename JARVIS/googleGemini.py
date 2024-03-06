#import requests
#import json
#import pyttsx3
#import speech_recognition
#import vertexai.preview
#from google.cloud import aiplatform
#
#engine = pyttsx3.init("sapi5")
#voices = engine.getProperty("voices")
#engine.setProperty("voice", voices[0].id)
#rate = engine.setProperty("rate", 170)
#
#def speak(audio):
#    engine.say(audio)
#    engine.runAndWait()
#    
#def takeCommand():
#    r = speech_recognition.Recognizer()
#    with speech_recognition.Microphone() as source:
#        print("Listening.....")
#        r.pause_threshold = 1
#        r.energy_threshold = 300
#        audio = r.listen(source,0,4)
#
#def answerQuestion():
#  """
#  Use the Google Gemini API to answer a user-provided question.
#  """
#  
#  # Capture user question
#  speak("ACTIVATED")
#  
#  question = takeCommand()
#  print(f"User question: {question}")
#
#  # Formulate prompt for Gemini
#  prompt = f"Answer the following question: {question}"
#
#  # Replace these with your actual values
#  project_id = "AIzaSyC4VWFrD4QAz4aNdOtTe1jN2YK1qzKpf6c"
#  model_version = "latest"
#
#  # Send request to Gemini API
#  from google.cloud import aiplatform
#  
#  client = aiplatform.gapic.PredictionServiceClient(project=project_id)
#
#  request = aiplatform.TextGenerationRequest(
#      content=prompt,
#      model_name=f"projects/{project_id}/locations/us-central1/models/{model_version}",
#  )
#
#  response = client.multimodal_generate_text(request=request)
#
#  # Process and present response
#  generated_text = response.text[0]
#  speak(f"Gemini's answer: {generated_text}")
#
#  # Optionally, add a confirmation or follow-up prompt

