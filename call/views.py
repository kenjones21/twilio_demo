from rest_framework.decorators import api_view
from twilio.twiml.voice_response import VoiceResponse
from twilio.jwt.client import ClientCapabilityToken
from django.http import HttpResponse

from twilio_rest import settings

# Create your views here.
@api_view(['GET', 'POST'])
def answer_call(request):
    resp = VoiceResponse()
    resp.say('Glad Tom is finally seemingly off calls, I can enjoy the rest of the day in peace.')
    print(str(resp))
    return HttpResponse(str(resp), content_type='text/xml')

def get_token(request):
    capability = ClientCapabilityToken(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    capability.allow_client_outgoing(settings.TWIML_APPLICATION_SID)
