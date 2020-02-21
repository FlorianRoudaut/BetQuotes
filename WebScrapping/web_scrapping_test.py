"""
high level support for doing this and that.

do unit test
handle multiple children
handle content
handle tag parameters
"""
import unittest
import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('/home/florian/Documents/Dev/BetQuotes/')

from WebScrapping.html_builder import build_html_tree

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
            <a href="https://www.w3schools.com">This is a second link</a>
            <img src="img_girl.jpg" width="500" height="600">
            <div class="cities">
                <h2>Paris</h2>
                <p>Paris is the capital of France.</p>
            </div>
        </p>
    </body>
</html> """

PAGE_WITH_COMMENT = """ <!DOCTYPE html>
<html>
    <body>
        <p>
            <!--This is a comment.-->
            <img src="img_girl.jpg" width="500" height="600">
        </p>
    </body>
</html> """

PAGE_WITH_TAG_IN_CONTENT = """ <!DOCTYPE html>
<html>
    <body>
        <p>Before Link<a href="https://www.pmu.fr/turf/#!/informations-legales/3" 
        target="_blank" class="cnil-link">Cliquez ici</a> After Link
        </p>
    </body>
</html> """

class SimplePageTest(unittest.TestCase):
    """ Test to parse the simple html page above"""

    def test_depth(self):
        """ Tests the function to compute the depth of the page """
        tree = build_html_tree(SIMPLE_PAGE)
        depth = tree.depth()
        self.assertEqual(depth, 3)

    def test_count_nodes(self):
        """ Tests the function to compute the depth of the page """
        tree = build_html_tree(SIMPLE_PAGE)
        nodes_count = tree.count_nodes()
        self.assertEqual(nodes_count, 4)

    def test_get_element_by_type(self):
        """ Tests the function to retrieve the element by tag type """
        tree = build_html_tree(SIMPLE_PAGE)

        nodes = tree.get_element_by_tag_type("h1")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].content, "My First Heading")

        nodes = tree.get_element_by_tag_type("p")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].content, "My first paragraph.")

    def test_retrieve_attribute(self):
        """ Tests the function to retrieve the attributes of an element """
        tree = build_html_tree(PAGE_WITH_ATTRIBUTE)

        nodes = tree.get_element_by_tag_type("p")
        self.assertEqual(nodes.__len__(), 2)
        paris_node = nodes[1]
        self.assertEqual(paris_node.content, 'Paris is the capital of France.')

        nodes = tree.get_element_by_tag_type("a")
        self.assertEqual(nodes.__len__(), 2)
        self.assertEqual(nodes[0].attributes.__len__(), 1)
        self.assertEqual(nodes[0].attributes['href'], '"https://www.w3schools.com"')

        nodes = tree.get_element_by_tag_type("img")
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].attributes.__len__(), 3)
        node = nodes[0]
        height = node.attributes["height"]
        self.assertEqual(height, '"600"')

    def test_get_element_by_attribute(self):
        """ Test o retrieve correctly an element using its attribute,
        like getting an element by class """
        tree = build_html_tree(PAGE_WITH_ATTRIBUTE)

        nodes = tree.get_element_by_attribute("class", '"cities"')
        self.assertEqual(nodes.__len__(), 1)
        self.assertEqual(nodes[0].attributes.__len__(), 1)

    def test_with_comment(self):
        """ Test to check comments are correctly handled"""
        tree = build_html_tree(PAGE_WITH_COMMENT)

        nodes = tree.get_element_by_tag_type("p")
        comment_node = nodes[0].children[0]
        self.assertIsNotNone(comment_node)
        self.assertEqual(comment_node.tag_type, "!--")
        self.assertEqual(comment_node.content, "This is a comment.")

        img_node = nodes[0].children[1]
        self.assertEqual(img_node.tag_type, "img")
        self.assertEqual(img_node.attributes["height"], '"600"')

    def test_page_with_tag_in_content(self):
        """ Test when a link is embedded in text"""
        tree = build_html_tree(PAGE_WITH_TAG_IN_CONTENT)

        nodes = tree.get_element_by_tag_type("p")
        paragraph = nodes[0]
        self.assertEqual(paragraph.content, "Before Link After Link")
        self.assertEqual(paragraph.children.__len__(), 1)
        link = paragraph.children[0]
        self.assertEqual(link.tag_type, "a")

if __name__ == '__main__':
    unittest.main()
