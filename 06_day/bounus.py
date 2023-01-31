contents = ['All carrots are to be sliced',
            'The carrots reportedly were sliced',
            'Who cares about damn carrots']

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip( contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)