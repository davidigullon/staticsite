import unittest
from htmlnode import HTMLNode  # Adjust path if needed

class TestHTMLNode(unittest.TestCase):

    def test_props_to_html_single_prop(self):
        node = HTMLNode(tag="a", props={"href": "https://example.com"})
        self.assertEqual(node.props_to_html(), 'href="https://example.com"')

    def test_props_to_html_multiple_props(self):
        node = HTMLNode(tag="img", props={"src": "image.png", "alt": "An image"})
        result = node.props_to_html()
        self.assertIn('src="image.png"', result)
        self.assertIn('alt="An image"', result)
        self.assertEqual(result.count("="), 2)

    def test_props_to_html_empty_props(self):
        node = HTMLNode(tag="div")
        self.assertEqual(node.props_to_html(), "")

if __name__ == "__main__":
    unittest.main()
