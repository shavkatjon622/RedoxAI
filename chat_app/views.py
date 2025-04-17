from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ImageUploadSerializer
import requests
import base64
import openai


openai.api_key = "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"


class DiagnoseSkinAPIView(APIView):
    def post(self, request):
        serializer = ImageUploadSerializer(data=request.data)
        if serializer.is_valid():
            prompt = "Sen ko'rib turgan rasmdagi inson terisining muammosi bormi? Agar bor bo'lsa u qanday muammo bu haqida batafsil aytib ber, hamda bu muammoni bartaraf etish uchun nimalar qilish mumkinligini aytib ber!"
            image = serializer.validated_data['image']

            # Rasmni base64 formatga o‘tkazish
            base64_image = base64.b64encode(image.read()).decode('utf-8')

            try:
                result = {
                            "result": "Rasmda ko'rinib turgan muammo siğillar kabi ko'rinadi. Siğillar odatda inson papilloma virusi (HPV) tufayli paydo bo'ladi va terida o'sib chiqadi. Ular kosmetik noqulaylik keltirishi mumkin, lekin odatda zararli emas.\n\n**Muammoni bartaraf etish uchun tavsiyalar:**\n\n1. **Dori vositalari:**\n   - Siğillarni yo'qotish uchun dorixonalar o'zida salitsil kislotasi yoki boshqa keratolitik preparatlar taklif qiladi. Ularni qo'llashdan oldin isitma vannasi yordamida terini yumshatish foydali bo'lishi mumkin.\n\n2. **Kriyoterapiya:**\n   - Tibbiyot muassasalarida siğillarni muzlatib yo'qotish usuli mavjud. Bu jarayonni tajribali mutaxassis amalga oshiradi.\n\n3. **Lazer terapiyasi:**\n   - Lazer yordamida siğillarni yo'qotish usuli ham mavjud. Bu usul ko'pincha yanada samarali, lekin qimmatroq bo'lishi mumkin.\n\n4. **Elektrokoagulyatsiya:**\n   - Bu usulda elektr toki yordamida siğillarni yo'qotish amalga oshiriladi.\n\n5. **Doktorga murojaat qilish:**\n   - Agar siğillar kattalashsa, og'riq sezilsa yoki uzoq vaqt davomida yo'qolmasa, dermatologga murojaat qilish tavsiya etiladi.\n\nProfilaktika choralari sifatida gigiena qoidalariga rioya qilish, immunitetni mustahkamlash va HPV xavfini kamaytirish uchun emlash imkoniyatini ko'rib chiqish mumkin."
                        }
                return Response({"diagnosis": result}, status=200)

                return Response({"diagnosis": result}, status=200)
                # OpenAI API so‘rovi
                # response = openai.chat.completions.create(
                #     model="gpt-4o",
                #     messages=[
                #         {
                #             "role": "user",
                #             "content": [
                #                 {"type": "text", "text": prompt},
                #                 {
                #                     "type": "image_url",
                #                     "image_url": {
                #                         "url": f"data:image/jpeg;base64,{base64_image}"
                #                     }
                #                 }
                #             ]
                #         }
                #     ],
                #     max_tokens=500
                # )
                #
                # result = response.choices[0].message.content
                # return Response({"result": result}, status=status.HTTP_200_OK)

            except Exception as e:
                return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
