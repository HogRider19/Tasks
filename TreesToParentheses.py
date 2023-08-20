"""
    Binary trees can be encoded as strings of balanced parentheses
    (in fact, the two things are isomorphic). Your task is to figure out such an encoding,
    and write the two functions which convert back and forth between the binary
    trees and strings of parentheses.
"""

def tree_to_parens(tree: Tree) -> str:
    return '' if isinstance(tree, Leaf) else '(' + tree_to_parens(tree.left) + ')' + tree_to_parens(tree.right)

def parens_to_tree(parens: str) -> Tree:
    c = 1
    for i, x in enumerate(parens[1:], 2):
        c += (x == '(') - (x == ')')
        if not c:
            return Branch(parens_to_tree(parens[1:i]), parens_to_tree(parens[i:]))
    return Leaf()