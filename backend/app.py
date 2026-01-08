# server.py

from flask import Flask, jsonify, request
from flask_cors import CORS
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
import re
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)
CORS(app) 

def normalize(name):
    return name.strip().upper()
CLUB_IMAGES = {
    normalize("FOSSCU"): "/assets/fosscu.webp",
    normalize("CREATIVE CELL"): "/assets/creative_cell.webp",
    normalize("DINOBOTS"): "/assets/dinobots.webp",
    normalize("E-CELL"): "/assets/e-cell.webp",
    normalize("GOOGLE DEVELOPER GROUPS"): "/assets/gdg_kiet.webp",
    normalize("INNOGEEKS"): "/assets/innogeeks.webp",
    normalize("KINESIS TECHNICAL SOCIETY"): "/assets/kts.webp",
    normalize("SAEKIET"): "/assets/saekiet.webp",
    normalize("VOID SOCIETY"): "/assets/void_society.webp",
    normalize("CP BYTE"): "/assets/CP_BYTE.webp",
    normalize("KIET MUSIC CLUB"): "/assets/Kiet_Music_club.webp",
    normalize("PRAGMATIC FASHION SOCIETY"): "/assets/Pragmatic_Fashion_Society.webp",
    normalize("KIET MOVIE SOCIETY"): "/assets/kiet_movie_society.webp",
    normalize("THE IMPECCABLES"): "/assets/impeccables.webp",
    normalize("KAVYANJALI"): "/assets/kavyanjali.webp",
    normalize("UDDESHHYA"): "/assets/Uddeshya.webp",
    normalize("NCC CLUB"): "/assets/NCC.webp",
    normalize("ODYSSEY"): "/assets/Odyssey.webp",
    normalize("STEPPERS DANCE CREW"): "/assets/SDC.webp",
}

@app.route("/api/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()
        user_prompt = data.get("prompt", "").strip()

        if not user_prompt:
            return jsonify({ "images": [], "clubs": [] })

        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash", # Changed to a standard stable version
            generation_config={
                "temperature": 0.2,
                "max_output_tokens": 300
            }
)

        internal_prompt = f"""
You are a recommendation engine for college clubs.
Based on the user's interest, select exactly 5 clubs from this list:
"FOSSCU", "CREATIVE CELL", "DINOBOTS", "E-CELL", "GOOGLE DEVELOPER GROUPS", "INNOGEEKS", 
"KINESIS TECHNICAL SOCIETY", "SAEKIET", "VOID SOCIETY", "CP BYTE", "KIET MUSIC CLUB", 
"PRAGMATIC FASHION SOCIETY", "KIET MOVIE SOCIETY", "THE IMPECCABLES", "KAVYANJALI", 
"UDDESHHYA", "NCC CLUB", "ODYSSEY", "STEPPERS DANCE CREW"

"FOSSCU": "Open Source, Linux, Git & Github, Blockchain development"
"CREATIVE CELL": "Creative Arts, Graphic Design, Content Writing",
"DINOBOTS": "Robotics & Automation, Electronics & Engineering, Competitive Technical Events, Innovation & Research",
"E-CELL": "Entrepreneurship, Event Management, Startup Promotion",
"GOOGLE DEVELOPER GROUPS": "Software Development, Emerging Google Technologies, Hackathons & Coding, Industry Readiness",
"INNOGEEKS": "Full-Stack Development, Open Source Contribution, National Hackathons, Innovation & Problem Solving",
"KINESIS TECHNICAL SOCIETY": "Web Development, Android Development, Machine Learning & AI, UI/UX Design, Competitive Programming",
"SAEKIET": "Mechanical Design, Automation production, Automobiles manufacturing",
"VOID SOCIETY": "Cybersecurity, Web3 & Blockchain development, Ethical Hacking",
"CP BYTE": "Competitive Programming & Coding, Web & Android Development, Machine Learning, Augmented Reality and Virtual Reality, Gen-AI, UI/UX",
"KIET MUSIC CLUB": "Instrumentalists, Vocalists, Producers, Rappers, Beatboxers",
"PRAGMATIC FASHION SOCIETY": "Runway Choreography, Thematic Productions, Garment Design, Professional Styling",
"KIET MOVIE SOCIETY": "Filmmaking, Direction, Cinematography, Scriptwriting, Post-production, Film Screenings",
"THE IMPECCABLES": "Creative Arts, Personality Development, Photography, Content Writing, Open Mic, Video Editing, Stand-up Comedy",
"KAVYANJALI": "Literary Organization, Multilingual, Kavi-Sammelans, Poetry, Hindi and Urdu Traditions",
"UDDESHHYA": "Student-run NGO, Underprivileged Welfare, Social Service, Living for a Reason",
"NCC CLUB": "Character, Courage, Discipline, Selfless Service, Community Engagement",
"ODYSSEY": "Communication Skills, Critical Thinking, Artistic Expression, LSRW Skills",
"STEPPERS DANCE CREW": "Contemporary, Hip-hop, Ballroom, Salsa, Rhythmic Expression"

User interest:
"{user_prompt}"

RULES:
1. Return ONLY a valid JSON array.
2. Do NOT use Markdown formatting (no ```json).
3. Do NOT add conversational text.
4. Example output: ["INNOGEEKS", "KIET MOVIE SOCIETY", "ODYSSEY"]
"""
        response = model.generate_content(internal_prompt)
        
        match = re.search(r'\[.*?\]', response.text, re.DOTALL)
        
        if not match:
            print("ERROR: No JSON list found in response:", response.text)
            return jsonify({ "images": [], "clubs": [] })

        json_str = match.group(0)
        clubs_raw = json.loads(json_str)

        clubs = [str(c).strip().upper() for c in clubs_raw]

        images = []
        valid_clubs = []
        
        for c in clubs:
            if c in CLUB_IMAGES:
                images.append(CLUB_IMAGES[c])
                valid_clubs.append(c)

        return jsonify({ "images": images, "clubs": valid_clubs })

    except Exception as e:
        print("ERROR:", e)
        return jsonify({ "images": [], "clubs": [] })


