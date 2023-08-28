from pymonad.tools import curry


@curry(2)
def tag(tag_name: str, attr: dict, content: str) -> str:
    attrs = " ".join([f"{key}={value}" for key, value in attr.items()])
    if attrs:
        attrs = " " + attrs
    return f"<{tag_name}{attrs}>{content}</{tag_name}>"


bold = tag("b")
italic = tag("i")

