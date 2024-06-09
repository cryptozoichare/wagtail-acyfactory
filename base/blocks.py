from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    RawHTMLBlock,
    URLBlock,
    ListBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageBlock(StructBlock):
    image = ImageChooserBlock(required=True)
    caption = CharBlock(required=False)
    attribution = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "base/blocks/image_block.html"
        
class LinkButtonBlock(StructBlock):
    url = URLBlock()
    text = CharBlock()
    icon = CharBlock(required=False)
    color_class = ChoiceBlock(choices=[('btn-primary', 'Primary'), ('btn-secondary', 'Secondary')],
                              default='btn-primary')
    
    class Meta:
        icon = "link-external"
        template = "base/blocks/link_button.html"
        


class HeadingBlock(StructBlock):
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(
        choices=[
            ("", "Select a heading size"),
            ("h2", "H2"),
            ("h3", "H3"),
            ("h4", "H4"),
        ],
        blank=True,
        required=False,
    )

    class Meta:
        icon = "title"
        template = "base/blocks/heading_block.html"


class BaseStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(icon="pilcrow")
    image_block = ImageBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )
    html_block = RawHTMLBlock()
    link_button_block = ListBlock(LinkButtonBlock,
                                  template="base/blocks/link_button_list.html",)
