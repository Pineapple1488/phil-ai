import os
import google.auth
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

# Load credentials from JSON file
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
SERVICE_ACCOUNT_FILE = "phil_credentials.json"  # Update this with the correct file name

credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

youtube = build("youtube", "v3", credentials=credentials)

def upload_video(video_path, title, description, tags, category="22", privacy="public"):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": category,
            },
            "status": {
                "privacyStatus": privacy,
            },
        },
        media_body=MediaFileUpload(video_path, resumable=True),
    )
    response = request.execute()
    print(f"✅ Uploaded: {title} (Video ID: {response['id']})")

# Example Usage
if __name__ == "__main__":
    upload_video("example.mp4", "AI Money Moves", "Automated affiliate marketing video", ["AI", "Money", "Affiliate"])
