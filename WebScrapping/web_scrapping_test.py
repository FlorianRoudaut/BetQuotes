"""
high level support for doing this and that.

do unit test
handle multiple children
handle content
handle tag parameters
"""
import unittest
import html_tree_builder

SIMPLE_PAGE = """ <!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html> """


class SimplePageTest(unittest.TestCase):
    """ Test to parse the simple html page above"""

    def test_depth(self):
        """ Tests the function to compute the depth of the page """
        tree = html_tree_builder.build_html_tree(SIMPLE_PAGE)
        depth = tree.depth()
        self.assertEqual(depth, 3)

    def test_count_nodes(self):
        """ Tests the function to compute the depth of the page """
        tree = html_tree_builder.build_html_tree(SIMPLE_PAGE)
        nodes_count = tree.count_nodes()
        self.assertEqual(nodes_count, 4)

    def test_get_element_by_type(self):
        """ Tests the function to retrieve the element by tag type """
        tree = html_tree_builder.build_html_tree(SIMPLE_PAGE)

        nodes = tree.get_element_by_tag_type("h1")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].content, "My First Heading")

        nodes = tree.get_element_by_tag_type("p")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].content, "My first paragraph.")


if __name__ == '__main__':
    unittest.main()
