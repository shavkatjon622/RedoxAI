from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
import requests
import base64

class DiagnoseSkinAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            image = serializer.validated_data['image']

            # 🔽 Rasmni base64 formatga o‘girish (ba'zi API lar shuni talab qiladi)
            image_data = image.read()
            base64_image = base64.b64encode(image_data).decode('utf-8')

            # ⚠️ Bu yerda siz istagan tekin API chaqiriladi (quyida misol bor)
            # api_url = "https://api-inference.huggingface.co/models/mpwolke/skin-diseases"
            # headers = {
            #     "Authorization": f"Bearer YOUR_HUGGINGFACE_TOKEN",  # Agar kerak bo‘lsa
            #     "Content-Type": "application/json"
            # }
            # payload = {
            #     "inputs": base64_image
            # }
            #
            # response = requests.post(api_url, headers=headers, json=payload)

            # if response.status_code == 200:
            #     result = response.json()
            #     return Response({"diagnosis": result}, status=200)
            # else:
            #     return Response({"error": "Model API ishlamadi"}, status=500)
            result = {
                        "id": "chatcmpl-1234567890",
                        "object": "chat.completion",
                        "created": 1699999999,
                        "model": "gpt-3.5-turbo",
                        "choices": [
                                {
                                    "index": 0,
                                    "message": {
                                        "role": "assistant",
                                        "content": "Test qilamiz nima bolyapti ekan?"
                                    },
                                    "finish_reason": "stop"
                                }
                                ],
                        "usage": {
                                "prompt_tokens": 9,
                                "completion_tokens": 13,
                                "total_tokens": 22
                            }
                    }

            return Response({"diagnosis" : result}, status=200)


        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
