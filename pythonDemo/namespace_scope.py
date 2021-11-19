class Something:
    @property
    def subspace(self):
        class SubSpaceClass:
            def do_smth(self):
                print('do_something')

        return SubSpaceClass()

    @property
    def another_subspace(self):
        class AnotherSubSpaceClass:
            def do_smth_else(self):
                print('do_something_else')

        return AnotherSubSpaceClass()


smth = Something()
smth.subspace.do_smth()

smth.another_subspace.do_smth_else()
