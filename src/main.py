# """Main app."""
# import logging
# import connexion
# import yaml
# from connexion.resolver import RelativeResolver
#
# LOGGER = logging.getLogger(__name__)
# app = connexion.App(__name__)
# application = app.app
# application.url_map.strict_slashes = False
#
# # app.add_api(
# #     specification,
# #     resolver=connexion.RestyResolver(API_PATH),
# #     options={"swagger_ui": application.config.get("SWAGGER_UI")},
# # ))
# app.add_api('openapi.yaml', resolver=RelativeResolver('adapters.endpoints'))
#
# print()
# print("###############")
# print(application.url_map)
# print("###############")
# print()
#
#
# def getall():
#     return "oi mundo"
#
#
# if __name__ == "__main__":
#     LOGGER.info("Starting application")
#     application.run(port=8080, server="gevent", debug=True)

from connexion import App, FlaskApp

app = FlaskApp(__name__)
def post_greeting(name: str = ""):
    return f"Hello {name}", 200

app.add_api("openapi.yaml")
application = app.app


if __name__ == "__main__":
    # LOGGER.info("Starting application")
    app.run(port=8080, server="gevent", debug=True)
