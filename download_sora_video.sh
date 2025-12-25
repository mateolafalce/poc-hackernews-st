#!/bin/bash

if [ -z "$1" ]; then
    echo "Error: You must provide the VIDEO_ID"
    echo "Usage: $0 <VIDEO_ID>"
    echo "Example: $0 video_694be2f087e881988b3d1e68967f72e5083bb23c1d98b598"
    exit 1
fi

VIDEO_ID="$1"
OUTPUT_FILE="sora_video_$(date +%Y%m%d_%H%M%S).mp4"

if [ -f "../.env" ]; then
    export $(grep -v '^#' ../.env | xargs)
elif [ -f ".env" ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "Error: .env file not found"
    exit 1
fi

if [ -z "$OPENAI_API_KEY" ]; then
    echo "Error: OPENAI_API_KEY is not defined in .env"
    exit 1
fi

echo "Downloading video: $VIDEO_ID"
echo "Saving to: ./articles_html/$OUTPUT_FILE"

curl -X GET "https://api.openai.com/v1/videos/$VIDEO_ID/content" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -o "./articles_html/$OUTPUT_FILE" \
  --progress-bar

if [ $? -eq 0 ]; then
    FILE_SIZE=$(du -h "../articles_html/$OUTPUT_FILE" | cut -f1)
    echo ""
    echo " Video downloaded successfully!"
    echo "  File: ../articles_html/$OUTPUT_FILE"
    echo "  Size: $FILE_SIZE"
else
    echo ""
    echo " Error downloading video"
    exit 1
fi
