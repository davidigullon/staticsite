import unittest
from textnode import TextNode, TextType
from split_nodes_delimiter import split_nodes_delimiter

class TestSplitNodesDelimiter(unittest.TestCase):

    def test_basic_code_split(self):
        node = TextNode("This is `code` inside text", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" inside text", TextType.TEXT)
        ])

    def test_multiple_code_blocks(self):
        node = TextNode("`a` `b` `c`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("a", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("b", TextType.CODE),
            TextNode(" ", TextType.TEXT),
            TextNode("c", TextType.CODE)
        ])

    def test_bold_text(self):
        node = TextNode("This is **bold** text", TextType.TEXT)
        result = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(result, [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ])

    def test_italic_text(self):
        node = TextNode("Some _italic_ content", TextType.TEXT)
        result = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(result, [
            TextNode("Some ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" content", TextType.TEXT)
        ])

    def test_unmatched_delimiter_raises(self):
        node = TextNode("This has `no end", TextType.TEXT)
        with self.assertRaises(Exception) as context:
            split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertIn("Unmatched delimiter", str(context.exception))

    def test_non_text_node_passes_through(self):
        node1 = TextNode("Keep me", TextType.CODE)
        node2 = TextNode("Split `this`", TextType.TEXT)
        result = split_nodes_delimiter([node1, node2], "`", TextType.CODE)
        self.assertEqual(result, [
            TextNode("Keep me", TextType.CODE),
            TextNode("Split ", TextType.TEXT),
            TextNode("this", TextType.CODE)
        ])

    def test_empty_string_node(self):
        node = TextNode("", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(result, [])

    def test_text_with_adjacent_delimiters(self):
        node = TextNode("``", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)

    def test_preserve_url_in_non_text_node(self):
        input_nodes = [TextNode("An image", TextType.IMAGE, url="http://example.com")]
        result = split_nodes_delimiter(input_nodes, "`", TextType.CODE)
        self.assertEqual(result, input_nodes)  # Expect unchanged list with one IMAGE node


if __name__ == "__main__":
    unittest.main()