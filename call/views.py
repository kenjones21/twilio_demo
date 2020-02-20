from rest_framework.decorators import api_view
from twilio.twiml.voice_response import VoiceResponse
from twilio.jwt.client import ClientCapabilityToken
from django.http import HttpResponse, JsonResponse

from twilio_rest import settings

# Create your views here.
@api_view(['GET', 'POST'])
def answer_call(request):
    resp = VoiceResponse()
    resp.say('Glad Tom is finally seemingly off calls, I can enjoy the rest of the day in peace.')
    return HttpResponse(str(resp), content_type='text/xml')

def get_token(request):
    capability = ClientCapabilityToken(
        settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    capability.allow_client_outgoing(settings.TWIML_APPLICATION_SID)
    capability.allow_client_incoming('general')

    token = capability.to_jwt()
    return JsonResponse({'token': token.decode('utf-8')})
