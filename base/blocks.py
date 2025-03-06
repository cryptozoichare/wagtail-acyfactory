from wagtail.blocks import (
    CharBlock,
    ChoiceBlock,
    ListBlock,
    RawHTMLBlock,
    RichTextBlock,
    StreamBlock,
    StructBlock,
    URLBlock,
)
from wagtail.embeds.blocks import EmbedBlock
from wagtail.images.blocks import ImageBlock


from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock

class CardBlock(blocks.StructBlock):
    """A Bootstrap 5 Card Block"""
    image = ImageBlock(required=False, help_text="Optional card image")
    title = blocks.CharBlock(required=True, max_length=100)
    text = blocks.TextBlock(required=True, help_text="Card body text")
    footer = blocks.CharBlock(required=False, max_length=100, help_text="Optional footer text")

    class Meta:
        template = "base/blocks/card_block.html"
        icon = "placeholder"
        label = "Card"


class RowBlock(blocks.StructBlock):
    cards = blocks.ListBlock(CardBlock(), label="Cards")

    class Meta:
        template = "base/blocks/row_block.html"



class FigureBlock(StructBlock):
    image = ImageBlock(required=True)
    caption = CharBlock(required=False)

    class Meta:
        icon = "image"
        template = "base/blocks/figure_block.html"
        
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

class ImageLinkBlock(StructBlock):
    image = ImageBlock()
    url = URLBlock()

    class Meta:
        template = "base/blocks/image_link_block.html"


class BaseStreamBlock(StreamBlock):
    heading_block = HeadingBlock()
    paragraph_block = RichTextBlock(icon="pilcrow")
    figure_block = FigureBlock()
    embed_block = EmbedBlock(
        help_text="Insert a URL to embed. For example, https://www.youtube.com/watch?v=SGJFWirQ3ks",
        icon="media",
    )
    html_block = RawHTMLBlock()
    link_button_block = ListBlock(LinkButtonBlock,
                                  icon = "link-external",
                                  template="base/blocks/link_button_list.html",)
    image_link_block = ImageLinkBlock()
    row = RowBlock()

# class SimpleFlexWrap():