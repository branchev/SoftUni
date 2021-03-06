class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def __repr__(self):
        output = ""
        for doc in self.documents:
            output += doc.__repr__() + "\n"
        return output

    def add_category(self, category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id, new_name):
        category = self.get_category(category_id)
        category.edit(new_name)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        topic = self.get_topic(topic_id)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = self.get_document(document_id)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.get_category(category_id)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.get_topic(topic_id)
        self.topics.remove(topic)

    def get_document(self, document_id):
        return [d for d in self.documents if d.id == document_id][0]

    def get_category(self, cat_id):
        return [c for c in self.categories if c.id == cat_id][0]

    def get_topic(self, topic_id):
        return [t for t in self.topics if t.id == topic_id][0]
