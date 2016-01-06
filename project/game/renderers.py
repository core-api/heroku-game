from rest_framework.renderers import BaseRenderer
from coreapi.codecs import HTMLCodec, CoreJSONCodec


class CoreAPIJSONRenderer(BaseRenderer):
    media_type = 'application/vnd.coreapi+json'

    def render(self, data, media_type=None, renderer_context=None):
        codec = CoreJSONCodec()
        return codec.dump(data, indent=True)


class CoreAPIHTMLRenderer(BaseRenderer):
    media_type = 'text/html'

    def render(self, data, media_type=None, renderer_context=None):
        codec = HTMLCodec()
        extra_css = '#board > td {font-family: Courier}'
        return codec.dump(data, extra_css=extra_css)
