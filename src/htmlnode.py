class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children if children is not None else []
		self.props = props if props is not None else {}

	def to_html(self):
		raise NotImplementedError()

	def props_to_html(self):
		props_string = " ".join(f'{key}="{value}" ' for key, value in self.props.items()).strip()
		return props_string
	
	def __repr__(self):
		return (
			f"HTMLNode(tag={self.tag!r}, value={self.value!r}, "
			f"children={self.children!r}, props={self.props!r})"
		)
	
class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag=tag, value=value, children=[], props=props)

	def to_html(self):
		if self.value is None:
			raise ValueError("LeafNode must have a value")
		
		if self.tag is None:
			return self.value
		
		props_str = self.props_to_html()
		if props_str:
			return f"<{self.tag} {props_str}>{self.value}</{self.tag}>"
		else:
			return f"<{self.tag}>{self.value}</{self.tag}>"
		
	def test_leaf_to_html_p(self):
		node = LeafNode("p", "Hello, world!")
		self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

	def test_to_html_with_strong():
		node = LeafNode("strong", "Bold text")		
		assert node.to_html() == "<strong>Bold text</strong>"

	def test_to_html_with_emphasis():
		node = LeafNode("em", "Italic text")
		assert node.to_html() == "<em>Italic text</em>"