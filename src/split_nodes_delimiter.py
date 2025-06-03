from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # If node is not plain text, add it as-is and skip splitting
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue  # crucial to avoid splitting non-text nodes

        # Split the text by the delimiter
        parts = node.text.split(delimiter)

        # If even number of parts => unmatched delimiter
        if len(parts) % 2 == 0:
            raise Exception(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        # We'll build new nodes from the parts
        for i, part in enumerate(parts):
            if i % 2 == 1:
                # This should be the special text type (like CODE, BOLD, etc)
                if part == "":
                    raise Exception(f"Empty content between delimiters '{delimiter}' in text: {node.text}")
                new_nodes.append(TextNode(part, text_type))
            else:
                # Normal text
                if part != "":
                    new_nodes.append(TextNode(part, TextType.TEXT))

    return new_nodes

