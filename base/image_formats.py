from django.utils.html import format_html
from wagtail.images.formats import Format, register_image_format, unregister_image_format

unregister_image_format('left')
unregister_image_format('right')

# Re-register the image formats with your custom feature
register_image_format(
    Format("left", ("Left-aligned"), "richtext-image float-start me-1", "width-500")
)
register_image_format(
    Format("right", ("Right-aligned"), "richtext-image float-end ms-1", "width-500")
)
register_image_format(Format('thumbnail', 'Thumbnail', 'richtext-image img-thumbnail', 'max-120x120'))

# class CaptionedImageFormat(Format):

#     def image_to_html(self, image, alt_text, extra_attributes=None):

#         default_html = super().image_to_html(image, alt_text, extra_attributes)

#         return format_html("{}<figcaption>{}</figcaption>", default_html, alt_text)


# register_image_format(
#     CaptionedImageFormat('captioned_fullwidth', 'Full width captioned', 'bodytext-image', 'width-750')
# )