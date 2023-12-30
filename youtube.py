import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from googleapiclient.http import MediaFileUpload

scopes = ["https://www.googleapis.com/auth/youtube.upload"]


def main():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "./google.json"

    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file, scopes
    )
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "description": "#staycozy  #cozycoregear #winterwardrobe  #linkinbio  #buynowwearnow #tiktokmademebuyit #selfheatingjacket #winter #fyp #winterbuys #christmas #christmasgifts",
                "title": "Buy yours now at cozycore.com!!! link in bio.",
            },
            "status": {"privacyStatus": "public", "selfDeclaredMadeForKids": False},
        },
        # TODO: For this request to work, you must replace "YOUR_FILE"
        #       with a pointer to the actual file you are uploading.
        media_body=MediaFileUpload("./test_File.mp4"),
    )
    response = request.execute()


if __name__ == "__main__":
    main()