from treebeard import mp_tree

class CategoryQueryset(mp_tree.MP_NodeQuerySet):
    def public(self):
        return self.filter(is_public=True)