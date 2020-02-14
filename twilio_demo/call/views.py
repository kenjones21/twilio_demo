from rest_framework.decorators import api_view
from twilio.twiml.voice_response import VoiceResponse
from django.http import HttpResponse

# Create your views here.
@api_view(['GET', 'POST'])
def answer_call(request):
    resp = VoiceResponse()
    resp.say('Fuck the law they can eat my dick thats word the pimp')
    print(str(resp))
    return HttpResponse(str(resp), content_type='text/xml')
