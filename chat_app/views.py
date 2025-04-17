from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
import requests
import base64
import openai


openai.api_key = "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"




class ImageUploadSerializer(APIView):
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





# class DiagnoseSkinAPIView(APIView):
#     def post(self, request):
#         serializer = ImageUploadSerializer(data=request.data)
#         if serializer.is_valid():
#             prompt = "Sen ko'rib turgan rasmdagi inson terisining muammosi bormi? Agar bor bo'lsa u qanday muammo bu haqida batafsil aytib ber, hamda bu muammoni bartaraf etish uchun nimalar qilish mumkinligini aytib ber!"
#             image = serializer.validated_data['image']
#
#             # Rasmni base64 formatga o‘tkazish
#             base64_image = base64.b64encode(image.read()).decode('utf-8')
#
#             try:
#                 # OpenAI API so‘rovi
#                 response = openai.chat.completions.create(
#                     model="gpt-4o",
#                     messages=[
#                         {
#                             "role": "user",
#                             "content": [
#                                 {"type": "text", "text": prompt},
#                                 {
#                                     "type": "image_url",
#                                     "image_url": {
#                                         "url": f"data:image/jpeg;base64,{base64_image}"
#                                     }
#                                 }
#                             ]
#                         }
#                     ],
#                     max_tokens=500
#                 )
#
#                 result = response.choices[0].message.content
#                 return Response({"result": result}, status=status.HTTP_200_OK)
#
#             except Exception as e:
#                 return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
