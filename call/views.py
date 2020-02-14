from rest_framework.decorators import api_view
from twilio.twiml.voice_response import VoiceResponse
from django.http import HttpResponse

# Create your views here.
@api_view(['GET', 'POST'])
def answer_call(request):
    resp = VoiceResponse()
    resp.say('Glad Tom is finally seemingly off calls, I can enjoy the rest of the day in peace.')
    print(str(resp))
    return HttpResponse(str(resp), content_type='text/xml')
