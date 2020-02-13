"""
high level support for doing this and that.

do unit test
handle multiple children
handle content
handle tag parameters
"""
import unittest
import html_builder

SIMPLE_PAGE = """ <!DOCTYPE html>
<html>
    <body>
        <h1>My First Heading</h1>
        <p>My first paragraph.</p>
    </body>
</html> """

PAGE_WITH_ATTRIBUTE = """ <!DOCTYPE html>
<html>
    <body>
        <p>
            <a href="https://www.w3schools.com">This is a link</a>
            <img src="img_girl.jpg" width="500" height="600">
            <div class="cities">
                <h2>Paris</h2>
                <p>Paris is the capital of France.</p>
            </div>
        </p>
    </body>
</html> """


class SimplePageTest(unittest.TestCase):
    """ Test to parse the simple html page above"""

    def test_depth(self):
        """ Tests the function to compute the depth of the page """
        tree = html_builder.build_html_tree(SIMPLE_PAGE)
        depth = tree.depth()
        self.assertEqual(depth, 3)

    def test_count_nodes(self):
        """ Tests the function to compute the depth of the page """
        tree = html_builder.build_html_tree(SIMPLE_PAGE)
        nodes_count = tree.count_nodes()
        self.assertEqual(nodes_count, 4)

    def test_get_element_by_type(self):
        """ Tests the function to retrieve the element by tag type """
        tree = html_builder.build_html_tree(SIMPLE_PAGE)

        nodes = tree.get_element_by_tag_type("h1")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].content, "My First Heading")

        nodes = tree.get_element_by_tag_type("p")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].content, "My first paragraph.")

    def test_retrieve_attribute(self):
        """ Tests the function to retrieve the attributes of an element """
        tree = html_builder.build_html_tree(PAGE_WITH_ATTRIBUTE)

        nodes = tree.get_element_by_tag_type("a")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].attributes.__len__(), 1)

        nodes = tree.get_element_by_tag_type("img")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].attributes.__len__(), 3)
        node = nodes[0]
        height = node.attributes["height"]
        self.assertEqual(height, '"600"')

    def test_get_element_by_attribute(self):
        """ Test o retrieve correctly an element using its attribute,
        like getting an element by class """
        tree = html_builder.build_html_tree(PAGE_WITH_ATTRIBUTE)

        nodes = tree.get_element_by_attribute("class", '"cities"')
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].attributes.__len__(), 1)


if __name__ == '__main__':
    unittest.main()
