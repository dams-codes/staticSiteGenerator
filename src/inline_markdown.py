from textnode import TextNode, TextType
import re


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    newNodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            newNodes.append(node)
        else:
            splitOnDelimiter = node.text.split(delimiter)
            if len(splitOnDelimiter) % 2 == 0:
                raise Exception("Invalid Markdown")
            for i, part in enumerate(splitOnDelimiter):
                if len(part) == 0:
                    continue
                if i % 2 == 0:
                    newNodes.append(TextNode(splitOnDelimiter[i], TextType.TEXT))
                else:
                    newNodes.append(TextNode(splitOnDelimiter[i], text_type))
    return newNodes


def split_nodes_image(old_nodes):
    newNodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if node.text_type != TextType.TEXT:
            newNodes.append(node)
        else:
            for image_alt, image_link in images:
                splitOnDelimiter = node.text.split(f"![{image_alt}]({image_link})", 1)
                if splitOnDelimiter[0] != "":
                    newNodes.append(TextNode(splitOnDelimiter[0], TextType.TEXT))
                newNodes.append(TextNode(image_alt, TextType.IMAGE, image_link))
                node = TextNode(splitOnDelimiter[1], TextType.TEXT)
            if len(node.text) != 0:
                newNodes.append(node)
    return newNodes


def split_nodes_link(old_nodes):
    newNodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if node.text_type != TextType.TEXT:
            newNodes.append(node)
        else:
            for link_alt, link_link in links:
                splitOnDelimiter = node.text.split(f"[{link_alt}]({link_link})", 1)
                if splitOnDelimiter[0] != "":
                    newNodes.append(TextNode(splitOnDelimiter[0], TextType.TEXT))
                newNodes.append(TextNode(link_alt, TextType.LINK, link_link))
                node = TextNode(splitOnDelimiter[1], TextType.TEXT)
            if len(node.text) != 0:
                newNodes.append(node)
    return newNodes


def extract_markdown_images(text):
    pattern = r"!\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def extract_markdown_links(text):
    pattern = r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)"
    matches = re.findall(pattern, text)
    return matches


def main():
    # node = TextNode("This is text with a `code block` word", TextType.TEXT)
    # new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    # print(new_nodes)
    # node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
    # new_nodes2 = split_nodes_delimiter([node2], "`", TextType.CODE)
    # print(new_nodes2)
    # for i in new_nodes:
    #     print(i)
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    # print(extract_markdown_images(text))
    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    node2 = TextNode(
        "Hello ![cat](http://cat.png) world",
        TextType.TEXT,
    )
    new_nodes2 = split_nodes_image([node2])
    print(new_nodes2)


if __name__ == "__main__":
    main()