if __name__ == "__main__":
    app.run(debug=True, port=3000)
# # server.py

# from flask import Flask, jsonify, request
# from flask_cors import CORS
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os
# import json

# # Load environment variables
# load_dotenv()

# # Configure Gemini
# genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# # Create Flask app
# app = Flask(__name__)
# CORS(app)  # Allow browser requests

# CLUB_IMAGES = {
#     "FOSSCU": "/assets/fosscu.webp",
#     "CREATIVE CELL": "/assets/creative_cell.webp",
#     "DINOBOTS": "/assets/dinobots.webp",
#     "E-CELL": "/assets/e-cell.webp",
#     "GOOGLE DEVELOPER GROUPS": "/assets/gdg_kiet.webp",
#     "INNOGEEKS": "/assets/innogeeks.webp",
#     "KINESIS TECHNICAL SOCIETY": "/assets/kinesis.webp",
#     "SAEKIET": "/assets/saekiet.webp",
#     "VOID SOCIETY": "/assets/void_society.webp",
#     "CP BYTE": "/assets/CP_BYTE.webp",
#     "KIET MUSIC CLUB": "/assets/Kiet_Music_club.webp",
#     # "TEDxKIET": "/assets/TEDxKIET.webp",
#     "PRAGMATIC FASHION SOCIETY": "/assets/Pragmatic_Fashion_Society.webp",
#     "KIET MUSIC CLUB": "/assets/Kiet_Music_club.webp",
#     "THE IMPECCABLES": "/assets/impeccables.webp",
#     "KAVYANJALI": "/assets/kavyanjali.webp",
#     "UDDESHHYA": "/assets/Uddeshya.webp",
#     "NCC CLUB": "/assets/NCC.webp",
#     "ODYSSEY": "/assets/Odyssey.webp",
#     "STEPPERS DANCE CREW" : "/assets/SDC.webp",
#     "KINESIS TECHNICAL SOCIETY": "/assets/kts.webp",

# }

# def normalize(name):
#     return name.strip().upper()

# CLUB_IMAGES = {
#     normalize("FOSSCU"): "/assets/fosscu.webp",
#     normalize("CREATIVE CELL"): "/assets/creative_cell.webp",
#     normalize("DINOBOTS"): "/assets/dinobots.webp",
#     normalize("E-CELL"): "/assets/e-cell.webp",
#     normalize("GOOGLE DEVELOPER GROUPS"): "/assets/gdg_kiet.webp",
#     normalize("INNOGEEKS"): "/assets/innogeeks.webp",
#     normalize("KINESIS TECHNICAL SOCIETY"): "/assets/kts.webp",
#     normalize("SAEKIET"): "/assets/saekiet.webp",
#     normalize("VOID SOCIETY"): "/assets/void_society.webp",
#     normalize("CP BYTE"): "/assets/CP_BYTE.webp",
#     normalize("KIET MUSIC CLUB"): "/assets/Kiet_Music_club.webp",
#     # normalize("TEDxKIET"): "/assets/TEDxKIET.webp",
#     normalize("PRAGMATIC FASHION SOCIETY"): "/assets/Pragmatic_Fashion_Society.webp",
#     normalize("KIET MOVIE SOCIETY"): "/assets/kiet_movie_society.webp",
#     normalize("THE IMPECCABLES"): "/assets/impeccables.webp",
#     normalize("KAVYANJALI"): "/assets/kavyanjali.webp",
#     normalize("UDDESHHYA"): "/assets/Uddeshya.webp",
#     normalize("NCC CLUB"): "/assets/NCC.webp",
#     normalize("ODYSSEY"): "/assets/Odyssey.webp",
#     normalize("STEPPERS DANCE CREW"): "/assets/SDC.webp",
# }

