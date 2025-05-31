import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_noteq_all_diff(self):
        node = TextNode("Some text", TextType.ITALIC)
        node2 = TextNode("Diff text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_noteq_diff_type(self):
        node = TextNode("Same text", TextType.ITALIC)
        node2 = TextNode("Same text", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_diff_link(self):
        node = TextNode("Some text", TextType.LINK, "http://example.com")
        node2 = TextNode("Some text", TextType.LINK, "http://other.com")
        self.assertNotEqual(node, node2)

    def test_eq_with_none_url(self):
        node = TextNode("Click here", TextType.LINK)
        node2 = TextNode("Click here", TextType.LINK, None)
        self.assertEqual(node, node2)


if __name__ == "__main__":
    unittest.main()
