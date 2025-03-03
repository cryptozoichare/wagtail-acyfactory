from wagtail.images.formats import (
    Format,
    register_image_format,
    unregister_image_format,
)

unregister_image_format('left')
unregister_image_format('right')
unregister_image_format('fullwidth')

# Re-register the image formats with your custom feature
register_image_format(
    Format("left", ("Left-aligned"), "richtext-image float-start me-1", "width-500")
)
register_image_format(
    Format("right", ("Right-aligned"), "richtext-image float-end ms-1", "width-500")
)
register_image_format(
    Format("fullwidth", ("Full width"), "richtext-image full-width img-fluid", "width-800")
)
register_image_format(Format('thumbnail', 'Thumbnail', 'richtext-image img-thumbnail', 'max-120x120'))