import unittest
from block_to_block import BlockType, block_to_block_type

class TestBlockToBlockType(unittest.TestCase):

    def test_heading(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("#### Final Level"), BlockType.HEADING)

    def test_code_block(self):
        code = "```\nprint('Hello, world')\n```"
        self.assertEqual(block_to_block_type(code), BlockType.CODE)

    def test_quote_block(self):
        quote = "> This is a quote\n> It spans multiple lines"
        self.assertEqual(block_to_block_type(quote), BlockType.QUOTE)

    def test_unordered_list(self):
        ul = "- Item one\n- Item two\n- Item three"
        self.assertEqual(block_to_block_type(ul), BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        ol = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(ol), BlockType.ORDERED_LIST)

    def test_ordered_list_wrong_start(self):
        bad_ol = "0. Zero item\n1. First Item"
        self.assertEqual(block_to_block_type(bad_ol), BlockType.PARAGRAPH)

    def test_undordered_list_missing_dash(self):
        bad_ul = "- Item one\nItem two"
        self.assertEqual(block_to_block_type(bad_ul), BlockType.PARAGRAPH)

    def test_quote_mixed(self):
        bad_quote = "> This is quoted\nThis is not"
        self.assertEqual(block_to_block_type(bad_quote), BlockType.PARAGRAPH)

    def test_paragraph(self):
        para = "This is a plain paragraph of text.\nIt does not follow any special formatting"
        self.assertEqual(block_to_block_type(para), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()