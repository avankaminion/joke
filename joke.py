
import logging
import ask_sdk_core.utils as ask_utils

from ask_sdk_core.skill_builder import SkillBuilder
from ask_sdk_core.dispatch_components import AbstractRequestHandler
from ask_sdk_core.dispatch_components import AbstractExceptionHandler
from ask_sdk_core.handler_input import HandlerInput

from ask_sdk_model import Response

import random

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


jokes = [
        "Did you hear about the semi-colon that broke the law? He was given two consecutive sentences.",
        "I ate a clock yesterday, it was very time-consuming.",
        "I've just written a song about tortillas; actually, it's more of a rap.",
        "I woke up this morning and forgot which side the sun rises from, then it dawned on me.",
        "I recently decided to sell my vacuum cleaner as all it was doing was gathering dust.",
        "If you shouldn't eat at night, why do they put a light in the fridge?",
        "My socks got really holy. I can only wear them to church.",
        "I fear my stuttering brother may never finish his prison sentence.",
        "The longest I’ve ever gone without a pun was 7 days. Pretty weak.",
        "This gravity joke is getting a bit old, but I fall for it every time.",
        "What happens when a cop gets into bed? He becomes an undercover cop.",
        "Why are eggs not very much into jokes? Because they could crack up.",
        " Farting in a lift is wrong on so many levels!",
        "Two atoms are walking down the street. One atom says to the other, “Hey! I think I lost an electron! The other asks, “Are you sure?” “Yes, I’m positive!”",
        "I went to the library to get a medical book on abdominal pain. Somebody had torn the appendix out.",
        "Why did Shakespeare write with ink? Because he couldn't decide what pencil to use... 2B or not 2B!",
        "Want to hear a joke about a balloon? Oh wait, it just got away from me!",
        "Did you hear the rumour about butter? Well, I’m not going to spread it!"
  ]


class LaunchRequestHandler(AbstractRequestHandler):
    """Handler for Skill Launch."""
    def can_handle(self, handler_input):
        # type: (HandlerInput) -> bool

        return ask_utils.is_request_type("LaunchRequest")(handler_input)

    def handle(self, handler_input):
        # type: (HandlerInput) -> Response
        speak_output = "Hey there! I am a Joke Bot. You can ask me to tell you a random Joke that might just make your day better!"

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )

class JokeIntentHandler(AbstractRequestHandler):
    def can_handle(self, handler_input):
        return ask_utils.is_intent_name("JokeIntent")(handler_input)

    def handle(self, handler_input):
        speak_output = random.choice(jokes)

        return (
            handler_input.response_builder
                .speak(speak_output)
                .ask(speak_output)
                .response
        )







sb = SkillBuilder()

sb.add_request_handler(LaunchRequestHandler())
sb.add_request_handler(JokeIntentHandler())

handler = sb.lambda_handler()
# Make sure IntentReflectorHandler is last so it
# Doesn't override your custom intent handlers


        