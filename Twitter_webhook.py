import requests
import json

webhook_url = 'https://discordapp.com/api/webhooks/************'

main_content = {
  "username": "Twitter通知BOT",
  "avatar_url": "https://img.icons8.com/color/452/twitter--v1.png",
  "content": "新しい投稿です！(@Call56S)",
  "embeds": [
    {
      "author": {
        "name": "Birdie♫",
        "url": "https://www.reddit.com/r/cats/",
        "icon_url": "https://i.imgur.com/R66g1Pe.jpg"
      },
      "title": "Title",
      "url": "https://google.com/",
      "description": "yey",
      "color": 15258703,
      "fields": [
        {
          "name": "Text",
          "value": "More text",
          "inline": True
        },
        {
          "name": "yey",
          "value": "yey",
          "inline": True
        },
        {
          "name": "Use `\"inline\": true` parameter, if you want to display fields in the same line.",
          "value": "ok"
        },
        {
          "name": "nyanya!",
          "value": "うにゃ"
        }
      ],
      "footer": {
        "text": "うにゃ",
        "icon_url": "https://img.icons8.com/color/452/twitter--v1.png"
      }
    }
  ]
}


requests.post(webhook_url,json.dumps(main_content),headers={'Content-Type': 'application/json'})
