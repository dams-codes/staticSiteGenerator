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
    images = []
    for node in old_nodes:
        print(extract_markdown_images(node))
        # splitOnImage = node.text.split("!", 1)
        # for i, part in enumerate(splitOnImage):
        #     print(i, part)
    #         if len(part) == 0:
    #             continue
    #         if i % 2 == 0:
    #             images.append(TextNode(splitOnImage[i], TextType.TEXT))
    #         else:
    #             images.append(TextNode(extract_markdown_images(splitOnImage[i]), TextType.IMAGE))
    # return images

def split_nodes_link(old_nodes):
    pass

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
    print(new_nodes)

if __name__ == "__main__":
    main()