class Node:
    def __init__(self, type, parts):
        self.type = type
        self.parts = parts

    def parts2str(self, separator='\n'):
        st = []

        for part in self.parts:
            st.append(str(part))

        return separator.join(st)

    def __repr__(self):
        return self.type + ":\n\t" + self.parts2str().replace("\n", "\n\t")

    def add_parts(self, parts):
        self.parts += parts
        return self