import os
import pandas as pd
import urllib.parse
from googleapiclient.discovery import build
from dotenv import load_dotenv
import csv

# Cargar la API Key desde .env
load_dotenv()
API_KEY = os.getenv("API_KEY")

# Función para extraer el video ID de una URL
def extract_video_id(url):
    parsed_url = urllib.parse.urlparse(url)
    query_params = urllib.parse.parse_qs(parsed_url.query)
    return query_params.get("v", [None])[0]


# Función para obtener los detalles del video
def get_video_metadata(youtube, video_id):
    request = youtube.videos().list(
        part="snippet,statistics,contentDetails",
        id=video_id
    )
    response = request.execute()

    if not response.get("items"):
        return None

    video_data = response["items"][0]

    return {
        "id": video_id,
        "channel": video_data["snippet"]["channelTitle"],
        "title_video": video_data["snippet"]["title"],
        "tags": ", ".join(video_data["snippet"].get("tags", [])),
        "description": video_data["snippet"]["description"],
        "views": int(video_data["statistics"].get("viewCount", 0)),
        "likes": int(video_data["statistics"].get("likeCount", 0)),
        "comment_count": int(video_data["statistics"].get("commentCount", 0)),
        "duration": video_data["contentDetails"]["duration"]
    }


# Función para obtener y escribir comentarios directamente en CSV
def get_video_comments(youtube, video_id, output_file):
    next_page_token = None
    comment_index = 1

    # Escribir encabezados en el CSV
    with open(output_file, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["video_id", "comment_id", "comment", "comment_likes"])

        while True:
            request = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                maxResults=100,
                pageToken=next_page_token
            )
            response = request.execute()

            for item in response.get("items", []):
                comment_data = item["snippet"]["topLevelComment"]["snippet"]
                writer.writerow([
                    video_id,
                    comment_index,
                    comment_data["textDisplay"],
                    comment_data["likeCount"]
                ])
                comment_index += 1

            next_page_token = response.get("nextPageToken")
            if not next_page_token:
                break

# URL del video
video_url = ""

# Extraer ID del video
video_id = extract_video_id(video_url)

if video_id:
    youtube = build("youtube", "v3", developerKey=API_KEY)

    # Obtener metadata y guardar directamente en CSV sin usar DataFrame
    metadata = get_video_metadata(youtube, video_id)
    if metadata:
        with open("metadata_video.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=metadata.keys())
            writer.writeheader()
            writer.writerow(metadata)

    # Obtener comentarios y escribirlos en CSV directamente
    get_video_comments(youtube, video_id, "comments_video.csv")

    print("CSVs generados correctamente: metadata_video.csv y comments_video.csv")
else:
    print("Error: No se pudo extraer el video ID de la URL proporcionada.")