# @app.route("/api/predict", methods=["POST"])
# def predict():
#     try:
#         data = request.get_json()
#         user_prompt = data.get("prompt", "").strip()

#         if not user_prompt:
#             # Return empty lists if no prompt provided
#             return jsonify({ "images": [], "clubs": [] })

#         model = genai.GenerativeModel(
#             model_name="gemini-2.5-flash",
#             generation_config={
#                 "temperature": 0.2,
#                 "max_output_tokens": 300
#             }
#         )

#         internal_prompt = f"""
# You are a recommendation engine.

# "FOSSCU": "Open Source, Linux, Git & Github, Blockchain development"
# "CREATIVE CELL": "Creative Arts, Graphic Design, Content Writing",
# "DINOBOTS": "Robotics & Automation, Electronics & Engineering, Competitive Technical Events, Innovation & Research",
# "E-CELL": "Entrepreneurship, Event Management, Startup Promotion",
# "GOOGLE DEVELOPER GROUPS": "Software Development, Emerging Google Technologies, Hackathons & Coding, Industry Readiness",
# "INNOGEEKS": "Full-Stack Development, Open Source Contribution, National Hackathons, Innovation & Problem Solving",
# "KINESIS TECHNICAL SOCIETY": "Web Development, Android Development, Machine Learning & AI, UI/UX Design, Competitive Programming",
# "SAEKIET": "Mechanical Design, Automation production, Automobiles manufacturing",
# "VOID SOCIETY": "Cybersecurity, Web3 & Blockchain development, Ethical Hacking",
# "CP BYTE": "Competitive Programming & Coding, Web & Android Development, Machine Learning, Augmented Reality and Virtual Reality, Gen-AI, UI/UX",
# "KIET MUSIC CLUB": "Instrumentalists, Vocalists, Producers, Rappers, Beatboxers",
# "PRAGMATIC FASHION SOCIETY": "Runway Choreography, Thematic Productions, Garment Design, Professional Styling",
# "KIET MOVIE SOCIETY": "Filmmaking, Direction, Cinematography, Scriptwriting, Post-production, Film Screenings",
# "THE IMPECCABLES": "Creative Arts, Personality Development, Photography, Content Writing, Open Mic, Video Editing, Stand-up Comedy",
# "KAVYANJALI": "Literary Organization, Multilingual, Kavi-Sammelans, Poetry, Hindi and Urdu Traditions",
# "UDDESHHYA": "Student-run NGO, Underprivileged Welfare, Social Service, Living for a Reason",
# "NCC CLUB": "Character, Courage, Discipline, Selfless Service, Community Engagement",
# "ODYSSEY": "Communication Skills, Critical Thinking, Artistic Expression, LSRW Skills",
# "STEPPERS DANCE CREW": "Contemporary, Hip-hop, Ballroom, Salsa, Rhythmic Expression"

# User interest:
# "{user_prompt}"

# Return ONLY a JSON array of STRICTLY 5 club names.
# Example:
# user_input ='I like drama and all I am not too good at coding I want a good base to start with. I also want to take part in debates, Donations and social work!'
# ["INNOGEEKS", "KIET MOVIE SOCIETY", "ODYSSEY", "UDDESHHYA", "KAVYANJALI"]
# """
#         response = model.generate_content(internal_prompt)
#         raw = response.text.strip()

#         # Robust JSON extraction: Find the first '[' and last ']'
#         start = raw.find("[")
#         end = raw.rfind("]") + 1 
        
#         if start == -1 or end == 0:
#             print("AI Response was not a valid array:", raw)
#             return jsonify({ "images": [], "clubs": [] })

#         # Parse the JSON string
#         clubs_raw = json.loads(raw[start:end])
        
#         # Normalize the names to match your CLUB_IMAGES keys (Uppercase)
#         clubs = [str(c).strip().upper() for c in clubs_raw]

#         # Fix: Map only if the club exists in your images dictionary
#         # Your original code: [CLUB_IMAGES[c] for c in clubs if c in clubs] 
#         # caused errors if a club name wasn't found in CLUB_IMAGES.
#         images = []
#         valid_clubs = []
#         for c in clubs:
#             if c in CLUB_IMAGES:
#                 images.append(CLUB_IMAGES[c])
#                 valid_clubs.append(c)
        
#         # Return the valid matches
#         return jsonify({ "images": images, "clubs": valid_clubs })
#     except Exception as e:
#         print("ERROR:", e)
#         return jsonify({ "images": [], "clubs": [] })


# if __name__ == "__main__":
#     app.run(debug=True, port=3000)
